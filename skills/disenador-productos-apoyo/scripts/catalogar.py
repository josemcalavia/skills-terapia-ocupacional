#!/usr/bin/env python3
"""Genera el catálogo de referencia a partir de la colección descargada.

Uso: python3 -I catalogar.py <carpeta>/originales <salida.md>

Solo usa material incluido en los ZIP (licencia CC BY-NC-SA 4.0): los parámetros
de los .scad y los apartados «Intencionalidad», «Recomendaciones de impresión» e
«Instalación» de los PDF de instrucciones. Necesita pdftotext (poppler).
"""
import glob, json, os, re, subprocess, sys


def params(path):
    out, sec, com = [], None, ""
    for l in open(path, encoding="utf-8", errors="ignore").read().splitlines():
        if re.match(r"^\s*(module|function)\b", l):
            break
        m = re.match(r"^\s*/\*\s*\[(.+?)\]\s*\*/", l)
        if m:
            sec = m.group(1); com = ""; continue
        m = re.match(r"^\s*//\s*(.+)", l)
        if m:
            com = m.group(1).strip(); continue
        m = re.match(r"^\s*([A-Za-z_]\w*)\s*=\s*([^;]+);\s*(?://\s*(.*))?", l)
        if m and sec != "Hidden":
            out.append((sec, m.group(1), m.group(2).strip(), (m.group(3) or "").strip(), com)); com = ""
    return out


def limpio(t, n):
    return re.sub(r"\s+", " ", t).strip()[:n]


def pdf(carpeta):
    r = {}
    for p in glob.glob(os.path.join(carpeta, "**", "*.pdf"), recursive=True):
        if re.search(r"reative|licen", p, re.I):
            continue
        try:
            t = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=60).stdout
        except Exception:
            continue
        m = re.search(r"Intencionalidad del dise[ñn]o\s*(.*?)(?:\n\s*\d+\.\s+[A-ZÁÉÍÓÚ¿]|\Z)", t, re.S)
        if m and "intencion" not in r:
            r["intencion"] = limpio(m.group(1), 700)
        m = re.search(r"Recomendaciones de impresi[oó]n(.*?)(?:\n\s*\d+\.\s+[A-ZÁÉÍÓÚ]|\Z)", t, re.S)
        if m:
            r["impresion"] = limpio(m.group(1), 900)
        m = re.search(r"\d+\.\s+(?:Instalaci[oó]n|Montaje)[^\n]*\n(.*?)(?:\n\s*\d+\.\s+[A-ZÁÉÍÓÚ]|\Z)", t, re.S)
        if m:
            r["instalacion"] = limpio(m.group(1), 600)
    return r


def main():
    base, salida = os.path.abspath(sys.argv[1]), sys.argv[2]
    ext = os.path.join(base, "extraidos")
    idx_path = os.path.join(base, "indice.json")
    indice = json.load(open(idx_path, encoding="utf-8")) if os.path.exists(idx_path) else {}
    md = ["# Catálogo de referencia: Diseños 3D de Accessibilitas (Fundación ONCE)", "",
          "Generado con `scripts/catalogar.py` a partir de los archivos de la colección "
          "(https://accessibilitas.es/disenos-3d/), que se distribuyen con licencia **CC BY-NC-SA 4.0**. "
          "Los extractos de parámetros e instrucciones pertenecen a Fundación ONCE / Accessibilitas y se "
          "reproducen con atribución y la misma licencia. Rutas relativas a `originales/`.", ""]
    for n in sorted(os.listdir(ext)):
        d = os.path.join(ext, n)
        if not os.path.isdir(d):
            continue
        info = indice.get(n, {})
        archivos = sorted(os.path.relpath(p, base) for p in glob.glob(os.path.join(d, "**", "*"), recursive=True)
                          if p.lower().endswith((".scad", ".stl", ".ino")) and "Librerias" not in p)
        scads = [s for s in sorted(glob.glob(os.path.join(d, "**", "*.scad"), recursive=True))
                 if os.path.basename(s) != "threads.scad" and os.path.getsize(s) < 200000]
        md += [f"## {n}", ""]
        if info.get("ficha"):
            md.append(f"- Ficha: {info['ficha']}")
        r = pdf(d)
        if r.get("intencion"):
            md.append(f"- Intencionalidad: {r['intencion']}")
        md.append("- Parametrizable: " + ("sí (OpenSCAD)" if scads else "no (solo STL)"))
        md.append("- Archivos: " + ", ".join(f"`{a}`" for a in archivos[:12]) + (" …" if len(archivos) > 12 else ""))
        for s in scads:
            ps = params(s)
            if not ps:
                continue
            md.append(f"- Parámetros de `{os.path.basename(s)}`:")
            for sec, k, v, opt, c in ps:
                md.append(f"  - [{sec}] `{k} = {v}`" + (f" {opt}" if opt.startswith("[") else "") + (f" — {c}" if c else ""))
        if r.get("impresion"):
            md.append(f"- Impresión: {r['impresion']}")
        if r.get("instalacion"):
            md.append(f"- Instalación: {r['instalacion']}")
        md.append("")
    open(salida, "w", encoding="utf-8").write("\n".join(md))
    print("Catálogo:", salida)


if __name__ == "__main__":
    main()
