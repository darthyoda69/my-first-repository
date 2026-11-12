# BW26 Oops-Mail: versendete Mail, rechtliche Bewertung und Rettungsplan

**Stand:** Do 12.11.2026, nachmittags
**Für:** Leon Benz, pimpertz
**Vertraulich.** Interne Arbeitsunterlage, keine Rechtsberatung. Vor Entscheidungen von einer Anwältin oder einem Anwalt für Wettbewerbsrecht prüfen lassen.

---

## 1. Kurzfassung

| | |
|---|---|
| **Was ist passiert?** | Am 12.11. um 11:54 Uhr ging ein Black-Week-Teaser raus, getarnt als interne Mail von Anna an Susanne. Empfänger: 11.691. |
| **Rechtliches Risiko jetzt** | **GELB (mittel).** Die Kampagnenserie stand auf ORANGE. Das ist sie nicht mehr, weil die Folgemail entschärft ist. |
| **Nach der Auflösung** | **GRÜN bis unteres GELB** |
| **Rettung** | Ehrliche Auflösungsmail heute um 18:30 Uhr an alle Empfänger, einschließlich VIP-Liste. Liegt als Entwurf bereit. |
| **Noch nötig** | GO für den Versand und GO für die Headline-Korrektur der Landingpage |
| **Restrisiko** | Eine Abmahnung wegen der Oops-Mail bleibt theoretisch möglich, bis die Ansprüche verjähren (6 Monate ab Kenntnis, § 11 UWG, also etwa Mai 2027). |

---

## 2. Die versendete Mail

### Versanddaten

| Feld | Wert |
|---|---|
| Kampagne | BW26 · 01 · Oops interne Mail (`01M6V230VQJYAAWCKD9Y803G5B`) |
| Status | **sent**, Do 12.11.2026, 11:54 Uhr (Europe/Berlin) |
| Empfänger | **11.691** auf 2.409 Domains |
| Absender | Anna \| pimpertz <anna@team.pimpertz.de>, Antworten an info@pimpertz.de |
| Betreff | Pimpertz Black Week \| Kannst du kurz drüberschauen? |
| Vorschautext | leer |
| Template | `VBCpUX`, Plaintext-Optik, ohne Bilder |
| Tracking | Öffnungen aus, Klicks aus, UTM an. Ohne Klick-Tracking hängt Klaviyo vermutlich keine UTMs an, deshalb kamen sie nicht an. |
| Smart Sending | an |

### Zielgruppe

- **Eingeschlossen:**
  - Segment „BW26 · Engaged Kern (Bounce 0 all-time)“ (`VjJSvF`, 11.716 Profile). Bedingungen: E-Mail-Marketing erlaubt; geöffnet in 180 Tagen oder geklickt in 365 Tagen oder Umsatz ≥ 10 € in 365 Tagen oder aktiv auf der Website in 90 Tagen oder neu angemeldet in 60 Tagen; 0 Bounces über alle Zeit.
  - VIP-Liste „VIP Pre-Sale 24h“ (`Syrjty`)
- **Ausgeschlossen:**
  - Sunset Suppressed (Auto)
  - Sunset Liste/Exclude
  - Sunset: Never Engaged + High Bounce
  - Exclude: High Bounce Risk
  - Ausschluss · Weiterleitungsadressen ohne Kauf
  - Ausschluss · Verbände/SchwimmWelten

### Text (wie versendet)

> Hey Susanne,
>
> der Black-Week-Countdown für unsere Kunden ist fertig. Bei ein paar Sachen kommen wir auf bis zu 40 % Rabatt. Schon ordentlich.
>
> Kannst du kurz drüberschauen, bevor wir die Mail an alle Kunden rausschicken? Geplant ist nächste Woche, bis dahin sollte das noch niemand sehen.
>
> https://pimpertz.de/pages/black-week
>
> LG
> Anna
>
> \-- 
> pimpertz · Inhaber Susanne Benz · Pappelweg 12 · 72202 Nagold · Telefon 07452 888090 3 · Telefax 07452 888090 5 · info@pimpertz.de · www.pimpertz.de
>
> *(grau, 11 px)* Du bekommst diese Mail für die besten Angebote von Pimpertz. Abmelden

Kopie im Repo: `templates/BW26_01_Oops_V3_Susanne_VERSENDET_2026-11-12.html`

