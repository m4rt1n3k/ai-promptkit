# kit_prompt

Run when the user says **`from workspace ai-promptkit run kit_prompt`** (or `kit_prompt`).

## Load

Read this file from the **ai-promptkit** repo. Write results to the **user’s project workspace** (the repo they are working in), not into ai-promptkit.

## Inputs

- This chat (decisions, user quotes)
- Optional `session:`, `topics:`, `notes:` from the user message
- Target repo: git branch/status/diff, existing `PROMPT.md`, `TODO.md` (read only for active track), legacy `prompt.md` / README
- Template if creating new: [templates/PROMPT.template.md](./templates/PROMPT.template.md)

## Task

Create or **merge** `PROMPT.md` at the target repo root (`PROMPT.md` capitals).

- Distill; do not paste the whole chat.
- If target already has a custom `PROMPT.md`, keep its structure; update state, meta, append one §9 log row.
- Near-term actions in §6 only; backlog stays in `TODO.md`.
- Append-only §9 log: Date | Topics | Session | Summary.
- No secrets. Under ~400 lines.

## Do not

Update `TODO.md` (use `kit_todo` or `kit_handoff`).

## Reply

Short: target path, what changed in `PROMPT.md`, 3–5 bullets.
