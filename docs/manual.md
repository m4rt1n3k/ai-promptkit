# Manual — ai-promptkit

Human guide for using this repo as a **shared prompt library** across projects.

## 1. What this repo is

ai-promptkit ships **portable prompts** in `prompts/` and a **handoff orchestrator** (`prompts/handoff.md`). Consumer projects add it as a git submodule and bootstrap a `docs/` + `prompts/` layout on their own repo.

This repo does **not** run a dispatcher or CI orchestration — you paste prompts into Cursor Agent or point the agent at submodule paths.

## 2. Submodule setup

In a consumer project:

```bash
git submodule add https://github.com/m4rt1n3k/ai-promptkit vendor/ai-promptkit
git submodule update --init --recursive
cp -r vendor/ai-promptkit/prompts .
```

First-time consumer repo: run the bootstrap prompt (see §4.1).

## 3. Working cycle

### Pass 1 — Development

| Step | Read / do |
|------|-----------|
| Orient | README · `docs/conventions.md` · `TODO.md` |
| Develop | Code with Cursor Agent |
| Handoff | `prompts/handoff.md` (or invoke via submodule) |
| Commit | When ready (handoff drafts message only) |

### Pass 2 — Usage / ops

| Step | Read / do |
|------|-----------|
| Orient | README · `docs/manual.md` |
| Operate | Follow procedures; no handoff unless docs change |

## 4. Core workflows

### 4.1 Bootstrap a new consumer repo

1. Add submodule (§2).
2. In Agent chat on the **consumer** repo:
   ```text
   Read vendor/ai-promptkit/prompts/bootstrap-docs-prompts-layout.md and run it on this workspace.
   ```
3. Review scaffolded `docs/` and `prompts/`.
4. Run handoff after first real session.

### 4.2 End-of-session handoff

1. Open the **consumer** project in Cursor.
2. Agent chat:
   ```text
   Run prompts/handoff.md — end of session handoff.
   ```
   Or without local copy:
   ```text
   Read vendor/ai-promptkit/prompts/handoff.md and execute on this workspace.
   ```
3. Review `docs/devlog.md`, `TODO.md`, and any doc diffs.
4. Commit when ready.

### 4.3 Install design discipline

Once per consumer repo:

```text
Read vendor/ai-promptkit/prompts/install-design-rule.md and run on this workspace.
```

Creates `.cursor/rules/design-discipline.mdc`.

### 4.4 Maintain ai-promptkit itself

1. Open **this** repo in Cursor.
2. Edit `prompts/*.md` or templates.
3. Run `prompts/handoff.md` on this workspace.
4. Consumer repos pull submodule + re-copy `prompts/` when they want updates.

## 5. Troubleshooting

| Symptom | Fix |
|---------|-----|
| Handoff writes to ai-promptkit instead of my app | Open the app repo; re-run with explicit "this workspace" |
| TODO filled with invented tasks | Restate tasks in chat; handoff step 5 only closes/states user-mentioned work |
| Missing `docs/devlog.md` | Run bootstrap prompt once |
| Stale prompts | `git submodule update` + re-copy `prompts/` |

## 6. References

- [prompts/invoke.md](../prompts/invoke.md) — invoke phrases
- [prompts/README.md](../prompts/README.md) — prompt registry
- [conventions.md](conventions.md) — agent rules
