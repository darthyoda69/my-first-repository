#!/usr/bin/env python3
"""
pimpertz – Klaviyo Relaunch 2026: Template-Generator.

Baut alle neuen E-Mail-Templates (Flows + Black Week 2026) aus EINEM
Design-System, damit Farben, Typo, Abstände und Footer überall identisch sind.

Design-Basis: mailsupply Master Bundle (Josh Rauer, ex-SNOCKS), "Bite Pack"
Layout-Logik (farbiger Hero-Block mit großer Headline, Code-Box, Pill-Button,
nummerierte FAQ, Review-Block, heller Footer) – übersetzt in die pimpertz-CI
(Schwarz #0E0A04, Gelb #FDBD13, Orange #FF7500, Poppins/Archivo).

Aufruf:  python3 build_templates.py   -> schreibt templates/*.html
"""
from pathlib import Path

OUT = Path(__file__).parent / "templates"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Design-Tokens
INK = "#0E0A04"
YELLOW = "#FDBD13"
ORANGE = "#FF7500"
WATER = "#E3F2FB"      # helles Wasserblau (Footer / ruhige Flächen)
POOL = "#0B6FB8"       # Akzentblau für Links
WHITE = "#FFFFFF"
GREY = "#6B6B6B"
FONT = "'Poppins', Arial, 'Helvetica Neue', Helvetica, sans-serif"
FONT_H = "'Archivo', 'Poppins', Arial, Helvetica, sans-serif"

LOGO = "https://d3k81ch9hvuctc.cloudfront.net/company/Xrfryr/images/44898588-67aa-4cfe-9055-ed23f006730c.png"
HERO_BOX = "https://d3k81ch9hvuctc.cloudfront.net/company/Xrfryr/images/699d58cc-be72-4b9d-a38d-903542aa18f4.png"
HERO_DUO = "https://d3k81ch9hvuctc.cloudfront.net/company/Xrfryr/images/1990dd20-bd63-4a8f-aa1f-c0c9866b77ef.png"
CDN = "https://cdn.shopify.com/s/files/1/0940/6604/9288/files/"
SHOP = "https://pimpertz.de"

P = {  # Produkte (Bild, URL)
    "seep_rolle": (CDN + "Seepferdchen_Abzeichen_in_Rollenware.png?v=1747937648", SHOP + "/products/seepferdchen-abzeichen"),
    "seep_buegel": (CDN + "Schwimmabzeichen_Bilder_pimpertz.de.png?v=1755008174", SHOP + "/products/seepferdchen-abzeichen-zum-aufbuegeln"),
    "seep_set": (CDN + "Produktbilder_pimpertz.de_3_d7599bb9-bb4d-48ae-b175-c7e56d3e98b2.png?v=1747834882", SHOP + "/products/seepferdchen-abzeichen-zum-aufbuegeln-urkunde-set"),
    "urkunde": (CDN + "Produktbilder_pimpertz.de_4.png?v=1747834882", SHOP + "/products/seepferdchen-abzeichen-urkunde"),
    "pass": (CDN + "deutscher-schwimmpass.jpg?v=1742473297", SHOP + "/products/deutscher-schwimmpass"),
    "bronze_rolle": (CDN + "Produktbilder_pimpertz.de.png?v=1744878121", SHOP + "/products/schwimmabzeichen-bronze"),
    "bronze_set": (CDN + "pz-1361SP-set-djsa-easyplus-850x850.png?v=1745309385", SHOP + "/products/schwimmabzeichen-bronze-zum-aufbuegeln-set"),
    "glamour": (CDN + "pz_1301GW_sa-fruehschwimmer-glamour-weiss-850x850-1.png?v=1744705046", SHOP + "/products/seepferdchen-abzeichen-glamour-weiss"),
    "trixi": (CDN + "pz_1304P_Trixi-Abzeichen-easy-plus_Vielseitigkeitsabzeichen.png?v=1744125606", SHOP + "/products/trixi-schwimmabzeichen-zum-aufbuegeln"),
}

