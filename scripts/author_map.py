"""Map the many spellings of group members' names to their author profile slugs.

Crossref/ORCID give names such as "Ángel Martín Pendás", "A. Martín Pendás",
"A. Martin Pendas" or "Angel Martín-Pendás". Hugo Blox links an author entry to a
profile (content/authors/<slug>/) only when the entry is the slug itself, so every
variant is rewritten to the slug. A match needs one of the surname keys plus either
the member's first name or its initial, so "Francisco Muñoz" or "Abran Costales"
are not taken for group members.
"""

import re
import unicodedata
from typing import List

# slug: (first name, surname keys after normalisation)
MEMBERS = {
    "angel-pendas": ("angel", ["martin pendas", "m pendas"]),
    "evelio-francisco": ("evelio", ["francisco"]),
    "aurora-costales": ("aurora", ["costales"]),
    "dimas-suarez": ("dimas", ["suarez"]),
    "natalia-diaz": ("natalia", ["diaz"]),
    "maria-menendez": ("maria", ["menendez herrero"]),  # not María Isabel Menéndez
    "daniel-barrena": ("daniel", ["barrena"]),
    "diogo-rodrigues": ("diogo", ["rodrigues"]),
}
TITLES = {"dr", "prof", "professor"}
# Odd records (reversed order, corrupted encodings) matched literally.
ALIASES = {
    "Pendás A. Martín": "angel-pendas",
    "Martín Pendás": "angel-pendas",
    "A. Martriaan Pendás": "angel-pendas",
    "A. Mart\ufffdn Pend\ufffds": "angel-pendas",
}


def _norm(name: str) -> str:
    name = name.replace("ı", "i")  # dotless i appears in some Crossref records
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    name = re.sub(r"[.\-‐‑,]", " ", name.lower())
    return re.sub(r"\s+", " ", name).strip()


def canonical(name: str) -> str:
    """Return the member slug for a name, or the name unchanged."""
    if name in MEMBERS:
        return name
    if name in ALIASES:
        return ALIASES[name]
    n = _norm(name)
    if not n:
        return name
    tokens = [t for t in n.split() if t not in TITLES]
    if len(tokens) < 2:
        return name
    first, rest = tokens[0], " ".join(tokens[1:])
    for slug, (given, keys) in MEMBERS.items():
        if first != given and first != given[0]:
            continue
        padded = f" {rest} "
        if any(f" {k} " in padded for k in keys):
            return slug
    return name


def canonical_list(names: List[str]) -> List[str]:
    """Canonicalise a list of authors and drop repeated entries."""
    out, seen = [], set()
    for a in names:
        c = canonical(a.strip())
        key = c if c in MEMBERS else _norm(c)
        if key in seen:
            continue
        seen.add(key)
        out.append(c)
    return out
