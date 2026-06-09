# Update devlog

Use at end of session (standalone or as step 2 of [`handoff.md`](handoff.md)).

Copy everything below the line into a new agent chat.

---

## Task: Append devlog row

You are in the **target repository** (cwd = repo root).

**Goal:** Prepend **one row** to the table in `docs/devlog.md` (newest first). Column order: **Interval | Topics | Summary | Author | Refs**.

### Format

| Column | Rules |
|--------|--------|
| **Interval** | `YYYY-MM-DD HH:MM:SS` with seconds when known. **Local wall clock** — never `±HH:MM`. Start on line 1, end on line 2 in the cell (`<br/>`), or `start/end` on one line. Use `?` for unknown start only if end is known. |
| **Topics** | Short backtick tags, e.g. `handoff`, `api`, `docs-layout` — not sentences. |
| **Summary** | **Outcomes only** — what was delivered or decided (1–2 short sentences). No step-by-step narration, no file lists, no quotes from chat. |
| **Author** | Line 1: `Human Name [human]`. Line 2: `Agent Name [ai]`. Use `<br/>` between lines. No model version strings unless the user insists. |
| **Refs** | Link related ADRs when the session touched architectural choices (paths relative to `docs/devlog.md`), e.g. `[ADR-0001](adr/0001-slug.md)`. PR/issue URLs or `—` if none. |

Append-only; **newest row first**. Each row = one session. No chat quotes or extra tables below the log.

### Editing rules

- **Prepend only** — insert the new row immediately below the table header row; do not edit or delete existing rows.
- Do not invent work not evidenced in chat or `git diff`.
- If the session was trivial (single typo, no decision), skip devlog and say so.
- If the session warrants a **new** ADR, use [`suggest-adr.md`](suggest-adr.md) separately; then cite that ADR in **Refs**.

### Example row

```markdown
| 2026-06-09 10:15:00<br/>2026-06-09 11:42:33 | `handoff`, `devlog` | Devlog format rules codified; update-devlog prompt aligned. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
```

### Target

File: `docs/devlog.md` — title, append links, and table only.
