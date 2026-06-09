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
| Handoff | `Run prompts/handoff.md — end of session handoff.` |
| Design rule | `Read subs/ai-promptkit/prompts/install-design-rule.md and run on this workspace.` |
| Base handoff only | `Read subs/ai-promptkit/prompts/handoff.md and execute on this workspace.` |

## Submodule update

```bash
git submodule update --remote subs/ai-promptkit
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| No `prompts/handoff.md` | Run init |
| Handoff targets wrong repo | Open consumer project; say "this workspace" |
| Submodule empty | `git submodule update --init subs/ai-promptkit` |

## References

- [prompts/init.md](../prompts/init.md)
- [prompts/README.md](../prompts/README.md)
- [conventions.md](conventions.md)
