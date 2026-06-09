# ADR-0001: Prompts library over kit workers

- Status: accepted
- Date: 2026-06-09

## Context

ai-promptkit originally shipped `kits/*.md` workers (`kit_prompt`, `kit_todo`, `kit_handoff`, etc.) invoked by phrase from other workspaces. Consumer repos kept monolithic `PROMPT.md`, `MANUAL.md`, and `TODO.md` at root. This split agent context, human docs, and session logs awkwardly and did not submodule cleanly.

A parallel design emerged: flat `prompts/` library, `docs/` layers (manual, conventions, devlog, adr), and `handoff.md` as orchestrator.

## Decision

1. **ai-promptkit** is a **submodule prompt library**, not a kit dispatcher.
2. Portable workflows live in `prompts/`; orchestration in `prompts/handoff.md`.
3. Consumer repos bootstrap `docs/` + `prompts/` via `bootstrap-docs-prompts-layout.md`.
4. Legacy `kits/` and root `PROMPT.md` / `MANUAL.md` are removed; stub redirects point to `docs/`.
5. Invoke model: read prompt from `vendor/ai-promptkit/prompts/...` or copy `prompts/` locally.

## Alternatives considered

- **Keep kits** — rejected; duplicate orchestration vs prompts, harder to copy across repos.
- **JSON prompt registry + runner** — rejected; over-engineered for IDE paste workflow.
- **Single monolithic AGENTS.md** — rejected; mixes human manual, agent rules, and session log.

## Consequences

- Consumer repos need one-time bootstrap; submodule update + copy for prompt changes.
- `kit_*` invoke phrases replaced by `Run prompts/handoff.md` or read-from-submodule phrases.
- Design discipline moves to `install-design-rule.md` → `.cursor/rules/design-discipline.mdc`.
