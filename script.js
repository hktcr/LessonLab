/**
 * LessonLab — Shared Script
 * Handles auth, outline view, and progress tracking.
 */

/* ── DOM Elements & State ── */
const DOM = {
    loginScreen: () => document.getElementById('loginScreen'),
    loginInput: () => document.getElementById('passwordInput'),
    loginError: () => document.getElementById('loginError'),
    mainApp: () => document.getElementById('mainApp'),
    progressBar: () => document.getElementById('progressBar'),
    expandToggle: () => document.getElementById('expandToggle'), // Future-proof
};

/* ── Initialization ── */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Auth Gate
    if (LESSON_LAB_AUTH.isAuthenticated()) {
        showApp();
    } else {
        // Bind login events
        const btn = document.getElementById('loginBtn');
        if (btn) btn.onclick = doLogin;

        const input = DOM.loginInput();
        if (input) {
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') doLogin();
            });
            input.focus();
        }
    }

    // Bind logout event
    const logoutBtn = document.querySelector('.logout-btn');
    if (logoutBtn) {
        logoutBtn.onclick = doLogout;
    }
});

/* ── Concepts FAB Logic ── */
const CONCEPTS = (() => {
    let modalOverlay, modalBody;

    function init() {
        // Only run if we are in a lesson page (have lesson-sections)
        if (!document.querySelector('.lesson-section')) return;

        createFAB();
        createModal();
        harvestConcepts();
    }

    function createFAB() {
        const fab = document.createElement('button');
        fab.className = 'fab-btn';
        fab.innerHTML = '<span>🔑</span> Begrepp';
        fab.onclick = openModal;
        document.body.appendChild(fab);
    }

    function createModal() {
        // Overlay
        modalOverlay = document.createElement('div');
        modalOverlay.className = 'modal-overlay';
        modalOverlay.onclick = (e) => {
            if (e.target === modalOverlay) closeModal();
        };

        // Modal
        const modal = document.createElement('div');
        modal.className = 'concepts-modal';

        // Header
        const header = document.createElement('div');
        header.className = 'modal-header';
        header.innerHTML = `
            <div class="modal-title"><span>🔑</span> Nyckelbegrepp</div>
            <button class="modal-close" onclick="CONCEPTS.closeModal()">×</button>
        `;

        // Body
        modalBody = document.createElement('div');
        modalBody.className = 'modal-body';

        modal.appendChild(header);
        modal.appendChild(modalBody);
        modalOverlay.appendChild(modal);
        document.body.appendChild(modalOverlay);
    }

    function harvestConcepts() {
        const vocabItems = document.querySelectorAll('.vocab-item');
        const list = document.createElement('div');
        list.className = 'modal-list';

        if (vocabItems.length === 0) {
            list.innerHTML = '<p style="color:var(--text-muted);text-align:center;">Inga begrepp hittades i denna lektion.</p>';
        } else {
            vocabItems.forEach(item => {
                const term = item.querySelector('.vocab-term')?.textContent || '';
                const def = item.querySelector('.vocab-def')?.textContent || '';

                if (term) {
                    const el = document.createElement('div');
                    el.className = 'modal-item';
                    el.innerHTML = `
                        <span class="modal-term">${term}</span>
                        <span class="modal-def">${def}</span>
                    `;
                    list.appendChild(el);
                }
            });
        }

        modalBody.innerHTML = '';
        modalBody.appendChild(list);
    }

    function openModal() {
        modalOverlay.classList.add('open');
    }

    function closeModal() {
        modalOverlay.classList.remove('open');
    }

    return { init, openModal, closeModal };
})();

/* ── Auth Logic ── */
async function doLogin() {
    const input = DOM.loginInput();
    const error = DOM.loginError();
    await LESSON_LAB_AUTH.handleLogin(input, error, showApp);
}

function doLogout() {
    LESSON_LAB_AUTH.logout();
    const app = DOM.mainApp();
    const screen = DOM.loginScreen();
    const input = DOM.loginInput();

    if (app) app.classList.remove('visible');
    if (screen) screen.classList.remove('hidden');
    if (input) {
        input.value = '';
        input.focus();
    }
}

function showApp() {
    const screen = DOM.loginScreen();
    const app = DOM.mainApp();

    if (screen) screen.classList.add('hidden');
    if (app) {
        app.classList.add('visible');
        initLessonView();
    }
}

/* ── Lesson View Logic ── */
function initLessonView() {
    // 1. Initialize Progress Bar
    window.addEventListener('scroll', updateProgress);

    // 2. Initialize Key Concepts FAB
    if (typeof CONCEPTS !== 'undefined') CONCEPTS.init();

    // 3. Initialize Sections (Outline View)
    // In outline view, everything should be collapsed by default unless manually opened
    // Note: We are moving away from having "open" class hardcoded in HTML

    const headers = document.querySelectorAll('.section-header');
    headers.forEach(header => {
        header.onclick = () => {
            const section = header.parentElement;
            toggleSection(section);
        };
    });

    // 3. Add global expand/collapse (if key pressed)
    document.addEventListener('keydown', (e) => {
        if (e.key === 'e' && (e.metaKey || e.ctrlKey)) {
            e.preventDefault();
            expandAll();
        }
    });
}

function updateProgress() {
    const bar = DOM.progressBar();
    if (!bar) return;

    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;

    bar.style.width = pct + '%';
}

function toggleSection(sectionElement) {
    const wasOpen = sectionElement.classList.contains('open');

    if (wasOpen) {
        sectionElement.classList.remove('open');
    } else {
        sectionElement.classList.add('open');
        // Auto-scroll to title if it's way off screen?
        // sectionElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

function expandAll() {
    document.querySelectorAll('.lesson-section').forEach(el => el.classList.add('open'));
}

function collapseAll() {
    document.querySelectorAll('.lesson-section').forEach(el => el.classList.remove('open'));
}
