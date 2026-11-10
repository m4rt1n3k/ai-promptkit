"""Kontrola stránky MASTER.md podle master/protocol.md.

Použití:
    python check.py [MASTER.md]        zkontroluje stránku
    python check.py --inbox [SLOŽKA]   vypíše otevřené otázky ze všech MASTER.md pod složkou

Návratový kód: 0 bez chyb, 1 chyby, 2 soubor nebo složka neexistuje.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

PAGE = "MASTER.md"
SECTIONS = ("Rozhodni", "Víme", "Záměr", "Rozhodnuto")
MAX_LINES = 60
MAX_OPEN = 3
MAX_DECIDED = 12
STATUS_WORDS = {"?": "hypotéza", "▶": "sázka", "~": "zjištěno", "✓": "ověřeno", "✗": "vyvráceno"}
NEEDS_EVIDENCE = "~✓✗"
INTENT_REQUIRED = ("Cíl:", "Hotovo, když:", "Vždy se mě zeptej:")
INTENT_RECOMMENDED = ("Agenti smí sami:",)
DECISION_PARTS = (
    ("A)", "možnost A)"),
    ("B)", "možnost B)"),
    ("Doporučuji", "„Doporučuji“"),
    ("Bez odpovědi:", "„Bez odpovědi:“"),
)
SKIP_DIRS = {"extern", "node_modules", "venv", "__pycache__"}

COMMENT = re.compile(r"<!--.*?-->", re.S)
NUMBERED = re.compile(r"\s*\d+\.\s")
BULLET = re.compile(r"\s*[-*]\s")
EVIDENCE = re.compile(r"(^|\s)→\s*\S")
PLACEHOLDER = re.compile(r"<(?=\S)[^<>/:\n]+(?<=\S)>")


class Report:
    def __init__(self) -> None:
        self.entries: list[tuple[str, str]] = []

    def error(self, msg: str) -> None:
        self.entries.append(("CHYBA", msg))

    def warn(self, msg: str) -> None:
        self.entries.append(("VAROVÁNÍ", msg))

    def tip(self, msg: str) -> None:
        self.entries.append(("TIP", msg))

    def info(self, msg: str) -> None:
        self.entries.append(("INFO", msg))

    @property
    def errors(self) -> int:
        return sum(level == "CHYBA" for level, _ in self.entries)


def plural(n: int, one: str, few: str, many: str) -> str:
    return f"{n} {one if n == 1 else few if 2 <= n <= 4 else many}"


def shorten(text: str, width: int = 60) -> str:
    return text if len(text) <= width else text[: width - 1].rstrip() + "…"


def read(path: Path) -> str:
    return COMMENT.sub("", path.read_text(encoding="utf-8-sig"))


def split_sections(text: str) -> tuple[dict[str, list[str]], list[str]]:
    """Vrátí řádky jednotlivých oddílů a pořadí, v jakém oddíly na stránce jsou."""
    found: dict[str, list[str]] = {}
    order: list[str] = []
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            current = next((s for s in SECTIONS if re.match(rf"{s}\b", title)), None)
            if current:
                found.setdefault(current, [])
                order.append(current)
            continue
        if current:
            found[current].append(line)
    return found, order


def items(lines: list[str], start: re.Pattern[str]) -> list[list[str]]:
    """Seskupí řádky do položek; položka začíná řádkem, který odpovídá `start`."""
    groups: list[list[str]] = []
    for line in lines:
        if start.match(line):
            groups.append([line])
        elif groups and line.strip():
            groups[-1].append(line)
    return groups


def answer(question: list[str]) -> str | None:
    """Text za „→“; None, když řádek „→“ chybí."""
    for line in question:
        if line.strip().startswith("→"):
            return line.strip()[1:].strip()
    return None


def question_title(question: list[str]) -> str:
    bold = re.search(r"\*\*(.+?)\*\*", question[0])
    return bold.group(1) if bold else NUMBERED.sub("", question[0], count=1).strip()


def recommendation(question: list[str]) -> str:
    found = re.search(r"Doporučuji\s+([^:.]+)", " ".join(question))
    return found.group(1).strip() if found else "?"


def check_decisions(lines: list[str], report: Report) -> None:
    questions = items(lines, NUMBERED)
    if len(questions) > MAX_OPEN:
        report.error(
            f"Rozhodni: {plural(len(questions), 'otázka', 'otázky', 'otázek')}, smějí být nejvýš {MAX_OPEN}. "
            "Méně důležité vyřeš v mezích Záměru sám, nebo je odlož."
        )
    for n, question in enumerate(questions, 1):
        block = "\n".join(question)
        missing = [label for key, label in DECISION_PARTS if key not in block]
        if missing:
            report.error(f"Rozhodni {n}: chybí {', '.join(missing)}.")
        reply = answer(question)
        if reply is None:
            report.warn(f"Rozhodni {n}: chybí řádek „→“ pro odpověď.")
        elif reply:
            report.info(f"Rozhodni {n}: odpověď „{reply}“ čeká na zapracování.")


def check_claims(lines: list[str], report: Report) -> None:
    bets = 0
    legend = ", ".join(f"{symbol} {word}" for symbol, word in STATUS_WORDS.items())
    for item in items(lines, BULLET):
        head = BULLET.sub("", item[0], count=1).strip()
        status, claim = head[:1], head[1:].strip()
        text = " ".join(line.strip() for line in item)
        if status not in STATUS_WORDS:
            report.error(f"Víme: „{shorten(head)}“ nemá na začátku stav ({legend}).")
            continue
        name = shorten(claim)
        if status == "▶":
            bets += 1
            if "ověříme:" not in text:
                report.error(f"Víme: sázka „{name}“ nemá „ověříme:“ s hodnotitelem a prahem.")
        if status in NEEDS_EVIDENCE and not EVIDENCE.search(text):
            report.error(f"Víme: „{name}“ je {STATUS_WORDS[status]}, ale za „→“ nemá důkaz.")
    if bets > 1:
        report.error(f"Víme: {plural(bets, 'sázka', 'sázky', 'sázek')} naráz, smí být nejvýš jedna.")


def check_intent(lines: list[str], report: Report) -> None:
    text = "\n".join(lines)
    for key in INTENT_REQUIRED:
        if key not in text:
            report.error(f"Záměr: chybí „{key}“.")
    for key in INTENT_RECOMMENDED:
        if key not in text:
            report.warn(f"Záměr: chybí „{key}“, agenti proto nevědí, co smějí udělat bez ptaní.")


def check_decided(lines: list[str], report: Report) -> None:
    decided = [" ".join(item) for item in items(lines, BULLET)]
    if len(decided) > MAX_DECIDED:
        report.warn(
            f"Rozhodnuto: {plural(len(decided), 'záznam', 'záznamy', 'záznamů')}. "
            "Nech posledních asi 10, starší zůstanou v gitu."
        )
    followed = sum("člověk (doporučeno)" in entry for entry in decided)
    total = followed + sum("člověk (jinak)" in entry for entry in decided)
    if total < 5:
        return
    if followed >= 0.9 * total:
        report.tip(
            f"Člověk přijal {followed} z {total} doporučení. "
            "Navrhni, které z těchto rozhodnutí přesunout do „Agenti smí sami“."
        )
    elif followed <= 0.5 * total:
        report.tip(
            f"Člověk přijal jen {followed} z {total} doporučení. "
            "Zeptej se, co chybí v Záměru nebo v „Platí vždy“."
        )


def check(path: Path) -> int:
    text = read(path)
    report = Report()
    found, order = split_sections(text)

    for name in SECTIONS:
        if name not in found:
            report.error(f"Chybí oddíl „## {name}“.")
        elif order.count(name) > 1:
            report.error(f"Oddíl „## {name}“ je na stránce víckrát.")
    if list(dict.fromkeys(order)) != [name for name in SECTIONS if name in found]:
        report.warn(f"Oddíly mají být v pořadí {', '.join(SECTIONS)}.")

    lines = sum(1 for line in text.splitlines() if line.strip())
    if lines > MAX_LINES:
        report.error(
            f"Stránka má {plural(lines, 'neprázdný řádek', 'neprázdné řádky', 'neprázdných řádků')}, "
            f"smí mít nejvýš {MAX_LINES}. Podrobnosti přesuň do odkazovaných souborů."
        )

    check_decisions(found.get("Rozhodni", []), report)
    check_claims(found.get("Víme", []), report)
    if "Záměr" in found:
        check_intent(found["Záměr"], report)
    check_decided(found.get("Rozhodnuto", []), report)
    if PLACEHOLDER.search(text):
        report.warn("Stránka obsahuje nevyplněná místa <…> ze šablony.")

    for level, msg in report.entries:
        print(f"{level}: {msg}")
    if report.errors:
        print(f"{path}: {plural(report.errors, 'chyba', 'chyby', 'chyb')}.")
        return 1
    print(f"{path}: bez chyb.")
    return 0


def inbox(root: Path) -> int:
    pages: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS)
        if PAGE in filenames:
            pages.append(Path(dirpath) / PAGE)

    waiting = 0
    for page in pages:
        found, _ = split_sections(read(page))
        questions = [q for q in items(found.get("Rozhodni", []), NUMBERED) if not answer(q)]
        if not questions:
            continue
        print(f"\n{page.parent.resolve().name}  ({page})")
        for question in questions:
            print(f"  - {question_title(question)}  [doporučeno: {recommendation(question)}]")
        waiting += len(questions)

    print(f"\nOtevřené otázky: {waiting} · projekty s {PAGE}: {len(pages)}")
    return 0


def main(argv: list[str]) -> int:
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure:
        reconfigure(encoding="utf-8", errors="replace")

    if argv[:1] in (["-h"], ["--help"]):
        print((__doc__ or "").strip())
        return 0
    if argv[:1] == ["--inbox"]:
        root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
        if not root.is_dir():
            print(f"Složka {root} neexistuje.")
            return 2
        return inbox(root)

    path = Path(argv[0]) if argv else Path(PAGE)
    if not path.is_file():
        print(f"{path} neexistuje. Založ ho podle protocol.md, oddíl Start.")
        return 2
    return check(path)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
