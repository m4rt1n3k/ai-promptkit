# Init — onboard project

After submodule add. Prerequisite:

```bash
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git subs/ai-promptkit
```

Invoke:

```text
Read subs/ai-promptkit/prompts/init.md and run on this workspace.
```

---

## Task: Initialize layout

Consumer project (cwd = repo root). Goal: `prompts/handoff.md` works; docs scaffold exists.

### Target layout (consumer)

```text
<project>/
├── subs/ai-promptkit/       # submodule — base prompts (read-only)
├── prompts/
│   ├── README.md            # project prompt registry
│   ├── handoff.md           # extends base — required
│   ├── <name>.md            # optional local prompts
│   └── <domain>/<name>.md   # optional grouped prompts
├── docs/
│   ├── README.md
│   ├── manual.md            # project ops + link to kit manual
│   ├── conventions.md
│   ├── devlog.md
│   └── adr/README.md
├── TODO.md
└── README.md
```

**Not** part of consumer layout: `templates/`, `tools/` (stay in submodule unless copied).

### 1. Verify submodule

`subs/ai-promptkit/prompts/handoff.md` must exist. Else stop — user runs submodule command above.

### 2. Discover

Report: **empty** | **partial** | **legacy** | **initialized**.

Check against target layout. Legacy: `PROMPT.md`, `MANUAL.md`, `kits/`, `vendor/ai-promptkit`.

### 3. Scaffold

**Empty/partial:** create missing files from `subs/ai-promptkit/templates/`:

- `docs/README.md`, `docs/devlog.md`, `docs/conventions.md`, `docs/adr/README.md`
- `docs/manual.md` — brief project ops + link to `subs/ai-promptkit/docs/manual.md`
- `prompts/README.md` (from `project-prompts-README.md`, set project name)
- `TODO.md` (from `todo.md` if missing)

**Legacy:** list moves; **ask user before reorganizing**:

| From | To |
|------|-----|
| `MANUAL.md` | `docs/manual.md` |
| `PROMPT.md` rules | `docs/conventions.md` |
| `PROMPT.md` log | `docs/devlog.md` |
| `vendor/ai-promptkit` | `subs/ai-promptkit` |
| `kits/` | `prompts/handoff.md` |

Stub old paths one release if moved. Do not bulk-copy base prompts into `prompts/`.

**Initialized:** repair gaps only.

### 4. Create `prompts/handoff.md`

From `subs/ai-promptkit/templates/handoff-extend.md` if missing or not delegating to base:

- Steps 1–5 → `subs/ai-promptkit/prompts/handoff.md`
- Empty **Project steps** placeholder

Daily invoke: `Run prompts/handoff.md — end of session handoff.`

### 5. README

Add submodule path + handoff invoke phrase to project `README.md`.

Offer design rule (`install-design-rule.md`) only if user agrees.

### Constraints

- Write to consumer repo only, not `subs/ai-promptkit`.
- No commit unless asked. No invented TODOs or workflows.
- Reorganization needs explicit approval.

### Output

1. State (empty/partial/legacy/initialized)
2. Created / migrated / skipped (vs target layout)
3. Handoff invoke phrase
4. Commit message draft if changed
