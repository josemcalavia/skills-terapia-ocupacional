#!/usr/bin/env python3
"""Descarga la colección de Diseños 3D de Accessibilitas (Fundación ONCE) como referencia.

Uso: python3 -I descargar_originales.py <carpeta_de_trabajo>

Crea <carpeta>/originales/ con:
  zips/<producto>.zip          el archivo original tal como se publica
  extraidos/<producto>/        su contenido (.scad, .stl, PDF de instrucciones y licencia)
  indice.json                  producto -> URL de la ficha y del ZIP

Los diseños se distribuyen con licencia CC BY-NC-SA 4.0 (incluida en cada ZIP).
Se descargan para estudiarlos y como referencia técnica; no se redistribuyen.
Si ya existe un ZIP, no se vuelve a descargar.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, zipfile

BASE = "https://accessibilitas.es/disenos-3d/"
UA = {"User-Agent": "Mozilla/5.0 (disenador-productos-apoyo)"}


def get(url, timeout=60):
    p = urllib.parse.urlsplit(url)
    url = urllib.parse.urlunsplit(p._replace(path=urllib.parse.quote(urllib.parse.unquote(p.path))))
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = os.path.join(os.path.abspath(sys.argv[1]), "originales")
    for d in ("zips", "extraidos"):
        os.makedirs(os.path.join(out, d), exist_ok=True)

    fichas, pagina = [], 1
    while True:
        url = BASE if pagina == 1 else f"{BASE}page/{pagina}/"
        try:
            html = get(url).decode("utf-8", "ignore")
        except Exception:
            break
        nuevas = sorted(set(re.findall(r"https://accessibilitas\.es/20\d\d/\d\d/[a-z0-9-]+/", html)) - set(fichas))
        if not nuevas:
            break
        fichas += nuevas
        pagina += 1
        time.sleep(0.5)
    print(f"{len(fichas)} fichas encontradas")

    indice = {}
    for ficha in fichas:
        slug = ficha.rstrip("/").rsplit("/", 1)[1]
        try:
            html = get(ficha).decode("utf-8", "ignore")
        except Exception as e:
            print("FALLO ficha", slug, e); continue
        m = re.search(r"href=['\"]?(https://accessibilitas\.es/wp-content/uploads/[^'\" >]+\.zip)", html, re.I)
        t = re.search(r"<title>([^<|–-]+)", html)
        indice[slug] = {"ficha": ficha, "zip": m.group(1) if m else None,
                        "titulo": t.group(1).strip() if t else slug}
        if not m:
            print("Sin ZIP:", slug); continue
        destino = os.path.join(out, "zips", slug + ".zip")
        if not os.path.exists(destino):
            try:
                open(destino, "wb").write(get(m.group(1), timeout=300))
            except Exception as e:
                print("FALLO descarga", slug, e); continue
            time.sleep(0.5)
        carpeta = os.path.join(out, "extraidos", slug)
        os.makedirs(carpeta, exist_ok=True)
        try:
            with zipfile.ZipFile(destino) as z:
                for info in z.infolist():
                    n = info.filename
                    if n.startswith("__MACOSX") or ".." in n.split("/") or n.startswith("/"):
                        continue
                    z.extract(info, carpeta)
            print("OK", slug)
        except zipfile.BadZipFile:
            print("ZIP dañado:", slug)
    json.dump(indice, open(os.path.join(out, "indice.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Índice:", os.path.join(out, "indice.json"))


if __name__ == "__main__":
    main()
