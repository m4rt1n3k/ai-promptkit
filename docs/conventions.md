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

1. Daily invoke: `prompts/handoff.md` (extends base steps 1–5).
2. Devlog: prepend one row; outcomes only; no chat quotes below table.
3. TODO: user-stated tasks only — do not invent backlog.
4. No secrets in docs. Do not commit unless asked.

## Prompts

- Contract: title → `---` → task body; cwd = repo root.
- Onboarding: run `subs/ai-promptkit/prompts/init.md` once after submodule add.
- Do not edit `subs/ai-promptkit/`. Fork single files into `prompts/` only when needed.
- Resolve paths: `prompts/<file>` first, else `subs/ai-promptkit/prompts/<file>`.

## Design discipline

Minimal correct changes. Template: `subs/ai-promptkit/templates/design.rule.mdc` → `.cursor/rules/design-discipline.mdc`.
