# Base prompts

Shipped at `subs/ai-promptkit/prompts/` on consumer repos. Project prompts live in `<project>/prompts/`.

**Onboard:** [init.md](init.md) · **Start session:** [takeover.md](takeover.md) · **End session:** `prompts/handoff.md` on consumer · **Guide:** [docs/manual.md](../docs/manual.md)

| ID | File | When |
|----|------|------|
| `init` | [init.md](init.md) | Once after submodule add |
| `takeover` | [takeover.md](takeover.md) | Start of new chat — before coding on existing or new area |
| `handoff` | [handoff.md](handoff.md) | End of session (base steps 1–5) |
| `session-summary` | [session-summary.md](session-summary.md) | Commit message draft |
| `update-devlog` | [update-devlog.md](update-devlog.md) | Append devlog row |
| `regenerate-docs` | [regenerate-docs.md](regenerate-docs.md) | After layout/CLI change |
| `sync-pyproject` | [sync-pyproject.md](sync-pyproject.md) | Python `pyproject.toml` create/update |
| `suggest-adr` | [suggest-adr.md](suggest-adr.md) | Irreversible design choice |
| `install-design-rule` | [install-design-rule.md](install-design-rule.md) | Once per repo |
