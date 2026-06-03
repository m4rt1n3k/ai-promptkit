# kit_todo

Run when the user says **`from workspace ai-promptkit run kit_todo`** (or `kit_todo`).

## Load

Read this file from **ai-promptkit**. Write to the **user’s project workspace**, not ai-promptkit.

## Inputs

- This chat only for **what to put in TODO**
- Optional `session:`, `topics:`, `active:` from the user message
- Existing `TODO.md` (merge), `PROMPT.md` (sync active track if present)
- Template if new: [templates/TODO.template.md](./templates/TODO.template.md)

## Task

Create or **merge** `TODO.md` at the target repo root.

**Backlog rule (important):** Add or update **only** plans and tasks the **user stated in this chat**. Do **not** invent pipeline items, mind-branches, or “recommended next steps” unless the user asked for them.

- Keep Legend (severity, time, status) if missing.
- **Active track:** one row or `_none_` if the user gave no task.
- Move items to Done only if the user said they are finished in this chat.
- Align topics with the newest `PROMPT.md` §9 row (`Interval`, `Author`) if you also run `kit_handoff`.

## Do not

Update `PROMPT.md` (use `kit_prompt` or `kit_handoff`) or `MANUAL.md` (use `kit_manual` or `kit_handoff`).

## Reply

Short: target path, what changed in `TODO.md`, list of TODO IDs touched.
