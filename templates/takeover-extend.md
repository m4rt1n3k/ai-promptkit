# Takeover — <project-name>

Extends `extern/ai-promptkit/prompts/takeover.md`. Daily start-of-session routine.

Invoke:

```text
Run prompts/takeover.md
```

Short form: `run /prompts/takeover`. Optional: append `Focus on <path or module>.`

---

## Task: Takeover before coding

<project-name> (cwd = repo root).

### Steps — Base

Follow `extern/ai-promptkit/prompts/takeover.md` in full:

1. **Refresh submodule** (`git submodule update --init --recursive --remote`) when `extern/ai-promptkit` is present
2. Read-only deep explore → debrief → ready for user task

### Project steps

*Add project-specific orientation here when needed. Example: required env files, which service to run, domain glossary.*

*End of session: `Run prompts/handoff.md` (or `run /prompts/handoff`).*

### Constraints

Same as base: evidence with paths; do not invent backlog; do not commit unless asked (including submodule bump); stay read-only until the user asks to implement — except the submodule refresh step.
