# PROMPT.md — ai-promptkit

## 0. Meta

- Purpose: Kit workers for handoff and design discipline on **other** repos (and this repo when asked).
- Last updated: 2026-06-03 (§9 ISO interval; table only)
- Active track: `_none_` (see [TODO.md](./TODO.md))
- Companion: [TODO.md](./TODO.md) · [MANUAL.md](./MANUAL.md)
- Repo: [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## 1. Mission

Ship `**kits/*.md`** workers invoked from another workspace:

```text
from workspace ai-promptkit run kit_prompt
from workspace ai-promptkit run kit_todo
from workspace ai-promptkit run kit_handoff
from workspace ai-promptkit run kit_manual
from workspace ai-promptkit run kit_design
```

Default: write to the **opened project**. This repo is the target only when the user says so (e.g. `run kit_handoff on yourself`). `kit_handoff` updates `TODO.md`, `PROMPT.md`, and `MANUAL.md`. File roles and working cycle: [README.md](README.md) (*Handoff file ecosystem*).

## 2. Hard constraints

1. **Distill §§0–8** — not chat logs; **§9** = intro paragraph + single table, local ISO date-times, no quoted conversation (see `kits/kit_prompt.md`).
2. `**kit_todo`** — only TODO items the **user stated** in that chat; do not invent backlog.
3. **No secrets** in handoff files.
4. **Minimal kits** — no dispatcher, cold-start docs, or automation layer in this repo (IDE invoke only).

## 3. User inputs (binding / preference)

- [binding] Invoke from other workspaces: `from workspace ai-promptkit run <kit>`.
- [binding] `PROMPT.md` + `TODO.md` on target repos; merge; §9 structure described once at top of §9; table rows only.
- [preference] `kit_design`: minimal optimal solution; do not go deep into possibilities (rule on target).
- [preference] Simplified toolbox—removed extra docs/automations/rules from earlier iteration.

## 4. Decisions


| ID  | Decision                                                | Why                                          |
| --- | ------------------------------------------------------- | -------------------------------------------- |
| D1  | IDE phrase invoke, not in-repo dispatcher               | User: too complicated                        |
| D2  | `kit_design` → `.cursor/rules/kit-design.mdc` on target | Behavioral setup separate from handoff files |
| D3  | Target `kit_todo` = user-mentioned tasks only           | User: do not invent unless asked             |


## 5. Current state

- Branch: `main` (tracks `origin/main`; local ahead of last push — uncommitted)
- Path: `C:\Users\VLAD\HOME\CODE_m4rt1n3k\ai-promptkit`
- **In repo:** `README.md`, `PROMPT.md`, `TODO.md`, `MANUAL.md`, `kits/` (`kit_prompt`, `kit_todo`, `kit_handoff`, `kit_manual`, `kit_design`, `templates/`)
- **Removed (uncommitted):** `docs/`, `automations/`, `.cursor/rules/`, `PROMPT-TODO-handoff-plan.md`
- Works: five handoff-related kits in README; templates for PROMPT/TODO/MANUAL/design rule

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

Append-only log in **one table**; **newest row first**. Each row = one kit conversation. Times are **local wall clock** (Central Europe on this machine; no `±HH:MM` in cells). **Interval:** `YYYY-MM-DD HH:MM:SS` with seconds when known — start on the first line, end on the second (`<br/>` in the cell), or `start/end` on one line. No chat quotes below the table. **Author:** `Name [human]` and `Agent [ai]` on two lines. **Summary** = outcomes only.

| Interval | Topics | Author | Summary | Refs |
|----------|--------|--------|---------|------|
| 2026-06-03 08:52:00<br/>2026-06-03 09:03:05 | `kit_prompt`, `interval-format` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Interval format `YYYY-MM-DD HH:MM:SS`; require precise seconds when available. | — |
| 2026-06-03 08:52:00<br/>2026-06-03 09:00:00 | `kit_prompt`, `section-9` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | §9 intro paragraph; local times without offset; interval `/` vs two-line documented. | — |
| 2026-06-03 08:49:00<br/>2026-06-03 08:52:00 | `kit_prompt`, `section-9` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Table only—removed conversation fences. | — |
| 2026-06-03 08:46:00<br/>2026-06-03 08:49:00 | `kit_prompt`, `interval` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Fixed intervals; no 00:00–23:59 placeholders. | — |
| 2026-06-03 08:43:00<br/>2026-06-03 08:46:00 | `kit_prompt`, `author-format` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Author format `Name [human]` + `Agent [ai]`. | — |
| 2026-06-03 08:40:00<br/>2026-06-03 08:43:00 | `kit_prompt`, `author` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Author column must name specific human and AI. | — |
| 2026-06-03 08:35:00<br/>2026-06-03 08:40:00 | `kit_prompt`, `section-9` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | `Interval` + `Author`; dropped `Session`. | — |
| 2026-06-03 08:32:00<br/>2026-06-03 08:35:00 | `kit_prompt`, `kit_design` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | §9 table + captions removed; kit_design anti-redundancy. | — |
| 2026-06-03 08:28:00<br/>2026-06-03 08:32:00 | `kit_prompt`, `section-9` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Richer §9; table row per conversation (later revised). | — |
| 2026-06-03 08:24:00<br/>2026-06-03 08:28:00 | `kit_manual`, `MANUAL.md` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Added kit_manual; handoff updates TODO + PROMPT + MANUAL. | — |
| 2026-06-02 17:30:00<br/>2026-06-02 18:04:27 | `handoff`, `ai-promptkit` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | kit_handoff on this repo; PROMPT/TODO refreshed. | — |
| 2026-06-02 16:45:56<br/>2026-06-02 17:30:00 | `kit_design` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | Added kit_design worker + template rule. | D2, TODO#kit-design-refine |
| 2026-06-02 16:09:27<br/>2026-06-02 16:45:56 | `kit-workers`, `simplify` | Vladislav Martinek [human]<br/>Cursor Agent(Auto) [ai] | IDE-only invoke; stripped dispatcher, cold-start, automations. | D1 |


