---
name: tailwind-fluid-typography-agent
description: Integrate and customize a Tailwind CSS v4 fluid typography system using semantic utilities and @theme variables. Use when building or refactoring UI typography to clamp-based fluid scaling, creating type documentation pages, migrating from breakpoint-based text sizing, or applying consistent heading/body/caption classes across Astro, React, Vue, Next.js, and plain HTML projects.
---

# Apply the fluid typography system

Use this skill to install, configure, and roll out semantic typography classes driven by CSS `clamp()` and Tailwind v4 `@theme` variables.

## Follow this workflow

1. Identify where global CSS is loaded in the target project.
2. Copy `assets/advanced-fluid-typography.css` into the target project (usually `src/styles/`).
3. Ensure `@import "tailwindcss";` appears once in the app global stylesheet.
4. Import the copied typography file after Tailwind in global CSS.
5. Replace legacy text-size patterns with semantic classes (see `references/class-map.md`).
6. Adjust `--fluid-*` variables for the project’s viewport and scale goals.
7. Verify headings/body/captions at 320px, 768px, 1280px, and 1920px.

## Keep changes safe and consistent

- Prefer semantic typography classes (`.text-h1`, `.text-body`, `.text-caption`) over one-off size utilities.
- Keep non-typography styling in native Tailwind utilities.
- Do not duplicate Tailwind imports across multiple CSS files.
- Keep configuration in one authoritative stylesheet.

## Read these references when needed

- Read `references/integration.md` for framework-specific install and migration flow.
- Read `references/class-map.md` for class intent and mapping from common Tailwind size patterns.
