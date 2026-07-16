# Conventions

Agent rules for repos using ai-promptkit.

## Files

**Consumer** (after [init.md](../prompts/init.md)):

| File | Job |
|------|-----|
| `extern/ai-promptkit/prompts/` | Base prompts (read-only) |
| `prompts/handoff.md` | Extends base — daily end (`Run prompts/handoff.md`) |
| `prompts/takeover.md` | Extends base — daily start (`Run prompts/takeover.md`) |
| `prompts/` | Other project prompts |
| `docs/{manual,conventions,devlog,adr}/` | Project docs |

**Upstream (ai-promptkit itself):** same `docs/` + `prompts/` paths, but no `extern/`; `prompts/handoff.md` is the base (not a wrapper).

## Daily routines

1. **Takeover** — start of work in a **new chat**: `Run prompts/takeover.md` (`run /prompts/takeover`). First action on consumers: `git submodule update --init --recursive --remote`.
2. **Handoff** — end of work in the **current chat**: `Run prompts/handoff.md` (`run /prompts/handoff`); extends base steps 1–5 (+ 3b for Python).
3. Devlog: prepend one row; outcomes only; no chat quotes below table.
4. TODO: user-stated tasks only — do not invent backlog.
5. No secrets in docs. Do not commit unless asked (including submodule pointer bumps from takeover).
6. `pyproject.toml`: consumer Python projects only — [sync-pyproject.md](../prompts/sync-pyproject.md). Not used in ai-promptkit upstream.

## Session rhythm

1. **Handoff** — end of work session in the **current chat** (consumer: `prompts/handoff.md`).
2. **Takeover** — start of work session in a **new chat** (consumer: `prompts/takeover.md`), especially before coding on human-written code or a new area. Refreshes `extern/ai-promptkit` before explore.
3. Takeover reads devlog/TODO/conventions first; it does not duplicate handoff (no commit summary, no devlog append).
4. Takeover stays read-only for project files until the user asks to implement (submodule refresh is allowed); development continues in the same chat after the debrief.

## Prompts

- Contract: title → `---` → task body; cwd = repo root.
- Onboarding: run `extern/ai-promptkit/prompts/init.md` once after submodule add.
- Do not edit `extern/ai-promptkit/`. Fork single files into `prompts/` only when needed.
- Resolve paths: `prompts/<file>` first, else `extern/ai-promptkit/prompts/<file>`.

## Design discipline

Minimal correct changes. Template: `extern/ai-promptkit/templates/design.rule.mdc` → `.cursor/rules/design-discipline.mdc`.
