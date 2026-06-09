# Handoff — end of session

Base steps 1–5. Consumers use `prompts/handoff.md` (extends this) after [init.md](init.md).

| Step | Prompt | Output |
|------|--------|--------|
| 1 | [session-summary.md](session-summary.md) | Commit draft |
| 2 | [update-devlog.md](update-devlog.md) | Devlog row |
| 3 | [regenerate-docs.md](regenerate-docs.md) | Docs if structure changed |
| 4 | [suggest-adr.md](suggest-adr.md) | ADR if needed |
| 5 | (below) | TODO.md |

---

## Task: Session handoff

Target repository (cwd = repo root). Execute in order.

### Step 1 — Commit summary

Follow [session-summary.md](session-summary.md).

### Step 2 — Devlog

Follow [update-devlog.md](update-devlog.md). Prepend one row to `docs/devlog.md`.

### Step 3 — Regenerate docs

If layout, workflows, CLI, or prompts changed: [regenerate-docs.md](regenerate-docs.md). Else skip.

### Step 4 — ADR

If irreversible design choice: [suggest-adr.md](suggest-adr.md). Else skip.

### Step 5 — TODO

Update `TODO.md`: close done items; add tasks **only if user stated them**. Do not invent backlog.

### Constraints

Read `git status`. Do not invent changes. Do not commit unless asked. Devlog is append-only.