### Wer die Mail bekommen hat (nach Domain)

| Gruppe | Empfänger |
|---|---:|
| Private Mailanbieter (gmail, gmx, web.de, t-online usw.) | Großteil |
| DLRG (rund 100 Ortsgruppen und Bezirke, dazu dlrg.de) | 108 |
| Wasserwacht und Rotes Kreuz (z. B. wasserwacht.bayern 30, brk.de 6) | 64 |
| Sportbünde und Verbände (Kreis- und Stadtsportbünde, Sportjugend, LSB Sachsen-Anhalt, dguv.de, Schwimmverband Wuppertal) | ca. 14 |
| Schulen (ohne Schwimmschulen) | ca. 360 |
| Städte, Bäder, Stadtwerke | über 200 |
| Kanzleien (dierlamm-rechtsanwaelte.com, heuvelslaw.com, rechtsanwalt-presch.de) | 3 |
| Testdienste für Zustellbarkeit (z. B. deliverabilitylabs.com, emailreach.co) | 14 |
| Weiterleitungsadressen mit Kauf | 4 |

- **Nicht dabei:** Landesschwimmverbände, DSV, SchwimmWelten. Die Sperrung hat gegriffen.
- **Vollständige Liste:** `oops_empfaenger_domains_2026-11-12.csv`

---

## 3. Rechtliche Bewertung

**Methode:** Schwere (1–5) × Wahrscheinlichkeit (1–5). Score 1–4 GRÜN, 5–9 GELB, 10–15 ORANGE, 16–25 ROT.

### Übersicht

| Nr. | Risiko | Erste Bewertung | Heute (Auflösung als Entwurf) | Nach Auflösung und offenen Punkten |
|---|---|:-:|:-:|:-:|
| R1 | Werbecharakter verschleiert (Betreff, „interne Mail“) | 9 GELB | 9 GELB | **6 GELB** |
| R2 | Einwilligung der Empfänger | 9 GELB | 4 GRÜN* | **4 GRÜN*** |
| R3 | Folgemails setzen die Täuschung fort | **12 ORANGE** | 9 GELB | **4 GRÜN** |
| R4 | Klaviyo-Konto, Spam-Beschwerden | 8 GELB | 8 GELB | **4 GRÜN** (bei Spam unter 0,1 %) |
| R5 | VIP-Liste ohne Double-Opt-in, kein Datenschutzlink am Formular | 6 GELB | 6 GELB | 6 GELB, bis umgesetzt |
| R6 | „Bis zu −40 % auf offizielle Schwimmabzeichen“ (Landingpage) | 6 GELB | 6 GELB | **2 GRÜN** nach Korrektur |
| R7 | Streichpreise, 30-Tage-Tiefstpreis (§ 11 PAngV) | 4 GRÜN | 4 GRÜN | 4 GRÜN (bitte bestätigen) |
| R8 | Ruf bei Vereinen, Schulen, Behörden | 6 GELB | 6 GELB | **4 GRÜN** |
| R9 | Vorsorglich angelegte Profile der Verbände (DSGVO) | 2 GRÜN | 2 GRÜN | 2 GRÜN |
| R10 | Abmeldelink, Impressumsangaben | 2 GRÜN | 2 GRÜN | 2 GRÜN |

\* Laut Leon sind alle Empfänger Abonnenten, importiert aus dem früheren eigenen Shop. In Klaviyo sind rund 35 % als „nie abonniert“ geführt, ohne Datum und ohne Herkunft. Der Nachweis aus dem Altsystem (Datum, Anmeldeweg) muss aufbewahrt werden.

### R1: Werbecharakter verschleiert

**Rechtsgrundlagen:**
- **§ 6 Abs. 2 DDG:** Absender und kommerzieller Charakter dürfen in Kopf- und Betreffzeile nicht absichtlich verschleiert werden. Ein Verstoß ist eine Ordnungswidrigkeit nach § 33 DDG.
- **§ 5a Abs. 4 UWG:** Der kommerzielle Zweck muss erkennbar sein.
- **§ 5 UWG:** Irreführung. Abmahnfähig über § 3a bzw. § 7 UWG.

**Was gegen uns spricht:**
- „Kannst du kurz drüberschauen?“ und „bis dahin sollte das noch niemand sehen“ sind bewusst als interne Mail gestaltet.
- Die Absicht ist in den Planungsunterlagen dokumentiert.

