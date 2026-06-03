# MANUAL.md — user and admin guide

## 0. Meta

- Purpose: (one sentence — what this document helps a human do)
- Audience: (e.g. end users, operators, admins)
- Last updated: YYYY-MM-DD
- Related: [PROMPT.md](./PROMPT.md) (agent handoff) · [TODO.md](./TODO.md) (plans)
- Repo / product: (name; environment if relevant)

## 1. Overview

What the product or repo is for, in plain language. Who should read which sections below.

Point readers to the project **README** for the PROMPT · TODO · MANUAL ecosystem and **two-pass** cycle (pass 1: README+PROMPT+TODO+develop+handoff; pass 2: README+MANUAL). Do not duplicate that block here. MANUAL is the home for **pass 2 (usage)** procedures; link [PROMPT.md](./PROMPT.md) / [TODO.md](./TODO.md) only when a workflow crosses into development.

### 1.1 Project-specific workflows (optional)

Add mermaid or phase tables here only for **domain** loops the user described (deploy, review, etc.)—not the generic kit handoff cycle (that belongs in README).

## 2. Prerequisites

- Access, accounts, tools, or data needed before starting
- Where configuration lives (paths only; no secrets)

## 3. Roles and responsibilities

| Role | Can do | Cannot do / escalates to |
|------|--------|---------------------------|
| … | … | … |

## 4. Core workflows

Repeat this subsection per major process. Use **numbered steps** a human can follow without reading code.

### 4.1 (Workflow name)

**When:** …  
**Who:** …  
**Outcome:** …

Optional: mermaid here if this workflow has branches, loops, or many actors—otherwise numbered steps only.

1. …
2. …

**Checks:** how to confirm success  
**If something fails:** what to try, who to contact

### 4.2 (Next workflow)

…

## 5. Routine operations

- Start / stop / deploy / backup / restore (as applicable)
- How to run common commands or UIs (command text only if user provided it)

## 6. Administration

- Settings, users, permissions, maintenance windows
- Policies the user stated in session (not invented)

## 7. Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| … | … | … |

## 8. Glossary

| Term | Meaning |
|------|---------|
| … | … |

## 9. References

- External docs, runbooks, support channels (URLs or paths only)
- Kit: [ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit) — `kit_manual` maintains this file

## 10. Changelog (append-only)

| Date | Topics | Session | Summary |
|------|--------|---------|---------|
| YYYY-MM-DD | … | … | … |