GREETING = "Hallo{% if first_name %} {{ first_name }}{% endif %},"


# ---------------------------------------------------------------- Bausteine
def doc(title: str, preheader: str, body: str, bg: str = "#F4F4F4") -> str:
    return f"""<!DOCTYPE html>
<html lang="de" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting"><title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
 body{{margin:0;padding:0;background:{bg};}} table{{border-collapse:collapse;}} img{{border:0;display:block;max-width:100%;height:auto;}}
 a{{color:{POOL};}} .btn a{{text-decoration:none!important;}}
 @media only screen and (max-width:480px){{ .px{{padding-left:20px!important;padding-right:20px!important;}} .h1{{font-size:34px!important;}} .col{{display:block!important;width:100%!important;}} }}
</style>
</head>
<body style="margin:0;padding:0;background:{bg};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{preheader}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" width="100%" style="background:{bg};"><tr><td align="center" style="padding:0;">
<table role="presentation" width="600" style="width:600px;max-width:600px;background:{WHITE};">
{body}
</table></td></tr></table>
</body></html>"""


def header(bg=INK) -> str:
    return f"""<tr><td align="center" style="background:{bg};padding:26px 0;">
<a href="{SHOP}"><img src="{LOGO}" width="170" alt="pimpertz – Offizielle Schwimmabzeichen" style="width:170px;"></a></td></tr>"""


def hero(kicker: str, headline: str, sub: str = "", bg=YELLOW, fg=INK, img: str | None = None, img_link=SHOP) -> str:
    kick = f'<div style="font:600 14px/1.4 {FONT};letter-spacing:2px;text-transform:uppercase;color:{fg};opacity:.85;">{kicker}</div>' if kicker else ""
    subh = f'<div style="font:400 17px/1.5 {FONT};color:{fg};padding-top:14px;">{sub}</div>' if sub else ""
    pic = f'<tr><td style="padding:0 30px 30px;background:{bg};"><a href="{img_link}"><img src="{img}" width="540" alt="" style="width:100%;border-radius:18px;"></a></td></tr>' if img else ""
    return f"""<tr><td class="px" align="center" style="background:{bg};padding:44px 40px 30px;">
{kick}<div class="h1" style="font:800 44px/1.05 {FONT_H};color:{fg};padding-top:10px;">{headline}</div>{subh}</td></tr>{pic}"""


def text(html: str, align="left", bg=WHITE, pad="10px 40px", size=16) -> str:
    return f'<tr><td class="px" align="{align}" style="background:{bg};padding:{pad};font:400 {size}px/1.6 {FONT};color:{INK};">{html}</td></tr>'


def button(label: str, href: str, bg=INK, fg=WHITE, wrap_bg=WHITE, pad="18px 40px 30px") -> str:
    return f"""<tr><td align="center" style="background:{wrap_bg};padding:{pad};">
<table role="presentation" class="btn" style="border-collapse:separate;"><tr><td align="center" style="background:{bg};border-radius:999px;border:2px solid {INK};">
<a href="{href}" style="display:inline-block;padding:16px 38px;font:700 16px/1 {FONT};color:{fg};text-decoration:none;">{label}</a>
</td></tr></table></td></tr>"""


def code_box(code: str, label="Dein Code:", bg=WHITE) -> str:
    return f"""<tr><td align="center" style="background:{bg};padding:6px 40px 4px;">
<div style="font:400 13px/1.4 {FONT};color:{INK};letter-spacing:1px;">{label}</div>
<div style="display:inline-block;margin-top:8px;padding:12px 28px;border:2px dashed {INK};border-radius:12px;font:800 26px/1 'Courier New',monospace;color:{INK};letter-spacing:3px;">{code}</div>
</td></tr>"""


def divider(color=YELLOW) -> str:
    return f'<tr><td align="center" style="padding:18px 0;"><div style="width:120px;border-top:3px solid {color};font-size:1px;line-height:1px;">&nbsp;</div></td></tr>'


