# AI vibecoding — agent handoff

Team-ProGrammar workspace for **conversation handoff** and vibecoding practices. Canonical kit: repo-root [`PROMPT.md`](./PROMPT.md) + [`TODO.md`](./TODO.md).

Migrated from standalone `C:\Users\VLAD\agent-handoff` (2026-06-02). Full specification: [`PROMPT-TODO-handoff-plan.md`](./PROMPT-TODO-handoff-plan.md).

## Quick start (new agent)

```text
Read PROMPT.md, then TODO.md; confirm PROMPT §5 Current state matches this repo; work only the Active track in TODO unless I say otherwise.
```

## Copy into another project

1. Copy `PROMPT.md`, `TODO.md`, and `.cursor/rules/agent-handoff-bootstrap.mdc` to that repo’s root (adjust §0 Meta purpose).
2. Import or recreate the automation from [`automations/export-handoff-prefill.json`](./automations/export-handoff-prefill.json).
3. Say **handoff** or **export PROMPT** before switching models; optional trigger body: `session: my-label` and `topics: tag1, tag2`.

## Automation

See [`automations/README.md`](./automations/README.md). Open the prefill in Cursor Automations (Glass), save, then use the webhook URL or manual run with handoff notes in the prompt.

## Files

| File | Role |
|------|------|
| `PROMPT.md` | Mission, constraints, decisions, state, next actions, tagged log |
| `TODO.md` | Plans, mind-branches, severity, time priority |
| `PROMPT-TODO-handoff-plan.md` | Complete plan/spec (reference) |
| `.cursor/rules/agent-handoff-bootstrap.mdc` | Tells agents to read both files first |
| `docs/COLD-START-VERIFY.md` | Cold-start agent checklist |
