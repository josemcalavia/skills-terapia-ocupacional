#!/usr/bin/env python3
"""Fabrica las piezas de un diseño OpenSCAD y comprueba que caben en la impresora.

Uso:
  python3 -I fabricar.py <carpeta_del_diseno> [--set NOMBRE] [--solo-vistas]

La carpeta debe contener:
  - un único .scad principal (el que no empiece por "_" ni sea una librería)
  - diseno.json con, como mínimo:
      {"nombre": "...",
       "impresora": {"nombre": "Elegoo Centauri Carbon", "volumen_mm": [256, 256, 256]},
       "piezas": [{"id": "pomo", "Mostrar": "Pomo", "material": "PLA", "cantidad": 1}]}
    Si falta "impresora", se comprueba contra 220 x 220 x 250 mm (cama habitual).
    Si el .scad no tiene variable Mostrar, use "Mostrar": null.
  - opcional: <scad>.json con conjuntos de parámetros del Customizer
    (se selecciona con --set; por defecto el primero, si existe).

Genera en la carpeta:
  stl/<id>.stl          STL binario por pieza
  3mf/<id>.3mf          misma pieza en 3MF (Elegoo Slicer lo abre directamente)
  vistas/<id>.png       render para revisar el diseño
  informe_fabricacion.json  medidas, volumen, avisos y comprobaciones
"""
import glob, json, os, subprocess, sys, struct, shutil, tempfile

def buscar_openscad():
    cands = [os.environ.get("OPENSCAD"), shutil.which("openscad"),
             "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD",
             os.path.expanduser("~/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"),
             r"C:\Program Files\OpenSCAD\openscad.exe", "/usr/bin/openscad", "/snap/bin/openscad"]
    cands += glob.glob("/Volumes/*/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD")
    for c in cands:
        if c and os.path.exists(c):
            return c
    sys.exit("No encuentro OpenSCAD. Instálalo (https://openscad.org/downloads.html, mejor una versión "
             "«development snapshot» por el motor manifold) o indica su ruta en la variable OPENSCAD.")


OPENSCAD = None
LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib")
IMPRESORA_POR_DEFECTO = {"nombre": "impresora genérica", "volumen_mm": [220, 220, 250]}
DENSIDAD = {"PLA": 1.24, "PETG": 1.27, "TPU": 1.21, "ABS": 1.04, "ASA": 1.07,
            "PLA-CF": 1.30, "PETG-CF": 1.30, "PA-CF": 1.20}


def escena(carpeta):
    cands = [f for f in os.listdir(carpeta) if f.endswith(".scad") and not f.startswith("_")]
    if len(cands) != 1:
        sys.exit(f"Se esperaba un único .scad principal en {carpeta}, hay: {cands}")
    return os.path.join(carpeta, cands[0])


def correr(args, env):
    r = subprocess.run([OPENSCAD, *args], capture_output=True, text=True, env=env, timeout=1800)
    return r.returncode, r.stdout + r.stderr


