# Auftrag: BW26 Oops-Mail sauber aufsetzen und versandfertig machen (pimpertz.de)

Du arbeitest für Leon (pimpertz.de, offizielle Schwimmabzeichen). Ziel: die Oops-Mail (Black Week 2026 Teaser, Plaintext, „versehentlich weitergeleitete interne Mail“) an die **größtmögliche Zielgruppe ohne Reputationsrisiko** versandfertig machen. Grundlage: Analyse aller Kampagnen 2025/2026 in `klaviyo-relaunch-2026/analyse_segmente_warming_2026-11.md` (Repo `darthyoda69/my-first-repository`, Branch `claude/keen-cerf-2wrao5`).

Werkzeuge: Klaviyo-MCP (Kampagnen, Templates, Listen, Segmente lesen), Shopify-MCP, **Claude in Chrome** (Leon ist in Chrome bei Klaviyo und Shopify eingeloggt) für alles, was die Klaviyo-API nicht kann: Segmente anlegen und reaktivieren.

## Harte Regeln

1. **Nichts an Kund:innen versenden oder einplanen ohne ein ausdrückliches „GO“ von Leon im Chat.** Vor dem GO zeigst du ihm die finale Empfängerzahl, das Template, die Sendezeit und die Ausschlüsse.
2. Testmails nur an **leonbenz@leon-benz.com**.
3. Keine anderen Kampagnen, Flows oder Preise ändern als hier beschrieben.
4. Keine Wettbewerber nennen, keine Verkaufszahlen nach außen.
5. Wenn ein Schritt zwei- oder dreimal scheitert: stoppen, Leon berichten, was passiert ist.

## Feste IDs

| Objekt | ID |
|---|---|
| Oops-Kampagne | `01M6V230VQJYAAWCKD9Y803G5B` |
| Oops-Nachricht | `01M6V2310JM00R2V54CVK96PVY` |
| Oops-Variation | `01M6V23117VBFCP9VRYC3KQX3Y` |
| Oops-Audience | `01M6V230X0T418SYPCH2CAZQSQ` |
| Template V2 „reiner Leak“ (empfohlen) | `Y3NzDB` |
| Template V1 „weitergeleitet + PS“ | `UjMNuv` |
| Liste VIP Pre-Sale 24h | `Syrjty` |
| Liste Sunset Suppressed (Auto) | `VCEPyM` |
| Liste Sunset Liste/Exclude E-Mail | `WBLTej` |
| Segment Sunset: Never Engaged + High Bounce (Hybrid), aktiv | `YwBMns` |
| Segment Exclude: High Bounce Risk (3+ Bounces), inaktiv | `VytNtv` |
| Conversion-Metrik Placed Order | `ViEwFh` |
| Shopify-Landingpage `/pages/black-week` (unveröffentlicht) | `gid://shopify/Page/172227297544` |

## Schritt 1: Kern-Segment anlegen (Klaviyo-Oberfläche via Chrome)

Klaviyo → Listen & Segmente → Segment erstellen. Name: **`BW26 · Engaged Kern (Bounce 0 all-time)`**

Bedingungen, alle mit **UND** verknüpft:

1. **Kann E-Mail-Marketing empfangen** (Person kann Marketing-E-Mails empfangen).
2. **Eine der folgenden (ODER-Gruppe):**
   - „Opened Email“ mindestens 1× in den letzten **180 Tagen**, Filter „Apple Privacy Open“ bzw. `machine_open` = **false**
   - „Clicked Email“ mindestens 1× in den letzten **365 Tagen**, Filter „Bot Click“ = **false**
   - „Placed Order“, **Summe Wert ≥ 10** in den letzten **365 Tagen**
   - „Active on Site“ mindestens 1× in den letzten **90 Tagen**
   - „Subscribed to Email Marketing“ mindestens 1× in den letzten **60 Tagen**
3. **„Bounced Email“ 0× über alle Zeit** (all time).

