import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

def get_flashcard(term, definition):
    return f"""                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">{term}</div>
                        <div class="flashcard-back">{definition}</div>
                    </div>
                </div>"""

biomassa = get_flashcard("biomassa", "Den sammanlagda vikten av allt levande i ett ekosystem (t.ex. hur mycket alla växter och djur i en skog väger tillsammans).")
n_pyramid = get_flashcard("näringspyramid", "En modell som visar att energin (och biomassan) minskar för varje steg i näringskedjan. (Eftersom bara ca 10 % av energin går vidare blir pyramiden smalare i toppen, vilket betyder att det finns färre toppkonsumenter).")
bioack = get_flashcard("bioackumulation", "När miljögifter lagras i kroppen eftersom de inte kan brytas ner. Koncentrationen (halten) ökar därför ju högre upp i näringskedjan man kommer.")

symbios = get_flashcard("symbios", "Ett samlingsnamn för när olika arter lever i ett tätt och långvarigt samspel med varandra.")
mutualism = get_flashcard("mutualism", "En typ av symbios där alla inblandade arter vinner på samarbetet (t.ex. mykorrhiza mellan träd och svamp).")
kommensalism = get_flashcard("kommensalism", "En typ av symbios där den ena arten vinner på det, medan den andra är helt opåverkad (t.ex. havstulpaner som får åka med på en val).")
parasitism = get_flashcard("parasitism", "En typ av symbios där den ena arten vinner, medan den andra utnyttjas och tar skada (t.ex. fästing och hund).")

konkurrens = get_flashcard("konkurrens", "När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser).")
ekologisk_nisch = get_flashcard("ekologisk nisch", "En arts \"yrke\" eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut.")

# Create the new slide 1
new_slide_1 = f"""<!-- Slide 1: Repetition -->
        <div class="slide active" data-slide="1">
            <h1>1. Repetition</h1>
            <p class="subtitle">Nyckelbegrepp från i tisdags</p>
            
            <div class="glossary-grid" style="margin-top: 4rem;">
{biomassa}
{n_pyramid}
{bioack}
            </div>
        </div>

        """

parts = content.split('<!-- Slide ')
header = parts[0]
slides = parts[1:]

def inject_fc(slide_str, fc_html):
    return slide_str.rsplit('</div>', 1)[0] + f'\n            <div class="glossary-grid" style="margin-top: 3rem;">\n{fc_html}\n            </div>\n        </div>'

slides[1] = inject_fc(slides[1], symbios)
slides[2] = inject_fc(slides[2], mutualism)
slides[3] = inject_fc(slides[3], kommensalism)
slides[4] = inject_fc(slides[4], parasitism)
slides[5] = inject_fc(slides[5], konkurrens)
slides[6] = inject_fc(slides[6], ekologisk_nisch)

# Renumber and rebuild
new_slides = [new_slide_1] + ["<!-- Slide " + s for s in slides]

for i in range(1, len(new_slides)):
    new_slides[i] = re.sub(r'Slide \d+:', f'Slide {i+1}:', new_slides[i], count=1)
    new_slides[i] = re.sub(r'data-slide="\d+"', f'data-slide="{i+1}"', new_slides[i])
    new_slides[i] = new_slides[i].replace('class="slide active"', 'class="slide"')

final_html = header + "".join(new_slides)

# Update total slides in JS
final_html = final_html.replace('const totalSlides = 8;', 'const totalSlides = 9;')
final_html = final_html.replace('1 / 8', '1 / 9')

# Update Overview Modal
old_overview = """<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.5rem;">
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(1)"><strong>1.</strong> Samspel i naturen</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(2)"><strong>2.</strong> Vad är symbios?</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(3)"><strong>3.</strong> Mutualism</button>
                <button class="card pos-neu" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(4)"><strong>4.</strong> Kommensalism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(5)"><strong>5.</strong> Parasitism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(6)"><strong>6.</strong> Konkurrens</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(7)"><strong>7.</strong> Ekologisk nisch</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3); border-top: 4px solid var(--accent-neu);" onclick="goToSlide(8)"><strong>8.</strong> Gloslista V.19</button>
            </div>"""

new_overview = """<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.5rem;">
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3); border-top: 4px solid var(--accent-pos);" onclick="goToSlide(1)"><strong>1.</strong> Repetition (Glosor)</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(2)"><strong>2.</strong> Samspel i naturen</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(3)"><strong>3.</strong> Vad är symbios?</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(4)"><strong>4.</strong> Mutualism</button>
                <button class="card pos-neu" style="padding: 1.5rem; cursor: pointer; text it; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(5)"><strong>5.</strong> Kommensalism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(6)"><strong>6.</strong> Parasitism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(7)"><strong>7.</strong> Konkurrens</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(8)"><strong>8.</strong> Ekologisk nisch</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3); border-top: 4px solid var(--accent-neu);" onclick="goToSlide(9)"><strong>9.</strong> Gloslista V.19 (Alla)</button>
            </div>"""

final_html = final_html.replace(old_overview, new_overview)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(final_html)

