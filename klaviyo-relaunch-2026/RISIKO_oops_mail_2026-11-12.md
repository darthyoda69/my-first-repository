# Legal Risk Assessment: Oops-Mail BW26 · 01 (versendet 12.11.2026)

**Datum:** 12.11.2026
**Erstellt von:** Claude (KI-Assistenz) für Leon Benz, pimpertz
**Gegenstand:** Kampagne „BW26 · 01 · Oops interne Mail“ (Klaviyo `01M6V230VQJYAAWCKD9Y803G5B`), versendet Do 12.11.2026, 11:54 Uhr
**Vertraulich:** Ja, interne Arbeitsunterlage. Keine Rechtsberatung. Vor Entscheidungen von einer Anwältin oder einem Anwalt für Wettbewerbsrecht prüfen lassen.

---

## 0. Ergebnis auf einen Blick

| Nr. | Risiko | Schwere | Wahrsch. | Score | Ampel |
|---|---|:-:|:-:|:-:|:-:|
| R1 | Werbecharakter verschleiert (Betreff und „interne Mail“) | 3 | 3 | 9 | GELB |
| R2 | Ca. 1/3 der Empfänger ohne Newsletter-Einwilligung, und der Pflichthinweis für Bestandskunden fehlt | 3 | 3 | 9 | GELB |
| R3 | Die geplante Ups-Mail und alle Folgemails verlängern R1 und R2 | 3 | 4 | **12** | **ORANGE** |
| R4 | Klaviyo-Konto: Richtlinie gegen irreführende Betreffzeilen, Spam-Beschwerden | 4 | 2 | 8 | GELB |
| R5 | VIP-Liste ohne Double-Opt-in, kein Datenschutzlink am Formular | 2 | 3 | 6 | GELB |
| R6 | „Bis zu −40 % auf offizielle Schwimmabzeichen“ (Landingpage) | 2 | 3 | 6 | GELB |
| R7 | Streichpreise (§ 11 PAngV, niedrigster Preis der letzten 30 Tage) | 2 | 2 | 4 | GRÜN |
| R8 | Ruf bei Vereinen und Schwimmschulen, wenn der Trick auffliegt | 3 | 2 | 6 | GELB |
| R9 | Vorsorglich angelegte Profile der Verbände (DSGVO) | 1 | 2 | 2 | GRÜN |
| R10 | Abmeldelink, Absenderangaben, Impressum | 1 | 2 | 2 | GRÜN |

**Gesamt:** Die Mail allein ist **GELB**. Bleiben Ups-Mail und Folgemails unverändert, wird die ganze Kampagnenserie **ORANGE**. Mit den Maßnahmen in Abschnitt 6 ist das Restrisiko **GELB bis GRÜN**. Die wichtigsten Maßnahmen sind Textänderungen, die nichts kosten.

---

## 1. Risikobeschreibung

Die Mail ist als interne Nachricht von „Anna“ an die Inhaberin Susanne Benz gestaltet. Sie gibt vor, versehentlich bei Kund:innen gelandet zu sein. Betreff: „Pimpertz Black Week | Kannst du kurz drüberschauen?“. Im Text steht: „bevor wir die Mail an alle Kunden rausschicken? Geplant ist nächste Woche, bis dahin sollte das noch niemand sehen.“ In Wahrheit ist die Mail die Werbung selbst, an ca. 11.700 Empfänger.

Die Mail wirft zwei Rechtsfragen auf. Erstens: Ist der Werbecharakter erkennbar, oder wird er verschleiert? Zweitens: Durfte jede einzelne Adresse überhaupt Werbung bekommen?

## 2. Hintergrund (geprüfte Fakten)

- **Status:** `sent`, Sendezeit 10:54 UTC (11:54 Uhr Berlin), statischer Versand, Smart Sending an.
- **Zielgruppe:**
  - eingeschlossen: Segment „BW26 · Engaged Kern (Bounce 0 all-time)“ (`VjJSvF`, 11.716 Profile) und VIP-Liste `Syrjty` (52 Profile)
  - ausgeschlossen: Sunset-Listen und -Segmente, High Bounce, Weiterleitungsadressen ohne Kauf (`RZJSsB`), Verbände/SchwimmWelten (`WV9f4K`)
- **Einwilligungsstatus**, Stichprobe von 100 Profilen aus `VjJSvF`, nicht zufällig gezogen, nur als Richtwert:
  - **65 SUBSCRIBED**: 54 über den Shopify-Checkout, 10 über ein Klaviyo-Formular, 1 per API. Keine davon mit Double-Opt-in.
  - **35 NEVER_SUBSCRIBED**: alle sind Käufer.
  - Hochgerechnet: **ca. 4.000 Empfänger ohne Newsletter-Einwilligung**. Sie stützen sich nur auf das Bestandskundenprivileg (§ 7 Abs. 3 UWG).