def usp_row(items) -> str:
    cells = "".join(
        f'<td class="col" width="{int(100/len(items))}%" align="center" valign="top" style="padding:10px 8px;">'
        f'<div style="font:800 26px/1 {FONT_H};color:{ORANGE};">{i+1}</div>'
        f'<div style="font:700 15px/1.3 {FONT};color:{INK};padding-top:8px;">{t}</div>'
        f'<div style="font:400 13px/1.45 {FONT};color:{GREY};padding-top:4px;">{d}</div></td>'
        for i, (t, d) in enumerate(items))
    return f'<tr><td class="px" style="padding:10px 30px 20px;"><table role="presentation" width="100%"><tr>{cells}</tr></table></td></tr>'


def faq(title: str, items) -> str:
    rows = "".join(
        f'<tr><td align="center" style="padding:14px 40px 4px;"><div style="display:inline-block;width:30px;height:30px;line-height:30px;border-radius:50%;background:{YELLOW};font:700 14px/30px {FONT};color:{INK};">{i+1}</div>'
        f'<div style="font:700 18px/1.3 {FONT_H};color:{INK};padding-top:8px;">{q}</div>'
        f'<div style="font:400 15px/1.5 {FONT};color:{GREY};padding-top:4px;">{a}</div></td></tr>'
        for i, (q, a) in enumerate(items))
    return f'<tr><td align="center" style="padding:36px 40px 4px;font:800 32px/1.1 {FONT_H};color:{INK};">{title}</td></tr>{rows}'


def review(quote: str, name: str, product: str) -> str:
    return f"""<tr><td class="px" style="padding:26px 40px;">
<table role="presentation" width="100%" style="border:3px solid {ORANGE};border-radius:16px;"><tr><td align="center" style="padding:26px 28px;">
<div style="color:{YELLOW};font-size:22px;letter-spacing:5px;">★★★★★</div>
<div style="font:400 17px/1.5 {FONT};color:{INK};padding-top:12px;">„{quote}“</div>
<div style="font:600 14px/1.4 {FONT};color:{INK};padding-top:12px;">{name} · <span style="color:{GREY};font-weight:400;">verifizierter Kauf</span></div>
<div style="font:400 13px/1.4 {FONT};color:{GREY};padding-top:4px;">{product}</div>
</td></tr></table></td></tr>"""


def products(items, bg=WHITE, show_price=True) -> str:
    """items: (key, name, price_text, old_price_text|None)"""
    cells = []
    for key, name, price, old in items:
        img, url = P[key]
        old_html = f'<span style="text-decoration:line-through;color:{GREY};font-weight:400;">{old}</span>&nbsp;' if old else ""
        price_html = f'<div style="font:700 16px/1.3 {FONT};color:{INK};padding-top:4px;">{old_html}{price}</div>' if show_price and price else ""
        cells.append(
            f'<td class="col" width="{int(100/len(items))}%" valign="top" align="center" style="padding:8px;">'
            f'<a href="{url}"><img src="{img}" width="170" alt="{name}" style="width:100%;max-width:170px;border-radius:12px;background:#fff;"></a>'
            f'<div style="font:600 14px/1.35 {FONT};color:{INK};padding-top:10px;">{name}</div>{price_html}'
            f'<div style="padding-top:8px;"><a href="{url}" style="font:700 13px/1 {FONT};color:{INK};">Ansehen →</a></div></td>')
    return f'<tr><td class="px" style="background:{bg};padding:10px 24px 24px;"><table role="presentation" width="100%"><tr>{"".join(cells)}</tr></table></td></tr>'


