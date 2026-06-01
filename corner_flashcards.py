import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Add CSS for corner-flashcard
css_to_add = """
        .corner-flashcard {
            position: absolute;
            bottom: 3rem;
            right: 4rem;
            width: 240px;
            height: 140px;
            z-index: 50;
        }
        .corner-flashcard .flashcard-front {
            font-size: 1.4rem;
        }
        .corner-flashcard .flashcard-back {
            font-size: 1rem;
            padding: 1rem;
        }
"""
content = content.replace("</style>", css_to_add + "</style>")

# 2. Slide 3
s3_old = """            <div class="glossary-grid" style="margin-top: 3rem;">
                <div class="flashcard\""""
s3_new = """            <div class="corner-flashcard">
                <div class="flashcard\""""
content = content.replace(s3_old, s3_new)

# 3. Slide 4 (Mutualism) - Revert slide-split
s4_old = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Mellan ekorren och fågeln sitter en varelse som inte liknar någonting.', 'Rötterna lyser.', 'Det är inte tydligt hur kopplingen mellan svampens hyfer (mycelet) och trädets rötter ser ut.'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">mutualism</div>
                        <div class="flashcard-back">En typ av symbios där alla inblandade arter vinner på samarbetet (t.ex. mykorrhiza mellan träd och svamp).</div>
                    </div>
                </div>
            </div>
        </div>
    </div>"""
s4_new = """            <div class="image-container" style="margin: 2rem auto;">
                <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="max-height: 50vh; cursor: pointer;" onclick="openImageModal(this.src, this.src, ['Mellan ekorren och fågeln sitter en varelse som inte liknar någonting.', 'Rötterna lyser.', 'Det är inte tydligt hur kopplingen mellan svampens hyfer (mycelet) och trädets rötter ser ut.'])">
            </div>
            <p class="subtitle" style="font-style: italic;">
                Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
            </p>

            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">mutualism</div>
                        <div class="flashcard-back">En typ av symbios där alla inblandade arter vinner på samarbetet (t.ex. mykorrhiza mellan träd och svamp).</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s4_old, s4_new)

# 4. Slide 5 (Kommensalism)
s5_old = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Inga uppenbara felaktigheter?'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: havstulpaner som får biologisk snålskjuts av valar.
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">kommensalism</div>
                        <div class="flashcard-back">En typ av symbios där den ena arten vinner på det, medan den andra är helt opåverkad (t.ex. havstulpaner som får åka med på en val).</div>
                    </div>
                </div>
            </div>
        </div>
    </div>"""
s5_new = """            <div class="image-container" style="margin: 2rem auto;">
                <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="max-height: 50vh; cursor: pointer;" onclick="openImageModal(this.src, this.src, ['Inga uppenbara felaktigheter?'])">
            </div>
            <p class="subtitle" style="font-style: italic;">
                Exempel: havstulpaner som får biologisk snålskjuts av valar.
            </p>

            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">kommensalism</div>
                        <div class="flashcard-back">En typ av symbios där den ena arten vinner på det, medan den andra är helt opåverkad (t.ex. havstulpaner som får åka med på en val).</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s5_old, s5_new)

# 5. Slide 6 (Parasitism)
s6_old = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Fästingen har fem ben på sin högra sida.'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">parasitism</div>
                        <div class="flashcard-back">En typ av symbios där den ena arten vinner, medan den andra utnyttjas och tar skada (t.ex. fästing och hund).</div>
                    </div>
                </div>
            </div>
        </div>
    </div>"""
s6_new = """            <div class="image-container" style="margin: 2rem auto;">
                <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="max-height: 50vh; cursor: pointer;" onclick="openImageModal(this.src, this.src, ['Fästingen har fem ben på sin högra sida.'])">
            </div>
            <p class="subtitle" style="font-style: italic;">
                Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
            </p>

            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">parasitism</div>
                        <div class="flashcard-back">En typ av symbios där den ena arten vinner, medan den andra utnyttjas och tar skada (t.ex. fästing och hund).</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s6_old, s6_new)

# 6. Slide 7 (Konkurrens)
# We change grid-template-columns back to repeat(2, 1fr) if we want, or just auto-fit.
s7_old_grid = """            <div class="content-grid" style="margin-top: 2rem; grid-template-columns: repeat(3, 1fr); align-items: start;">"""
s7_new_grid = """            <div class="content-grid" style="margin-top: 3rem;">"""
content = content.replace(s7_old_grid, s7_new_grid)

s7_old_flashcard = """                <div class="flashcard-wrapper" style="margin-top: 0; align-self: stretch;">
                    <div class="flashcard" style="width: 100%;" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                        <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                            <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                            </svg>
                        </button>
                        <div class="flashcard-inner">
                            <div class="flashcard-front">konkurrens</div>
                            <div class="flashcard-back">När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser).</div>
                        </div>
                    </div>
                </div>
            </div>"""
s7_new_flashcard = """            </div>
            
            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">konkurrens</div>
                        <div class="flashcard-back">När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser).</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s7_old_flashcard, s7_new_flashcard)

# 7. Slide 8 (Ekologisk Nisch)
s8_old_grid = """            <div class="content-grid" style="margin: 3rem 0; grid-template-columns: repeat(3, 1fr); align-items: start;">"""
s8_new_grid = """            <div class="content-grid" style="margin: 3rem 0;">"""
content = content.replace(s8_old_grid, s8_new_grid)

s8_old_flashcard = """                <div class="flashcard-wrapper" style="margin-top: 0; align-self: stretch;">
                    <div class="flashcard" style="width: 100%;" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                        <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                            <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                            </svg>
                        </button>
                        <div class="flashcard-inner">
                            <div class="flashcard-front">ekologisk nisch</div>
                            <div class="flashcard-back">En arts "yrke" eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut.</div>
                        </div>
                    </div>
                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>"""
s8_new_flashcard = """            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>

            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">ekologisk nisch</div>
                        <div class="flashcard-back">En arts "yrke" eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut.</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s8_old_flashcard, s8_new_flashcard)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)
