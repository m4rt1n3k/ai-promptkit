# TODO.md — plans and pipeline

## 0. Meta

- Last updated: 2026-06-02
- Context: [PROMPT.md](./PROMPT.md)
- Legend: see below

## Legend

### Severity

| Tag | Meaning |
|-----|---------|
| **must-have** | Required for current milestone / blocking |
| **nice-to-have** | Valuable but deferrable without breaking milestone |

### Time priority

| Tag | Meaning |
|-----|---------|
| **now** | Do in current session or before next handoff |
| **next** | Immediately after active track |
| **soon** | This week / current sprint |
| **later** | No fixed date; backlog |
| **by:YYYY-MM-DD** | Hard target (use explicit date when known) |

### Status

`idea` → `mind-branch` → `planned` → `in-progress` → `blocked` → `done` → `dropped`

- **mind-branch** — exploratory path; may merge into a plan or be dropped without guilt.

---

## Active track

| ID | Title | Severity | Time | Status | Notes |
|----|-------|----------|------|--------|-------|
| _none_ | — | — | — | — | Set next plan-id on handoff |

---

## Pipeline (committed plans)

| ID | Title | Severity | Time | Status | Depends | PROMPT topics |
|----|-------|----------|------|--------|---------|---------------|
| plan-5 | Roll out to asset-ontology | nice-to-have | soon | planned | plan-4 | `ontology` |
| plan-6 | Roll out to em-testbench | nice-to-have | later | planned | plan-5 | `em-testbench` |

---

## Mind-branches (exploratory, in pipeline)

| ID | Title | Severity | Time | Status | Parent / related | Hypothesis |
|----|-------|----------|------|--------|------------------|------------|
| branch-yaml-frontmatter | YAML front-matter on PROMPT/TODO | nice-to-have | later | mind-branch | plan-4 | Enables tooling (`active_track:`) without parsing markdown tables |
| branch-pr-checklist | PR checklist for handoff files | nice-to-have | later | mind-branch | plan-4 | CI or template reminds updates on constraint changes |
| branch-vibecoding-docs | ProGrammar vibecoding playbooks in this folder | nice-to-have | later | mind-branch | — | Team-specific guides alongside handoff kit |

---

## Done / dropped (archive)

| ID | Title | Closed | Outcome |
|----|-------|--------|---------|
| plan-1 | Scaffold PROMPT.md and TODO.md | 2026-06-02 | Templates at repo root |
| plan-2 | Create Cursor Automation prefill | 2026-06-02 | `automations/export-handoff-prefill.json` + README |
| plan-3 | Bootstrap cursor rule | 2026-06-02 | `.cursor/rules/agent-handoff-bootstrap.mdc` |
| plan-4 | First handoff export + cold-start verify | 2026-06-02 | `docs/COLD-START-VERIFY.md`; PROMPT/TODO populated |
| plan-7 | Migrate kit to AI vibecoding workspace | 2026-06-02 | SharePoint folder; superseded by plan-8 (D6) |
| plan-8 | Canonical home in ai-promptkit git repo | 2026-06-02 | `github.com/m4rt1n3k/ai-promptkit`; PROMPT §5 + README updated |

---

## Session index

| Session label | Date | TODO IDs touched | PROMPT log row |
|---------------|------|------------------|----------------|
| plan-prompt-todo | 2026-06-02 | — | 2026-06-02 (planning) |
| implement-plan | 2026-06-02 | plan-1, plan-2, plan-3, plan-4 | 2026-06-02 (implementation) |
| move-to-ai-vibecoding | 2026-06-02 | plan-7 | 2026-06-02 (migration) |
| canonical-git-home | 2026-06-02 | plan-8 | 2026-06-02 (repo-placement) |