**Was für uns spricht:**
- „pimpertz“ steht im Absender, „Pimpertz Black Week“ im Betreff.
- Rabatt und Shop-Link stehen im Text, die Fußzeile nennt „Angebote“ und hat einen Abmeldelink.
- Die schnelle, offene Auflösung am selben Tag.

**Realistisches Szenario:** Abmahnung durch einen Mitbewerber oder Verband.
- Kosten: ca. 1.000–2.500 €.
- Dazu eine Unterlassungserklärung mit Vertragsstrafe, üblich ab 5.000 € pro Verstoß.
- Ein Bußgeld der Behörde ist in der Praxis selten.
- Ein Urteil speziell zu gefälschten Oops-Mails ist nicht bekannt.

### R3: Folgemails

- Die ursprünglich geplante Ups-Mail hätte die Täuschung fortgesetzt: „ist dir eine interne Mail von mir in den Posteingang gerutscht … Danke fürs Dichthalten“. **Ersetzt** durch eine ehrliche Auflösung (Abschnitt 5).
- Für die Mails 02 bis 06 gilt: kein weiteres Fake-Format, klarer Werbebetreff.

### R6: „Bis zu −40 %“

- −40 % gibt es nur auf das Starterkit Pirat Pimpi (6,95 € auf 4,17 €). Das höchste Abzeichen liegt bei −38 % (Regenbogen-Seepferdchen).
- 13 von 106 Artikeln liegen bei −30 % oder mehr, 41 haben 0 %.
- In der Mail ist die Aussage durch „bei ein paar Sachen“ eingeschränkt und damit vertretbar.
- Auf der Landingpage („auf offizielle Schwimmabzeichen“) ist sie so nicht haltbar. Die Korrektur liegt als Entwurf bereit.

### R5: VIP-Liste

- Die Liste `Syrjty` läuft mit Single-Opt-in. Der Hinweis am Formular hat keinen Link zur Datenschutzerklärung.
- **Lösung:** Double-Opt-in einschalten und Datenschutzlink ergänzen, bis zum 22.11.

Ausführliches Memo: `RISIKO_oops_mail_2026-11-12.md`

---

## 4. Rettungsplan

Die Lage ist **keine Alarmstufe Rot**. Es gibt keine Beschwerde, keine Abmahnung und keine Anfrage einer Behörde. Der Plan folgt den gängigen Empfehlungen für Oops-Mails:
- schnell auflösen, am besten am selben Tag
- an alle Empfänger der ersten Mail schicken
- kurz und ehrlich bleiben, keine gespielte Entschuldigung
- das Format nicht wiederholen

### Stufe 1: heute, Do 12.11.

| # | Maßnahme | Status |
|---|---|---|
| 1 | Auflösungsmail um **18:30 Uhr** an alle Empfänger der Oops-Mail, einschließlich VIP-Liste (Abschnitt 5) | Entwurf fertig, Testmail verschickt, **wartet auf GO** |
| 2 | Landingpage: „Bis zu −40 % auf ausgewählte Artikel“ statt „… auf offizielle Schwimmabzeichen“ (3 Stellen) | Entwurf `landingpage/black-week_ENTWURF_headline.html`, **wartet auf GO** |
| 3 | Antworten an info@ mit Vorlage, noch am selben Tag | Vorlage `templates/ANTWORTVORLAGE_info_Oops-Rueckfragen.md` |
| 4 | Wer sich beschwert oder um Abmeldung bittet: sofort abmelden, freundlich antworten, nicht diskutieren | laufend |

### Stufe 2: die nächsten 72 Stunden

- **Fr 13.11. vormittags:** Klaviyo-Berichte der Oops- und der Ups-Mail prüfen.
  - Spam über 0,1 % oder Bounces über 1 %: keine weiteren Kampagnen, bis die Ursache klar ist.
- info@ täglich auf Beschwerden durchsehen.
- Social Media und Elterngruppen beobachten. Bei öffentlicher Diskussion einheitlich antworten: „War ein Teaser, wir haben noch am selben Tag aufgelöst.“
- Die Oops-Mail auswerten: Klicks über Microsoft Clarity, gefiltert auf `/pages/black-week` ab 12.11. 11:54 Uhr (dort als Direktaufrufe ohne UTM), plus Neuzugänge der VIP-Liste.

