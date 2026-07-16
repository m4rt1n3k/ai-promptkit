# Devlog

Newest first. Format: [update-devlog.md](../prompts/update-devlog.md).

| Interval | Topics | Summary | Author | Refs |
|----------|--------|---------|--------|------|
| 2026-07-16 17:32:00<br/>2026-07-16 17:33:20 | `takeover`, `submodule` | Takeover step 0b: `git submodule update --init --recursive --remote` before explore; debrief reports status. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-07-16 17:24:00<br/>2026-07-16 17:25:51 | `init`, `handoff`, `takeover` | Init creates daily `prompts/handoff.md` + `prompts/takeover.md` wrappers; invoke `Run prompts/…` / `run /prompts/…`. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-07-16 16:59:00<br/>2026-07-16 17:00:55 | `extern`, `submodule` | Submodule path `subs/` → `extern/`; docs, prompts, templates, wiki skip-dir updated. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-06-22 10:00:00<br/>2026-06-22 10:40:47 | `sync-pyproject`, `handoff`, `init` | sync-pyproject prompt, handoff step 3b + init integration; upstream pyproject-free; init/handoff verified on kit repo. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-06-10 11:45:00<br/>2026-06-10 12:13:57 | `session-summary`, `handoff`, `teams` | session-summary - topic-detail format, Teams note; handoff step 1 updated. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-06-09 12:00:00<br/>2026-06-09 17:31:15 | `handoff`, `init`, `simplify`, `subs` | Rebuilt as minimal prompts/ + docs/; init.md onboarding; subs/ dual layout; removed kits, bootstrap, invoke. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
| 2026-06-09 12:00:00<br/>2026-06-09 12:30:00 | `rebuild`, `prompts`, `submodule` | Replaced kits/ with prompts/_shared layout; docs/ + submodule invoke model. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
| 2026-06-03 08:52:00<br/>2026-06-03 09:03:05 | `kit_prompt`, `interval-format` | Interval format `YYYY-MM-DD HH:MM:SS`; require precise seconds when available. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | — |
| 2026-06-02 16:09:27<br/>2026-06-02 16:45:56 | `kit-workers`, `simplify` | IDE-only invoke; stripped dispatcher, cold-start, automations. | Vladislav Martinek [human]<br/>Cursor Agent [ai] | [ADR-0001](adr/0001-prompts-over-kits.md) |
