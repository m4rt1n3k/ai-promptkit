# PROMPT.md — ai-promptkit

## 0. Meta

- Purpose: Kit workers for handoff and design discipline on **other** repos (and this repo when asked).
- Last updated: 2026-06-02
- Active track: `_none_` (see [TODO.md](./TODO.md))
- Companion: [TODO.md](./TODO.md)
- Repo: [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## 1. Mission

Ship **`kits/*.md`** workers invoked from another workspace:

```text
from workspace ai-promptkit run kit_prompt
from workspace ai-promptkit run kit_todo
from workspace ai-promptkit run kit_handoff
from workspace ai-promptkit run kit_design
```

Default: write to the **opened project**. This repo is the target only when the user says so (e.g. `run kit_handoff on yourself`).

## 2. Hard constraints

1. **Distill** — handoff files are not chat logs.
2. **`kit_todo`** — only TODO items the **user stated** in that chat; do not invent backlog.
3. **No secrets** in handoff files.
4. **Minimal kits** — no dispatcher, cold-start docs, or automation layer in this repo (IDE invoke only).

## 3. User inputs (binding / preference)

- [binding] Invoke from other workspaces: `from workspace ai-promptkit run <kit>`.
- [binding] `PROMPT.md` + `TODO.md` on target repos; merge, append-only §9 log on targets.
- [preference] `kit_design`: minimal optimal solution; do not go deep into possibilities (rule on target).
- [preference] Simplified toolbox—removed extra docs/automations/rules from earlier iteration.

## 4. Decisions

| ID | Decision | Why |
|----|----------|-----|
| D1 | IDE phrase invoke, not in-repo dispatcher | User: too complicated |
| D2 | `kit_design` → `.cursor/rules/kit-design.mdc` on target | Behavioral setup separate from handoff files |
| D3 | Target `kit_todo` = user-mentioned tasks only | User: do not invent unless asked |

## 5. Current state

- Branch: `main` (tracks `origin/main`; local ahead of last push — uncommitted)
- Path: `C:\Users\VLAD\HOME\CODE_m4rt1n3k\ai-promptkit`
- **In repo:** `README.md`, `PROMPT.md`, `TODO.md`, `kits/` (`kit_prompt`, `kit_todo`, `kit_handoff`, `kit_design`, `templates/`)
- **Removed (uncommitted):** `docs/`, `automations/`, `.cursor/rules/`, `PROMPT-TODO-handoff-plan.md`
- Works: four kits documented in README; templates for PROMPT/TODO/design rule

## 6. Next actions

1. Commit and push when you want the simplified kit layout on GitHub.
2. On other repos: `from workspace ai-promptkit run kit_prompt` (etc.) — see TODO `roll-out-kits` if batching later.
3. Later: refine `kit_design` — TODO `kit-design-refine`.

## 7. References

- Kits: [kits/](kits/)
- Templates: [kits/templates/](kits/templates/)

## 8. Anti-goals

- Monolithic handoff automation prefills in this repo.
- Invented pipeline on target repos during `kit_todo`.

## 9. Conversation log

| Date | Topics | Session | Summary | Refs |
|------|--------|---------|---------|------|
| 2026-06-02 | `kit-workers`, `simplify` | `minimal-ide-invoke` | IDE-only invoke; stripped dispatcher, cold-start, automations. | D1 |
| 2026-06-02 | `kit_design` | `add-design-kit` | Added `kit_design` worker + template rule. | D2, TODO#kit-design-refine |
| 2026-06-02 | `handoff`, `ai-promptkit` | `kit-handoff-self` | User ran `kit_handoff` on this repo; PROMPT/TODO refreshed from session. | — |
