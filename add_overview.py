import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Rename fullscreen-btn to action-btn
content = content.replace('.fullscreen-btn {', '.action-btn {\n            position: relative;')
content = content.replace('.fullscreen-btn:hover', '.action-btn:hover')

# Remove the fixed positioning from action-btn since we'll wrap them in a container
content = content.replace('            position: fixed;\n            bottom: 2rem;\n            right: 2.5rem;', '')

# 2. Update the buttons in the HTML
old_buttons = """        <button class="fullscreen-btn" onclick="toggleFullScreen()" title="Helskärm">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>
            </svg>
        </button>"""

new_buttons = """        <div style="position: fixed; bottom: 2rem; right: 2.5rem; display: flex; gap: 1rem; z-index: 100;">
            <button class="action-btn" onclick="openOverviewModal()" title="Översikt (Alla slides)">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="7" height="7"></rect>
                    <rect x="14" y="3" width="7" height="7"></rect>
                    <rect x="14" y="14" width="7" height="7"></rect>
                    <rect x="3" y="14" width="7" height="7"></rect>
                </svg>
            </button>
            <button class="action-btn" onclick="toggleFullScreen()" title="Helskärm">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>
                </svg>
            </button>
        </div>"""

content = content.replace(old_buttons, new_buttons)

# 3. Add Overview Modal HTML
overview_modal = """
    <div id="overviewModal" class="modal" onclick="if(event.target === this) closeOverviewModal()">
        <button class="modal-close" onclick="closeOverviewModal()">✕</button>
        <div class="modal-content" style="max-width: 900px; padding: 3rem; background: var(--card-bg); border-radius: 1.2rem; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(20px);">
            <h2 style="color: var(--text); margin-bottom: 2rem; text-align: left;">Slidesöversikt</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.5rem;">
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(1)"><strong>1.</strong> Samspel i naturen</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(2)"><strong>2.</strong> Vad är symbios?</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(3)"><strong>3.</strong> Mutualism</button>
                <button class="card pos-neu" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(4)"><strong>4.</strong> Kommensalism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(5)"><strong>5.</strong> Parasitism</button>
                <button class="card pos-neg" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(6)"><strong>6.</strong> Konkurrens</button>
                <button class="card pos-pos" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3);" onclick="goToSlide(7)"><strong>7.</strong> Ekologisk nisch</button>
                <button class="card" style="padding: 1.5rem; cursor: pointer; text-align: left; font-family: inherit; color: var(--text); background: rgba(0,0,0,0.3); border-top: 4px solid var(--accent-neu);" onclick="goToSlide(8)"><strong>8.</strong> Gloslista V.19</button>
            </div>
        </div>
    </div>
"""

content = content.replace('    <div id="imageModal" class="modal"', overview_modal + '\n    <div id="imageModal" class="modal"')

# 4. Add Overview JS functions
overview_js = """
        function openOverviewModal() {
            document.getElementById('overviewModal').classList.add('active');
        }

        function closeOverviewModal() {
            document.getElementById('overviewModal').classList.remove('active');
        }

        function goToSlide(n) {
            closeOverviewModal();
            showSlide(n);
        }
"""

content = content.replace('        function closeImageModal() {', overview_js + '\n        function closeImageModal() {')
content = content.replace('                closeImageModal();\n            }\n        });', '                closeImageModal();\n                closeOverviewModal();\n            }\n        });')

# Make sure toggleErrorBtn is an action-btn, not fullscreen-btn
content = content.replace('class="fullscreen-btn" style="position: relative', 'class="action-btn" style="position: relative')
content = content.replace(".closest('.fullscreen-btn'))", ".closest('.action-btn'))")

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

