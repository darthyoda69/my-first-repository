# Ausschlussliste: Verbände, SchwimmWelten, Weiterleitungsadressen

Stand 12.11.2026. Quellen: Klaviyo-Profile (exakte Adressprüfung), Shopify-Kunden inkl. Bestellanzahl, Impressum schwimmwelten.de, Verbandsseiten, eure Gmail-Korrespondenz.

## 1. SchwimmWelten GmbH und Verbände: erledigt (von Marketing abgemeldet)

SchwimmWelten GmbH, Tiergartenstraße 13/2, 69121 Heidelberg (HRB 751356, AG Mannheim). Geschäftsführer laut Impressum: Holger Voigt, Dr. Manuel Kopitz, Frank Müller-Steidner, Frank Rabe, Emanuel Vailakis. Getragen von den Landesschwimmverbänden Baden, Berlin, NRW, Sachsen, Württemberg.

| Adresse | Person / Organisation | Rolle | Shopify-Bestellungen | Klaviyo-Status jetzt |
|---|---|---|---:|---|
| holger.voigt@bsvonline.de | Holger Voigt, Badischer Schwimm-Verband | GF SchwimmWelten | 0 | abgemeldet |
| f.rabe@schwimmverband.nrw | Frank Rabe, Schwimmverband NRW | GF SchwimmWelten | 0 | abgemeldet (war seit 18.11.2025 gesperrt) |
| f.rabe@cityweb.de | Frank Rabe (vermutlich privat) | GF SchwimmWelten | 0 | abgemeldet |
| emanuel.vailakis@svw-online.de | Emanuel Vailakis, Schwimmverband Württemberg | GF SchwimmWelten | – | abgemeldet (vorsorglich angelegt) |
| gs@lsv-sachsen.de | Sächsischer Schwimm-Verband, Geschäftsstelle (Frank Müller-Steidner) | GF SchwimmWelten | 0 | abgemeldet |
| info@berliner-schwimm-verband.de | Berliner Schwimm-Verband (Dr. Manuel Kopitz) | GF SchwimmWelten | – | abgemeldet (vorsorglich angelegt) |
| info@schwimmwelten.de | SchwimmWelten GmbH | Firma | – | abgemeldet (vorsorglich angelegt) |
| info@bsvonline.de | Badischer Schwimm-Verband | Verband | – | abgemeldet (vorsorglich angelegt) |
| info@svw-online.de | Schwimmverband Württemberg | Verband | – | abgemeldet (vorsorglich angelegt) |
| info@schwimmverband.nrw | Schwimmverband NRW | Verband | – | abgemeldet (vorsorglich angelegt) |
| info@lsv-sachsen.de | Sächsischer Schwimm-Verband | Verband | – | abgemeldet (vorsorglich angelegt) |
| info@lsv-brandenburg.de | Landesschwimmverband Brandenburg (Maren Nagel) | Verband | 0 | abgemeldet |
| sbz@lsv-sh.de | Landesschwimmverband Schleswig-Holstein (Sascha Thodt) | Verband | 0 | abgemeldet |
| info@lsv-sh.de | Landesschwimmverband Schleswig-Holstein | Verband | – | abgemeldet (vorsorglich angelegt) |
| info@dsv.de | Deutscher Schwimm-Verband | Verband | – | abgemeldet (vorsorglich angelegt) |
| marion.huerse@lsv-sh.de | LSV Schleswig-Holstein | Verband | 0 | war schon gesperrt (Hard Bounce) |
| katja.kugelstadt@lsv-sh.de | LSV Schleswig-Holstein | Verband | 0 | war schon gesperrt (Hard Bounce) |

Abmeldung über die Klaviyo-API: keine Bestätigungsmail, kein Flow auf „abgemeldet“ vorhanden. Transaktionsmails (Bestellung/Versand) laufen weiter.

## 2. Verbandsbezug mit Käufen: nicht angefasst, bitte entscheiden

| Adresse | Organisation | Shopify-Bestellungen | Umsatz | Klaviyo |
|---|---|---:|---:|---|
| focke@schwimmverband-wuppertal.de | Schwimmverband Wuppertal e.V. (Petra Focke) | 5 | 2.497,95 € | abonniert |
| dieterhaendeler@gmx.de | Freie Schwimmer Wuppertal 07 e.V. (Carmen Händeler) | 4 | 477,80 € | abonniert |

Empfehlung: drinlassen, das sind Vereinsstrukturen und Kunden.

Ebenfalls Kunden, keine Konkurrenz: DLRG-Ortsgruppen, Wasserwacht-Gruppen, Vereine mit „LSV“ im Namen (z. B. LSV Delphin 1990 Ludwigsfelde, lsv1990.de, lsv02.agriesert@web.de).

