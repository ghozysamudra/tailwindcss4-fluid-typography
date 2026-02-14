# Fluid Typography for Tailwind CSS v4

An Astro.js landing page and documentation site for a fluid typography system built on Tailwind CSS v4 and CSS `clamp()`.

## Features

- Editorial-style responsive landing page
- Fluid typography system (`@theme` variables + semantic classes)
- Interactive type scale demo with viewport simulation
- Configuration Generator with:
  - presets (`Balanced`, `Editorial`, `Dramatic`)
  - slider + number inputs
  - reset action
  - generated CSS output
  - generated font-size variable table preview
- Light/dark theme toggle
- Fully responsive layout and mobile-safe code blocks

## Tech Stack

- Astro 5
- Tailwind CSS v4 via `@tailwindcss/vite`
- Vanilla client-side JavaScript for interactive demos

## Project Structure

```text
.
├── src/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   └── styles/
│       ├── advanced-fluid-typography.css
│       └── global.css
├── public/
├── astro.config.mjs
└── package.json
```

## Getting Started

```bash
npm install
npm run dev
```

Open `http://localhost:4321`.

## Build

```bash
npm run build
npm run preview
```

## Core Typography Variables

The generator and system are built around these values:

```css
@theme {
  --fluid-min-width: 360;
  --fluid-max-width: 1280;
  --fluid-min-base: 16;
  --fluid-max-base: 18;
  --fluid-min-ratio: 1.2;
  --fluid-max-ratio: 1.25;
}
```

## Notes

- Main typography source: `src/styles/advanced-fluid-typography.css`
- Public downloadable CSS files are available in `public/`

## License

MIT