def footer() -> str:
    return f"""<tr><td align="center" style="background:{WATER};padding:34px 40px;font:400 12px/1.6 {FONT};color:{GREY};">
<img src="{LOGO}" width="110" alt="pimpertz" style="width:110px;background:{INK};padding:8px 12px;border-radius:8px;margin-bottom:14px;">
<div><strong style="color:{INK};">Offizielle Schwimmabzeichen seit 25 Jahren</strong><br>Schneller Versand aus Nagold · Kauf auf Rechnung für Vereine &amp; Schulen</div>
<div style="padding-top:12px;">{{{{ organization.name }}}} · {{{{ organization.full_address }}}}</div>
<div style="padding-top:8px;">Du erhältst diese E-Mail, weil du dich bei pimpertz angemeldet hast. {{% unsubscribe 'Hier abmelden' %}} · {{% manage_preferences 'Einstellungen' %}}</div>
</td></tr>"""


# ---------------------------------------------------------------- Templates
T = {}

# ============ FLOWS (Challenger-Varianten für A/B gegen die bestehenden Mails)
T["FLOW_Welcome_E1_Challenger"] = ("Willkommen bei pimpertz – dein Code wartet",
 "Offizielle Schwimmabzeichen, schnell geliefert – und 10 % auf deine erste Bestellung.",
 header() + hero("Willkommen im Team", "Hier sind 10&nbsp;% für den ersten Schwimmerfolg.",
   "Ob Seepferdchen, Bronze oder Gold – bei uns bekommst du die offiziellen Abzeichen in jeder Ausführung.", img=HERO_BOX)
 + code_box("WILLKOMMEN10", bg=YELLOW)  # TODO: Code muss in Shopify existieren (oder durch {% coupon_code %} ersetzen)
 + button("Jetzt einlösen", SHOP + "/collections/all", wrap_bg=YELLOW)
 + text(f"<p>{GREETING}</p><p>schön, dass du da bist! Wir sind pimpertz aus Nagold und liefern seit 25 Jahren offizielle Schwimmabzeichen an Familien, Schwimmschulen und Vereine in ganz Deutschland.</p><p>Damit du direkt das Richtige findest, hier die drei Fragen, die wir am häufigsten hören:</p>", pad="34px 40px 0")
 + faq("Du fragst. Wir antworten.", [
   ("Aufnähen, aufbügeln oder aufkleben?", "Rollenware zum Aufnähen ist der Klassiker. <strong>easy plus</strong> bügelst du in 30 Sekunden auf, <strong>kinderleicht</strong> klebt ohne Bügeleisen."),
   ("Sind die Abzeichen offiziell?", "Ja – alle Abzeichen und Urkunden entsprechen der Deutschen Prüfungsordnung Schwimmen."),
   ("Wie schnell ist meine Bestellung da?", "Wir verschicken direkt aus unserem Lager in Nagold – schnell und zuverlässig.")])
 + button("Zu den Bestsellern", SHOP + "/collections/all")
 + products([("seep_set", "Seepferdchen-Set mit Urkunde", "", None), ("pass", "Deutscher Schwimmpass", "", None), ("glamour", "Seepferdchen Glamour", "", None)], show_price=False)
 + review("Ein super tolles Team, hervorragende Qualität und natürlich eine schnelle Lieferung.", "Benjamin D.", "Stundenschwimmer-Abzeichen")
 + footer())

T["FLOW_Warenkorb_E1_Challenger"] = ("Dein Warenkorb wartet auf dich",
 "Du hast etwas liegen lassen – wir haben es für dich aufgehoben.",
 header() + hero("Kurze Erinnerung", "Fast geschafft – wie die letzte Bahn.", "Dein Warenkorb ist gespeichert. Ein Klick, und das Abzeichen ist unterwegs.", bg=WATER)
 + f"""<tr><td align="center" style="padding:30px 40px 0;">
{{% if event.AddedItemImageURL %}}<a href="{{{{ event.AddedItemURL|default:'{SHOP}/cart' }}}}"><img src="{{{{ event.AddedItemImageURL }}}}" width="260" alt="" style="width:260px;border-radius:16px;"></a>{{% endif %}}
<div style="font:700 20px/1.3 {FONT};color:{INK};padding-top:16px;">{{{{ event.AddedItemProductName|default:'Dein Schwimmabzeichen' }}}}</div>
</td></tr>"""
 + button("Zurück zum Warenkorb", "{{ event.CheckoutURL|default:'" + SHOP + "/cart' }}")
 + text(f"<p>{GREETING}</p><p>du hast dir etwas ausgesucht, aber die Bestellung noch nicht abgeschlossen. Kein Stress – dein Warenkorb ist gespeichert.</p>")
 + usp_row([("Offiziell", "Nach Deutscher Prüfungsordnung"), ("Schnell", "Versand direkt aus Nagold"), ("Auf Rechnung", "Für Vereine &amp; Schulen")])
 + review("Ein super tolles Team, hervorragende Qualität und natürlich eine schnelle Lieferung.", "Benjamin D.", "Stundenschwimmer-Abzeichen")
 + footer())

