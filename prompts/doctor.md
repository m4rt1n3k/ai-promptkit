# Doctor — read-only Spec Kit integration check

Invoke:

```text
Read extern/ai-promptkit/prompts/doctor.md and run on this workspace.
```

## Checks

1. `specify version` succeeds.
2. `.specify/` and the selected native command/skill integration exist.
3. `constitution-template`, `spec-template` and `plan-template` resolve with `devl-spiral` while retaining native content.
4. `extern/ai-promptkit` is a registered, initialized submodule at its committed SHA with no consumer-local edits.
5. If `.specify/feature.json` exists, its active feature directory and native artifacts resolve.
6. Feature specifications using DEV|L contain a human maturity judgment, selected grade agent, initiation provenance, inherited evidence, real-world application target and evidence consumers.
7. No ai-promptkit-created shadow delivery context exists outside `.specify/`, `specs/` and `extern/ai-promptkit/`; legitimate proposal, manuscript or exploitation outputs are stored in their declared authoritative systems.
8. Local Markdown links in the kit and active native feature resolve.

Report **Check | PASS/WARN/FAIL/N/A | Evidence | Exact remediation**, one overall status and one next lifecycle or native Spec Kit action.

Do not mutate files, initialize, fetch, upgrade, create context or commit.
