#!/usr/bin/env python3
"""Rewrite author lists of existing publication pages with scripts/author_map.py.

Usage: python scripts/normalize_authors.py [--dry-run]
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from author_map import canonical_list  # noqa: E402

CONTENT = Path("content/publication")
BLOCK = re.compile(r"^authors:\n((?:- .*\n)+)", re.M)


def main(dry: bool) -> None:
    changed = 0
    for f in sorted(CONTENT.glob("*/index.md")):
        text = f.read_text(encoding="utf-8")
        m = BLOCK.search(text)
        if not m:
            continue
        old = [line[2:] for line in m.group(1).splitlines()]
        new = canonical_list(old)
        if new == old:
            continue
        changed += 1
        block = "authors:\n" + "".join(f"- {a}\n" for a in new)
        if dry:
            print(f.parent.name, old, "->", new)
        else:
            f.write_text(text[:m.start()] + block + text[m.end():], encoding="utf-8")
    print(f"{changed} files {'would change' if dry else 'changed'}")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
