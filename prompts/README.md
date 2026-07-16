# Base prompts

Shipped at `extern/ai-promptkit/prompts/` on consumer repos. Project prompts live in `<project>/prompts/`.

**Onboard:** [init.md](init.md) · **Consumer daily:** `prompts/takeover.md` + `prompts/handoff.md` · **Guide:** [docs/manual.md](../docs/manual.md)

| ID | File | When |
|----|------|------|
| `init` | [init.md](init.md) | Once after submodule add — creates project `prompts/handoff.md` + `prompts/takeover.md` |
| `takeover` | [takeover.md](takeover.md) | Base start-of-session (consumers extend via `prompts/takeover.md`) |
| `handoff` | [handoff.md](handoff.md) | Base end-of-session (consumers extend via `prompts/handoff.md`) |
| `session-summary` | [session-summary.md](session-summary.md) | Commit message draft |
| `update-devlog` | [update-devlog.md](update-devlog.md) | Append devlog row |
| `regenerate-docs` | [regenerate-docs.md](regenerate-docs.md) | After layout/CLI change |
| `sync-pyproject` | [sync-pyproject.md](sync-pyproject.md) | Python `pyproject.toml` create/update |
| `suggest-adr` | [suggest-adr.md](suggest-adr.md) | Irreversible design choice |
| `install-design-rule` | [install-design-rule.md](install-design-rule.md) | Once per repo |
