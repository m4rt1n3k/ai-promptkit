# Handoff — <project-name>

Extends `extern/ai-promptkit/prompts/handoff.md`. Daily end-of-session routine.

Invoke:

```text
Run prompts/handoff.md
```

Short form: `run /prompts/handoff`.

---

## Task: Session handoff

<project-name> (cwd = repo root).

### Steps 1–5 — Base

Follow `extern/ai-promptkit/prompts/handoff.md` steps 1–5 in order (step 3b syncs `pyproject.toml` when the Python project changed).

### Project steps

*Add project-specific steps here when needed. Example: extra validation, deploy checklist, domain-specific doc refresh.*

*Next chat / new area: `Run prompts/takeover.md` (or `run /prompts/takeover`) before coding.*

### Constraints

Same as base: read `git status`; do not invent changes; do not commit unless asked.
