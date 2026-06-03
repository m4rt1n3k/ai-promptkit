# kit_manual

Run when the user says **`from workspace ai-promptkit run kit_manual`** (or `kit_manual`).

## Load

Read this file from **ai-promptkit**. Write to the **user’s project workspace**, not ai-promptkit.

## Inputs

- This chat (workflows, roles, steps the user described)
- Optional `session:`, `topics:`, `notes:` from the user message
- Target repo: existing `MANUAL.md`, `PROMPT.md`, `TODO.md` (read for context; do not copy agent handoff verbatim)
- Template if creating new: [templates/MANUAL.template.md](./templates/MANUAL.template.md)

## Audience

**Humans** — operators, admins, end users. Plain language, complete sentences, ordered steps. Not written for coding agents.

## Task

Create or **merge** `MANUAL.md` at the target repo root (`MANUAL.md` capitals).

- Describe **how the system is used** and **how work flows** end to end (who does what, in what order, with what inputs/outputs).
- Use headings, numbered steps, and tables where they help a reader follow the process.
- Pull facts from the chat and from `PROMPT.md` / `TODO.md` only when they reflect **user-stated** workflow; do not invent procedures, roles, or policies.
- If the target already has a custom `MANUAL.md`, keep its structure; update sections that changed in this session; append one row to § Changelog when present.
- Link to `PROMPT.md` / `TODO.md` for agent handoff, not as a substitute for human steps.
- No secrets. Prefer under ~600 lines; split rare deep dives into linked docs only if the user named those paths.

## Diagrams (Mermaid)

Add or update **mermaid** fenced blocks when a diagram communicates the workflow **better than prose alone**. Keep numbered steps for “how to do it”; use diagrams for **shape** of the process (order, branches, loops, actors).

### When to add a diagram

| Situation | Prefer |
|-----------|--------|
| Generic two-pass cycle (README: development + usage) | Link README; do not copy into MANUAL |
| Repeating **domain** ops loop the user described | `flowchart` + short phase table in MANUAL §1.1 |
| **Branching** (AI vs human track, approve/reject, env choice) | `flowchart` with clear branch labels |
| **Sequence** over time (request → review → deploy) | `sequenceDiagram` |
| **States** (draft → review → published) | `stateDiagram-v2` |
| **Who talks to whom** (user, app, admin, external API) | `sequenceDiagram` or `flowchart` |
| Simple linear checklist (≤5 steps, no branches) | Numbered list only — **no** diagram |

### When not to

- Do not diagram speculative flows the user did not describe.
- Do not replace procedural detail (commands, field names, checks) with a picture—keep steps in text under the diagram.
- Do not add decorative charts, pie graphs, or Gantt unless the user asked for scheduling visuals.

### How to write them

1. Place under **Overview** (e.g. `### 1.1 … (schematic)`) or at the start of the relevant **§4 workflow**—one primary loop diagram per manual is enough unless the user named several distinct processes.
2. **Before** the fence: 1–3 sentences on what the diagram shows.
3. **After** the fence: optional **phase table** (Phase | Read/do | Actor) and **Notes** (e.g. branches not mutually exclusive, what “handoff” updates).
4. **Inside** ` ```mermaid ` … ` ``` `:
   - `flowchart TD` or `LR` for loops and pipelines; `subgraph` for Preparation / Core / Handoff-style phases.
   - Short node labels; use `<br/>` for a second line sparingly.
   - Show **return edges** for loops (e.g. handoff → next cycle).
   - Use only nodes and edges the user (or existing `MANUAL.md`) already established.
5. **Merge:** If `MANUAL.md` already has mermaid for the same process, **edit that block** when the workflow changed; do not add a second conflicting diagram.

### Example pattern (kit-style repos only when user described this loop)

Ecosystem and default cycle: target repo **README** (not MANUAL). Domain workflows: [templates/MANUAL.template.md](./templates/MANUAL.template.md) §1.1.

## Do not

- Update `PROMPT.md` or `TODO.md` (use `kit_prompt`, `kit_todo`, or `kit_handoff`).
- Paste chat logs or agent-oriented distill rules into the manual.
- Document speculative or “recommended” workflows unless the user asked for them.
- Use mermaid for invented or generic “best practice” flows the user did not describe.

## Reply

Short: target path, what changed in `MANUAL.md`, 3–5 bullets (audience + main workflows touched). Note if any mermaid block was **added**, **updated**, or **left unchanged** (and why).
