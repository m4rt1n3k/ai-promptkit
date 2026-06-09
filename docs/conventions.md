# Conventions — agent governance

Rules for agents working on repos that use ai-promptkit.

## Documentation layers

| Layer | File | Job |
|-------|------|-----|
| Map | `README.md` | Structure, links, who reads what |
| Manual | `docs/manual.md` | Human workflows and procedures |
| Conventions | `docs/conventions.md` | Agent rules (this file) |
| Devlog | `docs/devlog.md` | Session outcomes table (append-only) |
| ADR | `docs/adr/` | Irreversible architectural choices |
| Prompts | `prompts/` | Invocable AI task bodies |

Do not store chat logs in conventions. Session narrative goes in devlog only.

## Handoff rules

1. **Devlog** — prepend one row; outcomes only; local ISO times with seconds; no quotes below table.
2. **TODO** — only tasks the user stated in the session; do not invent pipeline items.
3. **No secrets** in docs, devlog, or TODO.
4. **Do not commit** unless the user explicitly asks.
5. **Regenerate docs** only when layout, workflows, CLI, or prompt registry changed.

## Design discipline

Prefer minimal correct changes. Do not explore many alternatives unless asked. See `templates/design.rule.mdc` for the Cursor rule text.

## Prompt file contract

Every prompt file:

1. Human-readable title and when-to-use (above `---`)
2. `---`
3. Copy-paste task body with explicit cwd = repo root

## Submodule policy

- ai-promptkit submodule is **read-only** in consumer repos.
- Customize `prompts/handoff.md` on the consumer after copy; propose upstream changes for shared prompts.
- Sync `prompts/` after submodule updates.

## Anti-goals

- Monolithic `PROMPT.md` with embedded chat history
- In-repo kit dispatchers or JSON orchestration state
- Invented backlog during handoff
- Heavy doc frameworks (MkDocs, etc.) without explicit request