T["FLOW_Checkout_E1_Challenger"] = ("Du warst fast fertig ✓",
 "Deine Bestellung ist nur einen Klick entfernt.",
 header() + hero("Checkout gespeichert", "Nur noch ein Klick bis zum Ziel.", "Deine Artikel liegen bereit:", bg=YELLOW)
 + f"""<tr><td class="px" style="padding:24px 40px 0;"><table role="presentation" width="100%">
{{% for item in event.extra.line_items|slice:':3' %}}<tr>
<td width="90" style="padding:8px 0;">{{% if item.product.images.0.src %}}<img src="{{{{ item.product.images.0.src }}}}" width="80" alt="" style="width:80px;border-radius:10px;">{{% endif %}}</td>
<td style="padding:8px 12px;font:600 15px/1.4 {FONT};color:{INK};">{{{{ item.product.title }}}}<br><span style="font-weight:400;color:{GREY};">Menge: {{{{ item.quantity|floatformat:0 }}}}</span></td></tr>{{% endfor %}}
</table></td></tr>"""
 + button("Bestellung abschließen", "{{ event.extra.checkout_url|default:'" + SHOP + "/cart' }}")
 + text(f"<p>{GREETING}</p><p>bei der Bestellung ist etwas dazwischengekommen? Vereine und Schulen können bei uns bequem <strong>auf Rechnung</strong> bestellen – einfach im Checkout auswählen. Fragen? Antworte direkt auf diese Mail, wir melden uns persönlich.</p>")
 + usp_row([("Offiziell", "Nach Deutscher Prüfungsordnung"), ("Schnell", "Versand direkt aus Nagold"), ("Persönlich", "Echter Support aus Nagold")])
 + footer())

T["FLOW_Produktsuche_E1_Challenger"] = ("Noch auf der Suche nach dem richtigen Abzeichen?",
 "Wir helfen dir, die passende Ausführung zu finden.",
 header() + hero("Gesehen &amp; gemerkt", "Das passende Abzeichen für jeden Erfolg.", "Du hast dir {{ event.ProductName|default:'unsere Abzeichen' }} angesehen – hier ist alles, was du wissen musst.", bg=WATER)
 + f"""<tr><td align="center" style="padding:28px 40px 0;">{{% if event.ImageURL %}}<a href="{{{{ event.URL|default:'{SHOP}' }}}}"><img src="{{{{ event.ImageURL }}}}" width="260" alt="" style="width:260px;border-radius:16px;"></a>{{% endif %}}</td></tr>"""
 + button("Nochmal ansehen", "{{ event.URL|default:'" + SHOP + "' }}")
 + faq("Welche Ausführung passt?", [
   ("Rollenware", "Zum Aufnähen – der günstige Klassiker, ideal für Vereine und große Mengen."),
   ("easy plus", "Zum Aufbügeln – hält auch nach vielen Wäschen, in 30 Sekunden fertig."),
   ("kinderleicht", "Zum Aufkleben – ganz ohne Bügeleisen, perfekt für Eltern.")])
 + products([("seep_rolle", "Seepferdchen Rollenware", "", None), ("seep_buegel", "Seepferdchen easy plus", "", None), ("seep_set", "Set mit Urkunde", "", None)], show_price=False)
 + footer())

