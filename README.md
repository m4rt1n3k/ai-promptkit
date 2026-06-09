# ai-promptkit

Base prompts + dev culture for consumer projects. Submodule at `subs/ai-promptkit`; project prompts in `prompts/`.

**Repo:** [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## Setup (once)

```bash
mkdir -p subs
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git subs/ai-promptkit
```

```text
Read subs/ai-promptkit/prompts/init.md and run on this workspace.
```

## Daily

```text
Run prompts/handoff.md — end of session handoff.
```

## Docs

| Who | Read |
|-----|------|
| Human | [docs/manual.md](docs/manual.md) |
| Agent | [docs/conventions.md](docs/conventions.md) |
| Prompts | [prompts/README.md](prompts/README.md) |

## Layouts

**Consumer** (after init) — see [init.md](prompts/init.md):

```text
<project>/
├── subs/ai-promptkit/
├── prompts/handoff.md    # extends base — created by init
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
