import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Add CSS for glossary-link
css_to_add = """
        .glossary-link {
            cursor: pointer;
            text-decoration: underline;
            text-decoration-style: dotted;
            text-underline-offset: 6px;
            transition: opacity 0.2s;
        }
        .glossary-link:hover {
            opacity: 0.8;
        }
"""
content = content.replace("</style>", css_to_add + "</style>")

# 2. Add openDirectModal JS
js_to_add = """        function openDirectModal(event, element) {
            event.stopPropagation();
            modalZoom = 1.0;
            document.getElementById('modalWord').style.fontSize = '4rem';
            document.getElementById('modalExplanation').style.fontSize = '2.2rem';
            document.getElementById('modalWord').textContent = element.getAttribute('data-word');
            document.getElementById('modalExplanation').textContent = element.getAttribute('data-explanation');
            document.getElementById('flashcardModal').classList.add('active');
        }
"""
content = content.replace("function openModal(event, btn) {", js_to_add + "\n        function openModal(event, btn) {")

# 3. Slide 3
content = content.replace('<h2>Vad är <span style="color: var(--accent-neu);">symbios</span>?</h2>', 
                          '<h2>Vad är <span class="glossary-link" style="color: var(--accent-neu);" data-word="symbios" data-explanation="Ett samlingsnamn för när olika arter lever i ett tätt och långvarigt samspel med varandra." onclick="openDirectModal(event, this)">symbios</span>?</h2>')

s3_flashcard = """            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">symbios</div>
                        <div class="flashcard-back">Ett samlingsnamn för när olika arter lever i ett tätt och långvarigt samspel med varandra.</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s3_flashcard, "")

# 4. Slide 4
content = content.replace('<h2 style="color: var(--accent-pos);">1. Mutualism <span style="font-weight: 300; opacity: 0.8;">(+/+)</span></h2>', 
                          '<h2 style="color: var(--accent-pos);">1. <span class="glossary-link" data-word="mutualism" data-explanation="En typ av symbios där alla inblandade arter vinner på samarbetet (t.ex. mykorrhiza mellan träd och svamp)." onclick="openDirectModal(event, this)">Mutualism</span> <span style="font-weight: 300; opacity: 0.8;">(+/+)</span></h2>')

s4_flashcard = """            <div class="corner-flashcard">
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
content = content.replace(s4_flashcard, "")

# 5. Slide 5
content = content.replace('<h2 style="color: var(--accent-neu);">2. Kommensalism <span style="font-weight: 300; opacity: 0.8;">(+/0)</span></h2>', 
                          '<h2 style="color: var(--accent-neu);">2. <span class="glossary-link" data-word="kommensalism" data-explanation="En typ av symbios där den ena arten vinner på det, medan den andra är helt opåverkad (t.ex. havstulpaner som får åka med på en val)." onclick="openDirectModal(event, this)">Kommensalism</span> <span style="font-weight: 300; opacity: 0.8;">(+/0)</span></h2>')

s5_flashcard = """            <div class="corner-flashcard">
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
content = content.replace(s5_flashcard, "")

# 6. Slide 6
content = content.replace('<h2 style="color: var(--accent-neg);">3. Parasitism <span style="font-weight: 300; opacity: 0.8;">(+/-)</span></h2>', 
                          '<h2 style="color: var(--accent-neg);">3. <span class="glossary-link" data-word="parasitism" data-explanation="En typ av symbios där den ena arten vinner, medan den andra utnyttjas och tar skada (t.ex. fästing och hund)." onclick="openDirectModal(event, this)">Parasitism</span> <span style="font-weight: 300; opacity: 0.8;">(+/-)</span></h2>')

s6_flashcard = """            <div class="corner-flashcard">
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
content = content.replace(s6_flashcard, "")

# 7. Slide 7
content = content.replace('<h2 style="color: var(--accent-neg);">Konkurrens <span style="font-weight: 300; opacity: 0.8;">(-/-)</span></h2>', 
                          '<h2 style="color: var(--accent-neg);"><span class="glossary-link" data-word="konkurrens" data-explanation="När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser)." onclick="openDirectModal(event, this)">Konkurrens</span> <span style="font-weight: 300; opacity: 0.8;">(-/-)</span></h2>')

s7_flashcard = """            <div class="corner-flashcard">
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
content = content.replace(s7_flashcard, "")

# 8. Slide 8
content = content.replace('<h2 style="color: var(--accent-pos);">Ekologisk nisch</h2>', 
                          '<h2 style="color: var(--accent-pos);"><span class="glossary-link" data-word="ekologisk nisch" data-explanation="En arts \'yrke\' eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut." onclick="openDirectModal(event, this)">Ekologisk nisch</span></h2>')

s8_flashcard = """            <div class="corner-flashcard">
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
# Double quotes issue in explanation string for slide 8: handled in python by using data-explanation with single quotes. 
content = content.replace(s8_flashcard, "")


with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

