#!/usr/bin/env python3
"""Memoria de aprendizajes del diseñador de productos de apoyo.

Los aprendizajes son de cada persona o equipo, no de la skill: se guardan en la
carpeta de trabajo (aprendizajes.json y su versión legible aprendizajes.md), así
que no se pierden al actualizar la skill. La carpeta de trabajo se busca así:
  1) opción --trabajo RUTA;  2) variable DISENADOR_TRABAJO;
  3) subiendo desde la carpeta actual hasta encontrar
     preferencias-disenador-productos-apoyo.md o una carpeta disenos/;
  4) la carpeta actual.

Uso:
  aprendizajes.py nuevo --categoria C --ambito A --regla "..." --porque "..."
                        [--diseno SLUG] [--guia "Nombre o rol"] [--confianza propuesta|confirmada|validada]
  aprendizajes.py cambiar ID --confianza validada|descartada|confirmada [--nota "..."]
  aprendizajes.py buscar [palabras ...] [--categoria C] [--todas]
  aprendizajes.py listar
  aprendizajes.py diseno SLUG    (aprendizajes nacidos de ese diseño)
  Todas admiten --trabajo RUTA antes del subcomando.
"""
import argparse, datetime, json, os, sys, unicodedata

MARCA = "<!-- ENTRADAS: no borrar esta línea; el script añade debajo -->"
CABECERA = """# Aprendizajes del diseñador de productos de apoyo

Memoria viva: decisiones de diseño que han funcionado o fallado y criterios de las
personas que guían los diseños. **Se lee al empezar cada diseño y prevalece sobre las
convenciones genéricas.** No se edita a mano: se gestiona con `scripts/aprendizajes.py`.

- **Confianza:** ○ propuesta (sin probar) · ● confirmada (decidida por quien guía, con su
  porqué) · ✔ validada (comprobada con una pieza impresa o en uso) · ✘ descartada (no
  funcionó; se conserva para no repetir el error).
- **Ámbito:** a qué tipo de pieza se aplica («encajes a presión sobre ejes», «todas»…).

"""
DATA = MD = None


def carpeta_trabajo(explicita=None):
    if explicita:
        return os.path.abspath(explicita)
    if os.environ.get("DISENADOR_TRABAJO"):
        return os.path.abspath(os.environ["DISENADOR_TRABAJO"])
    d = os.getcwd()
    while True:
        if os.path.exists(os.path.join(d, "preferencias-disenador-productos-apoyo.md")) \
                or os.path.isdir(os.path.join(d, "disenos")):
            return d
        padre = os.path.dirname(d)
        if padre == d:
            return os.getcwd()
        d = padre
CATEGORIAS = ["orientacion", "holguras", "uniones", "material", "ergonomia", "seguridad",
              "imprimibilidad", "parametros", "documentacion", "proceso", "evitar"]
CONFIANZAS = ["propuesta", "confirmada", "validada", "descartada"]
PESO = {"validada": 0, "confirmada": 1, "propuesta": 2, "descartada": 3}
ICONO = {"propuesta": "○", "confirmada": "●", "validada": "✔", "descartada": "✘"}


