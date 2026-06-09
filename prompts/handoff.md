# Handoff — end-of-session orchestration

Run at the end of an AI-assisted session, before commit or PR.

**Sub-prompts** (each usable standalone):

| Step | Prompt | Output |
|------|--------|--------|
| 1 | [`session-summary.md`](session-summary.md) | Commit message draft |
| 2 | [`update-devlog.md`](update-devlog.md) | Row in `docs/devlog.md` |
| 3 | [`regenerate-docs.md`](regenerate-docs.md) | README, manual, wiki (if structure changed) |
| 4 | [`suggest-adr.md`](suggest-adr.md) | ADR draft or skip (if architectural) |
| 5 | (inline below) | `TODO.md` active track update |

Copy everything below the line into a new agent chat with `git status` and session context.

---

## Task: Session handoff

You are in the **target repository** (cwd = repo root).

Execute these steps **in order** in this chat. Apply file edits when the user expects handoff to update docs (default: yes for devlog; ask before large doc rewrites).

### Step 1 — Commit summary

Follow [`session-summary.md`](session-summary.md). Output the commit message draft first.

### Step 2 — Devlog

Follow [`update-devlog.md`](update-devlog.md). Prepend one row to `docs/devlog.md` (outcomes-only summary; ADRs in Refs; no content below the table).

### Step 3 — Regenerate docs (conditional)

If this session changed repo layout, workflows, CLI, or prompt registry, follow [`regenerate-docs.md`](regenerate-docs.md). Otherwise state "Step 3 skipped — no structural doc changes."

### Step 4 — ADR (conditional)

If the session made an irreversible design choice, follow [`suggest-adr.md`](suggest-adr.md). Otherwise state "Step 4 skipped — no new ADR."

### Step 5 — TODO.md

Review `TODO.md`:

- Close completed items in active track / pipeline (status → `done`).
- Add new `must-have` / `next` items **only if the session surfaced follow-up work the user stated**.
- Do not invent tasks unrelated to the session.

### Constraints

- Read `git status` and diff; **do not invent** changes.
- **Do not commit** unless the user explicitly asks.
- **Do not** rewrite devlog history — append only.
- Point future doc work to `docs/conventions.md` and `prompts/README.md`.

### Reference paths

| Doc | Path |
|-----|------|
| User manual | `docs/manual.md` |
| Conventions | `docs/conventions.md` |
| Devlog | `docs/devlog.md` |
| ADR index | `docs/adr/README.md` |
| Prompt registry | `prompts/README.md` |