T["FLOW_PostPurchase_CrossSell_Challenger"] = ("Das nächste Abzeichen wartet schon",
 "Nach dem Seepferdchen ist vor Bronze – alles für die nächste Etappe.",
 header() + hero("Danke für deine Bestellung", "Nach dem Seepferdchen ist vor Bronze.", "Damit der nächste Erfolg gleich gefeiert werden kann – hier die nächsten Etappen:", bg=YELLOW, img=HERO_DUO)
 + products([("bronze_set", "Bronze-Set mit Schwimmpass", "", None), ("pass", "Deutscher Schwimmpass", "", None), ("trixi", "Seehund Trixi", "", None)], show_price=False)
 + button("Alle Abzeichen entdecken", SHOP + "/collections/all")
 + text(f"<p>{GREETING}</p><p><strong>Für Vereine &amp; Schwimmschulen:</strong> Du bestellst regelmäßig? Antworte einfach auf diese Mail – wir richten dir gern eine Sammelbestellung auf Rechnung ein.</p>", pad="10px 40px 30px")
 + footer())

# ============ BLACK WEEK 2026
BW_PRICES = [  # (key, Name, BW-Preis, Normalpreis)
    ("seep_rolle", "Seepferdchen Rollenware", "0,59 €", "0,85 €"),
    ("pass", "Deutscher Schwimmpass", "0,67 €", "1,00 €"),
    ("seep_set", "Seepferdchen-Set easy plus + Urkunde", "1,12 €", "1,95 €"),
]
BW_PRICES_2 = [
    ("urkunde", "Seepferdchen Urkunde", "0,44 €", "0,60 €"),
    ("bronze_rolle", "Bronze/Silber/Gold Rollenware", "0,59 €", "0,85 €"),
    ("bronze_set", "Bronze-Set easy plus + Pass", "1,34 €", "2,25 €"),
]
BW_URL = SHOP + "/collections/black-week"   # TODO: Collection in Shopify anlegen
VIP_URL = SHOP + "/pages/black-week-vip"     # TODO: Landingpage oder Collection

def bw_header() -> str:
    return header(INK)