def norm(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def cargar():
    return json.load(open(DATA, encoding="utf-8")) if os.path.exists(DATA) else []


def fmt(e):
    s = (f"### {e['id']} · {ICONO[e['confianza']]} {e['confianza']} · {e['categoria']}\n"
         f"- **Regla:** {e['regla']}\n- **Por qué:** {e['porque']}\n- **Ámbito:** {e['ambito']}\n"
         f"- **Origen:** {e.get('diseno') or '—'} · guía: {e.get('guia') or '—'} · {e['fecha']}\n")
    for h in e.get("historial", []):
        s += f"- {h['fecha']}: → {h['confianza']}" + (f" — {h['nota']}" if h.get("nota") else "") + "\n"
    return s


def guardar(entradas):
    json.dump(entradas, open(DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    cab = (open(MD, encoding="utf-8").read().split(MARCA)[0] if os.path.exists(MD) else CABECERA) + MARCA + "\n"
    cuerpo = ""
    for cat in CATEGORIAS:
        es = sorted([e for e in entradas if e["categoria"] == cat], key=lambda e: (PESO[e["confianza"]], e["id"]))
        if es:
            cuerpo += f"\n## {cat.capitalize()}\n\n" + "\n".join(fmt(e) for e in es)
    open(MD, "w", encoding="utf-8").write(cab + cuerpo)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trabajo", help="carpeta de trabajo donde se guardan los aprendizajes")
    sp = ap.add_subparsers(dest="cmd", required=True)
    n = sp.add_parser("nuevo")
    n.add_argument("--categoria", required=True, choices=CATEGORIAS)
    n.add_argument("--ambito", required=True)
    n.add_argument("--regla", required=True)
    n.add_argument("--porque", required=True)
    n.add_argument("--diseno", default="")
    n.add_argument("--guia", default="")
    n.add_argument("--confianza", default="confirmada", choices=CONFIANZAS[:3])
    c = sp.add_parser("cambiar")
    c.add_argument("id")
    c.add_argument("--confianza", required=True, choices=CONFIANZAS)
    c.add_argument("--nota", default="")
    b = sp.add_parser("buscar")
    b.add_argument("palabras", nargs="*")
    b.add_argument("--categoria", choices=CATEGORIAS)
    b.add_argument("--todas", action="store_true", help="incluir propuestas sin confirmar")
    sp.add_parser("listar")
    d = sp.add_parser("diseno")
    d.add_argument("slug")
    a = ap.parse_args()
    global DATA, MD
    base = carpeta_trabajo(a.trabajo)
    DATA = os.path.join(base, "aprendizajes.json")
    MD = os.path.join(base, "aprendizajes.md")
    print(f"(aprendizajes en {base})", file=sys.stderr)

    es = cargar()
    hoy = datetime.date.today().isoformat()
    if a.cmd == "nuevo":
        nid = "A%03d" % (max([int(e["id"][1:]) for e in es] or [0]) + 1)
        e = {"id": nid, "categoria": a.categoria, "ambito": a.ambito, "regla": a.regla, "porque": a.porque,
             "diseno": a.diseno, "guia": a.guia, "confianza": a.confianza, "fecha": hoy, "historial": []}
        # Aviso de posibles duplicados: muchas palabras en común con otra regla
        pal = set(w for w in norm(a.regla).split() if len(w) > 4)
        for o in es:
            comun = pal & set(w for w in norm(o["regla"]).split() if len(w) > 4)
            if len(comun) >= max(3, len(pal) // 2):
                print(f"AVISO: se parece a {o['id']} ({o['confianza']}): {o['regla']}")
        es.append(e); guardar(es); print(fmt(e))
    elif a.cmd == "cambiar":
        e = next((x for x in es if x["id"] == a.id.upper()), None)
        if not e:
            sys.exit(f"No existe {a.id}")
        e["historial"].append({"fecha": hoy, "confianza": a.confianza, "nota": a.nota})
        e["confianza"] = a.confianza
        guardar(es); print(fmt(e))
    elif a.cmd in ("buscar", "listar", "diseno"):
        r = es
        if a.cmd == "diseno":
            r = [e for e in es if e.get("diseno") == a.slug]
        if a.cmd == "buscar":
            if a.categoria:
                r = [e for e in r if e["categoria"] == a.categoria]
            if a.palabras:
                ws = [norm(w) for w in a.palabras]
                r = [e for e in r if any(w in norm(" ".join([e["regla"], e["porque"], e["ambito"], e["categoria"]]))
                                         for w in ws) or e["ambito"].lower() == "todas"]
            if not a.todas:
                r = [e for e in r if e["confianza"] != "propuesta"]
        r = sorted(r, key=lambda e: (PESO[e["confianza"]], e["id"]))
        print("\n".join(fmt(e) for e in r) if r else "Sin aprendizajes que coincidan.")


if __name__ == "__main__":
    main()
