# Install design discipline rule

Use once per target repo to set agent behavior (replaces legacy `kit_design`).

Copy everything below the line into a new agent chat.

---

## Task: Install design discipline Cursor rule

You are in the **target repository** (cwd = repo root).

**Goal:** Create or update `.cursor/rules/design-discipline.mdc` with `alwaysApply: true`.

### Content

Use the template from ai-promptkit [`templates/design.rule.mdc`](../templates/design.rule.mdc) (or copy verbatim if submodule path unavailable).

### Rules

- Merge with existing rule if present; do not remove project-specific lines.
- Do not update `docs/`, `TODO.md`, or prompt files.
- Do not invent backlog items.

### Reply

Confirm target path and that `design-discipline.mdc` was written or updated.
