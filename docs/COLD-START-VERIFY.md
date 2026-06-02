# Cold-start verification (first export)

Use this checklist to confirm a **new agent** can continue without chat history.

## Preconditions

- Workspace root is **AI vibecoding** (this folder) or a repo that copied these files.
- `.cursor/rules/agent-handoff-bootstrap.mdc` is present (`alwaysApply: true`).

## Steps

1. Start a **new** chat (or switch model).
2. Send only:

   ```text
   Read PROMPT.md, then TODO.md; confirm PROMPT §5 Current state matches this repo; work only the Active track in TODO unless I say otherwise. Report what you would do next in one paragraph.
   ```

3. **Expected agent behavior**
   - Reads both files before proposing code changes.
   - Confirms branch/paths match §5 (or reports mismatch).
   - Names **Active track** from `TODO.md` (after export: none or maintenance — see TODO Active track table).
   - Does not ask to re-derive the PROMPT/TODO split from scratch.

## Pass criteria

| Check | Pass if |
|-------|---------|
| File pair | Agent cites `PROMPT.md` and `TODO.md` |
| Constraints | Agent respects §2 (no secrets, append-only log, capitals PROMPT) |
| Backlog | Agent points multi-track work to TODO, not PROMPT §6 essay |
| Log tags | Agent can explain Topics vs Session from §9 |

## This session (2026-06-02)

Kit migrated from `agent-handoff` into Team-ProGrammar **AI vibecoding** folder.

**Simulated cold-start answer (reference):** Active track is `_none_` until next handoff sets a plan-id. Next work for user: save automation in UI if needed, run handoff at session end, optional roll-out to other repos (TODO plan-5, plan-6).
