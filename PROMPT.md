# PROMPT.md — agent handoff

## 0. Meta

- Purpose: Maintain distilled agent memory and session continuity when switching LLMs or starting fresh chats.
- Audience: coding agent / reviewer
- Last updated: 2026-06-02
- Active track: none (see [TODO.md](./TODO.md); run handoff to set next plan-id)
- Companion: [TODO.md](./TODO.md)
- Repo: **ai-promptkit** — ProGrammar team handoff kit ([github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)); evolved from `agent-handoff` and SharePoint **AI vibecoding**

## 1. Mission

Provide a **repeatable handoff system** in this workspace: repo-root **`PROMPT.md`** (truth, constraints, current state, tagged log) and **`TODO.md`** (prioritized plans and mind-branches). A new agent with zero chat history can continue work using only these files, the repo, and `.cursor/rules`.

**Definition of done (this repo):** Handoff kit present; bootstrap rule active; automation prefill documented; **ai-promptkit** is the canonical git home for the PROMPT/TODO pattern (reference kit + team docs).

## 2. Hard constraints (must not violate)

1. **Distill, do not archive** — `PROMPT.md` is not a chat transcript.
2. **Canonical filename** — always `PROMPT.md` (capitals) for new work.
3. **Split memory from backlog** — near-term actions in PROMPT §6; multi-track work in `TODO.md`.
4. **Append-only log** — section 9 rows are appended, not rewritten per message.
5. **No secrets** in either file.
6. **Do not duplicate** full `.cursor/rules` text — reference paths only.
7. **Do not edit** the Cursor plan file at `~/.cursor/plans/conversation_handoff_prompt.md_4122d518.plan.md`.

## 3. User inputs (verbatim where it matters)

- [binding] Store conversation extract for LLM switch: **what** and **how**, important things, hierarchical — so a different agent can repeat work from scratch.
- [binding] Use **`PROMPT.md`** (capitals); keep **`TODO.md`** beside it for structured plans and **mind-branches** in the pipeline.
- [binding] Tag conversation log with **session/chat topics**; tag TODO items with **must-have** / **nice-to-have** and **time-related prioritization** (`now`, `next`, `soon`, `later`, `by:YYYY-MM-DD`).
- [binding] Canonical home is the **ai-promptkit** git repo (was agent-handoff, then SharePoint AI vibecoding).
- [preference] Meta-prompt suitable for **Cursor Automations**; explicit trigger (handoff / export) because scheduled runs may lack chat context unless notes are provided.

## 4. Decisions made

| ID | Decision | Why | Alternatives rejected |
|----|----------|-----|------------------------|
| D1 | Two-file split: `PROMPT.md` + `TODO.md` | Separates durable truth from prioritized backlog | Single combined file (too noisy) |
| D2 | Log columns: Date, Topics, Session, Summary | Topics vs session disambiguates threads | Untagged date-only log |
| D3 | TODO severity: must-have \| nice-to-have | Clear milestone blocking | Priority P0/P1 only |
| D4 | TODO time: now \| next \| soon \| later \| by:date | Time prioritization without over-planning | Due dates only |
| D5 | Canonical kit in **AI vibecoding** workspace (SharePoint) | Team docs folder; replaced standalone `agent-handoff` | Keep only `C:\Users\VLAD\agent-handoff` — **superseded 2026-06-02** by D6 |
| D6 | Canonical kit in **ai-promptkit** git repo | Versioned source of truth; GitHub + local clone under `HOME\CODE_m4rt1n3k` | SharePoint-only or unversioned folder |

## 5. Current state

- Branch: `main` @ `df25257` (tracks `origin/main`)
- Remote: `https://github.com/m4rt1n3k/ai-promptkit.git`
- Workspace (local): `C:\Users\VLAD\HOME\CODE_m4rt1n3k\ai-promptkit`
- Files: `PROMPT.md`, `TODO.md`, `README.md`, `PROMPT-TODO-handoff-plan.md` (full spec), `.cursor/rules/agent-handoff-bootstrap.mdc`, `automations/`, `docs/COLD-START-VERIFY.md`
- Works: Full handoff kit; git initialized; bootstrap rule applies in this repo
- Pending: User saves automation in Cursor UI if not done yet; roll out to other repos (TODO plan-5, plan-6)
- Historical locations: `C:\Users\VLAD\agent-handoff`; SharePoint `Team-ProGrammar - Dokumenty\AI vibecoding` (may lag git — treat this repo as canonical)
- Open questions: Which target repos adopt first (asset-ontology, em-testbench, PV placement)? Sync SharePoint copy from git or retire folder?

## 6. Next actions (ordered, near-term only)

1. **Save** the handoff automation in Cursor Automations (from `automations/export-handoff-prefill.json`) if not already saved.
2. Run **handoff** at end of sessions in this workspace (or say **export PROMPT**).
3. Optional: copy kit into other active repos; see TODO plan-5, plan-6.

## 7. References

- Full spec (local): [PROMPT-TODO-handoff-plan.md](./PROMPT-TODO-handoff-plan.md)
- Plan (read-only): `C:\Users\VLAD\.cursor\plans\conversation_handoff_prompt.md_4122d518.plan.md`
- Download copy: `C:\Users\VLAD\Downloads\PROMPT-TODO-handoff-plan.md`
- Git remote: [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)
- Prior kit locations: `C:\Users\VLAD\agent-handoff`; SharePoint **AI vibecoding** (superseded by this repo per D6)
- Examples: `C:\Users\VLAD\HOME\CODE\team-me\asset-ontology\PROMPT.md`, `em-testbench/prompt.md`
- Project rule: [.cursor/rules/agent-handoff-bootstrap.mdc](.cursor/rules/agent-handoff-bootstrap.mdc)
- Automation prefill: [automations/export-handoff-prefill.json](automations/export-handoff-prefill.json)

## 8. Anti-goals / out of scope

- Application/runtime code for handoff (files + automation only).
- Editing the Cursor plan artifact.
- Full chat archival or per-message log rows.
- Renaming legacy `prompt.md` in other repos until those repos are actively touched.

## 9. Conversation log (append-only, tagged)

| Date | Topics | Session | Summary | Refs |
|------|--------|---------|---------|------|
| 2026-06-02 | `agent-handoff`, `automation`, `planning` | `plan-prompt-todo` | Adopted PROMPT.md + TODO.md split, topic/session log tags, severity/time on TODO; exported plan to Downloads. | D1–D4 |
| 2026-06-02 | `agent-handoff`, `implementation` | `implement-plan` | Scaffolded `agent-handoff` repo, templates, bootstrap rule, automation prefill, first handoff export. | TODO#plan-1–plan-4 |
| 2026-06-02 | `agent-handoff`, `migration` | `move-to-ai-vibecoding` | Moved full handoff kit from `agent-handoff` workspace into Team-ProGrammar AI vibecoding folder; D5 canonical home. | D5 |
| 2026-06-02 | `ai-promptkit`, `git`, `repo-placement` | `canonical-git-home` | Canonical home moved to git repo `m4rt1n3k/ai-promptkit`; PROMPT §5 and docs updated for local clone path and `main` branch. | D6, TODO#plan-8 |
