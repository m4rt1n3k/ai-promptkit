# kit_design

Run when the user says **`from workspace ai-promptkit run kit_design`** (or `kit_design`).

## Load

Read this file from **ai-promptkit**. Write to the **user’s project workspace**, not ai-promptkit.

## Task

Create or update **`.cursor/rules/kit-design.mdc`** at the target repo root with `alwaysApply: true` and this behavior:

```markdown
---
description: Minimal, optimal solutions—no deep exploration unless asked
alwaysApply: true
---

# Design discipline

- Solve the **stated problem** with the **smallest correct change**.
- Prefer one clear approach over comparing many alternatives.
- Do **not** go deep into possibilities, option trees, or speculative refactors unless the user asks.
- Skip nice-to-haves and “while we’re here” work unless requested.
- If something is out of scope for now, note it briefly; do not implement it.
- Do **not** repeat the same fact in two places (e.g. a table row plus a heading or caption that restates interval, author, or title). Say it once in the most structured spot.
```

Merge with existing rule if present; do not remove project-specific lines.

Template: [templates/kit-design.rule.mdc](./templates/kit-design.rule.mdc).

## Do not

- Update `PROMPT.md`, `TODO.md`, or `MANUAL.md` (use other kits).
- Invent backlog items on the target repo.

## Reply

Confirm target path and that `kit-design.mdc` was written or updated.