Speichern. Warten, bis das Segment fertig berechnet ist. Dann per API `get_segment` mit `profile_count` die Zahl lesen und notieren.

Warum so, alles aus echten Daten:
- **Engaged-Segment statt Listen:** 0,1 % statt 4 % Bounce, beste Klick- und Kaufrate (BF 2025).
- **180/365 Tage statt 90:** Seit Juli lief keine Kampagne. Sonst fehlen die WM-Engagierten.
- **Käufer erst ab 10 € Umsatz:** Kleinkäufer ohne Engagement hatten 3,7–5,4 % Abmeldungen und kaum Käufe.
- **Bounce 0 all-time:** Erste Kampagne nach 4 Monaten Pause wird von Gmail und GMX streng bewertet. Kostet nur ein paar hundert aktive Profile.
- **Neu-Abonnent:innen und Website-Aktive:** frische, nachweislich gültige Adressen. Das erhöht die Reichweite ohne Bounce-Risiko.

## Schritt 2: „Exclude: High Bounce Risk“ reaktivieren (Chrome)

https://www.klaviyo.com/lists/VytNtv öffnen → Definition bearbeiten → ohne Änderung speichern. Prüfen per API, dass `is_active = true`.

## Schritt 3: Zielgruppe der Oops-Kampagne setzen (API)

`update_campaign_audience` auf `01M6V230X0T418SYPCH2CAZQSQ`:
- **included:** `[<ID BW26 · Engaged Kern>, "Syrjty"]`
- **excluded:** `["VCEPyM", "WBLTej", "YwBMns", "VytNtv"]`

Nicht mehr enthalten sein dürfen: `XYPHUn` (pimpertz Email Liste ALL), `XMtiyK` (Shopify Profile), `QPHGqT` (Exit Popup), `QP8bSs` (SMS List). Danach die Audience mit `get_campaigns` + include `campaign-audiences` gegenlesen.

**Empfängerzahl:** `refresh_campaign_recipient_estimation` + `get_campaign_recipient_estimation`. Falls das scheitert, Kern-Segment + VIP-Liste per `profile_count` addieren und als Näherung angeben. Erwartung: etwa 5.000–9.000.

## Schritt 4: Inhalt und Einstellungen der Oops-Mail (bereits erledigt am 12.11.2026, nur gegenlesen)

- **Template:** `VBCpUX` „[NEU 2026] BW26_01_Oops_V3_Susanne_Plaintext“ ist der Variation `01M6V23117VBFCP9VRYC3KQX3Y` zugewiesen. Inhalt: interne Mail Anna → Susanne, ein Link `https://pimpertz.de/pages/black-week`, echte pimpertz-Signatur, Abmeldelink. HTML- und Textteil sind inhaltsgleich. Kein Bild, keine Tabelle, keine Webfonts.
- **Betreff:** `Black-Week-Countdown – kurz drüberschauen?`. Preview-Text leer, damit Gmail die erste Zeile „Hey Susanne, …“ zeigt.
- **Absender:** `Anna | pimpertz` <anna@team.pimpertz.de> (Standard-Absender des Kontos). Antworten gehen an info@pimpertz.de.
- **Tracking:** Öffnungen aus, Klicks aus, UTM aus. Kein Tracking-Pixel, kein umgeschriebener Link, maximal „echte“ Mail. Gemessen wird über Neuzugänge der VIP-Liste (`Subscribed to List`, Quelle „Black Week 2026 LP“) und Bounce-, Abmelde- und Spamraten.
- **Smart Sending:** an. Kein Send Time Optimization, keine Zeitzonen-Zustellung, ein fixer Versand.
- **Kampagnenname** ändern in `BW26 · 01 · Oops interne Mail · <Datum> 10:15`.

## Schritt 5: Landingpage veröffentlichen (Shopify)

