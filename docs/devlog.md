# Devlog

Append-only session log. **Newest row first.** Format rules: [`prompts/update-devlog.md`](../prompts/update-devlog.md).

| Interval | Topics | Summary | Author | Refs |
|----------|--------|---------|--------|------|
| 2026-06-09 12:00:00<br/>2026-06-09 12:30:00 | `rebuild`, `prompts`, `submodule` | Replaced kits/ with prompts/_shared layout; docs/ + submodule invoke model. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
| 2026-06-03 08:52:00<br/>2026-06-03 09:03:05 | `kit_prompt`, `interval-format` | Interval format `YYYY-MM-DD HH:MM:SS`; require precise seconds when available. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-06-02 16:09:27<br/>2026-06-02 16:45:56 | `kit-workers`, `simplify` | IDE-only invoke; stripped dispatcher, cold-start, automations. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
