# Regenerate documentation

Step 3 of [handoff.md](handoff.md). Skip if only application code changed.

---

## Task: Refresh docs

Target repository (cwd = repo root).

1. **README.md** — links to `docs/manual.md`, `docs/conventions.md`, `docs/devlog.md`, `prompts/README.md`.
2. **docs/manual.md**, **docs/conventions.md** — update if workflows changed.
3. **Wiki** — `python tools/build_wiki.py` if script exists.
4. Fix broken links. Update `TODO.md` if session closed tasks.

Do not edit generated wiki by hand. Do not commit unless asked.
