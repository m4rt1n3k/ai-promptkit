# kit_prompt

Run when the user says **`from workspace ai-promptkit run kit_prompt`** (or `kit_prompt`).

## Load

Read this file from the **ai-promptkit** repo. Write results to the **user’s project workspace** (the repo they are working in), not into ai-promptkit.

## Inputs

- This chat (for distilling §§0–8 and for §9 Summary / Topics)
- Optional `topics:`, `notes:` from the user message (Topics column only). Legacy `session:` → extra topic tag, not a table column.
- Target repo: git branch/status/diff, existing `PROMPT.md`, `TODO.md` (read only for active track), legacy `prompt.md` / README
- Template if creating new: [templates/PROMPT.template.md](./templates/PROMPT.template.md)

## Task

Create or **merge** `PROMPT.md` at the target repo root (`PROMPT.md` capitals).

- **§§0–8:** Distill for the next agent; do not paste the whole chat there.
- If target already has a custom `PROMPT.md`, keep its structure; update state and meta; prepend **one new row** to the §9 table (see below).
- Near-term actions in §6 only; backlog stays in `TODO.md`.
- No secrets anywhere. Prefer §§0–8 under ~400 lines.

## §9 Conversation log

When writing §9 on the target `PROMPT.md`, start with a **short intro paragraph** (after `## 9` title, before the table) that states how the log works—see template. Do not repeat that explanation on every row.

§9 body = intro paragraph + **one markdown table** (header + separator + data rows). No fenced blocks, no quoted chat.

1. **Order:** Prepend the **new** row immediately below the separator (newest first). Keep existing rows; do not delete unless asked.
2. **Intro (once):** Newest first; one row per kit conversation; times are **local wall clock** without `±HH:MM` in cells (state timezone or “local” once in the intro if needed). Interval = `YYYY-MM-DD HH:MM:SS` (space between date and time; **always include seconds** when known).
3. **Columns:** `Interval | Topics | Author | Summary | Refs`
   - **Interval:** local date-time without timezone suffix.
     - **Format:** `YYYY-MM-DD HH:MM:SS` (e.g. `2026-06-03 08:46:27`). Use real seconds from the thread, `git log`, file `LastWriteTime`, or `Get-Date` at kit run—do not truncate to `:00` unless seconds are truly unknown.
     - **Display:** two lines in the cell: `start<br/>end` (preferred), or one line `start/end` with `/` between instants.
     - **Start** = first message time if visible, else earliest evidence above. **End** = last message or **now** at kit run. Never full-day placeholders; if start unknown use `?<br/>YYYY-MM-DD HH:MM:SS` and note in Summary.
   - **Topics:** comma-separated tags.
   - **Author:** `<FullName> [human]<br/><Agent> [ai]` — human from `git config user.name` → GitHub owner → `$USERNAME`; AI from thread/model or `Cursor Agent(Auto)`.
   - **Summary:** one line (outcomes; may paraphrase user intent—chat text does not go in §9).
   - **Refs:** `D#`, `TODO#id`, or `—`.
3. §3 stays curated bullets; do not duplicate §9 into §3.

See [templates/PROMPT.template.md](./templates/PROMPT.template.md) §9.

## Do not

- Update `TODO.md` (use `kit_todo` or `kit_handoff`) or `MANUAL.md` (use `kit_manual` or `kit_handoff`).
- Add ` ```text ` / ` ``` ` blocks or pasted conversation under §9.
- Add extra headings or captions between table rows.
- Use `T` between date and time, omit seconds when they are known, or use full-day placeholders in Interval.
- Use `Human: … · AI: …`, generic `human`/`AI`, or device name as human identity.

## Reply

Short: target path, what changed in `PROMPT.md`, 3–5 bullets. Confirm §9: one new table row prepended (`YYYY-MM-DD HH:MM:SS` with seconds).
