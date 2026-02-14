---
name: tailwind-fluid-typography-migration-agent
description: Audit and migrate legacy Tailwind text size chains (for example text-3xl md:text-5xl) to semantic fluid typography classes (.text-h1, .text-body, .text-caption) with safe patch plans. Use when refactoring existing codebases to clamp-based typography, creating migration reports, or generating batch replacement proposals with minimal visual regressions.
---

# Migrate legacy typography safely

Use this skill to convert breakpoint-based text sizing into semantic fluid typography classes.

## Execute this workflow

1. Run `scripts/audit_typography_usage.py` to discover legacy text-size patterns.
2. Group findings by intent (display, heading, body, label).
3. Propose semantic replacements using `references/migration-rules.md`.
4. Apply edits in small batches by section/component.
5. Re-run the audit script and verify migrated files no longer contain legacy chains.
6. Validate visual hierarchy at mobile and desktop widths.

## Keep migrations low-risk

- Keep semantic HTML meaning unchanged unless explicitly requested.
- Prefer one semantic class replacement over mixed utility size stacks.
- Leave non-typography utilities untouched.
- Flag uncertain mappings instead of guessing.

## Use bundled resources

- Run `scripts/audit_typography_usage.py` for deterministic detection.
- Read `references/migration-rules.md` for mapping heuristics and exception handling.