### Stufe 3: falls eine Abmahnung kommt

1. Die beigefügte Unterlassungserklärung **nicht unterschreiben**. Sie ist fast immer zugunsten des Abmahnenden formuliert.
2. **Frist notieren.** Üblich sind 5 bis 10 Tage ab Zugang. Wer nicht reagiert, riskiert eine einstweilige Verfügung.
3. **Sofort eine Anwältin oder einen Anwalt für Wettbewerbsrecht beauftragen.** Eine Fristverlängerung ist oft möglich. Meist wird eine angepasste Unterlassungserklärung abgegeben, eingeschränkt formuliert und mit angepasster Vertragsstrafe.
4. Unterlagen sichern:
   - beide Mails
   - Versandzeiten
   - Empfängerzahl
   - dieses Dossier

### Stufe 4: falls eine Behörde anfragt

Gemeint sind ein Bußgeld nach DDG oder eine Anfrage der Datenschutzaufsicht Baden-Württemberg. Nicht selbst antworten, alles über die Anwältin oder den Anwalt laufen lassen.

### Dauerhaft

- Kein zweites Fake-Format in dieser oder einer späteren Kampagne.
- In jeder Mail die Fußzeile mit dem Hinweis auf kostenlosen Widerspruch (Text in Abschnitt 5).
- Double-Opt-in für die VIP-Liste und Datenschutzlink am Formular.
- Nachweis der Einwilligungen aus dem Altshop sichern. Ideal: die betroffenen Profile mit Original-Datum als „subscribed“ nachimportieren.
- Die 14 Adressen von Testdiensten abmelden und ins Ausschluss-Segment aufnehmen.
- Die VIP-Mail am 23.11. beginnt mit einem Satz zur Auflösung, für alle, die sich vorher eingetragen haben.

---

## 5. Die Auflösungsmail

### Einstellungen

| Feld | Wert |
|---|---|
| Kampagne | BW26 · 01b · Ups Auflösung · Do 12.11. 18:30 (`01M77VCKZZFY19XN9P0TDEH0WR`) |
| Status | **Entwurf**, nicht eingeplant |
| Geplanter Versand | Do 12.11.2026, 18:30 Uhr (Europe/Berlin), nach GO |
| Absender | Anna \| pimpertz <anna@team.pimpertz.de>, Antworten an info@pimpertz.de |
| Betreff | Ups. Das war kein Versehen. |
| Vorschautext | Die Rabatte bis 40 % gibt es wirklich, und du kommst 24 Stunden früher rein. |
| Template | `UyYyj3` (Plaintext-Optik wie die Oops-Mail) |
| Zielgruppe | **eingeschlossen:** Kern-Segment `VjJSvF` und VIP-Liste `Syrjty`. **Ausgeschlossen:** dieselben sechs Ausschlüsse wie bei der Oops-Mail. |
| Smart Sending | **aus**, sonst würden heute fast alle Empfänger übersprungen |
| Tracking | Öffnungen an, Klicks an, UTM nach Klaviyo-Standard |
| Testmail | am 12.11. an leonbenz@leon-benz.com verschickt |

### Text

> Hallo,
>
> vorhin ist bei dir eine „interne“ Mail von mir an Susanne gelandet. Okay, erwischt: Die war Absicht. 😉
>
> Die Rabatte gibt es aber wirklich. In der Black Week sparst du bis zu 40 % auf ausgewählte Artikel.
>
> Und weil du die Mail bekommen hast, kommst du früher rein: Trag dich bis Sonntag, 22.11., ein. Dann bekommst du am Montag, 23.11., um 10:30 Uhr deinen Zugang, 24 Stunden vor allen anderen.
>
> https://pimpertz.de/pages/black-week
>
> Schon eingetragen? Dann bist du drin und musst nichts weiter tun.
>
> Viele Grüße
> Anna
>
> \-- 
> pimpertz · Inhaber Susanne Benz · Pappelweg 12 · 72202 Nagold · Telefon 07452 888090 3 · info@pimpertz.de · www.pimpertz.de
>
> *(grau, 11 px, Link in derselben Farbe)* Du erhältst diese E-Mail, weil du bei pimpertz bestellt oder dich für unseren Newsletter angemeldet hast. Du kannst der Nutzung deiner E-Mail-Adresse für Werbung jederzeit widersprechen, ohne dass dir dafür andere als die Übermittlungskosten nach den Basistarifen entstehen: Abmelden

