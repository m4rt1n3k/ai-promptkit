# PROMPT.md — agent handoff

## 0. Meta

- Purpose: (one sentence)
- Audience: coding agent / reviewer
- Last updated: YYYY-MM-DD
- Active track: (TODO plan-id or `_none_`)
- Companion: [TODO.md](./TODO.md) · [MANUAL.md](./MANUAL.md) (human workflows)
- Repo: (name + remote URL if git)

## 1. Mission

What we are building or fixing; definition of done.

## 2. Hard constraints (must not violate)

1. …

## 3. User inputs (verbatim where it matters)

- [binding] …
- [preference] …

## 4. Decisions made

| ID | Decision | Why | Alternatives rejected |
|----|----------|-----|------------------------|

## 5. Current state

- Branch / commit
- Workspace path
- What works / what is broken
- Open questions

## 6. Next actions (ordered, near-term only)

1. …
(Multi-track backlog → [TODO.md](./TODO.md))

## 7. References

- Legacy / domain docs (paths only)
- Kit: [ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## 8. Anti-goals / out of scope

- …

## 9. Conversation log (append-only)

Append-only log in **one table**; **newest row first**. Each row = one kit conversation. Times are **local wall clock** (no `±HH:MM` in cells). **Interval:** `YYYY-MM-DD HH:MM:SS` with **seconds** when known — start then end on two lines in the cell (`<br/>`), or `start/end` on one line. No chat quotes under the table. Columns: **Interval**, **Topics**, **Author** (`Name [human]` and `Agent [ai]` on two lines), **Summary**, **Refs**.

| Interval | Topics | Author | Summary | Refs |
|----------|--------|--------|---------|------|
| YYYY-MM-DD HH:MM:SS<br/>YYYY-MM-DD HH:MM:SS | `topic-one` | Jane Doe [human]<br/>Cursor Agent(Composer) [ai] | One-line agent summary | — |
