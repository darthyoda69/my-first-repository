# pimpertz – Klaviyo Relaunch & Black Week 2026

Stand: 07.11.2026 · Status: **alles als Entwurf** – nichts ist live, geplant oder versendet.

## 1. Analyse Ist-Zustand (Klaviyo, letzte 365 Tage, Conversion = Placed Order)

### Flows

| Flow | Empfänger | Open | Click | Conv. | Umsatz | RPR | Unsub | Befund |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Checkout Abbruch | 4.265 | 43 % | 9,6 % | 6,2 % | 16.569 € | 4,51 € | 1,9 % | Top-Flow. **Mail 2 hat nur 80 % Zustellrate** → Bounce-/Suppression-Problem |
| Produktsuche Abbruch (Browse) | 1.344 | 46 % | 7,5 % | 4,6 % | 9.087 € | **6,97 €** | 2,3 % | Bester RPR, AOV 142 € – ausbauen |
| Warenkorb Abbruch | 2.083 | 47 % | 4,4 % | 4,0 % | 8.117 € | 3,98 € | 1,9 % | solide |
| Welcome Series | 11.778 | 50 % | 2,1 % | 0,85 % | 5.657 € | 0,49 € | **4,7 %** | Unsub viel zu hoch (Mail 2: 5,6 %), Conversion schwach |
| Bewertungsanfrage | 7.184 | 41 % | 5,6 % | 0,4 % | 3.984 € | 0,56 € | 2,4 % | ok |
| Post Purchase Cross-Sell | 1.559 | 53 % | **1,2 %** | 0,6 % | 262 € | 0,17 € | 2,1 % | Hohe Öffnung, kaum Klicks → Content-Problem |
| SMS-Flows (Order/Shipment) | 183 | – | – | – | – | – | – | **Zustellrate 53–60 %** → Nummern-Qualität prüfen |

Lücken / Baustellen:
- **Kein Back-in-Stock-Flow**, obwohl die Metrik „Subscribed to Back in Stock“ existiert.
- **Sunset-Flow nur Entwurf** – Kampagnen haben 1,2–5 % Abmelderate, Liste wird nicht gepflegt.
- **Kein Winback / keine B2B-Nachbestellung** – Vereine & Schwimmschulen kaufen saisonal Rollenware in großen Mengen, aber es gibt keinen Reorder-Reminder.
- Doppelte Altlasten: „First Purchase … Standard“ (Entwurf) neben „… Richtiger Trigger“ (live), „Price Drop“ (Entwurf).
- **Kampagnen-Lücke Dez 2025 – Mai 2026: 0 Kampagnen.**

### Black Week 2025 (Referenz)

| Kampagne | Datum | Empfänger | Open | Click | Umsatz | RPR |
|---|---|---:|---:|---:|---:|---:|
| Black Friday Warming | 18.11. | 13.519 | 32 % | 0,6 % | 1.339 € | 0,10 € |
| Vierteljahrhundert Aktion (VIP-Teaser) | 20.11. | 13.179 | 31 % | 4,9 % | 7.242 € | 0,57 € |
| **Black Week Launch (24h VIP Pre-Sale)** | 24.11. | 12.600 | 33 % | 6,0 % | **44.108 €** | **3,54 €** |
| Black Friday – Variante A | 28.11. | 2.113 | 50 % | 8,6 % | 5.536 € | 2,62 € |
| Black Friday – Variante B | 28.11. | 2.110 | 49 % | 5,7 % | 3.261 € | 1,55 € |

Shopify-Umsatz 24.–28.11.25: 24,9 k / 18,6 k / 8,3 k / 5,7 k / 12,8 k €. Learnings: **VIP-/Früher-Zugang ist der Hebel** (AOV 226 €), reiner „Warming“-Content verpufft, nur 1 Mail am BF-Tag selbst.

## 2. Template-Paket (mailsupply Master Bundle, Josh Rauer / ex-SNOCKS)

