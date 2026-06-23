# Conventions

Agent rules for repos using ai-promptkit.

## Files

**Consumer** (after [init.md](../prompts/init.md)):

| File | Job |
|------|-----|
| `subs/ai-promptkit/prompts/` | Base prompts (read-only) |
| `prompts/handoff.md` | Extends base — daily invoke |
| `prompts/` | Other project prompts |
| `docs/{manual,conventions,devlog,adr}/` | Project docs |

**Upstream (ai-promptkit itself):** same `docs/` + `prompts/` paths, but no `subs/`; `prompts/handoff.md` is the base (not a wrapper).

## Handoff

1. Daily invoke: `prompts/handoff.md` (extends base steps 1–5, including 3b for Python).
2. Devlog: prepend one row; outcomes only; no chat quotes below table.
3. TODO: user-stated tasks only — do not invent backlog.
4. No secrets in docs. Do not commit unless asked.
5. `pyproject.toml`: consumer Python projects only — [sync-pyproject.md](../prompts/sync-pyproject.md). Not used in ai-promptkit upstream.

## Session rhythm

1. **Handoff** — end of work session in the **current chat** ([handoff.md](../prompts/handoff.md)).
2. **Takeover** — start of work session in a **new chat** ([takeover.md](../prompts/takeover.md)), especially before coding on human-written code or a new area of the repo.
3. Takeover reads devlog/TODO/conventions first; it does not duplicate handoff (no commit summary, no devlog append).
4. Takeover is read-only exploration until the user asks to implement; development continues in the same chat after the debrief.

## Prompts

- Contract: title → `---` → task body; cwd = repo root.
- Onboarding: run `subs/ai-promptkit/prompts/init.md` once after submodule add.
- Do not edit `subs/ai-promptkit/`. Fork single files into `prompts/` only when needed.
- Resolve paths: `prompts/<file>` first, else `subs/ai-promptkit/prompts/<file>`.

## Design discipline

Minimal correct changes. Template: `subs/ai-promptkit/templates/design.rule.mdc` → `.cursor/rules/design-discipline.mdc`.
