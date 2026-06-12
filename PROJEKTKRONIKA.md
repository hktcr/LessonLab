
## 2026-03-19
- **Kemi:** Skapade interaktivt pH-demonstrationsverktyg. Verktyget har anpassats för högstadieelever med pedagogisk kontext, korrekt vetenskaplig notation (t.ex. H₂SO₄, OH⁻) och rensats enligt Håkans språkliga stilguide. Justerade även dag 2-manuset med en ny "Begreppsletning i provhäftet"-aktivitet.

## 2026-05-13
- **KlassPuls:** Systemet "KlassPuls" lanserades officiellt och integrerades i LessonLab-ekosystemet (inlett via Attenborough-lektionen).
- **Infrastruktur:** Verktyget paketerades i en Zero-Build arkitektur, med fullt stöd för "lärares skärmövertagande" (live-synkade hex-meddelanden som rundgår URL/CORS-problem) och dynamisk poängberäkning vid mjuka avbrott. 
- **Formalisering:** Replikeringslogiken systematiserades – inte bara i ett doldt KI-minne – utan via det publika Obsidian-workflowet `/klasspuls` och en teknisk `README.md` direkt i LessonLab/q-repot, i enlighet med principen för sökbarhet.

### 2026-06-02 | KlassPuls UX-revision — från komplexitet till klassrumsrobusthet

**Bakgrund & Syfte:**
- Inför lektion 2 av Attenborough-filmen behövde lärargränssnittet och elevvyn i KlassPuls (attenborough.html) finjusteras utifrån erfarenheter från första användningen.

**Utfört:**
- **Klassväljare borttagen.** Det dynamiska rumssystemet (där elever skrev in klassnamn) ersattes med ett enda delat rum. Läraren nollställer mellan klasser med befintlig knapp. Förenkling efter insikt att klassväljaren skapade fler problem (felstavningar, förvirring) än den löste.
- **Lärarpanel berikad:** Elev-länk med kopiera-knapp tillagd i headern. Rätt svarsalternativ markeras med ✅ i accordion-vyn. Scroll-bugg fixad (body hade `overflow:hidden` + vertikal centrering som dolde panelens topp på långa sidor).
- **Elevvy renodlad:** Titel visar bara filmnamnet utan "KlassPuls"-prefix. Vänttext ändrad till "visa första frågan" istället för "starta filmen". Frågenumrering är nu sessionsbaserad (Fråga 1, 2, 3…) istället för bankindex (Fråga 15 av 27), eftersom läraren styr antal pushade frågor per lektion.
- **Del 2-manus (LessonLab):** Action buttons (Slide, Elev-länk, Lärarpanel, Netflix) tillagda för paritet med del 1. Duplicerat gammalt innehåll med trasig teckenkodning städat bort, full omskrivning med korrekt UTF-8.
- **gAIa-verktyg:** Attenborough-kortet pekar nu på lärarpanelen (`?mode=teacher`) istället för elevvyn.

**Beslut & Lärdomar:**
- *Enkelhet > Elegans.* Klassväljaren var en tekniskt elegant lösning på ett problem som inte existerade i praktiken. En nollställ-knapp räckte.
- *Interna namn läcker.* "KlassPuls:" som titel i elevvyn och "Fråga 15 av 27" avslöjar systemets interna struktur för användaren utan att tillföra värde.

**Nästa steg:**
- Använda gränssnittet på lektion 2 av Attenborough och samla ytterligare feedback.

📡 Satelliter: RESUME — | PI — | Trackers — | TC —

*Signatur: gAIa 🌲 2026-06-02*

---

### 2026-06-04 | SoundPulse v1.0: Interaktiv lyssnarövning med självgående läge

**Koppling till tidigare arbete:**
- ✅ "Använda gränssnittet på lektion 2 av Attenborough" → Genomfört (2026-06-03)
- 🔄 KlassPuls-erfarenheterna (slot-arkitektur, klassrumsrobusthet) bar direkt frukt i SoundPulse

**Bakgrund & Syfte:**
- Håkan ville ett nytt verktygsformat i LessonLab: en **lyssnarövning** där eleverna lyssnar på ett radioprogram via smartboarden medan individuella frågor triggas automatiskt på varje elevs enhet vid exakta tidpunkter i programmet. Programmet: Dagens Eko om sammetsgetingen (*Vespa velutina*), 19.8 minuter, 259 transkriptionssegment.
- Till skillnad från KlassPuls (läraren pushar frågor manuellt) skulle SoundPulse vara helt **självgående**: läraren spelar upp ljud, övningen sköter resten.

