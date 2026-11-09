# Black Week 2026 – Arbeits-Briefing (pimpertz.de)

Stand 09.11.2026. Ansprechpartner: Leon.

## 1. Fahrplan

| Datum | Was | Kanal | Ziel |
|---|---|---|---|
| Di 10.11. | Teaser-Mail (Plaintext, wirkt wie weitergeleitete interne Mail) | Klaviyo | Traffic auf Landingpage, VIP-Eintragungen |
| Do 12.11. | Auflösungs-Mail „Ups“ | Klaviyo | zweite Welle VIP-Eintragungen |
| **Mo 23.11., 10:30 Uhr** | **VIP-Zugang öffnet** (24 h vor allen anderen) | Mail an VIP-Liste + Landingpage schaltet um | Vereine/Schwimmschulen decken Jahresbedarf |
| Di 24.11. | Launch für alle | Mail + Shop-Preise live | Volumen |
| Fr 27.11. | Black Friday – Angle „Jahresbedarf für Vereine“ | Mail | Großbestellungen |
| Mo 30.11. | Cyber Monday | Mail | Nachzügler |
| Di 01.12., 23:59 Uhr | Ende – „Last Chance“ | Mail | Abschluss |

## 2. Preise Black Week 2026 (brutto, gelten ab dem 1. Stück)

| SKU | Artikel | Normalpreis | Black Week | Rabatt |
|---|---|---:|---:|---:|
| 1301 | Seepferdchen Abzeichen (Rollenware) | 0,85 € | **0,59 €** | −31 % |
| 1360 | Deutscher Schwimmpass | 1,00 € | **0,67 €** | −33 % |
| 1350 | Seepferdchen Urkunde | 0,60 € | **0,44 €** | −27 % |
| 1350SP | Set Seepferdchen easy plus + Urkunde | 1,95 € | **1,12 €** | −42 % |
| 1311 / 1312 / 1313 | Bronze / Silber / Gold (Rollenware) | 0,85 € | **0,59 €** | −31 % |
| 1361SP | Set Bronze easy plus + Schwimmpass | 2,25 € | **1,34 €** | −40 % |

Headline-Claim: **„Bis zu −42 %“** (nie höher). Weitere Artikel folgen, sobald freigegeben. Streichpreise müssen dem niedrigsten Preis der letzten 30 Tage entsprechen (§ 11 PAngV) – also vor dem 23.11. keine Preise senken.

Mechanik wie 2025: **Preise werden im Shop gesenkt, keine Rabattcodes.**

## 3. Landingpages – Anforderungen

### `/pages/black-week` (existiert als Entwurf in Shopify, unveröffentlicht)
- Countdown bis **Mo 23.11.2026, 10:30 Uhr** (Europe/Berlin). Danach automatisch: „Die Black Week ist live“ + Button zu `/collections/black-week`.
- VIP-Formular (Vorname optional + E-Mail) → schreibt in Klaviyo-Liste **„VIP Pre-Sale 24h“** (List-ID `Syrjty`, Company-ID `Xrfryr`, Klaviyo Client-API). Ist im Entwurf bereits verdrahtet.
- Preisvorschau der 6 Artikel oben, drei USP-Kacheln (Offiziell nach Deutscher Prüfungsordnung · Seit 25 Jahren, Versand aus Nagold · Für Vereine: Kauf auf Rechnung, Rollenware).
- Look: Schwarz `#0E0A04`, Gelb `#FDBD13`, Orange `#FF7500` (sparsam), Wasserblau `#E3F2FB`, Poppins. Mobile first (die meisten öffnen die Mail am Handy).
- Quelle: Repo `klaviyo-relaunch-2026/landingpage/black-week.html`.

### `/collections/black-week` (muss bis Mo 23.11. existieren)
- Enthält genau die rabattierten Artikel. Sortierung: Seepferdchen Rolle, Schwimmpass, Urkunde, Set Seepferdchen, Bronze/Silber/Gold Rolle, Set Bronze.
- Header-Banner im Black-Week-Look (Canva-Kit „Sale“), Countdown bis Di 01.12. 23:59 wäre ein Plus.

### Optional: `/pages/black-week-vip`
- Nur, wenn wir VIPs eine eigene Seite geben wollen; sonst reicht `/pages/black-week`, die am Montag um 10:30 umschaltet.

## 4. Assets

