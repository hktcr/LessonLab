import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Add CSS for hover effects
css_to_add = """
        .card, .highlight-box, .warning-box {
            cursor: pointer;
            transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s;
        }
        .card:hover, .highlight-box:hover, .warning-box:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        }
"""
content = content.replace("</style>", css_to_add + "</style>")

# 2. Add openGenericModal JS
js_to_add = """        function openGenericModal(event, title, html) {
            event.stopPropagation();
            modalZoom = 1.0;
            document.getElementById('modalWord').style.fontSize = '4rem';
            document.getElementById('modalExplanation').style.fontSize = '2.2rem';
            document.getElementById('modalWord').innerHTML = title;
            document.getElementById('modalExplanation').innerHTML = html;
            document.getElementById('flashcardModal').classList.add('active');
        }
"""
content = content.replace("function openDirectModal", js_to_add + "\n        function openDirectModal")


# 3. Modify Slide 3 highlight-box
s3_box_old = """            <div class="highlight-box">
                En biologisk term för samlevnad mellan olika arter.
                Konsekvenserna av detta samspel avgör vilken typ av symbios det handlar om.
            </div>"""
s3_box_new = """            <div class="highlight-box" onclick="openGenericModal(event, 'Vad är symbios?', 'En biologisk term för samlevnad mellan olika arter.<br><br>Konsekvenserna av detta samspel avgör vilken typ av symbios det handlar om.')">
                En biologisk term för samlevnad mellan olika arter.
                Konsekvenserna av detta samspel avgör vilken typ av symbios det handlar om.
            </div>"""
content = content.replace(s3_box_old, s3_box_new)


# 4. Modify Slide 7 warning-box
s7_warn_old = """            <div class="warning-box">
                Detta leder till en biologisk konflikt.
                Den direkta konkurrensen kostar livsviktig energi för båda parter.
            </div>"""
s7_warn_new = """            <div class="warning-box" onclick="openGenericModal(event, 'Biologisk konflikt', 'Detta leder till en biologisk konflikt.<br><br>Den direkta konkurrensen kostar livsviktig energi för båda parter.')">
                Detta leder till en biologisk konflikt.
                Den direkta konkurrensen kostar livsviktig energi för båda parter.
            </div>"""
content = content.replace(s7_warn_old, s7_warn_new)


# 5. Modify Slide 7 cards
s7_card1_old = """                <div class="card pos-neg">
                    <h3>Utgång 1: Konkurrensuteslutning</h3>
                    <ul>
                        <li>Den ena arten utkonkurrerar den andra</li>
                        <li>Den svagare arten försvinner lokalt</li>
                    </ul>
                </div>"""
s7_card1_new = """                <div class="card pos-neg" onclick="openGenericModal(event, this.querySelector('h3').innerHTML, this.querySelector('ul').outerHTML)">
                    <h3>Utgång 1: Konkurrensuteslutning</h3>
                    <ul>
                        <li>Den ena arten utkonkurrerar den andra</li>
                        <li>Den svagare arten försvinner lokalt</li>
                    </ul>
                </div>"""
content = content.replace(s7_card1_old, s7_card1_new)

s7_card2_old = """                <div class="card pos-pos">
                    <h3>Utgång 2: Nischuppdelning</h3>
                    <ul>
                        <li>Arterna anpassar sig för att undvika varandra</li>
                        <li>Den direkta konkurrensen minskar</li>
                    </ul>
                </div>"""
s7_card2_new = """                <div class="card pos-pos" onclick="openGenericModal(event, this.querySelector('h3').innerHTML, this.querySelector('ul').outerHTML)">
                    <h3>Utgång 2: Nischuppdelning</h3>
                    <ul>
                        <li>Arterna anpassar sig för att undvika varandra</li>
                        <li>Den direkta konkurrensen minskar</li>
                    </ul>
                </div>"""
content = content.replace(s7_card2_old, s7_card2_new)


# 6. Modify Slide 8 cards
s8_card1_old = """                <div class="card pos-pos">
                    <h3>Talgoxen</h3>
                    <ul>
                        <li>Större och tyngre kropp</li>
                        <li>Födosöker på tjockare grenar, ofta lägre ner i trädkronan</li>
                    </ul>
                </div>"""
s8_card1_new = """                <div class="card pos-pos" onclick="openGenericModal(event, this.querySelector('h3').innerHTML, this.querySelector('ul').outerHTML)">
                    <h3>Talgoxen</h3>
                    <ul>
                        <li>Större och tyngre kropp</li>
                        <li>Födosöker på tjockare grenar, ofta lägre ner i trädkronan</li>
                    </ul>
                </div>"""
content = content.replace(s8_card1_old, s8_card1_new)

s8_card2_old = """                <div class="card pos-neu">
                    <h3>Blåmesen</h3>
                    <ul>
                        <li>Mindre och lättare kropp</li>
                        <li>Födosöker längst ut på tunna kvistar i trädkronan</li>
                    </ul>
                </div>"""
s8_card2_new = """                <div class="card pos-neu" onclick="openGenericModal(event, this.querySelector('h3').innerHTML, this.querySelector('ul').outerHTML)">
                    <h3>Blåmesen</h3>
                    <ul>
                        <li>Mindre och lättare kropp</li>
                        <li>Födosöker längst ut på tunna kvistar i trädkronan</li>
                    </ul>
                </div>"""
content = content.replace(s8_card2_old, s8_card2_new)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

