# Manual

## Onboarding (once per project)

| Step | Action |
|------|--------|
| 1 | Add submodule (terminal) |
| 2 | Run `init.md` (agent) |
| 3 | Use `prompts/handoff.md` (created by init) |

### Step 1 — Submodule

```bash
mkdir -p subs
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git subs/ai-promptkit
git submodule update --init --recursive
```

### Step 2 — Init

```text
Read subs/ai-promptkit/prompts/init.md and run on this workspace.
```

Creates `docs/`, `prompts/README.md`, and **`prompts/handoff.md`** (extends base handoff). Empty repo → scaffold. Existing repo → **asks before reorganizing**.

### Step 3 — Handoff

```text
Run prompts/handoff.md — end of session handoff.
```

Add project steps later under **Project steps** in `prompts/handoff.md`.

### Python projects

After init, consumer repos with Python code get `pyproject.toml` via init step 5 / handoff step 3b ([sync-pyproject.md](../prompts/sync-pyproject.md)). The ai-promptkit kit repo itself does not ship one.

## Session rhythm (handoff → takeover)

| Phase | Chat | Action |
|-------|------|--------|
| End session | Current (work) chat | Run handoff — persist devlog, TODO, commit draft |
| Start session | **New** chat | Run takeover — deep read, debrief, then code |

1. **Work** in the current chat; at session end run handoff (consumer: `prompts/handoff.md`).
2. **Next session** — especially on a different part of the codebase — open a **new chat** and run takeover before implementing.
3. Takeover is read-only exploration; after the debrief, continue development in that same chat.
4. Optional scope: append `Focus on <path or module>.` to the takeover invoke phrase.

### Takeover invoke

```text
Read subs/ai-promptkit/prompts/takeover.md and run on this workspace.
```

First time on an existing app repo: run `init.md` once, then `takeover.md` in a new chat before feature work.

## Layout

```text
<project>/
├── subs/ai-promptkit/       # base prompts — do not edit
├── prompts/
│   ├── handoff.md           # extend base (required after init)
│   ├── <name>.md            # local prompt
│   └── <domain>/<name>.md   # grouped prompts (only if many related)
├── docs/
└── TODO.md
```

Base prompts stay in the submodule. Project prompts stay in `prompts/`.

This matches [init.md](../prompts/init.md) target layout.

### Upstream vs consumer

| | Consumer project | ai-promptkit (this repo) |
|--|------------------|--------------------------|
| `subs/ai-promptkit/` | yes | no — this **is** the kit |
| `prompts/handoff.md` | extends base (from template) | **is** the base handoff |
| `prompts/README.md` | project registry | base prompt catalog |
| `templates/`, `tools/` | in submodule only | yes, ships here |

## Invoke phrases

| Task | Phrase |
|------|--------|
| Init | `Read subs/ai-promptkit/prompts/init.md and run on this workspace.` |
| Takeover | `Read subs/ai-promptkit/prompts/takeover.md and run on this workspace.` |
| Handoff | `Run prompts/handoff.md — end of session handoff.` |
| Sync pyproject | `Read subs/ai-promptkit/prompts/sync-pyproject.md and run on this workspace.` |
| Design rule | `Read subs/ai-promptkit/prompts/install-design-rule.md and run on this workspace.` |
| Base handoff only | `Read subs/ai-promptkit/prompts/handoff.md and execute on this workspace.` |

## Submodule update

Pull latest base prompts from the remote tracking branch (`main`). Initializes the submodule if missing; use from the consumer repo root:

```bash
git submodule update --init --recursive --remote
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| No `prompts/handoff.md` | Run init |
| Handoff targets wrong repo | Open consumer project; say "this workspace" |
| Submodule empty | `git submodule update --init --recursive --remote` |

## References

- [prompts/init.md](../prompts/init.md)
- [prompts/takeover.md](../prompts/takeover.md)
- [prompts/README.md](../prompts/README.md)
- [conventions.md](conventions.md)
