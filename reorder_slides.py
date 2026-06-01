import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. We need to extract the flashcard HTML blocks from the final slide so we can reuse them.
# The flashcards are inside <div class="flashcard"...> ... </div>
# We can use regex to find them, but it's simpler to just define them.

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
new_slide_1 = f"""
        <!-- Slide 1: Repetition -->
        <div class="slide active" data-slide="1">
            <div class="slide-header">
                <h2>1. Repetition</h2>
                <div class="subtitle">Begrepp från i tisdags</div>
            </div>
            
            <div class="glossary-grid" style="margin-top: 4rem;">
{biomassa}
{n_pyramid}
{bioack}
            </div>
        </div>
"""

# We need to split the content by slides and reconstruct it.
# Find all slides
slides_regex = r'(<!-- Slide \d+: .*? -->\s*<div class="slide.*?</div>\n        </div>)'
slides = re.findall(slides_regex, content, flags=re.DOTALL)

# Let's insert the flashcards into the appropriate slides.
# Currently:
# slides[0] = Samspel i naturen
# slides[1] = Vad är symbios?
# slides[2] = Mutualism
# slides[3] = Kommensalism
# slides[4] = Parasitism
# slides[5] = Konkurrens
# slides[6] = Ekologisk nisch
# slides[7] = Gloslista V.19

def inject_flashcard(slide_html, card_html):
    # Find the closing tag of the main content wrapper (e.g. before the last </div></div>)
    # The slides usually end with </div> \n </div>
    return slide_html.rsplit('</div>\n        </div>', 1)[0] + f'\n            <div class="glossary-grid" style="margin-top: 3rem;">\n{card_html}\n            </div>\n        </div>\n        </div>'

# Inject!
s2 = inject_flashcard(slides[1], symbios)
s3 = inject_flashcard(slides[2], mutualism)
s4 = inject_flashcard(slides[3], kommensalism)
s5 = inject_flashcard(slides[4], parasitism)
s6 = inject_flashcard(slides[5], konkurrens)
s7 = inject_flashcard(slides[6], ekologisk_nisch)

# Create the new array of slides
new_slides = [
    new_slide_1,
    slides[0],
    s2,
    s3,
    s4,
    s5,
    s6,
    s7,
    slides[7]
]

# Update data-slide attributes
for i in range(len(new_slides)):
    new_slides[i] = re.sub(r'data-slide="\d+"', f'data-slide="{i+1}"', new_slides[i])
    new_slides[i] = re.sub(r'<!-- Slide \d+:', f'<!-- Slide {i+1}:', new_slides[i])
    # Also remove "active" class from all except the first one
    if i == 0:
        new_slides[i] = new_slides[i].replace('class="slide"', 'class="slide active"')
    else:
        new_slides[i] = new_slides[i].replace('class="slide active"', 'class="slide"')

# Reconstruct HTML
# Replace the old slides block with the new slides
slides_block = "".join(slides)
new_slides_block = "".join(new_slides)
content = content.replace(slides_block, new_slides_block)

# Update totalSlides JS
content = content.replace('const totalSlides = 8;', 'const totalSlides = 9;')
content = content.replace('1 / 8', '1 / 9')

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
                <button class="card pos-neu" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(5)"><strong>5.</strong> Kommensalism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(6)"><strong>6.</strong> Parasitism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(7)"><strong>7.</strong> Konkurrens</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(8)"><strong>8.</strong> Ekologisk nisch</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3); border-top: 4px solid var(--accent-neu);" onclick="goToSlide(9)"><strong>9.</strong> Gloslista V.19 (Alla)</button>
            </div>"""

content = content.replace(old_overview, new_overview)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

