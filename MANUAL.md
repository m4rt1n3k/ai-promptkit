# MANUAL.md — ai-promptkit

## 0. Meta

- Purpose: Explain how humans use kit workers to keep project handoff files up to date.
- Audience: Developers and reviewers who run Cursor Agent in their own repos.
- Last updated: 2026-06-03
- Related: [PROMPT.md](./PROMPT.md) (agent context) · [TODO.md](./TODO.md) (plans)
- Repo: [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## 1. Overview

This file is the **human** guide for a target project. How **PROMPT.md**, **TODO.md**, and **MANUAL.md** fit together, the **two-pass** working cycle, and kit invoke phrases live in **[README.md](./README.md)** (*Handoff file ecosystem*).

- **Pass 1 (development):** README + PROMPT + TODO → develop → `kit_handoff` — see §4.1.  
- **Pass 2 (usage):** README + **this MANUAL** → follow procedures — see §4.0.

Here: step-by-step workflows, checks, and troubleshooting. Kits run from Agent chat in **your** workspace (pass 1); pass 2 usually needs no kit unless you are revising docs.

## 2. Prerequisites

- Cursor with Agent chat in the **target project** (the repo whose files should be updated).
- Local clone of ai-promptkit (path in README).
- Optional one-line hints in the same message: `session:`, `topics:`, `notes:`.

## 3. Roles and responsibilities

| Role | Can do | Cannot do / escalates to |
|------|--------|---------------------------|
| Developer in target repo | Run kits; review diffs to PROMPT/TODO/MANUAL | Expect kits to invent backlog or procedures you did not describe |
| Maintainer of ai-promptkit | Edit `kits/*.md` and templates | Kits do not auto-run; no in-repo dispatcher |

## 4. Core workflows

### 4.0 Usage pass (operators)

**When:** You use or maintain the project without a development session.  
**Who:** Operator, reviewer, anyone not coding this sprint.

1. Read [README.md](./README.md) (ecosystem, which pass you are in).
2. Read **MANUAL.md** (this file) and follow the relevant §4 workflow.
3. Done — no PROMPT/TODO required unless you hand off to development again.

### 4.1 End-of-session handoff — development pass (recommended)

Closes the **Update all** step in README *Pass 1 — Development iteration*.

**When:** You finish a meaningful development session and want the next agent (or teammate) to continue cleanly.  
**Who:** Developer in the target project.  
**Outcome:** Updated `TODO.md`, `PROMPT.md`, and `MANUAL.md` at the target repo root.

1. Open the **target project** in Cursor (not ai-promptkit unless you intend to update this repo).
2. In Agent chat, send:
   ```text
   from workspace ai-promptkit run kit_handoff
   ```
3. Optionally add context on the same message, for example:
   ```text
   session: feature-x-wrapup
   topics: api, auth
   notes: decided JWT; login still flaky on Safari
   ```
4. Review the three files. Confirm TODO items match what **you** asked for; confirm MANUAL steps match real workflows you described.
5. Commit when ready (kits do not commit for you).

**Checks:** `PROMPT.md` §9 has the structure paragraph + one table (local ISO times, no offset in cells); `TODO.md` active track matches your intent.

### 4.2 Update only agent handoff (PROMPT)

**When:** You need agent context refreshed but not a full handoff.  
**Who:** Developer in the target project.

1. In Agent chat:
   ```text
   from workspace ai-promptkit run kit_prompt
   ```
2. Review `PROMPT.md` only.

### 4.3 Update only plans (TODO)

**When:** You stated new or changed tasks and want `TODO.md` aligned.  
**Who:** Developer in the target project.

1. In Agent chat:
   ```text
   from workspace ai-promptkit run kit_todo
   ```
2. State tasks explicitly in chat; the kit must not invent pipeline items.
3. Review `TODO.md` only.

### 4.4 Update only human documentation (MANUAL)

**When:** You described workflows, roles, or operator steps and want them written for people.  
**Who:** Developer or doc owner in the target project.

1. In Agent chat:
   ```text
   from workspace ai-promptkit run kit_manual
   ```
2. Describe procedures in chat (who does what, in what order).
3. Review `MANUAL.md`; merge edits if you already had a custom structure.

### 4.5 Apply design discipline rule on a project

**When:** You want agents on a repo to prefer minimal, stated-scope changes.  
**Who:** Developer in the target project.

1. In Agent chat:
   ```text
   from workspace ai-promptkit run kit_design
   ```
2. Confirm `.cursor/rules/kit-design.mdc` exists on the target repo.

### 4.6 Handoff on ai-promptkit itself

**When:** You changed kits/templates in this repo and want this repo’s handoff files updated.  
**Who:** Maintainer.

1. Say explicitly that the target is **this** repo (e.g. `run kit_handoff on yourself` or work with ai-promptkit as the opened workspace).
2. Run `kit_handoff` as in §4.1.

## 5. Routine operations

- **New target repo:** First handoff creates `PROMPT.md`, `TODO.md`, and `MANUAL.md` from templates under `kits/templates/`.
- **Templates location:** [kits/templates/](kits/templates/) in ai-promptkit.
- **Kit source of truth:** [kits/](kits/) — one markdown file per kit command.

## 6. Administration

- Keep ai-promptkit clone updated (`git pull`) if kits change on GitHub.
- Do not put secrets in PROMPT, TODO, or MANUAL files.
- `kit_todo` and `kit_manual` follow the same rule: only document what the user stated unless they ask for broader drafts.

## 7. Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Files updated in ai-promptkit instead of my app | Target workspace was ai-promptkit | Open your app repo; re-run kit; or say “on yourself” only when intentional |
| TODO filled with tasks I never mentioned | Agent invented backlog | Re-run `kit_todo`; restate tasks; edit TODO |
| MANUAL reads like agent instructions | Wrong tone or copied PROMPT | Re-run `kit_manual`; describe steps for a human operator |
| No MANUAL.md after handoff | Old session before `kit_manual` | Run `kit_handoff` or `kit_manual` once |

## 8. Glossary

| Term | Meaning |
|------|---------|
| Kit | Worker spec in `kits/kit_*.md` invoked by phrase from another workspace |
| Handoff | `kit_handoff` — updates TODO, PROMPT, and MANUAL together |
| Active track | Single current plan row in `TODO.md` |

## 9. References

- [README.md](./README.md) — PROMPT · TODO · MANUAL ecosystem, working cycle, invoke phrases, kit table
- [kits/kit_handoff.md](kits/kit_handoff.md) — orchestration order

## 10. Changelog (append-only)

| Date | Topics | Session | Summary |
|------|--------|---------|---------|
| 2026-06-03 | `kit_manual`, `MANUAL.md` | `add-kit-manual` | Added kit_manual; wired into kit_handoff; seeded this manual. |
| 2026-06-03 | `readme`, `ecosystem` | `move-ecosystem-readme` | PROMPT·TODO·MANUAL ecosystem + cycle diagram moved to README; MANUAL = procedures only. |
| 2026-06-03 | `working-cycle` | `two-pass` | README: pass 1 development iteration, pass 2 usage; MANUAL §4.0 usage pass. |
| 2026-06-03 | `mermaid`, `kit_manual` | `manual-mermaid-kit` | kit_manual diagram rules; §1.1 loop schematic restored. |
