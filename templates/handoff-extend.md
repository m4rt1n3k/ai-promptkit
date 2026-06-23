# Handoff — <project-name>

Extends `subs/ai-promptkit/prompts/handoff.md`. Invoke: `Run prompts/handoff.md — end of session handoff.`

---

## Task: Session handoff

<project-name> (cwd = repo root).

### Steps 1–5 — Base

Follow `subs/ai-promptkit/prompts/handoff.md` steps 1–5 in order (step 3b syncs `pyproject.toml` when the Python project changed).

### Project steps

*Add project-specific steps here when needed. Example: extra validation, deploy checklist, domain-specific doc refresh.*

*Next chat on a new area: run `subs/ai-promptkit/prompts/takeover.md` before coding.*

### Constraints

Same as base: read `git status`; do not invent changes; do not commit unless asked.
