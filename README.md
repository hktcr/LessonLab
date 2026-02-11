# LessonLab 🧪

Lösenordsskyddad samling av genomgångsmanus för klassrummet.

## Struktur

```
LessonLab/
├── index.html              ← Entry-sida (lösenordsskydd + manusöversikt)
├── style.css               ← Gemensam dark theme
├── auth.js                 ← SHA-256 lösenordskontroll
├── biologins-grunder/
│   └── cellritning.html    ← Genomgångsmanus: Cellritning
└── README.md
```

## Lösenord

Appen är lösenordsskyddad med SHA-256 client-side hash.
Lösenordet sparas i `localStorage` efter inloggning.

## Lägga till nytt manus

1. Skapa en ny mapp under arbetsområdet (t.ex. `kemi/`)
2. Skapa en HTML-fil med samma struktur som `cellritning.html`
3. Lägg till en länk i `index.html` under rätt arbetsområdeskort

## Design

- Dark theme med glassmorphism
- Google Font: Inter
- Responsiv (mobil/surfplatta/desktop)
- Print-vänlig (`Ctrl+P`)
- Collapsible sections
- Scroll progress bar

---

*Del av GAIA Klassrumsverktyg · gAIa 🌲*
