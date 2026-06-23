# Takeover — understand codebase before coding

Run at the **start of a new chat** before working on human- or externist-written code, or before taking on a **different area** of the repo. Pair with [handoff.md](handoff.md): handoff ends the previous session; takeover opens the next one.

Overrides default shallow exploration — go deep, cite evidence, stay read-only until the user asks to implement.

Invoke:

```text
Read subs/ai-promptkit/prompts/takeover.md and run on this workspace.
```

Optional scope: append `Focus on <path or module>.`

---

## Task: Build takeover-ready mental model

Target repository (cwd = repo root). Goal: short debrief + serious findings + next steps — then user continues development in this chat. Not a refactor pass; not new docs unless user asks.

### 0. Mode

- **Fresh chat.** You do not have prior session context — read what the repo persisted.
- **Explore deeply.** Read source, tests, config, and CI — not only README.
- **Read-only** unless user explicitly asks to edit files.
- **Evidence required.** Cite `path` or `path:line` for claims and findings.
- **No invented backlog.** Do not add TODO items or ADRs unless user asks.

### 1. Session context (from last handoff)

Read first:

- Last 1–3 rows of `docs/devlog.md` — what was recently done
- `TODO.md` — user-stated open work
- `docs/conventions.md`, recent `docs/adr/` if relevant

If user gave a **focus** (path/module), limit exploration to that area plus dependencies; state the scope in the debrief.

### 2. Stated intent

Read, in order of relevance:

- `README.md`, `docs/manual.md`, `docs/conventions.md`
- Dependency manifests (`pyproject.toml`, `package.json`, `go.mod`, etc.)
- CI / deploy config (`.github/`, `Dockerfile`, etc.)

Extract: **what the project is for**, **who it serves**, **how it is run/tested**.

### 3. Map the codebase

Identify and list (for full repo or focused area):

- Top-level layout and ownership of each area
- Entry points (CLI, HTTP handlers, jobs, main binaries)
- External boundaries (DB, APIs, queues, filesystem)
- Test layout and what is actually exercised

Use search and file reads; do not guess module names.

### 4. Trace critical flows

Pick **2–3 flows** that matter for safe change in the target area. For each:

1. Entry point
2. Key modules/functions (with paths)
3. Data in / data out
4. Failure modes and where handled

Keep each flow to a tight bullet chain — not an essay.

### 5. Infer operating principles

From **code patterns** (not wishful docs), list 5–10 principles the project mostly follows.

Mark each as **consistent** | **mixed** | **unclear**, with 1–2 example paths.

### 6. Search for serious inconsistencies

Audit for:

- docs vs code drift
- duplicate / redundant implementations
- dead or misleading code paths
- layer or boundary violations
- convention breaks without local justification
- fragile coupling (globals, import side effects, circular deps)
- missing tests on hot or risky paths
- security or data-integrity risks at trust boundaries

**Report only findings with medium+ takeover risk.** Skip style nits and speculative nice-to-haves.

### 7. Takeover plan

Propose **3–7 ordered next steps** for development **in this chat**:

- what to read next (if anything)
- what is safe to change first
- what to avoid until understood

End with: **Ready for user task** — ask what to implement or wait for instruction.

### Constraints

- Do not commit unless asked.
- Do not bulk-edit docs; deliver in chat unless user requests a file.
- Do not propose large rewrites in this pass — flag for a later scoped task.
- If the repo is too large, state scope limits and what you sampled.

### Output format (use these headings exactly)

#### Debrief (≤15 lines)

What this codebase (or focused area) is, how it fits the project, and the 3 most important things to know before changing anything.

#### Critical flows

Numbered list (2–3 flows), each with cited path chain.

#### Operating principles

Bullet list with consistency rating and examples.

#### Serious findings

Table or bullets: **Finding** | **Risk** | **Evidence** | **Suggested follow-up (one line)**

If none: say so explicitly.

#### Takeover plan

Numbered next steps (3–7); last item is readiness to code.

#### Open questions

Only genuine unknowns that block safe work — not rhetorical.