- **Segmentlogik:** „Kann E-Mail-Marketing empfangen, Abo-Status: beliebig“ schließt bei Klaviyo Profile ein, die nie abonniert haben.
- **Live-Inhalt:** Kopie in `templates/BW26_01_Oops_V3_Susanne_VERSENDET_2026-11-12.html`.
  - Fußzeile, grau, 11 px: „Du bekommst diese Mail für die besten Angebote von Pimpertz. Abmelden“
  - Signatur: pimpertz, Inhaber Susanne Benz, Anschrift, Telefon, Fax, E-Mail
- **Tracking:** Öffnungen und Klicks aus, UTM **an**. Der Link trägt also UTM-Parameter.
- **Landingpage** `/pages/black-week`: seit 12.11. 09:19 UTC veröffentlicht.
  - Streichpreise, z. B. 0,85 € auf 0,61 €
  - Headline „Bis zu −40 % auf offizielle Schwimmabzeichen“
  - Formular mit Single-Opt-in, Hinweis ohne Datenschutzlink
- **Rabattstruktur** (Preisliste, 106 Artikel):
  - −40 % gibt es nur auf das „Starterkit Pirat Pimpi“ (6,95 € auf 4,17 €). Das ist kein Abzeichen.
  - Höchster Rabatt auf ein Abzeichen: Regenbogen-Seepferdchen, −38 %.
  - 13 Artikel liegen bei −30 % oder mehr, 41 Artikel haben 0 %.
- **Kampagnenbericht:** Noch keine Zahlen (Bounce, Spam, Abmeldungen) verfügbar. Erneut abrufen am 13.11.

## 3. Analyse der Hauptrisiken

### R1: Werbecharakter verschleiert. Schwere 3, Wahrscheinlichkeit 3, Score 9 (GELB)

**Rechtsgrundlagen:**
- **§ 6 Abs. 2 DDG** (früher § 6 TMG): Absender und kommerzieller Charakter dürfen in Kopf- und Betreffzeile nicht absichtlich verschleiert werden. Ein Verstoß ist eine Ordnungswidrigkeit, Bußgeld bis 50.000 €.
- **§ 5a Abs. 4 UWG**: Der kommerzielle Zweck muss kenntlich sein, wenn er sich nicht aus den Umständen ergibt.
- **§ 5 UWG**: Irreführung über die Umstände. Hier wird behauptet, die Mail sei nicht für die Empfänger gedacht.
- **§ 3a UWG**: Über diese Vorschrift können Mitbewerber und Verbände (z. B. die Wettbewerbszentrale) Verstöße gegen § 6 DDG abmahnen.

**Was gegen pimpertz spricht:**
- Der Betreff „Kannst du kurz drüberschauen?“ und die Anrede „Hey Susanne“ sollen gezielt wie eine interne Mail wirken.
- „bis dahin sollte das noch niemand sehen“ ist eine unwahre Tatsachenbehauptung über den Anlass der Mail.
- Die Absicht ist intern dokumentiert. Die Planungsdateien sprechen ausdrücklich von einer „versehentlich weitergeleiteten internen Mail“.

**Was für pimpertz spricht:**
- Der Absender heißt „Anna | pimpertz“, das Unternehmen ist also erkennbar.
- Der Betreff beginnt mit „Pimpertz Black Week“. Das weist auf eine Verkaufsaktion hin.
- Im Text stehen „bis zu 40 % Rabatt“ und ein Shop-Link. In der Fußzeile steht „für die besten Angebote“ mit Abmeldelink. Spätestens beim Lesen ist der Werbezweck klar.
- Ein Bußgeld der Behörden nach § 6 DDG ist in der Praxis selten.

**Realistisches Szenario:** Ein Mitbewerber oder ein Wettbewerbsverband bekommt die Mail und mahnt ab.
- Abmahnkosten: ca. 1.000–2.500 €.
- Gefordert wird eine strafbewehrte Unterlassungserklärung. Danach kostet jede weitere Mail im gleichen Stil eine Vertragsstrafe, üblich sind ab 5.000 € pro Verstoß.
- Das ist der eigentliche Hebel: Das „Oops“-Format wäre danach dauerhaft verbrannt.

**Wahrscheinlichkeit „möglich“:** Bei 11.700 Empfängern ist nicht auszuschließen, dass ein Mitbewerber, eine Agentur oder eine juristisch versierte Person die Mail bekommt.