Gefunden in Google Drive: `Open in Figma/Files/*.fig` (Sales, Bite, Muse, Pulse, Ease, Spa, Blank) und `Open in Canva` (Canva-Links). In Canva existiert bereits „Copy of Bite Collection“ mit begonnener pimpertz-Adaption (Schulstart).
Die neuen Templates übernehmen die **Bite-Pack-Logik** (Farb-Hero, große Headline, Code-Box, Pill-Button, nummerierte FAQ, Review-Block, heller Footer) in pimpertz-CI (Schwarz #0E0A04, Gelb #FDBD13, Orange #FF7500, Poppins/Archivo) und als **echtes HTML statt Bild-Mails** (Zustellbarkeit, Dark Mode, Barrierefreiheit).

Quelle aller Templates: `build_templates.py` → `templates/*.html`. Änderungen immer im Generator, nicht in Klaviyo direkt.

## 3. Neue Flow-Mails (Challenger für A/B-Test)

| Template | Einsatz | Hypothese |
|---|---|---|
| FLOW_Welcome_E1_Challenger | Welcome Series Mail 1 | FAQ + klare Ausführungs-Erklärung senkt Unsub, hebt Conversion |
| FLOW_Warenkorb_E1_Challenger | Warenkorb Abbruch Mail 1 | Dynamisches Produktbild + USPs |
| FLOW_Checkout_E1_Challenger | Checkout Abbruch Mail 1 | Line-Items + „Kauf auf Rechnung“ für Vereine |
| FLOW_Produktsuche_E1_Challenger | Produktsuche Abbruch Mail 1 | Beratung Rollenware / easy plus / kinderleicht |
| FLOW_PostPurchase_CrossSell_Challenger | Post Purchase Cross-Sell | Nächste Etappe (Seepferdchen → Bronze) statt generisch |

Einbau (Klaviyo-UI, da die API keine Flows editiert): Flow öffnen → Mail → „A/B-Test erstellen“ → Variante B = neues Template → Gewinner-Metrik **Placed Order / RPR**, 50/50, automatische Auswahl nach Signifikanz.

## 4. Black Week 2026 – Fahrplan

Preislogik (Entscheidung 09.11.2026): **exakt die Konditionsstruktur von 2025** je Produktlinie → `black-week-2026-preise.csv` bzw. `black-friday-2025/konditionen_2025_je_produktlinie.md`. Hero-Artikel: Seepferdchen Rolle 0,61 € · Schwimmpass 0,66 € · Urkunde 0,46 € · Set Seepferdchen 1,66 € · Bronze/Silber/Gold Rolle 0,61 € · Set Bronze 1,86 €. Headline „bis zu −40 %“.

| Datum | Mail | Zielgruppe | Ziel |
|---|---|---|---|
| **Di 10.11.** | BW26_01 „Oops – interne Mail“ | alle Engaged | Neugier, VIP-Liste über Klick aufbauen |
| Do 12.11. | Auto-Follow-up an Nicht-Öffner (Klaviyo) | Nicht-Öffner | Reichweite |
| **Mo 23.11. 10:30** | BW26_02 VIP Early Access | VIP-Liste + Klicker der Oops-Mail + Käufer 2025 | Wiederholung des stärksten Tages 2025 |
| Di 24.11. | BW26_03 Launch für alle | alle Engaged | Volumen |
| Fr 27.11. | BW26_04 Black Friday – Vereine/Jahresbedarf | B2B + Großbesteller | AOV |
| Mo 30.11. | BW26_05 Cyber Monday | alle Engaged, ohne Käufer der Woche | Nachzügler |
| Di 01.12. | BW26_06 Last Chance | Klicker ohne Kauf | Abschluss |

## 5. Offene Punkte vor Go-Live (bitte entscheiden/prüfen)

1. **„ab 500 Stück“**: SchwimmWelten zeigt öffentlich nur Einzelpreise (Shop-Export 02.04.26 + Live-Stichprobe: Aufnäher 0,79 €, Urkunde+Aufnäher 1,29 €). Annahme: BW-Preis gilt **ab 1 Stück**. Wenn er nur **ab 500 Stück** gelten soll → Mails 02–06 + FAQ anpassen und als Mengenrabatt in Shopify umsetzen.
2. **Marge**: In Shopify sind keine Einkaufspreise (unitCost) hinterlegt → Marge der BW-Preise nicht geprüft.
3. **Preisangaben (§ 11 PAngV)**: Durchgestrichene Preise müssen der niedrigste Preis der letzten 30 Tage sein. Aktuelle Preise vor dem 23.11. nicht senken.
4. **Shopify**: Collection `/collections/black-week` existiert noch nicht (Link in Mails 02–06). Landingpage `/pages/black-week` ist als Entwurf angelegt (Page 172227297544), noch unveröffentlicht. Preisumstellung Mo 23.11. 10:30, Rückstellung Di 01.12. 23:59.
5. **Claims prüfen**: „Kauf auf Rechnung für Vereine“, Welcome-Code `WILLKOMMEN10` muss in Shopify existieren.
6. **Hygiene vor BW**: Sunset-Flow aktivieren, Suppressions prüfen (Checkout-Mail 2 nur 80 % Zustellung), Kampagnen immer mit Ausschluss „Sunset Suppressed (Auto)“ + „Sunset Liste/Exclude E-Mail“.

## 6. In Klaviyo angelegt (Entwürfe)

Templates (`[NEU 2026] …`): Welcome `SP3mPm` · Warenkorb `VdT3U7` · Checkout `UjMJaA` · Produktsuche `UHwfMp` · Post-Purchase `SqHAac` · BW26_01 `VDvPFX` · BW26_02 `V7Hht6` · BW26_03 `XQfuRB` · BW26_04 `TNerXa` · BW26_05 `UiBe5S` · BW26_06 `RpXZUL`

Kampagnen (Status `draft`, nicht geplant):
- BW26 · 01 Oops – `01M6V230VQJYAAWCKD9Y803G5B`
- BW26 · 02 VIP – `01M6V23QW2PSAT5GTQ1HM97KZD`
- BW26 · 03 Launch – `01M6V23S3NVMDXX6DCKCCQ4RAN`
- BW26 · 04 Black Friday Vereine – `01M6V23V1VMWD3BMVCT1RCDFRB`
- BW26 · 05 Cyber Monday – `01M6V23WCE429FS7P8CJP1YARA`
- BW26 · 06 Last Chance – `01M6V23XRGREVNBTZQ5KNVP0YS`

Audience überall: Email Liste ALL + Shopify Profile + Exit Popup + VIP Pre-Sale; ausgeschlossen: beide Sunset-Listen + Segment „Sunset: Never Engaged + High Bounce“.

## 7. Josh-Rauer-Kits (mailsupply) auf pimpertz umgebaut – Canva

Originale unverändert, Arbeit nur auf Kopien `pimpertz · <Kit> · 2026`.

| Kit | Canva design_id | Status |
|---|---|---|
| Sale (Black Week, 28 Mails) | DAHaQcel-Qk | in Arbeit (VIP-Start auf Mo 23.11. 10:30 korrigiert) |
| Bite (Flows, 8 Mails) | DAHaQd2Zp74 | fertig, geprüft |
| Spa (Wasser-Kit, 8 Mails) | DAHaQdmHh28 | fertig, geprüft |
| Muse (Premium/Glamour, 8 Mails) | DAHaQQEoZo8 | fertig, geprüft |
| Pulse (Master-Stil, 8 Mails) | DAHaQYpgg4k | fertig, geprüft |
| Ease (sportlich, 8 Mails) | DAHaQXJT6K8 | fertig, geprüft |

Bildwelt: 12 Higgsfield-Motive (`pz26_*`) + Logo + 7 Produkt-Freisteller in Canva hochgeladen.

## 8. Black Week – Stand 09.11.

- Oops-Mail (Di 10.11.) als **Plain-Text** neu: Template `UjMNuv`, Kampagne `01M6V230VQJYAAWCKD9Y803G5B` zeigt darauf; einziger Link → `https://pimpertz.de/pages/black-week` (+ Pflicht-Abmeldelink).
- Landingpage `/pages/black-week` in Shopify angelegt (Page `172227297544`, **unveröffentlicht**): Countdown bis Mo 23.11. 10:30, VIP-Formular → Klaviyo-Liste „VIP Pre-Sale 24h“ (Syrjty) via Client API, Preisvorschau. Quelle: `landingpage/black-week.html`.
- Offen: LP veröffentlichen, Sendezeit Di festlegen, Collection `/collections/black-week` anlegen.
