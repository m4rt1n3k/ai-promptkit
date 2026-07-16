# Sync pyproject.toml

Used by [init.md](init.md) (Python projects) and [handoff.md](handoff.md) step 3 when Python deps, tooling, or package layout changed.

---

## Task: Create or update pyproject.toml

Target repository (cwd = repo root). Consumer project with `extern/ai-promptkit/` submodule.

### Skip when

- **Not a Python project** — no `.py` files outside `extern/`, and no `requirements*.txt`, `setup.py`, `setup.cfg`, or existing `pyproject.toml`.
- **ai-promptkit upstream** — this repo (has `templates/`, base `prompts/handoff.md`, no `extern/ai-promptkit/`). Upstream intentionally has no `pyproject.toml`.
- Session did not touch Python deps, tooling, layout, or `pyproject.toml` (handoff only).

### Detect project shape

Inspect repo before writing:

| Signal | Action |
|--------|--------|
| `src/` or installable package layout | May need `[build-system]` — only if project actually publishes or `pip install .` |
| Scripts only (`tools/`, `scripts/`) | Minimal `[project]` — metadata + `requires-python` + `[tool.*]` |
| `requirements.txt` / `requirements-dev.txt` | Mirror runtime deps in `[project.dependencies]`; dev extras in `[project.optional-dependencies.dev]` |
| Existing `pyproject.toml` | Update in place; preserve intentional choices |
| `uv.lock` / `poetry.lock` | Do not replace lockfiles; align `pyproject.toml` only |

Infer `requires-python` from code (`list[str]`, `str \| None` → ≥3.10; prefer ≥3.11 for new files).

### Create (missing file)

Minimal default for most consumer repos:

```toml
[project]
name = "<package-name>"          # from repo folder or README title; kebab-case
version = "0.1.0"
description = "<one line from README if present>"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
  "ruff>=0.9",
]

[tool.ruff]
target-version = "py311"
line-length = 100
src = ["src", "lib", "tools", "scripts"]   # keep only dirs that exist

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
```

Rules:

- `dependencies = []` when stdlib-only or deps not yet known.
- Do not add `[build-system]` unless the repo installs as a package.
- Do not invent package name if unclear — use repo directory name and note in output.

### Update (existing file)

Adjust only what changed this session:

- New/removed **runtime** deps → `[project.dependencies]`
- New/removed **dev** tools (ruff, mypy, pytest) → `[project.optional-dependencies.dev]` and matching `[tool.*]`
- Python syntax/features → `requires-python`, `target-version`
- New source roots → `[tool.ruff] src`, mypy paths if configured
- New CLI entry points → `[project.scripts]` only when a real module path exists

Do not remove user-added sections (hatch, poetry, uv settings) unless obsolete and session explicitly migrated them.

### Constraints

- Consumer repo only — never write `pyproject.toml` under `extern/ai-promptkit/`.
- Minimal correct diff. No fake deps. No heavy packaging without need.
- Do not commit unless asked.
- Report: **created** | **updated** | **skipped** (with reason).
