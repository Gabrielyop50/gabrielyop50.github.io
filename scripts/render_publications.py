#!/usr/bin/env python3
"""Build a browser-independent publication page from the manually edited CSV.

The GitHub Pages deployment runs this script on each push. Search is optional:
all publications are visible as normal HTML even when JavaScript is disabled.
"""
from __future__ import annotations

import csv
from html import escape
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/publications_manual.csv"
INDEX_PATH = ROOT / "index.html"
START = "<!-- BEGIN_GENERATED_PUBLICATIONS -->"
END = "<!-- END_GENERATED_PUBLICATIONS -->"


def html_link(label: str, href: str) -> str:
    parsed = urlsplit((href or "").strip())
    if parsed.scheme not in ("https", "http") or not parsed.netloc:
        return ""
    return f'<a href="{escape(href, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a>'


def publication_html(p: dict) -> str:
    title = escape(p["title"])
    primary = p.get("publication_url") or (
        "https://doi.org/" + p["doi"] if p.get("doi") else ""
    )
    title = html_link(p["title"], primary) or title
    authors = escape(re.sub(r";\\s*", "; ", p["authors"]))
    year = escape(p["year"])
    details = (
        f'<p class="pub-details">{escape(p["publication_details"])}</p>'
        if p.get("publication_details") else ""
    )
    links = []
    if p.get("doi"):
        links.append(html_link("DOI ↗", "https://doi.org/" + p["doi"]))
    elif p.get("publication_url"):
        links.append(html_link("Publication ↗", p["publication_url"]))
    for column, label in (
        ("preprint_url", "Preprint ↗"),
        ("data_url", "Data ↗"),
        ("full_text_url", "Full text ↗"),
        ("related_url", (p.get("related_label") or "Related version") + " ↗"),
    ):
        href = p.get(column, "")
        if href and not (column == "full_text_url" and href == p.get("publication_url")):
            links.append(html_link(label, href))
    links_html = (
        '<div class="pub-links">' + " ".join(filter(None, links)) + "</div>"
        if any(links) else ""
    )
    return (
        '<article class="publication">'
        f'<p class="pub-authors">{authors} ({year})</p>'
        f'<h4 class="pub-title">{title}</h4>'
        f'{details}{links_html}'
        '</article>'
    )


def render(rows: list[dict]) -> str:
    years: dict[str, list[dict]] = {}
    for p in rows:
        years.setdefault(p["year"], []).append(p)
    sections = []
    for year in sorted(years, key=int, reverse=True):
        works = "\n".join(publication_html(p) for p in years[year])
        sections.append(
            f'<section class="year-group" aria-label="Publications from {escape(year)}">'
            f'<h3>{escape(year)}</h3><div class="year-publications">{works}</div></section>'
        )
    return "\n".join(sections)


def build(output_dir: Path) -> None:
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("CSV has no publications")
    html = INDEX_PATH.read_text(encoding="utf-8")
    if html.count(START) != 1 or html.count(END) != 1:
        raise ValueError("Publication HTML template markers are missing or duplicated")
    prefix, remainder = html.split(START, 1)
    _, suffix = remainder.split(END, 1)
    html = prefix + START + "\n" + render(rows) + "\n" + END + suffix
    html = re.sub(
        r'(<span class="publication-count" id="publication-count" aria-live="polite">).*?(</span>)',
        lambda m: m.group(1) + str(len(rows)) + " works" + m.group(2),
        html, count=1, flags=re.S,
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(html, encoding="utf-8")
    if html.count('<article class="publication">') != len(rows):
        raise ValueError("HTML rendering lost publication entries")
    print(f"Rendered {len(rows)} publications to {output_dir / 'index.html'}")


if __name__ == "__main__":
    build(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site")