- **Canva-Kits (on-brand, fertig):** Sale/Black Week `pimpertz · Sale · 2026`, Flows: Pulse, Bite, Spa, Muse, Ease – alle im Canva-Team unter „pimpertz · … · 2026“.
- **Bildwelt:** 12 neue Motive in Canva (Präfix `pz26_`): Kind mit Seepferdchen am Pool, Aufbügeln, Trainer mit Urkunden, Flatlay auf Fliesen, zwei Black-Week-Produktshots (schwarz/gelb), Hoodie, Glamour, Schwimmer mit Bronze-Set, Unterwasser-Banner, Fliesen-Textur, High-Five.
- **Logo:** `pz26_logo_pimpertz` (für dunklen Grund gemacht – auf hellem Grund auf schwarze Fläche setzen).
- **Produkt-Freisteller:** `pz26_prod_*` (Seepferdchen Rolle, easy plus, Set + Urkunde, Urkunde, Schwimmpass, Set Bronze + Pass, Glamour Weiß).

## 5. Copy-Regeln

- Du-Form, warm, klar, kurz. Keine Großbuchstaben-Schreierei.
- **Keine Wettbewerber nennen** – kein „Verband“, kein „günstiger als …“.
- Keine Behauptungen, die wir nicht halten: kein „Versand am nächsten Werktag“, keine erfundenen Bewertungen/Siegel, keine falsche Knappheit.
- Erlaubt: „Offizielle Abzeichen nach Deutscher Prüfungsordnung“, „Seit 25 Jahren“, „Versand direkt aus Nagold“, „Kauf auf Rechnung für Vereine“, echte Bewertung Benjamin D. („Ein super tolles Team, hervorragende Qualität und natürlich eine schnelle Lieferung.“).
- Begriffe für Ausführungen: **Rollenware** (aufnähen, Vereine), **easy plus** (aufbügeln, 30 Sek.), **kinderleicht** (aufkleben, ohne Bügeleisen).

## 6. Learnings aus 2025 – was wir deshalb 2026 so machen

1. **VIP-Früher-Zugang ist der Hebel.** Der VIP-Launch-Tag war mit Abstand der stärkste Tag der ganzen Aktion. → Die gesamte Kommunikation vor dem 23.11. hat nur ein Ziel: Leute auf die VIP-Liste bringen. Landingpage und Teaser-Mails drehen sich um „24 Stunden früher rein“.
2. **Konkretes Datum + Versprechen schlägt Stimmung.** Der Teaser mit „startet am 24. November, 24 h früher für dich“ hat ein Vielfaches an Klicks gebracht gegenüber der reinen „Danke für 25 Jahre“-Mail. → Jede Mail nennt Datum, Uhrzeit und den konkreten Vorteil.
3. **Mehr Produkt und Preis im Bild gewinnt.** Im A/B-Test am Black Friday hat die Variante mit sichtbaren Produkten und Preisen die ruhigere Variante klar geschlagen (Klicks und Käufe). → Hero mit Produkt-Freisteller, Streichpreis → Aktionspreis, kein Stock-Foto ohne Produkt.
4. **Vereine kaufen in großen Mengen, wenn man sie direkt anspricht.** Die Bestellwerte am Launch-Tag waren deutlich höher als normal – Schwimmschulen decken den Jahresbedarf. → Eigene BF-Mail „Jahresbedarf sichern“ mit Rechenbeispiel (500 Seepferdchen + 500 Urkunden), Rollenware prominent, „Kauf auf Rechnung“ sichtbar.
5. **Nach dem Launch war Stille – ein Fehler.** Cyber Monday ohne Mail, kein „Last Chance“, am BF-Tag nur eine Mail an ein kleines Segment. Die Nachfrage war noch da. → 2026: Fr/Mo/Di je eine Mail mit eigenem Angle (Vereine, Cyber Monday, Ende um 23:59).
6. **Plaintext/persönlich für Teaser, Design für Angebote.** Persönliche, textbasierte Mails erzeugen Neugier und Antworten; die Angebots-Mails brauchen das volle On-brand-Design mit Preisen. → Di 10.11. und Do 12.11. Plaintext von „Anna“, ab 23.11. Design-Mails aus dem Sale-Kit.
7. **Hygiene:** Abmeldungen entstehen vor allem bei den breiten Sendungen an alle Listen. → Immer mit Sunset-Ausschlüssen senden, Engaged-Segmente zuerst, Nicht-Öffner als Follow-up.
8. **Rabatt-Kommunikation ehrlich halten.** 2025 war „bis zu 40 %“ Headline, die meisten Artikel lagen darunter. → 2026 ist „bis zu −42 %“ rechnerisch echt (Set Seepferdchen); die Kernartikel liegen bei −27 bis −33 %. Das sagen wir so, keine aufgeblasenen Prozentzahlen.

Details im Rückblick `rueckblick_black_friday_2025.md`, Preise 2025 je Artikel in `preisliste_black_friday_2025.csv`.
