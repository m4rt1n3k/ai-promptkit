# Handoff automation

## Import into Cursor Automations

1. Open Cursor **Automations** (Glass).
2. Create a new automation and use **Import** / editor prefill, or ask an agent to open the editor with `automations/export-handoff-prefill.json` as `prefillWorkflowData`.
3. **Save** in the UI — webhook URL and auth are assigned after save.
4. Enable file/git tools in the automation as needed for your target repo (cloud agent defaults usually include workspace file access).

## Trigger

- **Webhook** — POST with optional JSON body containing handoff notes.
- **Manual run** — from Automations UI before switching LLMs.

Suggested prompt prefix when running:

```text
session: my-thread-label
topics: tag-one, tag-two
handoff notes: (what changed, blockers, active plan-id)
```

## Behavior

Runs the meta-prompt in `export-handoff-prefill.json`: merges `PROMPT.md` and `TODO.md` at the **workspace repo root** (the project the automation checks out or runs against). Point the automation at **ai-promptkit** ([github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)), or copy this kit’s files into another repo first.

## Related

- Templates: [`../PROMPT.md`](../PROMPT.md), [`../TODO.md`](../TODO.md)
- Bootstrap rule: [`../.cursor/rules/agent-handoff-bootstrap.mdc`](../.cursor/rules/agent-handoff-bootstrap.mdc)