## 3. Shopify-Kundenkonten der Landesverbände ohne E-Mail (keine Mails möglich)

Berliner, Württembergischer, Saarländischer, Rheinland-, Thüringer, Mecklenburg-Vorpommern-, Niedersachsen-, Bayerischer (inkl. Herr Gerstacker), Bremer, Hamburger, Hessischer, Sachsen-Anhalt-, Schleswig-Holstein-, Westdeutscher, Brandenburger Schwimmverband sowie Schwimmverband Rhein-Wupper: alle 0 Bestellungen, ohne hinterlegte E-Mail.

## 4. Weiterleitungs- und Wegwerfadressen: Liste nur über Klaviyo-Segment möglich

Die Klaviyo-API sucht nur nach exakten Adressen, nicht nach Domains. Shopify ignoriert Domain-Filter. In Shopify gibt es keine @privaterelay.appleid.com-Adressen.

Segment in der Klaviyo-Oberfläche anlegen: **„Ausschluss · Weiterleitungsadressen ohne Kauf“**. Bedingungen mit UND verknüpft:

1. **E-Mail endet auf** einer dieser Domains (ODER-Gruppe):
   - `@privaterelay.appleid.com` (Mit Apple anmelden)
   - `@mozmail.com` (Firefox Relay)
   - `@duck.com` (DuckDuckGo)
   - `@simplelogin.com`, `@aleeas.com`, `@slmail.me`, `@simplelogin.fr` (SimpleLogin / Proton)
   - `@passmail.net`, `@passinbox.com`, `@passfwd.com` (Proton Pass)
   - `@anonaddy.me`, `@anonaddy.com`, `@addy.io` (addy.io)
   - `@33mail.com`
   - `@trashmail.de`, `@wegwerfmail.de`, `@yopmail.com`, `@mailinator.com` (Wegwerf)
2. **Placed Order 0-mal über alle Zeit.**

Danach liest die API die Mitglieder des Segments aus, und daraus wird die vollständige Adressliste erstellt. Abmelden oder als Ausschluss in alle Kampagnen hängen.

**iCloud+ „E-Mail-Adresse verbergen“:** Diese Adressen enden auf normales `@icloud.com` und sehen zufällig aus. Ein zweites Segment „E-Mail endet auf @icloud.com UND Placed Order 0-mal“ anlegen, die Liste exportieren und die zufällig wirkenden Adressen von Hand markieren. Nicht pauschal alle @icloud.com sperren, sonst trifft es echte Eltern.

## 5. Dauerhafter Schutz

Segment **„Ausschluss · Verbände/SchwimmWelten“**: E-Mail enthält `schwimmwelten` ODER `bsvonline` ODER `svw-online` ODER `schwimmverband.nrw` ODER `lsv-sachsen` ODER `lsv-brandenburg` ODER `lsv-sh` ODER `berliner-schwimm-verband` ODER `@dsv.de`. Als Ausschluss in jede Kampagne. Damit sind auch künftige Neuanmeldungen aus den Verbänden abgedeckt.

## 6. Empfänger der Oops-Mail nach Domain (Stand 12.11.2026 abends)

11.691 Empfänger auf 2.409 Domains (vollständige Liste: `oops_empfaenger_domains_2026-11-12.csv`).

- DLRG: 108 Empfänger, rund 100 Ortsgruppen und Bezirke (plus dlrg.de)
- Wasserwacht und Rotes Kreuz: 64 (davon wasserwacht.bayern 30, brk.de 6)
- Sportbünde und Verbände: ca. 14 (Kreis- und Stadtsportbünde, Sportjugend, LSB Sachsen-Anhalt, dguv.de, Schwimmverband Wuppertal). Keine Landesschwimmverbände, kein DSV, nichts mit „bfs“.
- Schulen: ca. 360 (ohne Schwimmschulen). Kommunen, Bäder und Stadtwerke: über 200.
- Kanzleien: 3 (dierlamm-rechtsanwaelte.com, heuvelslaw.com, rechtsanwalt-presch.de)
- Testdienste für Zustellbarkeit (Seed-Adressen), 14 Empfänger: buyemailsoftware.com, deliverabble.com, deliverabilitylabs.com, emailreach.co, reputationwarmup.com, fastdirectorysubmitter.com, inboxdoctors.com, landininbox.com, reachsecret.com, smartemailers.com, postmasterpro.email, outreachrs.com. **Empfehlung: abmelden** und ins Ausschluss-Segment aufnehmen.
- Weiterleitungsadressen mit Kauf: 4 (passmail.net 2, duck.com, addy.io)
