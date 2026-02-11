/**
 * LessonLab — Auth Module
 * Client-side SHA-256 password gate with localStorage persistence.
 */

const LESSON_LAB_AUTH = (() => {
    const HASH = '3cc03f6b0c2f1bcd2231d554ee4307622a50f54f55fb60c340447668f8dbefd6';
    const STORAGE_KEY = 'lessonlab_auth';

    async function sha256(message) {
        const msgBuffer = new TextEncoder().encode(message);
        const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }

    async function verify(password) {
        const hash = await sha256(password);
        return hash === HASH;
    }

    function isAuthenticated() {
        return localStorage.getItem(STORAGE_KEY) === HASH;
    }

    function persist() {
        localStorage.setItem(STORAGE_KEY, HASH);
    }

    function logout() {
        localStorage.removeItem(STORAGE_KEY);
    }

    async function handleLogin(passwordInput, errorEl, onSuccess) {
        const password = passwordInput.value;
        if (!password) return;

        const valid = await verify(password);
        if (valid) {
            persist();
            onSuccess();
        } else {
            errorEl.textContent = 'Fel lösenord. Försök igen.';
            errorEl.classList.add('visible');
            passwordInput.value = '';
            passwordInput.focus();
            passwordInput.classList.add('shake');
            setTimeout(() => passwordInput.classList.remove('shake'), 500);
        }
    }

    return { verify, isAuthenticated, persist, logout, handleLogin };
})();
