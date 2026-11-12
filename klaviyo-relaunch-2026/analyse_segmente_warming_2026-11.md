# Segment- und Warming-Analyse aller Klaviyo-Kampagnen (Mai 2025 – Juli 2026)

Stand 12.11.2026. Quelle: Klaviyo Campaign Report (E-Mail, Conversion = Placed Order), Segment-Definitionen per API. Alle Werte sind echte Klaviyo-Zahlen; Raten = Anteil an Empfängern. Testsendungen an Seedlisten sind nicht berücksichtigt.

## 1. Warming-Mails Black Week 2025 im direkten Vergleich

| Datum | Betreff | Zielgruppe | Empfänger | Klickrate | Bounce | Abmelde | Spam | Conversion |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Di 18.11.25 | „Ein Vierteljahrhundert voller Bewegung – ein Dankeschön aus dem Wasser“ (kein Preview-Text) | alle Listen | 14.169 | **0,61 %** | 4,1 % | 1,11 % | 4 | 0,11 % |
| Do 20.11.25 | „Ein besonderer Moment für {{first_name}} startet am 24. November“ · Preview: „24 Stunden früherer Zugang – nur für unsere treuesten Kundinnen und Kunden“ | alle Listen | 13.803 | **4,93 %** | 3,9 % | 1,22 % | 2 | 0,44 % |

**Beste Warming-Mail: 20.11.2025.** Fast gleiche Zielgruppe, ~8× Klickrate. Unterschied ist der Inhalt: konkretes Datum + konkreter Vorteil (24 h früher) + Preview-Text statt allgemeinem Dank.
Schwäche beider Mails: an „pimpertz Email Liste ALL“ gesendet → Bounce 4,4–4,6 % auf dieser Liste (Reputationsrisiko ab ~2 %).

## 2. Angebotsmails Black Week 2025

| Datum | Zielgruppe | Empfänger | Öffnung | Klick | Bounce | Abmelde | Conversion |
|---|---|---:|---:|---:|---:|---:|---:|
| Mo 24.11. Launch | Segment „black week launch 25 years“ (alle Listen, Soft-Bounce-Filter) | 12.600 | 32,8 % | 6,0 % | 1,0 % | 1,85 % | 1,46 % |
| Fr 28.11. Black Friday | **„black friday mail, segment A“** | 4.051 | **50,0 %** | **6,9 %** | **0,1 %** | 2,74 % | **1,58 %** |
| Fr 28.11. Black Friday | Engaged Non-Opener der Warming-Mail | 1.641 | 33,3 % | **7,7 %** | 0,4 % | 2,26 % | 1,41 % |

## 3. Segmente aus WM 2026 (Juni) – kumuliert über alle Sendungen

| Segment (Definition) | Empfänger | Öffnung | Klick | Bounce | Abmelde | Spam | Conversion |
|---|---:|---:|---:|---:|---:|---:|---:|
| WM · B2B · engaged (Lifetime-Umsatz ≥ 10 €, je geöffnet/geklickt) | 12.051 | 56 % | **3,8 %** | 1,0 % | 1,95 % | 0 | **1,11 %** |
| WM · Non-Buyer · engaged (je geöffnet/geklickt, nie gekauft) | 12.433 | 56 % | 2,4 % | 2,0 % | 1,86 % | 1 | 0,26 % |
| WM · B2C · engaged (Käufer < 10 € Umsatz, je geöffnet/geklickt) | 4.257 | 55 % | 1,3 % | 0,3 % | **5,37 %** | 3 | 0,09 % |
| WM · B2B · dormant (≥ 10 €, nie geöffnet/geklickt) | 4.688 | 15 % | 1,1 % | **3,1 %** | 1,81 % | 0 | 0,20 % |
| WM · B2C · dormant (< 10 €, nie geöffnet/geklickt) | 2.284 | 21 % | 0,5 % | 0,3 % | 3,69 % | 1 | 0 % |
| Follow-up an Engaged Non-Opener (Launch) | 2.767 | 25 % | 1,7 % | 0,2 % | 2,50 % | 1 | 0,43 % |

