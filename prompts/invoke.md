# Invoke prompts from another workspace

How to run ai-promptkit prompts when the **opened project** is not ai-promptkit itself.

## Submodule layout (recommended)

Add ai-promptkit as a git submodule in the consumer repo:

```bash
git submodule add https://github.com/m4rt1n3k/ai-promptkit vendor/ai-promptkit
```

Typical paths:

```text
<your-repo>/
├── vendor/ai-promptkit/     # submodule (read-only upstream)
└── prompts/                 # copy from vendor/ai-promptkit/prompts/
```

**Sync prompts** after submodule update:

```bash
cp -r vendor/ai-promptkit/prompts .
```

On Windows (PowerShell):

```powershell
Copy-Item -Recurse -Force vendor\ai-promptkit\prompts .
```

## Cursor Agent phrases

Open **your project** in Cursor. In Agent chat:

### Full handoff

```text
Read vendor/ai-promptkit/prompts/handoff.md and execute it on this workspace.
```

Or if prompts were copied locally:

```text
Run prompts/handoff.md — end of session handoff.
```

### Single prompt

```text
Read vendor/ai-promptkit/prompts/update-devlog.md and run it on this workspace.
```

### Bootstrap a new repo

```text
Read vendor/ai-promptkit/prompts/bootstrap-docs-prompts-layout.md and run it on this workspace.
```

### Design discipline rule

```text
Read vendor/ai-promptkit/prompts/install-design-rule.md and run it on this workspace.
```

## Rules

- **Write target** = opened workspace root, not ai-promptkit (unless user says "on ai-promptkit itself").
- Submodule stays **read-only** — edit prompts on the consumer repo, or propose changes upstream.
- First-time setup: run [`bootstrap-docs-prompts-layout.md`](bootstrap-docs-prompts-layout.md) once.