T["BW26_01_Oops_Intern_Di_10-11"] = ("WG: Black Week Preise final – NICHT WEITERLEITEN",
 "Intern: Freigabe der Black-Week-Preise 2026 (Stand heute)",
 # bewusst „nüchtern“: sieht aus wie eine interne Mail, kein Hero, kein Design
 f"""<tr><td style="padding:28px 32px 0;font:400 14px/1.6 Arial,Helvetica,sans-serif;color:#222;">
<div style="color:#888;font-size:12px;border-bottom:1px solid #e5e5e5;padding-bottom:12px;margin-bottom:16px;">
<strong>Von:</strong> Team pimpertz &lt;anna@team.pimpertz.de&gt;<br><strong>An:</strong> intern-vertrieb<br><strong>Betreff:</strong> WG: Black Week Preise final – NICHT WEITERLEITEN</div>
<p>Hi zusammen,</p>
<p>anbei wie besprochen die finalen Black-Week-Preise. Ziel bleibt: <strong>günstiger als die Verbandsshops</strong> – auf die großen Mengen, die Vereine und Schwimmschulen für die Saison brauchen.</p>
<table role="presentation" width="100%" style="border:1px solid #ddd;font:400 13px/1.5 Arial,Helvetica,sans-serif;">
<tr style="background:#f3f3f3;"><td style="padding:6px 8px;"><strong>Artikel</strong></td><td style="padding:6px 8px;"><strong>aktuell</strong></td><td style="padding:6px 8px;"><strong>Black Week</strong></td></tr>
<tr><td style="padding:6px 8px;">Seepferdchen Rollenware</td><td style="padding:6px 8px;">0,85 €</td><td style="padding:6px 8px;"><strong>0,59 €</strong></td></tr>
<tr><td style="padding:6px 8px;">Deutscher Schwimmpass</td><td style="padding:6px 8px;">1,00 €</td><td style="padding:6px 8px;"><strong>0,67 €</strong></td></tr>
<tr><td style="padding:6px 8px;">Seepferdchen Urkunde</td><td style="padding:6px 8px;">0,60 €</td><td style="padding:6px 8px;"><strong>0,44 €</strong></td></tr>
<tr><td style="padding:6px 8px;">Set Seepferdchen easy plus + Urkunde</td><td style="padding:6px 8px;">1,95 €</td><td style="padding:6px 8px;"><strong>1,12 €</strong></td></tr>
<tr><td style="padding:6px 8px;">Bronze/Silber/Gold Rollenware</td><td style="padding:6px 8px;">0,85 €</td><td style="padding:6px 8px;"><strong>0,59 €</strong></td></tr>
<tr><td style="padding:6px 8px;">Set Bronze easy plus + Pass</td><td style="padding:6px 8px;">2,25 €</td><td style="padding:6px 8px;"><strong>1,34 €</strong></td></tr>
</table>
<p style="padding-top:12px;">Start: <strong>Mo 23.11., 12:00 Uhr für die VIP-Liste</strong> (24h früher), ab Di 24.11. für alle. Rollenware war letztes Jahr unser Bestseller – bitte nichts vorher rausgeben.</p>
<p>Danke &amp; Grüße<br>Anna</p>
<div style="margin-top:22px;padding:16px;border-left:4px solid {YELLOW};background:#FFF8E1;color:{INK};">
<strong>P.S. von uns an dich:</strong> Ups – die war eigentlich nicht für dich gedacht. 🙈 Aber jetzt, wo du sie schon gelesen hast:
<a href="{VIP_URL}" style="color:{INK};font-weight:700;">Sicher dir hier den 24h-Früher-Zugang</a>. Wir sagen auch niemandem was.</div>
</td></tr>
<tr><td style="padding:24px 32px 30px;font:400 11px/1.6 Arial,Helvetica,sans-serif;color:#999;">{{{{ organization.name }}}} · {{{{ organization.full_address }}}}<br>{{% unsubscribe 'Abmelden' %}}</td></tr>""")

T["BW26_02_VIP_EarlyAccess_Mo_23-11"] = ("Dein VIP-Zugang ist offen",
 "24 Stunden früher als alle anderen: die Black-Week-Preise sind live.",
 bw_header() + hero("Nur für VIPs · 24h früher", "Black Week.<br><span style='color:" + YELLOW + "'>Für dich schon jetzt.</span>",
   "Die besten Preise des Jahres auf offizielle Schwimmabzeichen – bevor alle anderen sie sehen.", bg=INK, fg=WHITE, img=HERO_BOX)
 + button("VIP-Zugang öffnen", VIP_URL, bg=YELLOW, fg=INK, wrap_bg=INK)
 + text(f"<p>{GREETING}</p><p>wie versprochen: Du bist früher dran. Ab jetzt gelten die Black-Week-Preise für dich – morgen um 12 Uhr öffnen wir für alle. Tipp: Die <strong>Seepferdchen-Rollenware</strong> war letztes Jahr unser Black-Week-Bestseller.</p>", pad="34px 40px 0")
 + products(BW_PRICES) + products(BW_PRICES_2)
 + button("Jetzt zuschlagen", VIP_URL)
 + footer())

