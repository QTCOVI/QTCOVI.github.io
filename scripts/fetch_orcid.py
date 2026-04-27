#!/usr/bin/env python3
"""
Fetch publications from ORCID public API and generate Hugo content files.

Usage:
    python scripts/fetch_orcid.py

Requires:
    pip install requests pyyaml

Config:
    config_site/orcid_ids.yaml  — list of member ORCID IDs
Output:
    content/publication/{slug}/index.md  — one file per unique publication
"""

import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import requests
import yaml

ORCID_API = "https://pub.orcid.org/v3.0"
CROSSREF_API = "https://api.crossref.org/works"
HEADERS = {"Accept": "application/json"}
CONTENT_DIR = Path("content/publication")
CONFIG_FILE = Path("config_site/orcid_ids.yaml")

# Map CSL/ORCID type strings to HugoBlox publication_types
TYPE_MAP = {
    "journal-article": "article-journal",
    "conference-paper": "paper-conference",
    "book": "book",
    "book-chapter": "chapter",
    "preprint": "article",
    "dataset": "dataset",
    "thesis": "thesis",
    "other": "article",
}


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80]


def get_orcid_works(orcid: str) -> List[Dict]:
    url = f"{ORCID_API}/{orcid}/works"
    r = requests.get(url, headers=HEADERS, timeout=30)
    if r.status_code != 200:
        print(f"  WARN: ORCID {orcid} returned {r.status_code}", file=sys.stderr)
        return []
    data = r.json()
    return data.get("group", [])


def get_orcid_work_detail(orcid: str, put_code: int) -> dict:
    url = f"{ORCID_API}/{orcid}/work/{put_code}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    if r.status_code != 200:
        return {}
    return r.json()


def get_crossref_metadata(doi: str) -> dict:
    url = f"{CROSSREF_API}/{doi}"
    try:
        r = requests.get(url, headers={"User-Agent": "QTCOVI-website/1.0 (mailto:martinpendas@uniovi.es)"},
                         timeout=20)
        if r.status_code == 200:
            return r.json().get("message", {})
    except Exception:
        pass
    return {}


def extract_doi(work: Dict) -> str:
    ext_ids = work.get("external-ids") or {}
    for eid in (ext_ids.get("external-id") or []):
        if eid.get("external-id-type") == "doi":
            return eid.get("external-id-value", "").strip().lower()
    return ""


def extract_year(work: Dict) -> Optional[int]:
    pub_date = work.get("publication-date") or {}
    year_val = pub_date.get("year", {})
    if isinstance(year_val, dict):
        val = year_val.get("value")
        if val:
            return int(val)
    elif isinstance(year_val, (int, str)):
        try:
            return int(year_val)
        except ValueError:
            pass
    return None


def _yaml_safe(text: str) -> str:
    """Strip characters that break YAML double-quoted scalars."""
    # Remove backslash escape sequences (LaTeX math, etc.)
    text = re.sub(r"\\[a-zA-Z{}\[\]|^_]", " ", text)
    text = text.replace("\\", " ")
    # Collapse MathJax/LaTeX delimiters and leftover braces
    text = re.sub(r"\$\$?.*?\$\$?", "", text, flags=re.DOTALL)
    text = re.sub(r"[{}]", "", text)
    # Replace double quotes to avoid breaking YAML
    text = text.replace('"', "'")
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def build_publication_md(title: str, authors: List[str], year: Optional[int],
                          journal: str, doi: str, abstract: str,
                          pub_type: str, member_slug: str) -> str:
    date_str = f"{year}-01-01T00:00:00Z" if year else "2000-01-01T00:00:00Z"
    author_list = "\n".join(f"- {a}" for a in authors) if authors else f"- {member_slug}"
    doi_line = f'doi: "{doi}"' if doi else 'doi: ""'
    url_doi = f"https://doi.org/{doi}" if doi else ""
    safe_title = _yaml_safe(title)
    safe_journal = _yaml_safe(journal)
    safe_abstract = _yaml_safe(abstract)[:1000] if abstract else ""

    return f"""---
title: "{safe_title}"
authors:
{author_list}
date: "{date_str}"
publishDate: "{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}"
publication_types: ["{pub_type}"]
publication: "{safe_journal}"
{doi_line}
abstract: "{safe_abstract}"
featured: false
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "{url_doi}"
url_video: ""
---
"""


def process_member(member: Dict, seen_dois: Set[str]) -> List[Tuple[str, str]]:
    orcid = member["orcid"]
    name = member["name"]
    slug = member["author_slug"]

    if "XXXX" in orcid:
        print(f"  Skipping {name}: ORCID not yet configured")
        return []

    print(f"Fetching works for {name} ({orcid})")
    groups = get_orcid_works(orcid)
    results = []

    for group in groups:
        summaries = group.get("work-summary", [])
        if not summaries:
            continue
        summary = summaries[0]
        put_code = summary.get("put-code")
        if not put_code:
            continue

        detail = get_orcid_work_detail(orcid, put_code)
        if not detail:
            continue

        title_data = detail.get("title", {}) or {}
        title = (title_data.get("title", {}) or {}).get("value", "Untitled")
        doi = extract_doi(detail)
        year = extract_year(detail)
        orcid_type = detail.get("type", "other")
        pub_type = TYPE_MAP.get(orcid_type, "article-journal")

        journal_title = ""
        journal_data = detail.get("journal-title") or {}
        if isinstance(journal_data, dict):
            journal_title = journal_data.get("value", "")

        # De-duplicate by DOI
        doi_key = doi if doi else f"notitle-{slugify(title)}"
        if doi_key in seen_dois:
            continue
        seen_dois.add(doi_key)

        # Enrich from CrossRef
        abstract = ""
        authors: List[str] = []
        if doi:
            cr = get_crossref_metadata(doi)
            if cr:
                abstract = cr.get("abstract", "")
                # Strip HTML from abstract
                abstract = re.sub(r"<[^>]+>", "", abstract)
                cr_authors = cr.get("author", [])
                for a in cr_authors:
                    given = a.get("given", "")
                    family = a.get("family", "")
                    authors.append(f"{given} {family}".strip())
                if not journal_title:
                    container = cr.get("container-title", [])
                    journal_title = container[0] if container else ""
            time.sleep(0.2)  # CrossRef rate limit

        file_slug = slugify(title)
        if year:
            file_slug = f"{year}-{file_slug}"

        md = build_publication_md(title, authors, year, journal_title,
                                  doi, abstract, pub_type, slug)
        results.append((file_slug, md))

        time.sleep(0.3)  # ORCID rate limit

    return results


def main():
    if not CONFIG_FILE.exists():
        print(f"Config file {CONFIG_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    members = config.get("members", [])
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    seen_dois: Set[str] = set()
    total = 0

    for member in members:
        pubs = process_member(member, seen_dois)
        for file_slug, md in pubs:
            pub_dir = CONTENT_DIR / file_slug
            pub_dir.mkdir(exist_ok=True)
            out_file = pub_dir / "index.md"
            if not out_file.exists():
                out_file.write_text(md, encoding="utf-8")
                print(f"  + wrote {out_file}")
                total += 1
            else:
                print(f"  ~ exists {out_file}")

    print(f"\nDone. {total} new publications written.")


if __name__ == "__main__":
    main()
