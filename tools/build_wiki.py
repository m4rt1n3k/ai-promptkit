#!/usr/bin/env python3
"""Minimal wiki builder: extract docstrings → docs/wiki/from-code.md."""

from __future__ import annotations

import ast
import os
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = REPO_ROOT / "docs" / "wiki"
OUTPUT = WIKI_DIR / "from-code.md"

# Directories to scan (edit per repo)
SCAN_DIRS = ("src", "lib", "tools")
SKIP_DIRS = {"__pycache__", "node_modules", ".git", "subs", "vendor"}


def iter_py_files() -> list[Path]:
    files: list[Path] = []
    for name in SCAN_DIRS:
        root = REPO_ROOT / name
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith(".py"):
                    files.append(Path(dirpath) / fn)
    return sorted(files)


def module_doc(path: Path, tree: ast.AST) -> str | None:
    doc = ast.get_docstring(tree)
    if not doc:
        return None
    rel = path.relative_to(REPO_ROOT).as_posix()
    lines = [f"### `{rel}`", "", doc.strip(), ""]
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            ndoc = ast.get_docstring(node)
            if ndoc:
                kind = "class" if isinstance(node, ast.ClassDef) else "def"
                lines += [f"#### `{node.name}` ({kind})", "", ndoc.strip(), ""]
    return "\n".join(lines)


def build() -> None:
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    sections: list[str] = [
        "# From code",
        "",
        "> Auto-generated. Do not edit by hand.",
        f"> Regen: `python tools/build_wiki.py` — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]
    for path in iter_py_files():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError:
            continue
        block = module_doc(path, tree)
        if block:
            sections.append(block)
    if len(sections) == 4:
        sections.append("_No documented Python modules found. Adjust `SCAN_DIRS` in `tools/build_wiki.py`._")
        sections.append("")
    OUTPUT.write_text("\n".join(sections), encoding="utf-8")
    readme = WIKI_DIR / "README.md"
    readme.write_text(
        "# Wiki\n\nAuto-generated reference. Regenerate:\n\n```bash\npython tools/build_wiki.py\n```\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    build()