### Warum diese Fassung

| Element | Zweck |
|---|---|
| „Okay, erwischt: Die war Absicht.“ | Beendet die Täuschung eindeutig. Das ist das stärkste Argument gegen R1. |
| „bis zu 40 % auf ausgewählte Artikel“ | Die Aussage ist korrekt, weil das Starterkit −40 % hat (R6). |
| An alle, auch an die VIP-Liste | Wer sich wegen der Oops-Mail eingetragen hat, erfährt von der Auflösung. |
| „Schon eingetragen? …“ | Kein Missverständnis bei den VIPs. |
| Fußzeile | Der Hinweis auf kostenlosen Widerspruch ist ab jetzt Standard (R2). |
| Versand am selben Tag | Die Täuschung bleibt nur etwa 6,5 Stunden im Raum. |

Dateien: `templates/BW26_01b_Ups_Aufloesung_Do_12-11_1830.html` und `.txt`

---

## 6. Offene Entscheidungen und nächste Schritte

| # | Aufgabe | Wer | Bis |
|---|---|---|---|
| 1 | Testmail prüfen: Posteingang, Darstellung am Handy, Link | Leon | heute, 18:00 Uhr |
| 2 | **GO Landingpage:** Headline-Korrektur live schalten | Leon → Claude | heute, 18:00 Uhr |
| 3 | **GO Versand:** Auflösungsmail für 18:30 Uhr einplanen, danach Status „scheduled“ bestätigen | Leon → Claude | heute, 18:00 Uhr |
| 4 | Berichte von Oops- und Ups-Mail prüfen (Spam, Bounces, Abmeldungen) | Claude | Fr 13.11., vormittags |
| 5 | 14 Adressen von Testdiensten abmelden | Claude (nach GO) | Fr 13.11. |
| 6 | Double-Opt-in für die VIP-Liste, Datenschutzlink am Formular | Leon / Claude | So 22.11. |
| 7 | Einstiegssatz zur Auflösung in die VIP-Mail vom 23.11. | Claude | Fr 20.11. |
| 8 | Neue Fußzeile in die Templates 02–06 übernehmen | Claude | Fr 20.11. |
| 9 | Streichpreise gegen den 30-Tage-Tiefstpreis bestätigen | Leon | Fr 20.11. |
| 10 | Nachweis der Einwilligungen aus dem Altshop sichern | Leon | Fr 20.11. |
| 11 | Kurzprüfung der Mails ab dem 23.11. durch eine Anwältin oder einen Anwalt für Wettbewerbsrecht | Leon | Fr 20.11. |

---

## Quellen

- [§ 6 DDG](https://www.gesetze-im-internet.de/ddg/__6.html)
- [IHK Frankfurt: E-Mail-Werbung](https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/wettbewerbsrecht/unlauterer-wettbewerb/unzumutbare-belaestigung/e-mail-werbung-5196268)
- [IHK Frankfurt: Abmahnverfahren](https://www.frankfurt-main.ihk.de/recht/uebersicht-alle-rechtsthemen/wettbewerbsrecht/abmahnverfahren-5196524)
- [WBS: Abmahnung im Wettbewerbsrecht](https://www.wbs.legal/wettbewerbsrecht/abmahnung/)
- [RA Plutte: Abmahnung erhalten](https://www.ra-plutte.de/abmahnung-erhalten/)
- [advocado: Modifizierte Unterlassungserklärung](https://www.advocado.de/index.php/ratgeber/zivilprozessrecht/unterlassungsanspruch/modifizierte-unterlassungserklaerung.html)
- [Validity: The Art of the Oops](https://www.validity.com/blog/the-art-of-the-oops-how-to-recover-from-an-email-marketing-mistake/)
- [Smaily: Oops emails](https://smaily.com/oops-emails-how-to-deal-with-mistakes-in-marketing-emails/)
- [dotdigital: What to do if you send an email by mistake](https://dotdigital.com/blog/what-to-do-if-you-send-an-email-by-mistake/)
- [Knak: Biggest Email Marketing Mistakes](https://knak.com/blog/when-oops-happens/)
