#!/usr/bin/env python3
"""Convierte instrucciones.md (Markdown sencillo) en un PDF de instrucciones.

Uso: python3 -I instrucciones_pdf.py <carpeta_del_diseno>

Admite: # título, ## sección, ### subsección, párrafos, listas con "- " o "1. ",
**negrita**, `código` e imágenes ![pie](ruta/relativa.png).
El PDF se guarda como "Instrucciones - <nombre>.pdf" con pie de licencia.
"""
import json, os, re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, ListFlowable, ListItem, KeepTogether

PIE = ("Diseño derivado de la colección de Diseños 3D de Accessibilitas (Fundación ONCE), "
       "licencia CC BY-NC-SA 4.0. Uso no comercial; las obras derivadas deben compartirse con la misma licencia.")


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", t)
    return t


def main():
    carpeta = os.path.abspath(sys.argv[1])
    meta = json.load(open(os.path.join(carpeta, "diseno.json"), encoding="utf-8"))
    md = open(os.path.join(carpeta, "instrucciones.md"), encoding="utf-8").read().splitlines()
    ss = getSampleStyleSheet()
    st = {
        "h1": ParagraphStyle("h1", parent=ss["Title"], fontSize=20, leading=24, spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontSize=14, leading=18, spaceBefore=10,
                             textColor=colors.HexColor("#1f4e79")),
        "h3": ParagraphStyle("h3", parent=ss["Heading3"], fontSize=12, leading=15),
        "p": ParagraphStyle("p", parent=ss["BodyText"], fontSize=11, leading=15, spaceAfter=6),
        "cap": ParagraphStyle("cap", parent=ss["BodyText"], fontSize=9, textColor=colors.grey,
                              alignment=1, spaceAfter=8),
    }
    out = os.path.join(carpeta, f"Instrucciones - {meta['nombre']}.pdf")
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=22 * mm,
                            title=f"Instrucciones - {meta['nombre']}", author=meta.get("autor", ""),
                            lang="es-ES")
    flow, lista, ordenada = [], [], False

    def cerrar_lista():
        nonlocal lista
        if lista:
            flow.append(ListFlowable([ListItem(Paragraph(inline(x), st["p"])) for x in lista],
                                     bulletType="1" if ordenada else "bullet",
                                     bulletFormat="%s." if ordenada else None, leftIndent=14))
            lista = []

    parrafo = []

    def cerrar_parrafo():
        nonlocal parrafo
        if parrafo:
            flow.append(Paragraph(inline(" ".join(parrafo)), st["p"]))
            parrafo = []

    for l in md + [""]:
        img = re.match(r"!\[(.*?)\]\((.+?)\)", l.strip())
        m_ul = re.match(r"^\s*[-*]\s+(.*)", l)
        m_ol = re.match(r"^\s*\d+[.)]\s+(.*)", l)
        if l.startswith("#"):
            cerrar_parrafo(); cerrar_lista()
            n = len(l) - len(l.lstrip("#"))
            flow.append(Paragraph(inline(l.lstrip("#").strip()), st["h%d" % min(n, 3)]))
        elif img:
            cerrar_parrafo(); cerrar_lista()
            p = os.path.join(carpeta, img.group(2))
            if os.path.exists(p):
                im = Image(p); r = min(150 * mm / im.imageWidth, 95 * mm / im.imageHeight)
                im.drawWidth, im.drawHeight = im.imageWidth * r, im.imageHeight * r
                flow.append(KeepTogether([im, Paragraph(inline(img.group(1)), st["cap"])]))
        elif m_ul or m_ol:
            cerrar_parrafo()
            if lista and ordenada != bool(m_ol):
                cerrar_lista()
            ordenada = bool(m_ol)
            lista.append((m_ul or m_ol).group(1))
        elif not l.strip():
            cerrar_parrafo(); cerrar_lista()
        else:
            cerrar_lista(); parrafo.append(l.strip())

    def pie(c, d):
        c.saveState(); c.setFont("Helvetica", 7.5); c.setFillColor(colors.grey)
        w = A4[0] - 40 * mm
        from reportlab.lib.utils import simpleSplit
        for i, linea in enumerate(simpleSplit(PIE, "Helvetica", 7.5, w)):
            c.drawString(20 * mm, 12 * mm - i * 9, linea)
        c.drawRightString(A4[0] - 20 * mm, 287 * mm, f"{meta['nombre']} · pág. {d.page}")
        c.restoreState()

    doc.build(flow, onFirstPage=pie, onLaterPages=pie)
    print(out)


if __name__ == "__main__":
    main()