Hinweis: „B2B“ ist in diesen Segmenten technisch „Lifetime-Umsatz ≥ 10 €“, nicht ein echtes Vereins-Flag.

## 4. Frühere Sendungen 2025 (Reputation)

| Kampagne | Zielgruppe | Empfänger | Bounce | Abmelde | Conversion |
|---|---|---:|---:|---:|---:|
| Go-to-live Seepferdchen (26.05.25) | Rapidmail Active Contacts | 7.492 | 4,5 % | **0,14 %** | 1,69 % |
| Follow-up Engaged Non-Opener (28.05.25) | Segment | 706 | 0,6 % | 0 % | **2,14 %** |
| Go-Live Special ALL (27.05.25) | pimpertz All (nicht Rapidmail) | 3.633 | **21,7 %** | 0,74 % | 1,27 % |
| Never Receiver Winback (20./21.08.25) | Never Received Warm-Up | 889 | **75,6 %** | 0,9 % | 0 % |

## 5. Learnings (nur aus den Zahlen oben)

1. **Engagement-Segment schlägt Liste.** Gleiche Saison: Listen-Versand 4 % Bounce, Engaged-Segment A 0,1 % Bounce, höchste Öffnungs-, Klick- und Kaufrate.
2. **Warming braucht Datum + Vorteil.** „Startet am 24. November / 24 h früher“ = 4,9 % Klick; „Dankeschön“ = 0,6 %.
3. **Follow-up an Engaged Non-Opener funktioniert jedes Mal** (BF 25: 7,7 % Klick; Mai 25: 2,1 % Conversion; WM 26: 0,43 %) bei sehr niedrigem Bounce.
4. **Käufer mit Umsatz ≥ 10 € sind die Kernzielgruppe** (WM 26: 1,11 % Conversion, 0 Spam).
5. **Kleinkäufer < 10 € und Dormant-Profile kosten Reputation**: 3,7–5,4 % Abmelderate, Spam-Beschwerden, fast keine Käufe.
6. **Nie ungeprüfte Alt-Listen anschreiben** (21,7 % bzw. 75,6 % Bounce).
7. Abmelderaten sind 2026 generell höher als 2025 (~2 % statt ~1 %) → Frequenz und Zielgruppe enger halten.

## 6. Zielgruppe für die Oops-Mail (BW26 · 01)

Ziel: VIP-Eintragungen, hohe Klickrate, Reputation schützen.

**Senden an**
- „black friday mail, segment A“ (XxRXUx): E-Mail-Einwilligung · kein Soft-Bounce in 300 Tagen · (geöffnet in 90 Tagen ODER geklickt in 120 Tagen ODER Bestellung in 300 Tagen) · keine Bestellung in den letzten 10 Tagen. Bestes Segment 2025.
- VIP-Liste „VIP Pre-Sale 24h“ (Syrjty)

**Ausschließen**
- Sunset Suppressed (Auto) · Sunset Liste/Exclude E-Mail · Sunset: Never Engaged + High Bounce (Hybrid) · Exclude: High Bounce Risk (3+ Bounces)

**Nicht mehr senden an** „pimpertz Email Liste ALL“, „Shopify Profile ab 07.08.2025“, „Exit Popup Liste“ als ganze Listen (Bounce-Treiber 2025).

**Do 12.11.-Nachfass („Ups“)**: nur an Engaged Non-Opener der Oops-Mail (Klaviyo-Follow-up, wie BF 25).

Blocker: Segment A und „High Bounce Risk“ sind in Klaviyo inaktiv (seit > 90 Tagen ungenutzt) und lassen sich per API nicht in eine Kampagne setzen. Einmal in der Klaviyo-Oberfläche öffnen → reaktivieren, danach Zielgruppe zuweisen.