### R2: Einwilligung und Bestandskundenprivileg. Schwere 3, Wahrscheinlichkeit 3, Score 9 (GELB)

**Rechtsgrundlagen:**
- **§ 7 Abs. 2 Nr. 2 UWG**: E-Mail-Werbung ist nur mit vorheriger ausdrücklicher Einwilligung erlaubt.
- **§ 7 Abs. 3 UWG** (Ausnahme für Bestandskunden). Werbung ist ohne Einwilligung nur erlaubt, wenn alle vier Bedingungen erfüllt sind:
  1. Die Adresse stammt aus einem Verkauf.
  2. Beworben werden eigene, ähnliche Waren.
  3. Der Kunde hat nicht widersprochen.
  4. Er wird **bei der Erhebung und bei jeder Verwendung klar und deutlich** darauf hingewiesen, dass er jederzeit widersprechen kann, ohne dass andere als Übermittlungskosten nach den Basistarifen entstehen.

**Befund:**
- Bedingungen 1–3 dürften bei den ca. 4.000 nie abonnierten Käufern erfüllt sein. In der Stichprobe sind alle Käufer, und Schwimmabzeichen sind ähnliche Waren.
- **Bedingung 4 ist in dieser Mail nicht erfüllt.** „Du bekommst diese Mail für die besten Angebote von Pimpertz. Abmelden“ ist kein Hinweis auf das Widerspruchsrecht und die Kostenfreiheit.
- Ob der Checkout bei der Erhebung darauf hinweist, ist nicht geprüft.
- Fehlt der Hinweis, gilt die Ausnahme nicht. Dann fehlt für diese Empfänger die Rechtsgrundlage, auch nach DSGVO (Art. 6, Art. 21).
- Zusätzlich hat keiner der SUBSCRIBED-Kontakte in der Stichprobe ein Double-Opt-in. Nach BGH-Rechtsprechung muss der Versender die Einwilligung beweisen, und das gelingt in der Praxis nur mit Double-Opt-in. Das ist ein Strukturthema des ganzen Kontos, nicht nur dieser Mail.

**Szenario:**
- Ein verärgerter Empfänger, etwa ein Vereinsvorstand, mahnt selbst oder über einen Anwalt ab (Unterlassungsanspruch). Kosten ca. 500–1.500 € pro Fall.
- Daneben sind Beschwerden bei der Datenschutzaufsicht Baden-Württemberg möglich, ebenso kleine Schadensersatzforderungen nach Art. 82 DSGVO.
- Die getarnte Machart erhöht die Verärgerung und damit die Wahrscheinlichkeit.

### R3: Folgemails verlängern das Risiko. Schwere 3, Wahrscheinlichkeit 4, Score 12 (ORANGE)

**Ups-Mail** (`BW26_01b_Ups_Aufloesung_Do_12-11.txt`): Sie löst die Täuschung nicht auf, sondern setzt sie fort.
- „am Dienstag ist dir eine interne Mail von mir in den Posteingang gerutscht“
- „Danke fürs Verständnis. Und fürs Dichthalten.“
- „am Dienstag“ stimmt nicht, die Mail ging am Donnerstag raus.

**Folgemails 02 bis 06:** Die Fußzeile lautet „Du erhältst diese E-Mail, weil du dich bei pimpertz angemeldet hast.“ Für ca. 1/3 der Empfänger ist das falsch. Der Pflichthinweis nach § 7 Abs. 3 fehlt auch hier.

Jede weitere Sendung an dieselben ca. 11.700 Empfänger erhöht die Wahrscheinlichkeit. Deshalb liegt die Wahrscheinlichkeit bei 4.

### R4: Klaviyo-Konto. Schwere 4, Wahrscheinlichkeit 2, Score 8 (GELB)

Die Nutzungsrichtlinie von Klaviyo verbietet irreführende Kopfzeilen und Betreffzeilen. Bei hoher Spam-Rate (über 0,1 %) drohen Prüfung und Sperre des Versands. Eine Sperre mitten in der Black Week wäre für das Geschäft schwerwiegend, deshalb Schwere 4. Die Wahrscheinlichkeit ist niedrig, weil das Segment sauber ist (0 Bounces über alle Zeit, nur engagierte Empfänger). Kontrolle: Kampagnenbericht am 13.11.

### R5 bis R10 kurz

