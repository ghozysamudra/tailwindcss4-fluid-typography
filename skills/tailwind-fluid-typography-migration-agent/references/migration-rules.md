# Migration Rules

## Primary mapping heuristics

- `text-5xl`, `text-6xl`, `text-7xl` chains -> `.text-display` or `.text-display-xl`
- `text-3xl`, `text-4xl` chains -> `.text-h1` or `.text-h2`
- `text-2xl` chains -> `.text-h2` or `.text-h3`
- `text-xl`, `text-lg` chains -> `.text-h3` or `.text-body-lg`
- `text-base` chains -> `.text-body`
- `text-sm` chains -> `.text-body-sm`
- `text-xs` + uppercase/tracking -> `.text-overline` or `.text-caption`

## Resolve ambiguity

When multiple mappings are plausible:

1. Use tag semantics (`h1`-`h6`, `p`, `span`) as first hint.
2. Use nearby context (hero, section title, card title, metadata).
3. Prefer conservative replacement (`.text-h2` over `.text-display-xl`) unless clearly hero/display.

## Keep these classes intact

Do not alter non-typography classes such as spacing, layout, colors, borders, shadows, animations, and state variants.

## Examples

- `<h1 class="text-4xl md:text-5xl lg:text-6xl">` -> `<h1 class="text-h1">`
- `<h2 class="text-2xl md:text-3xl">` -> `<h2 class="text-h2">`
- `<p class="text-base md:text-lg">` -> `<p class="text-body">`
- `<span class="text-xs uppercase tracking-wide">` -> `<span class="text-overline">`

## QA checks

- Ensure at most one semantic fluid typography class per element unless intentionally combined.
- Confirm no leftover responsive text-size chains in migrated files.
- Verify heading hierarchy remains readable at 320px and 1280px.
