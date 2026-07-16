# Manual

## Onboarding (once per project)

| Step | Action |
|------|--------|
| 1 | Add submodule (terminal) |
| 2 | Run `init.md` (agent) |
| 3 | Use daily `prompts/handoff.md` + `prompts/takeover.md` (created by init) |

### Step 1 — Submodule

```bash
mkdir -p extern
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
git submodule update --init --recursive
```

### Step 2 — Init

```text
Read extern/ai-promptkit/prompts/init.md and run on this workspace.
```

Creates `docs/`, `prompts/README.md`, and daily wrappers **`prompts/handoff.md`** + **`prompts/takeover.md`** (extend base prompts). Empty repo → scaffold. Existing repo → **asks before reorganizing**.

### Step 3 — Daily routines

Start of a new chat (especially a new area):

```text
Run prompts/takeover.md
```

End of session:

```text
Run prompts/handoff.md
```

Short forms: `run /prompts/takeover` · `run /prompts/handoff`. Add project-specific steps later under **Project steps** in each wrapper.

### Python projects

After init, consumer repos with Python code get `pyproject.toml` via init step 5 / handoff step 3b ([sync-pyproject.md](../prompts/sync-pyproject.md)). The ai-promptkit kit repo itself does not ship one.

## Session rhythm (handoff → takeover)

| Phase | Chat | Action |
|-------|------|--------|
| End session | Current (work) chat | Run handoff — persist devlog, TODO, commit draft |
| Start session | **New** chat | Run takeover — refresh `extern/ai-promptkit`, deep read, debrief, then code |

1. **Work** in the current chat; at session end: `Run prompts/handoff.md`.
2. **Next session** — especially on a different part of the codebase — open a **new chat** and `Run prompts/takeover.md` before implementing (takeover runs `git submodule update --init --recursive --remote` first).
3. Takeover is read-only exploration (except submodule refresh); after the debrief, continue development in that same chat.
4. Optional scope: append `Focus on <path or module>.` to the takeover invoke.

First time on an existing app repo: run `init.md` once, then `Run prompts/takeover.md` in a new chat before feature work.

## Submodule update

Normally done **inside takeover** (step 0b). Manual / troubleshooting from the consumer repo root:

```bash
git submodule update --init --recursive --remote
```

Commit the new submodule pointer only when you want the team pin updated.

## Layout

```text
<project>/
├── extern/ai-promptkit/       # base prompts — do not edit
├── prompts/
│   ├── handoff.md           # daily end — extends base (required)
│   ├── takeover.md          # daily start — extends base (required)
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
| `extern/ai-promptkit/` | yes | no — this **is** the kit |
| `prompts/handoff.md` | extends base (from template) | **is** the base handoff |
| `prompts/takeover.md` | extends base (from template) | **is** the base takeover |
| `prompts/README.md` | project registry | base prompt catalog |
| `templates/`, `tools/` | in submodule only | yes, ships here |

## Invoke phrases

| Task | Phrase |
|------|--------|
| Init | `Read extern/ai-promptkit/prompts/init.md and run on this workspace.` |
| Takeover (daily) | `Run prompts/takeover.md` (`run /prompts/takeover`) |
| Handoff (daily) | `Run prompts/handoff.md` (`run /prompts/handoff`) |
| Takeover (base only) | `Read extern/ai-promptkit/prompts/takeover.md and run on this workspace.` |
| Sync pyproject | `Read extern/ai-promptkit/prompts/sync-pyproject.md and run on this workspace.` |
| Design rule | `Read extern/ai-promptkit/prompts/install-design-rule.md and run on this workspace.` |
| Base handoff only | `Read extern/ai-promptkit/prompts/handoff.md and execute on this workspace.` |

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| No `prompts/handoff.md` or `prompts/takeover.md` | Run init |
| Handoff targets wrong repo | Open consumer project; say "this workspace" |
| Submodule empty | `git submodule update --init --recursive --remote` |

## References

- [prompts/init.md](../prompts/init.md)
- [prompts/takeover.md](../prompts/takeover.md)
- [prompts/README.md](../prompts/README.md)
- [conventions.md](conventions.md)