- **R5 (6, GELB):** Die VIP-Liste `Syrjty` läuft mit Single-Opt-in. Der Hinweis am Formular hat keinen Link zur Datenschutzerklärung. Lösung: Double-Opt-in für die Liste aktivieren und Datenschutzlink ergänzen, vor dem 23.11.
- **R6 (6, GELB):** Die Mail sagt „bei ein paar Sachen … bis zu 40 %“. Das ist durch die Einschränkung vertretbar. Die Landingpage verspricht aber „Bis zu −40 % auf offizielle Schwimmabzeichen“. Kein Abzeichen erreicht −40 %, maximal sind es −38 %. „Bis zu“-Werbung ist abmahnträchtig, wenn der Höchstwert nur für einen Randartikel gilt. Lösung: „Bis zu −40 %“ ohne „auf Schwimmabzeichen“ oder „bis zu −38 % auf Schwimmabzeichen“.
- **R7 (4, GRÜN):** Als Streichpreis muss der niedrigste Preis der letzten 30 Tage vor der Reduzierung stehen, hier vom 24.10. bis 22.11. Das ist erfüllt, wenn es in diesem Zeitraum keine Aktion gab und bis zum 23.11. keine Preise geändert werden. Bitte kurz bestätigen.
- **R8 (6, GELB):** Vereine, Schulen und Schwimmschulen sind institutionelle Kunden mit Vertrauensbeziehung. Wird die Masche öffentlich (Social Media, Elternforen), schadet das der Glaubwürdigkeit als Anbieter offizieller Abzeichen. Antworten auf die Mail landen bei info@pimpertz.de.
- **R9 (2, GRÜN):** Die Verbandsadressen wurden angelegt, um sie zu sperren. Grundlage ist das berechtigte Interesse (Art. 6 Abs. 1 lit. f DSGVO): Sperrlisten sollen sicherstellen, dass keine Werbung ankommt. Das ist üblich und vertretbar.
- **R10 (2, GRÜN):** Abmeldelink ist vorhanden, Klaviyo setzt den List-Unsubscribe-Header. Absender, Anschrift und Inhaberin stehen in der Signatur. Eine USt-IdNr. fehlt, falls vorhanden, ist bei E-Mails aber umstritten und nachrangig.

## 4. Was das Risiko erhöht

- Die Täuschungsabsicht ist intern schriftlich dokumentiert.
- Etwa 1/3 der Empfänger haben keine Einwilligung, und die Fußzeile erfüllt § 7 Abs. 3 Nr. 4 nicht.
- Es sind 5–6 Folgesendungen an dieselbe Zielgruppe geplant.
- Die Nische ist klein, Mitbewerber kennen sich und können unter Privatadressen auf der Liste stehen.

## 5. Was das Risiko senkt

- „pimpertz“ steht im Absender und im Betreff, „Black Week“ steht im Betreff. Rabatt und Shop-Link stehen im Text.
- Das Segment ist sauber: 0 Bounces über alle Zeit, nur engagierte Empfänger. Die Verbände und Weiterleitungsadressen ohne Kauf sind ausgeschlossen.
- Alle nie abonnierten Empfänger in der Stichprobe sind echte Käufer. Das Bestandskundenprivileg lässt sich also mit einer Textänderung ab der nächsten Mail herstellen.
- Abmeldelink und vollständige Kontaktdaten sind vorhanden.

## 6. Maßnahmen

| Maßnahme | Wirkung | Aufwand | Empfohlen |
|---|---|---|:-:|
| **A. Ups-Mail umschreiben:** Den Teaser ehrlich auflösen, nicht weiter täuschen | Hoch (R1, R3, R8) | Niedrig | **Ja** |
| **B. Fußzeile in allen Folgemails** auf einen Hinweis umstellen, der für Abonnenten und Käufer passt und § 7 Abs. 3 erfüllt (Text unten) | Hoch (R2, R3) | Niedrig | **Ja** |
| C. Folgemails mit klarem Werbebetreff, kein zweites „Oops“-Format | Hoch (R1, R4) | Niedrig | Ja |
| D. Landingpage-Headline korrigieren (R6) | Mittel | Niedrig | Ja |
| E. Double-Opt-in für die VIP-Liste und Datenschutzlink am Formular (R5) | Mittel | Niedrig | Ja |
| F. Streichpreise gegen den 30-Tage-Tiefstpreis prüfen (R7) | Mittel | Niedrig | Ja |
| G. Bericht am 13.11.: Spam über 0,1 % oder Bounce über 1 % heißt stoppen | Mittel (R4) | Niedrig | Ja |
| H. Kurze, ehrliche Antwortvorlage für info@ („Erwischt, das war unser Teaser …“) | Mittel (R8) | Niedrig | Ja |
| I. Nur noch Abonnenten mit Einwilligung anschreiben, also ohne nie abonnierte Käufer | Hoch (R2) | Mittel, kostet Reichweite (ca. 1/3) | Nur, wenn B nicht umgesetzt wird |
| J. Anwaltliche Vorprüfung der Folgemails und Notfallplan für Abmahnungen | Mittel | Mittel | Ja, vor dem 23.11. |

