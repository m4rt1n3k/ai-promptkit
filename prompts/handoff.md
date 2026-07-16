# Handoff — end of session

Base steps 1–5 (+ step 3b for Python `pyproject.toml`). Consumers use `prompts/handoff.md` (extends this) after [init.md](init.md). Daily: `Run prompts/handoff.md` (`run /prompts/handoff`).

| Step | Prompt | Output |
|------|--------|--------|
| 1 | [session-summary.md](session-summary.md) | Commit subject + body (`topic - detail`) |
| 2 | [update-devlog.md](update-devlog.md) | Devlog row |
| 3 | [regenerate-docs.md](regenerate-docs.md) | Docs if structure changed |
| 3b | [sync-pyproject.md](sync-pyproject.md) | `pyproject.toml` if Python project changed |
| 4 | [suggest-adr.md](suggest-adr.md) | ADR if needed |
| 5 | (below) | TODO.md |

Handoff **closes the current work chat** — devlog, TODO, and commit draft persist repo state so a **new chat** can run [takeover.md](takeover.md) cold-start on the same repo or a different area.

---

## Task: Session handoff

Target repository (cwd = repo root). Execute in order.

### Step 1 — Commit summary

Follow [session-summary.md](session-summary.md).

### Step 2 — Devlog

Follow [update-devlog.md](update-devlog.md). Prepend one row to `docs/devlog.md`.

### Step 3 — Regenerate docs

If layout, workflows, CLI, or prompts changed: [regenerate-docs.md](regenerate-docs.md). Else skip.

### Step 3b — Sync pyproject.toml

If Python deps, tooling, package layout, or `pyproject.toml` changed: [sync-pyproject.md](sync-pyproject.md). On first init of a Python consumer repo, run once even if this session only scaffolded layout. Else skip.

### Step 4 — ADR

If irreversible design choice: [suggest-adr.md](suggest-adr.md). Else skip.

### Step 5 — TODO

Update `TODO.md`: close done items; add tasks **only if user stated them**. Do not invent backlog.

### Constraints

Read `git status`. Do not invent changes. Do not commit unless asked. Devlog is append-only.

### Output

Deliver handoff results in chat. End with:

> Next session on this repo (especially a new area): start a **new chat** and `Run prompts/takeover.md` (or `run /prompts/takeover`) before coding. On this kit repo (upstream): run [takeover.md](takeover.md) directly.
