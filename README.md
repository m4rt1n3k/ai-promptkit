# ai-promptkit

Base prompts + dev culture for consumer projects. Submodule at `extern/ai-promptkit`; project prompts in `prompts/`.

**Repo:** [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## Setup (once)

```bash
mkdir -p extern
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
```

```text
Read extern/ai-promptkit/prompts/init.md and run on this workspace.
```

## Daily (after init on a consumer project)

```text
Run prompts/takeover.md
```

```text
Run prompts/handoff.md
```

Short forms: `run /prompts/takeover` · `run /prompts/handoff`. Those project files extend the base prompts in this repo.

## Docs

| Who | Read |
|-----|------|
| Human | [docs/manual.md](docs/manual.md) |
| Agent | [docs/conventions.md](docs/conventions.md) |
| Devlog | [docs/devlog.md](docs/devlog.md) |
| Prompts | [prompts/README.md](prompts/README.md) |

## Layouts

**Consumer** (after init) — see [init.md](prompts/init.md):

```text
<project>/
├── extern/ai-promptkit/
├── prompts/handoff.md    # daily end — extends base (init)
├── prompts/takeover.md   # daily start — extends base (init)
├── prompts/README.md
└── docs/
```

**This repo (upstream)** — no submodule, no extending handoff:

```text
ai-promptkit/
├── prompts/              # base prompts (handoff.md is the base, not a wrapper)
├── docs/
├── templates/            # seeds for init on consumer repos
└── tools/
```

Upstream handoff: `Run prompts/handoff.md` calls base steps directly.
