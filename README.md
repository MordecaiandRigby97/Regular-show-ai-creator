# Regular Show Voice Actor Explorer

A small Vite + React single-page application that highlights the voice actors from *Regular Show*. Browse cast biographies, follow source links, and play sample audio clips (placeholders included) for each performer.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (version 18 or newer recommended)
- npm (ships with Node.js)

### Installation

```bash
npm install
```

### Running the Development Server

```bash
npm run dev
```

This starts Vite on <http://localhost:5173>. The SPA automatically reloads when you edit files in `src/`.

### Building for Production

```bash
npm run build
```

A production build is created in `dist/`.

### Running Tests

```bash
npm test
```

Vitest runs the React Testing Library suite, covering data loading and audio accessibility behaviors for the voice actor list.

## Project Structure

```
├── public/
│   ├── audio/
│   │   ├── jg-quintel.mp3
│   │   ├── mark-hamill.mp3
│   │   ├── sam-marin.mp3
│   │   └── william-salyers.mp3
│   └── index.html
├── src/
│   ├── App.tsx
│   ├── components/
│   │   ├── VoiceActorCard.tsx
│   │   └── VoiceActorList.tsx
│   ├── data/
│   │   └── voiceActors.json
│   ├── index.tsx
│   ├── styles.css
│   ├── setupTests.ts
│   └── __tests__/
│       └── VoiceActorList.test.tsx
├── package.json
├── tsconfig.json
└── vite.config.ts
```

Audio files are placeholders—replace them with authentic clips if available and ensure you have the right to use them.
