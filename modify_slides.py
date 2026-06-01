import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# Add CSS
css_to_add = """
        .expand-btn {
            position: absolute;
            top: 10px; right: 10px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255,255,255,0.2);
            color: var(--text);
            width: 36px; height: 36px;
            border-radius: 0.5rem;
            cursor: pointer;
            z-index: 10;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .expand-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.1);
        }

        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            z-index: 1000;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 4rem;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .modal.active {
            display: flex;
            opacity: 1;
        }
        .modal-content {
            max-width: 1000px;
            animation: modalPop 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        @keyframes modalPop {
            from { transform: scale(0.9); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .modal-close {
            position: absolute;
            top: 2rem; right: 3rem;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 3rem;
            cursor: pointer;
            transition: color 0.3s;
        }
        .modal-close:hover { color: var(--accent-neg); }
"""

content = content.replace('        /* Mobile */', css_to_add + '\n        /* Mobile */')

# Add Modal HTML
modal_html = """
    <div id="flashcardModal" class="modal" onclick="if(event.target === this) closeModal()">
        <button class="modal-close" onclick="closeModal()">✕</button>
        <div class="modal-content">
            <h2 id="modalWord" style="color: var(--accent-neu); font-size: clamp(3rem, 6vw, 5rem); margin-bottom: 2rem; text-transform: capitalize;"></h2>
            <p id="modalExplanation" style="font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.6; color: var(--text);"></p>
        </div>
    </div>

    <script>"""

content = content.replace('    <script>', modal_html)

# Add JS functions
js_to_add = """
        function openModal(event, btn) {
            event.stopPropagation();
            const cardInner = btn.nextElementSibling;
            const word = cardInner.querySelector('.flashcard-front').textContent;
            const explanation = cardInner.querySelector('.flashcard-back').textContent;
            
            document.getElementById('modalWord').textContent = word;
            document.getElementById('modalExplanation').textContent = explanation;
            document.getElementById('flashcardModal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('flashcardModal').classList.remove('active');
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
"""

content = content.replace('        // Fullscreen functionality', js_to_add + '\n        // Fullscreen functionality')

# Modify Flashcards
svg_btn = """
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>"""

content = re.sub(r'(<div class="flashcard" onclick="this\.classList\.toggle\(\'flipped\'\)">)', r'\1' + svg_btn, content)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

