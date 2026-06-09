# Session summary — commit message draft

Use at end of session (standalone or as step 1 of [`handoff.md`](handoff.md)).

Copy everything below the line into a new agent chat with session context and `git status` / diff summary.

---

## Task: Draft commit message

You are in the **target repository** (cwd = repo root).

**Goal:** Produce a commit message draft for work done in this session. **Do not commit** unless the user explicitly asks.

### Inputs

- Conversation summary (what changed and why)
- `git status` and relevant diff hunks (user provides or you read)

### Output format

```text
Subject: <imperative, ≤72 chars, no file list>

- <what/why bullet>
- <what/why bullet>
```

### Rules

- Focus on **intent and outcome**, not a file manifest.
- Use this repo's vocabulary (read README or `docs/conventions.md` if unsure).
- If nothing committable, say so and list unstaged WIP.
- If session mixed unrelated concerns, suggest splitting into multiple commits.
