#!/usr/bin/env python3
"""Black Friday 2025 – realisierte Konditionen je SKU aus Shopify-Analytics.

Quelle: ShopifyQL `FROM sales … GROUP BY product_title, product_variant_sku`
- Baseline: 01.09.2025–16.11.2025 (Normalpreis-Phase)
- Black Week: 24.11.2025–02.12.2025 (Launch VIP 24.11. bis Ende 02.12.)
gross_sales in Shopify-Analytics ist netto (ohne 19 % USt). Stückpreise werden
als gross_sales / net_items_sold berechnet und mit 1,19 auf Brutto umgerechnet.
Aktueller Listenpreis: Shopify Admin API (productVariants), Stand 09.11.2026.
"""
import csv, json
from pathlib import Path

HERE = Path(__file__).parent
VAT = 1.19

baseline = json.loads((HERE / "data_baseline_2025-09-01_11-16.json").read_text())
bf = json.loads((HERE / "data_blackweek_2025-11-24_12-02.json").read_text())
prices = json.loads((HERE / "data_current_prices_2026-11-09.json").read_text())

def idx(rows):
    out = {}
    for title, sku, items, gross, disc, net, orders in rows:
        if not sku:
            continue
        out[sku] = dict(title=title, items=int(items), gross=float(gross), disc=float(disc), net=float(net), orders=int(orders))
    return out

B, F = idx(baseline), idx(bf)
P = {sku: float(p) for sku, p in prices.items()}

rows = []
for sku in sorted(set(B) | set(F), key=lambda s: -(F.get(s, {}).get("gross", 0))):
    b, f = B.get(sku), F.get(sku)
    title = (f or b)["title"]
    base_p = round(b["gross"] / b["items"] * VAT, 2) if b and b["items"] else None
    bf_p = round(f["gross"] / f["items"] * VAT, 2) if f and f["items"] else None
    cur = P.get(sku)
    ref = base_p or cur
    pct = round((bf_p / ref - 1) * 100) if (bf_p and ref) else None
    rows.append(dict(
        sku=sku, artikel=title,
        listenpreis_aktuell=cur,
        normalpreis_2025_realisiert=base_p,
        black_week_2025_realisiert=bf_p,
        rabatt_prozent=pct,
        stueck_black_week=f["items"] if f else 0,
        bestellungen_black_week=f["orders"] if f else 0,
        umsatz_netto_black_week=round(f["gross"], 2) if f else 0,
        stueck_baseline_11_wochen=b["items"] if b else 0,
    ))

with (HERE / "black_friday_2025_konditionen.csv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter=";")
    w.writeheader()
    for r in rows:
        w.writerow({k: (str(v).replace(".", ",") if isinstance(v, float) else v) for k, v in r.items()})

# Markdown
def eur(v): return f"{v:.2f} €".replace(".", ",") if v is not None else "–"
md = ["# Black Friday / Black Week 2025 – Konditionen je Artikel (pimpertz.de)", "",
      "Stand der Auswertung: 09.11.2026 · Quelle: Shopify Analytics + Admin API · Preise brutto inkl. 19 % USt.", "",
      "**Mechanik 2025:** Die Rabatte liefen über **gesenkte Listenpreise im Shop** (keine Rabattcodes). ",
      "Im Aktionszeitraum 17.11.–02.12. gingen 724 von 753 Bestellungen ohne Code raus; die wenigen Codes waren individuelle 5 %-Codes (Klaviyo/Welcome).", "",
      "Zeiträume: Normalpreis = Ø realisierter Preis 01.09.–16.11.2025 · Black Week = Ø realisierter Preis 24.11.–02.12.2025.", "",
      "## Top-Artikel nach Black-Week-Umsatz", "",
      "| SKU | Artikel | Listenpreis heute | Normalpreis 2025 | Black Week 2025 | Rabatt | Stück BW | Umsatz netto BW |",
      "|---|---|---:|---:|---:|---:|---:|---:|"]
for r in rows:
    if r["stueck_black_week"] >= 100 or r["umsatz_netto_black_week"] >= 200:
        md.append(f"| {r['sku']} | {r['artikel'][:60]} | {eur(r['listenpreis_aktuell'])} | {eur(r['normalpreis_2025_realisiert'])} | {eur(r['black_week_2025_realisiert'])} | {('%d %%' % r['rabatt_prozent']) if r['rabatt_prozent'] is not None else '–'} | {r['stueck_black_week']:,} | {eur(r['umsatz_netto_black_week'])} |".replace(",", "."))
md += ["", "## Alle Artikel", "", "Vollständige Liste mit allen SKUs: `black_friday_2025_konditionen.csv` (Semikolon-getrennt, Excel-ready).", "",
       "## Lesehilfe", "",
       "- *Normalpreis 2025 realisiert* kann leicht unter dem Listenpreis liegen (Welcome-Codes 5–10 %, Staffel-/Mengenbestellungen).",
       "- *Black Week 2025 realisiert* ist der tatsächlich bezahlte Ø-Stückpreis – also die echte Kondition, die Kund:innen gesehen haben.",
       "- Artikel mit wenigen Stück (< 20) sind statistisch wacklig, dort lieber den Listenpreis als Referenz nehmen.",
       ]
(HERE / "black_friday_2025_konditionen.md").write_text("\n".join(md), encoding="utf-8")
print(f"{len(rows)} SKUs geschrieben")
for r in rows[:12]:
    print(f"{r['sku']:10s} {eur(r['normalpreis_2025_realisiert']):>8} -> {eur(r['black_week_2025_realisiert']):>8}  ({r['rabatt_prozent']} %)  {r['stueck_black_week']} Stk")
