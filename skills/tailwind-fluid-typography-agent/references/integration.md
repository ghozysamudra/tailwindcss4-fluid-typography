# Integration Guide

## Astro / Vite / Tailwind v4

1. Put `advanced-fluid-typography.css` in `src/styles/`.
2. In global CSS:

```css
@import "tailwindcss";
@import "./advanced-fluid-typography.css";
```

3. Ensure global CSS is imported in the root layout/page entry.

## Next.js / React / Vue

1. Put `advanced-fluid-typography.css` in your styles folder.
2. In the single app-global stylesheet loaded once by the app shell:

```css
@import "tailwindcss";
@import "./advanced-fluid-typography.css";
```

3. Remove duplicate Tailwind imports from other CSS files.

## Suggested initial tuning

Start from:

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

Then adjust based on product tone:

- Dense UI: lower ratios (`1.15`-`1.22`)
- Balanced docs/marketing: `1.2`-`1.333`
- Hero-heavy branding: `1.333`-`1.5`

## Validation checklist

- No heading jumps at breakpoints.
- Body text remains readable on 320px mobile.
- Largest display size does not overpower desktop layouts.
- Old `text-3xl md:text-5xl` chains are replaced with semantic classes.
