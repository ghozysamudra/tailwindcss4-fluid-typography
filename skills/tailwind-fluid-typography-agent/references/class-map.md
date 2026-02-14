# Class Map

Use these semantic classes instead of direct size utilities.

## Display

- `.text-display-xl` - largest hero/display moments
- `.text-display-lg` - large display text
- `.text-display` - standard display text

## Headings

- `.text-h1`
- `.text-h2`
- `.text-h3`
- `.text-h4`
- `.text-h5`
- `.text-h6`

## Body and Utility Text

- `.text-body-xl`
- `.text-body-lg`
- `.text-body`
- `.text-body-sm`
- `.text-caption`
- `.text-overline`

## Common migration patterns

- `text-4xl md:text-5xl lg:text-6xl` -> `.text-h1`
- `text-3xl md:text-4xl` -> `.text-h2`
- `text-xl md:text-2xl` -> `.text-h3`
- `text-base md:text-lg` -> `.text-body`
- `text-sm` -> `.text-body-sm`
- `text-xs uppercase tracking-wide` -> `.text-overline`

## Usage note

Apply semantic class to any tag when design intent differs from semantic tag size.

Example: use `<h1 class="text-h2">...</h1>` when a page needs h1 semantics with smaller visual hierarchy.
