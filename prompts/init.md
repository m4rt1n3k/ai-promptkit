# Init — onboard project

After submodule add. Prerequisite:

```bash
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
```

Invoke:

```text
Read extern/ai-promptkit/prompts/init.md and run on this workspace.
```

---

## Task: Initialize layout

Consumer project (cwd = repo root). Goal: **daily routines** live in project `prompts/` so the user can run:

```text
Run prompts/handoff.md
```

```text
Run prompts/takeover.md
```

Short forms: `run /prompts/handoff` · `run /prompts/takeover`.

Those files **extend** base prompts under `extern/ai-promptkit/prompts/` (do not copy the whole base catalog into `prompts/`).

### Target layout (consumer)

```text
<project>/
├── extern/ai-promptkit/       # submodule — base prompts (read-only)
├── prompts/
│   ├── README.md            # project prompt registry
│   ├── handoff.md           # daily end — extends base (required)
│   ├── takeover.md          # daily start — extends base (required)
│   ├── <name>.md            # optional local prompts
│   └── <domain>/<name>.md   # optional grouped prompts
├── docs/
│   ├── README.md
│   ├── manual.md            # project ops + link to kit manual
│   ├── conventions.md
│   ├── devlog.md
│   └── adr/README.md
├── TODO.md
├── README.md
└── pyproject.toml           # Python projects only — see sync-pyproject.md
```

**Not** part of consumer layout: `templates/`, `tools/` (stay in submodule unless copied). **Not** in ai-promptkit upstream (this kit repo stays prompts-only).

### 1. Verify submodule

`extern/ai-promptkit/prompts/handoff.md` and `extern/ai-promptkit/prompts/takeover.md` must exist. Else stop — user runs submodule command above.

### 2. Discover

Report: **empty** | **partial** | **legacy** | **initialized**.

Check against target layout. Legacy: `PROMPT.md`, `MANUAL.md`, `kits/`, `vendor/ai-promptkit`, `subs/ai-promptkit`.

### 3. Scaffold

**Empty/partial:** create missing files from `extern/ai-promptkit/templates/`:

- `docs/README.md`, `docs/devlog.md`, `docs/conventions.md`, `docs/adr/README.md`
- `docs/manual.md` — brief project ops + link to `extern/ai-promptkit/docs/manual.md`
- `prompts/README.md` (from `project-prompts-README.md`, set project name)
- `TODO.md` (from `todo.md` if missing)

**Legacy:** list moves; **ask user before reorganizing**:

| From | To |
|------|-----|
| `MANUAL.md` | `docs/manual.md` |
| `PROMPT.md` rules | `docs/conventions.md` |
| `PROMPT.md` log | `docs/devlog.md` |
| `vendor/ai-promptkit` | `extern/ai-promptkit` |
| `subs/ai-promptkit` | `extern/ai-promptkit` |
| `kits/` | `prompts/handoff.md` + `prompts/takeover.md` |

Stub old paths one release if moved. Do not bulk-copy base prompts into `prompts/`.

**Initialized:** repair gaps only.

### 4. Create daily routines in `prompts/`

Create or repair **both** wrappers so daily work never requires typing the submodule path:

| Project file | Template | Extends |
|--------------|----------|---------|
| `prompts/handoff.md` | `templates/handoff-extend.md` | `extern/ai-promptkit/prompts/handoff.md` |
| `prompts/takeover.md` | `templates/takeover-extend.md` | `extern/ai-promptkit/prompts/takeover.md` |

For each file:

1. If missing, or present but **not** delegating to the base prompt above → write from the matching template.
2. Replace `<project-name>` with the consumer repo name.
3. Keep an empty **Project steps** section for later local customization.
4. Do **not** overwrite a customized wrapper that already correctly extends the base — only fill gaps / fix broken invoke lines.

**Daily invoke (document in README + `prompts/README.md`):**

```text
Run prompts/handoff.md
```

```text
Run prompts/takeover.md
```

Also accept short forms: `run /prompts/handoff` · `run /prompts/takeover`.

Rhythm: **takeover** at start of a new chat (especially a new area) → work → **handoff** at end of session.

### 5. Python — pyproject.toml

If the consumer repo uses Python (`.py` files, `requirements*.txt`, or planned package layout): follow [sync-pyproject.md](sync-pyproject.md) to create or refresh `pyproject.toml`. Skip for non-Python repos.

### 6. README

Add to project `README.md`:

- Submodule path: `extern/ai-promptkit`
- Daily phrases: `Run prompts/handoff.md` and `Run prompts/takeover.md` (short forms optional)

Offer design rule (`install-design-rule.md`) only if user agrees. On existing app repos (not empty), remind: after init, open a **new chat** and `Run prompts/takeover.md` before feature work.

### Constraints

- Write to consumer repo only, not `extern/ai-promptkit`.
- No commit unless asked. No invented TODOs or workflows.
- Reorganization needs explicit approval.
- Daily wrappers only — do not copy all base prompts into `prompts/`.

### Output

1. State (empty/partial/legacy/initialized)
2. Created / migrated / skipped (vs target layout)
3. Daily routines: `prompts/handoff.md` + `prompts/takeover.md` — created / repaired / left as-is
4. `pyproject.toml` — created / updated / skipped (Python only)
5. Invoke phrases to paste into project README
6. Commit message draft if changed
