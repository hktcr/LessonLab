# KODDOKUMENTATION: LessonLab

**Senast uppdaterad:** 2026-03-16  
**Teknikstack:** Vanilla HTML/CSS/JS + SHA-256 lösenordsskydd (klient-side)  
**Publicering:** GitHub Pages → `hktcr.github.io/LessonLab`  
**Repo:** `hktcr/LessonLab`

---

## Syfte och vision

Lösenordsskyddad samling av genomgångsmanus för NO-klassrummet. Varje manus är en fristående HTML-sida med collapsible sektioner, scroll progress bar och print-optimering. Mörkt tema med glassmorphism — designat för projektor.

---

## Arkitektur

```
LessonLab/
├── index.html              ← Landing page med lösenordsskydd + manusöversikt
├── style.css               ← Dark theme (20KB, glassmorphism)
├── auth.js                 ← SHA-256 lösenordskontroll med localStorage persistence
├── script.js               ← Collapsible sections, scroll progress, navigation
├── biologins-grunder/
│   └── cellritning.html    ← Genomgångsmanus: Cellritning
└── README.md
```

### Lösenordshantering (`auth.js`)

SHA-256 hash-verifiering utan server:

```javascript
// SHA-256 hash jämförs med förberäknat hash
async function verifyPassword(input) {
    const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
    const hex = Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
    return hex === EXPECTED_HASH;
}
```

Lösenord sparas i `localStorage` för att undvika omautentisering.

### Design

- **Font:** Inter via Google Fonts
- **Tema:** Mörkt med glassmorphism (`backdrop-filter: blur`)
- **Responsivt:** Mobil/surfplatta/desktop
- **Print-vänligt:** `Ctrl+P` med dedikerad print-CSS
- **Scroll progress bar** i toppen av manussidor

---

## Ändringslogg

### 2026-03-16 — Initial koddokumentation

Skapad som del av GAIA-bred koddokumentationsinsats.

---

*Signatur: gAIa 🌲*
