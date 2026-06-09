# Bootstrap: docs + prompts layout (cross-repo)

Apply the **docs / prompts / handoff** pattern to any repository.

**Before pasting:** copy prompts from ai-promptkit submodule (or clone):

```text
prompts/session-summary.md
prompts/update-devlog.md
prompts/regenerate-docs.md
prompts/suggest-adr.md
prompts/install-design-rule.md
prompts/handoff.md
prompts/invoke.md
tools/build_wiki.py         # optional; adapt SCAN_DIRS
```

Copy everything below the line into a new agent chat in the **target** repository (cwd = repo root).

---

## Task: Bootstrap docs and prompts layout

You are in the **target repository** (cwd = repo root). Implement a minimal **documentation layers + prompts library** redesign. Do not over-engineer.

### Design principles

1. **One job per file** — README maps; manual teaches use; devlog narrates; ADRs explain irreversible choices.
2. **`prompts/` = invocable AI** — everything pasted into a chat or skill; no parallel `agents/` tree.
3. **`handoff.md` = meta-prompt only** — it writes to `docs/` and `TODO.md`; it does not store state.
4. **Automation is thin** — optional `build_wiki.py`; doc regen stays LLM-driven via prompts.
5. **Prompt file contract** — human header, then `---`, then copy-paste task body.

### Target layout (create/adapt)

```text
<repo>/
├── README.md
├── TODO.md
├── docs/
│   ├── README.md
│   ├── manual.md
│   ├── conventions.md
│   ├── devlog.md
│   ├── adr/
│   └── wiki/
├── prompts/
│   ├── README.md
│   ├── handoff.md
│   ├── invoke.md
│   ├── session-summary.md
│   ├── update-devlog.md
│   ├── regenerate-docs.md
│   ├── suggest-adr.md
│   ├── install-design-rule.md
│   └── <domain>/              # repo-specific prompts only
└── tools/build_wiki.py        # optional
```

### Phase 0 — Discover (read only)

Scan the repo and report briefly:

| Look for | Typical legacy names |
|----------|----------------------|
| Monolithic agent doc | `PROMPT.md`, `AGENTS.md`, `CLAUDE.md` |
| User manual at root | `MANUAL.md` |
| External handoff | `kit_handoff`, ai-promptkit kits, scattered conversation logs |
| Agent packages | `agents/<name>/`, `INSTRUCTIONS.md` outside `prompts/` |
| Existing prompts | `prompts/*.md`, `tools/**/prompt.md` |
| Planning | `TODO.md`, `ROADMAP.md` |

List what will be **migrated**, **stubbed**, or **left unchanged**.

### Phase 1 — Scaffold

Create empty/skeleton files for the target layout. Seed from ai-promptkit [`templates/`](../templates/) when available.

If core `prompts/*.md` files are missing, create them from ai-promptkit; replace hardcoded repo name with this repo's name.

### Phase 2 — Migrate content

| From (if exists) | To | Action |
|------------------|-----|--------|
| `MANUAL.md` or long README workflows | `docs/manual.md` | Move workflows; drop embedded changelog → devlog |
| `PROMPT.md` § rules / checklist | `docs/conventions.md` | Extract governance only |
| `PROMPT.md` § conversation log | `docs/devlog.md` | Move table; newest first |
| Legacy decision tables | `docs/adr/000x-*.md` | Curate 2–5 irreversible choices |
| `PROMPT.md` repo map | `README.md` | Slim README to map + links |
| `prompts/_shared/*` (legacy) | `prompts/` | Flatten into prompts root |
| `kits/`, `kit_*` invoke | `prompts/handoff.md` | Replace with prompt orchestration |

**Stub redirects** at old paths for one release cycle:

```markdown
# <OLD>.md — moved
See [`docs/manual.md`](docs/manual.md) / [`docs/conventions.md`](docs/conventions.md) / [`prompts/handoff.md`](prompts/handoff.md).
```

### Phase 3 — `handoff.md` orchestration

Ensure `prompts/handoff.md` runs **in order**:

1. `session-summary.md` → commit message draft
2. `update-devlog.md` → append `docs/devlog.md`
3. `regenerate-docs.md` → if layout/CLI changed
4. `suggest-adr.md` → if architectural choice → draft ADR
5. Update `TODO.md` active track if session opened/closed tasks

Constraints: read `git status`; do not invent changes; do not commit unless asked.

### Phase 4 — `tools/build_wiki.py` (optional)

Create or adapt minimal script from ai-promptkit. Run once; commit `docs/wiki/` so readers need no build step.

### Phase 5 — Link sweep + design rule

- Update README "who reads what" table.
- Run [`install-design-rule.md`](install-design-rule.md) if user wants design discipline.
- Remove references to legacy `kit_*` — replace with `prompts/handoff.md`.

### Phase 6 — ADR for this migration

Create `docs/adr/000N-docs-prompts-layout.md` (status: `accepted`) documenting this bootstrap.

Append one row to `docs/devlog.md`.

### Deliberately skip (stay minimal)

- No MkDocs/Docusaurus unless user asks
- No prompt versioning IDs or JSON orchestration state
- No CI gate on wiki
- No merging `TODO.md` into devlog

### Deliverables checklist

```text
[ ] docs/{README,manual,conventions,devlog,adr/,wiki/}
[ ] prompts/{README,handoff,invoke,session-summary,update-devlog,...}
[ ] prompts/<domain>/ for repo-specific workflows (if any)
[ ] tools/build_wiki.py (optional)
[ ] Legacy stubs (PROMPT.md, MANUAL.md, kits/)
[ ] README updated
[ ] Commit message draft (do not commit unless asked)
```

### Output format

1. **Discovery summary** (what you found)
2. **Files created/moved** (table)
3. **Follow-ups** for the human
4. **Commit message draft**
