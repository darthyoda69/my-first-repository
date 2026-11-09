#!/usr/bin/env python3
"""Druckbare Preisliste Black Week 2026 (A4) aus black-week-2026-preise.csv."""
import csv
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether

HERE = Path(__file__).parent
OUT = HERE / "black-week-2026-preisliste.pdf"
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

INK, YEL = colors.HexColor("#0E0A04"), colors.HexColor("#FDBD13")
GROUPS = [  # (Überschrift, erste SKU der Gruppe)
    ("Seepferdchen", "1301"),
    ("Deutsches Schwimmabzeichen Bronze / Silber / Gold + Schwimmpass", "1311"),
    ("Frosch", "3001"),
    ("Seeräuber · Bobby · Seestern Stella · Pirat Pimpi", "1306"),
    ("Trixi · Stundenschwimmer (Totenkopf) · Lele Pahu", "1304"),
    ("Zubehör / Sonstiges", "4000"),
]
starts = {sku: name for name, sku in GROUPS}

rows = list(csv.DictReader((HERE / "black-week-2026-preise.csv").open(encoding="utf-8"), delimiter=";"))
groups, cur = [], None
for r in rows:
    if r["sku"] in starts:
        cur = [starts[r["sku"]], []]
        groups.append(cur)
    cur[1].append(r)

h1 = ParagraphStyle("h1", fontName="DVB", fontSize=20, leading=24, textColor=INK)
sub = ParagraphStyle("sub", fontName="DV", fontSize=9.5, leading=13, textColor=colors.HexColor("#444444"))
h2 = ParagraphStyle("h2", fontName="DVB", fontSize=12, leading=15, textColor=INK, spaceBefore=10, spaceAfter=4)
cell = ParagraphStyle("cell", fontName="DV", fontSize=8.5, leading=10.5)
cellb = ParagraphStyle("cellb", fontName="DVB", fontSize=8.5, leading=10.5)

def eur(v): return f"{v} €"
def rab(v): return "kein Rabatt" if v in ("0%", "") else v.replace("-", "−").replace("%", " %")

story = [Paragraph("Black Week 2026 – Preisliste", h1),
         Paragraph("pimpertz.de · Aktionszeitraum Mo 23.11. 10:30 Uhr (VIP) / Di 24.11. (alle) bis Di 01.12.2026, 23:59 Uhr · "
                   "Preise brutto inkl. 19 % USt., gelten ab dem 1. Stück · Mechanik: Preise im Shop gesenkt, keine Rabattcodes · "
                   "Konditionsstruktur identisch mit Black Week 2025.", sub), Spacer(1, 6)]
for name, items in groups:
    data = [["SKU", "Artikel", "Normal", "Black Week", "Rabatt"]]
    for r in items:
        disc = r["rabatt"] not in ("0%", "")
        data.append([r["sku"], Paragraph(r["artikel"], cell), eur(r["normalpreis_brutto"]),
                     Paragraph(eur(r["black_week_2026_brutto"]), cellb if disc else cell), rab(r["rabatt"])])
    t = Table(data, colWidths=[24*mm, 92*mm, 20*mm, 24*mm, 24*mm], repeatRows=1)
    st = [("FONT", (0, 0), (-1, -1), "DV", 8.5), ("FONT", (0, 0), (-1, 0), "DVB", 8.5),
          ("BACKGROUND", (0, 0), (-1, 0), INK), ("TEXTCOLOR", (0, 0), (-1, 0), YEL),
          ("ALIGN", (2, 0), (-1, -1), "RIGHT"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#DDDDDD")),
          ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for i, r in enumerate(items, start=1):
        if r["rabatt"] in ("0%", ""):
            st.append(("TEXTCOLOR", (0, i), (-1, i), colors.HexColor("#888888")))
    t.setStyle(TableStyle(st))
    story.append(KeepTogether([Paragraph(name, h2), t]) if len(items) <= 14 else Paragraph(name, h2))
    if len(items) > 14:
        story.append(t)

story += [Spacer(1, 10), Paragraph("Struktur: Kern-Rollenware + Schwimmpass + Urkunden −25 bis −34 % · Sets Abzeichen + Urkunde/Pass −15 bis −20 % · "
                                   "Easy −8 % · kinderleicht −5 bis −9 % · easy plus 0 bis −5 % · Glamour −15 bis −20 % · "
                                   "Seeräuber, Bobby, Seestern Stella, Pirat Pimpi (außer Starterkit), 50er-Pakete und Zubehör ohne Rabatt. "
                                   "Headline-Claim: „Bis zu −40 %“.", sub)]

def footer(c, d):
    c.saveState(); c.setFont("DV", 7.5); c.setFillColor(colors.HexColor("#888888"))
    c.drawString(15*mm, 10*mm, "pimpertz · Black Week 2026 · Stand 09.11.2026 · intern")
    c.drawRightString(A4[0]-15*mm, 10*mm, f"Seite {d.page}"); c.restoreState()

SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=15*mm, bottomMargin=18*mm,
                  title="Black Week 2026 – Preisliste", author="pimpertz").build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT, OUT.stat().st_size, "bytes")