**Vorschlag Fußzeile (B), grau und klein ist zulässig, der Text muss vollständig sein:**

> Du erhältst diese E-Mail, weil du bei pimpertz bestellt oder dich für unseren Newsletter angemeldet hast. Du kannst der Nutzung deiner E-Mail-Adresse für Werbung jederzeit widersprechen, ohne dass dir dafür andere als die Übermittlungskosten nach den Basistarifen entstehen: {% unsubscribe 'Abmelden' %}
> pimpertz · Inhaber Susanne Benz · Pappelweg 12 · 72202 Nagold · info@pimpertz.de

**Vorschlag Ups-Mail (A), Kernaussage:**

> Betreff: Ups. Das war kein Versehen.
> Ja, die Mail an „Susanne“ war unser Black-Week-Teaser 😉 Die Rabatte bis 40 % gibt es wirklich. Wer sich bis Sonntag einträgt, kommt am Montag, 23.11., um 10:30 Uhr 24 Stunden früher rein: https://pimpertz.de/pages/black-week

## 7. Empfohlenes Vorgehen

1. Die versendete Mail lässt sich nicht zurückholen. Keine weitere Mail in diesem Format.
2. Die Ups-Mail (A) mit Fußzeile (B) als ehrliche Auflösung versenden. Damit wird der Werbecharakter nachträglich offen und die Täuschung endet nach 1–2 Tagen. Das ist das stärkste Argument gegen eine Abmahnung.
3. B, C, D, E und F vor dem VIP-Start am 23.11. umsetzen.
4. Falls eine Abmahnung kommt: Die beigefügte Unterlassungserklärung **nicht unverändert unterschreiben**. Fristen notieren, sofort eine Anwältin oder einen Anwalt für Wettbewerbsrecht beauftragen. Meist wird eine modifizierte Erklärung abgegeben.

## 8. Restrisiko nach Umsetzung

| | vorher | nachher |
|---|:-:|:-:|
| R1 | 9 GELB | 6 GELB (die versendete Mail bleibt, die Auflösung entschärft sie) |
| R2 | 9 GELB | 4 GRÜN (die Folgemails erfüllen § 7 Abs. 3, die Oops-Mail bleibt ein Altfall) |
| R3 | 12 ORANGE | 4 GRÜN |
| R4 | 8 GELB | 4 GRÜN |
| R5/R6 | je 6 GELB | je 2 GRÜN |

## 9. Monitoring

- **13.11.:** Kampagnenbericht abrufen (Zustellung, Bounce, Spam, Abmeldungen). Antworten an info@ auf Beschwerden durchsehen.
- **Bis 1.12. täglich:** Eingang info@ und Post auf Abmahnungen oder Beschwerden prüfen.
- **Neu bewerten, wenn:**
  - eine Abmahnung eingeht,
  - die Datenschutzaufsicht anfragt,
  - die Spam-Rate über 0,1 % liegt,
  - die Mail öffentlich diskutiert wird.

## 10. Nächste Schritte

| # | Aufgabe | Verantwortlich | Bis |
|---|---|---|---|
| 1 | Ups-Mail nach Vorschlag A neu texten, Fußzeile B, Testmail an leonbenz@leon-benz.com, Versand nach GO | Leon / Claude | Sa 14.11. |
| 2 | Fußzeile B in die Templates 02–06 und in die Klaviyo-Templates übernehmen | Claude (nach GO) | So 15.11. |
| 3 | Landingpage-Headline (D) und Datenschutzlink (E) anpassen, Double-Opt-in für `Syrjty` einschalten | Leon / Claude | So 15.11. |
| 4 | Streichpreise gegen den Preisverlauf vom 24.10. bis heute bestätigen | Leon | Fr 20.11. |
| 5 | Kampagnenbericht der Oops-Mail auswerten | Claude | Fr 13.11. |
| 6 | Checkout-Hinweis bei der Adresserhebung (§ 7 Abs. 3 Nr. 4) im Shopify-Checkout prüfen und ergänzen | Leon | Fr 20.11. |
| 7 | Anwaltliche Kurzprüfung der Folgemails und der Fußzeile | Leon | Fr 20.11. |
