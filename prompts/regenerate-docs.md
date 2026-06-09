# Regenerate documentation

Use when repo structure, workflows, or CLI changed (step 3 of [`handoff.md`](handoff.md)).

Copy everything below the line into a new agent chat.

---

## Task: Refresh human docs and wiki

You are in the **target repository** (cwd = repo root).

**Goal:** Keep documentation layers consistent after structural or workflow changes.

### When to run

- New top-level folder or moved paths (`docs/`, `prompts/`, `tools/`)
- New CLI flags or scripts referenced in manual
- New prompt added to registry

Skip if session only changed application code with no doc/tool impact.

### Steps

1. **README.md** — verify directory map and "who reads what" links point to:
   - `docs/README.md`, `docs/manual.md`, `docs/conventions.md`, `docs/devlog.md`
   - `prompts/README.md`, `docs/wiki/` (if wiki exists)
2. **docs/manual.md** — update affected workflow sections and quick links.
3. **docs/conventions.md** — update governance, commands, known issues if needed.
4. **Wiki build** (if `tools/build_wiki.py` exists):
   ```bash
   python tools/build_wiki.py
   ```
5. **Cross-link sweep** — fix broken relative links in touched files.
6. **TODO.md** — update active track / pipeline if session opened or closed tasks.

### Rules

- Do not duplicate long reference content in README — link to the canonical doc.
- Do not edit generated wiki files by hand (`docs/wiki/from-code.md`, etc.).
- **Do not commit** unless user asks.