Leon hat das mit diesem Auftrag freigegeben. Seite `gid://shopify/Page/172227297544` per `pageUpdate` auf `isPublished: true` setzen. Danach in Chrome `https://pimpertz.de/pages/black-week` öffnen und prüfen:
- Countdown läuft (bis Mo 23.11.2026 10:30)
- VIP-Formular sichtbar
- Produktbilder laden
- Kein Theme-Seitentitel doppelt
- Mobil ohne seitliches Scrollen

Formular **nicht** mit fremden Adressen testen. Wenn überhaupt, nur mit leonbenz@leon-benz.com.

## Schritt 6: Testmail

`create_template_preview_send_job` mit dem zugewiesenen Template **nur an leonbenz@leon-benz.com**. Leon bitten zu prüfen: Posteingang statt Spam, Darstellung am Handy, Link führt auf die Live-Seite.

## Schritt 7: Freigabe einholen, dann einplanen

Leon diese Zusammenfassung schicken und auf **GO** warten:
- Empfängerzahl (Kern-Segment, VIP-Liste, geschätzt gesamt)
- Ausschlüsse
- Template, Betreff, Absender
- Vorgeschlagene Sendezeit: **Dienstag 17.11.2026, 10:15 Uhr (Europe/Berlin)**, oder ein früherer Termin, den Leon nennt. Wichtig ist Di bis Do zwischen 10 und 11:30 Uhr und mindestens 3 Tage vor dem VIP-Start am 23.11.

Erst nach GO: `schedule_campaign_message` mit der bestätigten Zeit. Danach Status lesen und bestätigen, dass sie wirklich „scheduled“ ist.

## Schritt 8: Ups-Nachfass-Mail (2 Tage nach Oops, 10:15)

Text: `klaviyo-relaunch-2026/templates/BW26_01b_Ups_Aufloesung_Do_12-11.txt`. Datum im Text auf den tatsächlichen Versandtag anpassen: „am Dienstag“ muss zum Oops-Tag passen.

1. Plaintext-Template wie V2 anlegen: minimales HTML, Link `https://pimpertz.de/pages/black-week`, Footer mit `{{ organization.name }} · {{ organization.full_address }}` und `{% unsubscribe 'Abmelden' %}`. Absender wie Oops.
2. Die Oops-Mail hat kein Klick-Tracking. Deshalb kein Klick-Segment, sondern die VIP-Liste als Ausschluss: Wer sich eingetragen hat, bekommt die Ups-Mail nicht.
3. Kampagnen-Entwurf: **included** Kern-Segment, **excluded** `Syrjty` (schon VIP) + die vier Ausschlüsse aus Schritt 3. Tracking wie bei der Oops-Mail aus.
4. Testmail an leonbenz@leon-benz.com, dann GO von Leon, dann einplanen.

## Schritt 9: Nach dem Oops-Versand auswerten (24 h danach)

`get_campaign_report` für die Oops-Mail: Zustellung, Bounce, Klick, Abmelde- und Spamrate, plus Neuzugänge VIP-Liste. Ampel:
- **Bounce < 0,5 % und Spam < 0,05 %:** Für Launch, Black Friday und Cyber Monday darf die Bounce-Bedingung auf „0 Bounces in den letzten 180 Tagen“ gelockert werden. Dafür ein zweites Kern-Segment anlegen, das erste nicht ändern.
- **Bounce > 1 % oder Spam > 0,1 %:** stoppen, Leon informieren, nicht lockern.

## Danach (nicht Teil dieses Auftrags, nur notieren)

- **BW26 · 02 VIP:** nur VIP-Liste `Syrjty`.
- **BW26 · 03 bis 06:** Kern-Segment (je nach Ampel) + gleiche Ausschlüsse.
- Kampagnennamen 02/03 tragen noch „12:00“, richtig ist 10:30.
- `/collections/black-week` muss bis Mo 23.11. existieren.
- Checkout-Abbruch-Flow (`XhdQ2i`) hatte im September 2026 303 harte Bounces (Fake- oder Bot-Checkouts) → nach der Black Week Flow-Filter setzen.