def leer_stl(path):
    """Devuelve (bbox_min, bbox_max, volumen_mm3, n_triangulos) de un STL binario."""
    with open(path, "rb") as f:
        f.read(80)
        n = struct.unpack("<I", f.read(4))[0]
        mn = [1e18] * 3; mx = [-1e18] * 3; vol = 0.0
        for _ in range(n):
            d = struct.unpack("<12fH", f.read(50))
            v = (d[3:6], d[6:9], d[9:12])
            for p in v:
                for i in range(3):
                    mn[i] = min(mn[i], p[i]); mx[i] = max(mx[i], p[i])
            a, b, c = v
            vol += (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
                    + a[2] * (b[0] * c[1] - b[1] * c[0])) / 6.0
    return mn, mx, abs(vol), n


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    carpeta = os.path.abspath(a[0])
    solo_vistas = "--solo-vistas" in a
    conjunto = a[a.index("--set") + 1] if "--set" in a else None
    global OPENSCAD
    OPENSCAD = buscar_openscad()
    scad = escena(carpeta)
    meta = json.load(open(os.path.join(carpeta, "diseno.json"), encoding="utf-8"))
    impresora = meta.get("impresora") or IMPRESORA_POR_DEFECTO
    cama = [float(v) for v in impresora["volumen_mm"]]
    params_file = os.path.splitext(scad)[0] + ".json"
    if os.path.exists(params_file) and conjunto is None:
        sets = json.load(open(params_file, encoding="utf-8")).get("parameterSets", {})
        conjunto = next(iter(sets), None)

    env = dict(os.environ, OPENSCADPATH=os.path.abspath(LIB))
    for d in ("stl", "3mf", "vistas"):
        os.makedirs(os.path.join(carpeta, d), exist_ok=True)

    informe = {"diseno": meta.get("nombre"), "scad": os.path.basename(scad),
               "conjunto_parametros": conjunto, "impresora": impresora["nombre"],
               "piezas": []}
    ok_global = True
    for p in meta["piezas"]:
        pid = p["id"]
        base = []
        if os.path.exists(params_file) and conjunto:
            base += ["-p", params_file, "-P", conjunto]
        if p.get("Mostrar") is not None:
            base += ["-D", f'Mostrar="{p["Mostrar"]}"']
        for k, v in (p.get("parametros") or {}).items():
            base += ["-D", f"{k}={json.dumps(v) if isinstance(v, str) else v}"]
        res = {"id": pid, "material": p.get("material", "PLA"), "cantidad": p.get("cantidad", 1),
               "avisos": [], "errores": []}

        png = os.path.join(carpeta, "vistas", pid + ".png")
        rc, log = correr(["--backend=manifold", "--render", "--imgsize=1000,800", "--viewall",
                          "--autocenter", "--colorscheme=Tomorrow", "-o", png, *base, scad], env)
        res["vista"] = os.path.relpath(png, carpeta)
        for line in log.splitlines():
            if "ECHO:" in line:
                res["avisos"].append(line.split("ECHO:", 1)[1].strip().strip('"'))
            if "WARNING" in line and "Ignoring unknown" not in line:
                res["avisos"].append(line.strip())
            if "ERROR" in line:
                res["errores"].append(line.strip())
        if rc != 0:
            res["errores"].append(f"OpenSCAD terminó con código {rc}")

        if not solo_vistas and rc == 0:
            stl = os.path.join(carpeta, "stl", pid + ".stl")
            summ = tempfile.mktemp(suffix=".json")
            rc2, log2 = correr(["--backend=manifold", "--export-format", "binstl", "--summary", "all",
                                "--summary-file", summ, "-o", stl, *base, scad], env)
            if rc2 != 0 or not os.path.exists(stl):
                res["errores"].append("No se pudo exportar el STL:\n" + log2[-1500:])
            else:
                correr(["--backend=manifold", "-o", os.path.join(carpeta, "3mf", pid + ".3mf"), *base, scad], env)
                mn, mx, vol, n = leer_stl(stl)
                dims = [round(mx[i] - mn[i], 2) for i in range(3)]
                res.update({"stl": os.path.relpath(stl, carpeta), "3mf": f"3mf/{pid}.3mf",
                            "medidas_mm": dims, "z_min": round(mn[2], 3), "triangulos": n,
                            "volumen_cm3": round(vol / 1000, 2),
                            "peso_macizo_g": round(vol / 1000 * DENSIDAD.get(res["material"], 1.25), 1)})
                if os.path.exists(summ):
                    try:
                        s = json.load(open(summ))
                        g = s.get("geometry", {})
                        res["manifold"] = g.get("status", "") in ("NoError", "") and g.get("manifold", True)
                        if g.get("status") not in (None, "NoError"):
                            res["errores"].append(f"Geometría no válida: {g.get('status')}")
                    except Exception:
                        pass
                if n == 0:
                    res["errores"].append("La pieza está vacía (0 triángulos)")
                xy_pieza, xy_cama = sorted(dims[:2]), sorted(cama[:2])
                if dims[2] > cama[2] or xy_pieza[0] > xy_cama[0] or xy_pieza[1] > xy_cama[1]:
                    res["errores"].append(f"No cabe en {impresora['nombre']} "
                                          f"({cama[0]:g}x{cama[1]:g}x{cama[2]:g} mm): {dims}")
                if abs(mn[2]) > 0.05:
                    res["avisos"].append(f"La pieza no apoya en Z=0 (z_min={mn[2]:.2f}); el laminador la bajará, "
                                         "pero revise que la cara de apoyo sea la prevista.")
        ok_global &= not res["errores"]
        informe["piezas"].append(res)

    informe["ok"] = ok_global
    json.dump(informe, open(os.path.join(carpeta, "informe_fabricacion.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(json.dumps(informe, ensure_ascii=False, indent=2))
    sys.exit(0 if ok_global else 1)


if __name__ == "__main__":
    main()
