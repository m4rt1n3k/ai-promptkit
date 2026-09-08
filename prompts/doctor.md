# Doctor — read-only Spec Kit integration check

Invoke:

```text
Read extern/ai-promptkit/prompts/doctor.md and run on this workspace.
```

## Checks

1. `specify version` satisfies the source preset's `requires.speckit_version`.
2. `.specify/` and the selected native command/skill integration exist.
3. `constitution-template`, `spec-template` and `plan-template` resolve with `devl-spiral` and a native base, without composition warnings. Inspect the output, not just exit codes. The installed preset manifest and template contents match the expected submodule source; `--dev` installs a copy.
4. `extern/ai-promptkit` is registered, initialized and has no consumer-local edits. Report committed, staged and checked-out SHAs. The expected source is the committed SHA unless an explicitly authorized upgrade is pending; report that pending pin as WARN, and an unexplained mismatch as FAIL.
5. If `.specify/feature.json` exists, its active feature directory and native artifacts resolve.
6. Feature specifications using DEV|L contain a human maturity judgment, selected grade agent, initiation provenance or a direct human mandate, inherited evidence, real-world application target and evidence consumers. A field-chain feature identifies its data, computation, building output and collection needed for later backtesting; a scientific improvement identifies the component, baseline, accuracy and resource claims to verify. Apply these checks only to the relevant feature scope.
7. No ai-promptkit-created shadow delivery context exists outside `.specify/`, `specs/` and `extern/ai-promptkit/`; legitimate proposal, manuscript or exploitation outputs are stored in their declared authoritative systems.
8. Local Markdown links in the kit and active native feature resolve.

Report **Check | PASS/WARN/FAIL/N/A | Evidence | Exact remediation**, one overall status and one next lifecycle or native Spec Kit action.

Do not mutate files, initialize, fetch, upgrade, create context or commit.
