# Suggest ADR

Use when session made an irreversible structural choice (step 4 of [`handoff.md`](handoff.md)).

Copy everything below the line into a new agent chat.

---

## Task: Propose Architecture Decision Record

You are in the **target repository** (cwd = repo root).

**Goal:** If this session changed **how** the system works (not routine data or bug fixes), draft a new ADR or say why none is needed.

### When to create ADR

- New authority rule (validation, naming, folder layout)
- Rejected alternative with lasting impact
- New tool pipeline or prompt orchestration pattern

### When to skip

- Fixed examples, typos, single-parameter additions
- Decisions already covered by an existing ADR

### Output

1. **Skip note** — one sentence, or
2. **Draft file** `docs/adr/NNNN-slug.md` using template in `docs/adr/README.md`:
   - Next number = highest existing + 1
   - Status: `proposed` until human accepts
3. **Update index** in `docs/adr/README.md`

### Rules

- Be concise; link to devlog row and changed files.
- Do not commit without user approval.