T["BW26_03_Launch_Alle_Di_24-11"] = ("Black Week ist live: bis zu –42 % auf Schwimmabzeichen",
 "Die besten Preise des Jahres – solange der Vorrat reicht.",
 bw_header() + hero("Black Week 2026", "Bis zu <span style='color:" + YELLOW + "'>–42&nbsp;%</span> auf offizielle Schwimmabzeichen.",
   "Seepferdchen, Schwimmpass, Urkunden &amp; Sets – so günstig wie nie.", bg=INK, fg=WHITE, img=HERO_DUO)
 + button("Zur Black Week", BW_URL, bg=YELLOW, fg=INK, wrap_bg=INK)
 + products(BW_PRICES) + products(BW_PRICES_2)
 + usp_row([("Offiziell", "Nach Deutscher Prüfungsordnung"), ("Für Vereine", "Kauf auf Rechnung"), ("Schnell", "Versand direkt aus Nagold")])
 + review("Ein super tolles Team, hervorragende Qualität und natürlich eine schnelle Lieferung.", "Benjamin D.", "Stundenschwimmer-Abzeichen")
 + footer())

T["BW26_04_BlackFriday_Vereine_Fr_27-11"] = ("Black Friday: Abzeichen für die ganze Saison sichern",
 "Für Vereine, Schulen und Schwimmschulen: jetzt den Jahresbedarf zum Bestpreis.",
 bw_header() + hero("Black Friday · Für Vereine &amp; Schwimmschulen", "Einmal bestellen. Die ganze Saison versorgt.",
   "Die Prüfungen 2027 kommen bestimmt – mit den Black-Friday-Preisen deckst du deinen Jahresbedarf jetzt am günstigsten.", bg=YELLOW, fg=INK)
 + text("<p><strong>Rechenbeispiel Schwimmschule:</strong> 500 Seepferdchen (Rollenware) + 500 Urkunden<br>Normal: <span style='text-decoration:line-through;'>725,00 €</span> → Black Friday: <strong>515,00 €</strong> – du sparst <strong>210,00 €</strong>.</p>", pad="30px 40px 0")
 + products(BW_PRICES)
 + button("Jahresbedarf sichern", BW_URL)
 + faq("Gut zu wissen", [
   ("Kauf auf Rechnung?", "Ja – für Vereine, Schulen und Behörden einfach im Checkout auswählen."),
   ("Lieferzeit bei großen Mengen?", "Auch große Mengen verschicken wir direkt aus unserem Lager in Nagold."),
   ("Gilt der Preis für jede Menge?", "Ja, die Black-Week-Preise gelten ab dem ersten Stück – bis zum 01.12.")])
 + footer())

T["BW26_05_CyberMonday_Mo_30-11"] = ("Cyber Monday: der letzte große Tag",
 "Heute noch alle Black-Week-Preise – morgen ist Schluss.",
 bw_header() + hero("Cyber Monday", "Letzter großer Tag.<br>Alle Preise. Noch heute.", "Ab morgen gelten wieder die regulären Preise.", bg=INK, fg=WHITE)
 + button("Jetzt noch sparen", BW_URL, bg=YELLOW, fg=INK, wrap_bg=INK)
 + text(f"<p>{GREETING}</p><p>die Black Week geht in die letzte Runde. Wenn du für Weihnachten, den nächsten Schwimmkurs oder die Saison 2027 vorsorgen willst: <strong>heute ist der Tag</strong>.</p>", pad="30px 40px 0")
 + products(BW_PRICES)
 + footer())

T["BW26_06_LastChance_Di_01-12"] = ("Letzte Chance: heute um Mitternacht ist Schluss",
 "Nur noch heute: die Black-Week-Preise auf Schwimmabzeichen.",
 bw_header() + hero("Nur noch heute", "LETZTE CHANCE.", "Um 23:59 Uhr enden die Black-Week-Preise.", bg=ORANGE, fg=WHITE)
 + button("Letzte Chance nutzen", BW_URL, bg=INK, fg=WHITE, wrap_bg=ORANGE)
 + products(BW_PRICES) + products(BW_PRICES_2)
 + footer())

# ---------------------------------------------------------------- schreiben
if __name__ == "__main__":
    for name, (subject, pre, body) in T.items():
        html = doc(subject, pre, body)
        (OUT / f"{name}.html").write_text(html, encoding="utf-8")
        print(f"{name:45s} {len(html):6d} chars | {subject}")
