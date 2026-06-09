# Prompt registry

Invocable AI workflows for shared development culture. **Contract:** human header → `---` → copy-paste task body.

Copy `prompts/` into consumer repos or invoke via submodule path (see [`invoke.md`](invoke.md)).

## Session orchestration

| ID | File | Inputs | Outputs | When |
|----|------|--------|---------|------|
| `handoff` | [`handoff.md`](handoff.md) | Session context, `git status` | Devlog, commit draft, doc refresh, TODO | End of vibe session |
| `invoke` | [`invoke.md`](invoke.md) | Submodule path | — | Multi-workspace setup |

## Portable prompts

| ID | File | Inputs | Outputs | When |
|----|------|--------|---------|------|
| `session-summary` | [`session-summary.md`](session-summary.md) | Git diff, chat | Commit message draft | Before commit |
| `update-devlog` | [`update-devlog.md`](update-devlog.md) | Session summary | `docs/devlog.md` row | After session |
| `regenerate-docs` | [`regenerate-docs.md`](regenerate-docs.md) | Changed paths/CLI | README, manual, wiki | Structure change |
| `suggest-adr` | [`suggest-adr.md`](suggest-adr.md) | Design discussion | `docs/adr/NNNN-*.md` draft | Irreversible choice |
| `bootstrap-layout` | [`bootstrap-docs-prompts-layout.md`](bootstrap-docs-prompts-layout.md) | Target repo cwd | Full docs/prompts scaffold | New repo or redesign |
| `install-design-rule` | [`install-design-rule.md`](install-design-rule.md) | Target repo cwd | `.cursor/rules/design-discipline.mdc` | Once per repo |

## Related docs

- [`docs/manual.md`](../docs/manual.md) — human workflows
- [`docs/conventions.md`](../docs/conventions.md) — agent governance