**Utfört (Process & Roller):**

*Session 1 (2026-06-01): Grundbygge*
- VEP-panel (5 roller: Ljudpedagog, UX-designer, Ekolog, Tillgänglighetsexpert, Systemarkitekt) granskade konceptet och frågorna.
- Grundarkitektur: transkript-synkad textvisning, visuella segment med bilder, 19 frågor (MC, match, freetext, feedback).
- Slot-baserad elevregistrering (40 slots) med heartbeat (15s) för att eliminera race conditions vid inloggning.

*Session 2 (2026-06-02): Klassrumstest & refaktorering*
- Testkört med ~20 elever. Upptäckte att "lärarpush"-läget skapade onödig komplexitet.
- **Beslut: Självgående läge.** All lärarpush-logik (`startLiveSync`, `teacherPushQuestion`, `sendTeacherMsg`, `clearTeacherMsg`) togs bort. Frågor triggas enbart av elevens egen ljudtid.
- Frågeordning fixades (hade fel sekvens), HTML-escaping av glossar fixades, tooltip-bindning (`q.question` → `q.text`) fixades.

*Session 3 (2026-06-04): Bugfix, stilgranskning & transkript*
- **Bugg 1: Dubbel hex-encoding.** `submitFeedback` hex-kodade svaret, sedan hex-kodade `_flushAnswers` det igen. Lärarvyn fick skräptecken istället för betyg och kommentarer. Fix: tog bort den första `strToHex()`.
- **Bugg 2: Komma-delimiter-kollision.** Kommatecken i elevkommentarer (t.ex. "Toppen, bra!") bröt sönder svarsdelimitern. Alla svar efter feedbackposten blev oläsbara, och rutorna i lärarvyn slutade färgas. Fix: escape-sekvens `\c` vid lagring, unescape vid läsning.
- **Bugg 3: Dubbel hexToStr i lärarvyn.** Feedbacksektionen avkodade data som redan avkodats. Fix: tog bort redundant `hexToStr()`.
- **Ny funktion: Kopieringsknapp** i feedbacksektionen. Läraren kan kopiera alla betyg och kommentarer till urklipp.
- **Stilgranskning (§4b):** 7 av 19 frågor hade em-dash i svarsalternativ. Samtliga ersatta med kolon, komma eller parentes.
- **Faktafel:** propolis ≠ bivax (F7), absurd distraktor "säljs i djuraffärer" (F14) ersatt med realistisk.
- **Omskrivningar:** F11 (kategoriseringsfråga → MC om signalkräftan), F15 (frågeställning matchade inte svaren → "Vilken typ av ekosystemtjänst är pollinering?"), F16 (predation kallades "samspel" → "förhållande").
- **Transkriptverifiering:** 7 segment korrigerade med Whisper large-v3 (ASR-brus, segment-bleed, felaktig ordidentifiering).

**Beslut & Lärdomar:**
- *Encoding-asymmetri är den farligaste buggkategorin.* Eleven ser "Tack!", läraren ser ingenting. Systemet *upplevs* som fungerande av alla utom den person som behöver datan.
- *Komma i fritext dödar delimiter-baserade protokoll.* Escape-sekvenser behövs i alla system som lagrar användartext i delimiterade strängar.
- *Stilguiden ska konsulteras FÖRE frågeskrivning, inte efter.* Sju em-dash-brott hade undvikits om §4b konsulterats under skapandet.
- *Självgående läge > lärarstyrt* för lyssnarövningar. Läraren ska fokusera på klassrummet, inte på att trycka "nästa fråga".
- *KV-API (keyvalue.immanuel.do) klarar 40 parallella slots* utan problem, men strängstorleken per nyckel är begränsad. Hex-encoding fördubblar storleken.

**Öppna frågor:**
- [ ] Feedback-data från det första klassrumstestet (2026-06-02) gick förlorad pga hex-buggen. Kan den återskapas från API:t?
- [ ] Ska SoundPulse-formatet generaliseras till andra SR-program (t.ex. Vetenskapsradion)?
- [ ] Behövs en egen PROJEKTKRONIKA för SoundPulse-repot, eller räcker LessonLab-krönikan?

**Nästa steg:**
- Testa den fixade versionen med en ny klass för att verifiera att feedback samlas in korrekt.
- Utvärdera feedbackdatan pedagogiskt: vilka frågor var för svåra/lätta?

📡 Satelliter: RESUME ✅ | PI — | Trackers — | TC —

*Signatur: gAIa 🌲 2026-06-04*

---
