from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent
DEFAULT_RESEARCH = ROOT.parent / "_data" / "research.yml"
DEFAULT_INDEX = ROOT.parent / "index.md"
DEFAULT_OUTDIR = ROOT / "build"


@dataclass(frozen=True)
class Publication:
    key: str
    title: str
    journal: str
    year: str
    doi: str
    first_authors: str
    other_authors: str
    section: str

    @property
    def doi_url(self) -> str:
        doi = normalize_doi(self.doi)
        return f"https://doi.org/{doi}" if doi else self.doi

    @property
    def display_authors(self) -> str:
        return display_authors(self.first_authors, self.other_authors)


def main() -> None:
    args = parse_args()
    outdir = args.outdir.resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    profile = parse_index(args.index)
    publications = parse_research(args.research)

    qmd_path = outdir / args.qmd_name
    bib_path = outdir / args.bib_name
    pdf_path = outdir / args.pdf_name

    bib_path.write_text(build_bibliography(publications), encoding="utf-8")
    qmd_path.write_text(build_quarto(profile, publications, bib_path.name), encoding="utf-8")

    if not args.no_render:
        render_pdf(qmd_path, pdf_path)

    print(f"Wrote {qmd_path}")
    print(f"Wrote {bib_path}")
    if pdf_path.exists():
        print(f"Wrote {pdf_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Quarto PDF CV from the Jekyll homepage and research data."
    )
    parser.add_argument("--research", type=Path, default=DEFAULT_RESEARCH)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--outdir", type=Path, default=DEFAULT_OUTDIR)
    parser.add_argument("--qmd-name", default="cv.qmd")
    parser.add_argument("--bib-name", default="references.bib")
    parser.add_argument("--pdf-name", default="cv.pdf")
    parser.add_argument(
        "--no-render",
        action="store_true",
        help="Only write the Quarto and BibTeX files; do not invoke quarto.",
    )
    return parser.parse_args()


def parse_index(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    text = strip_front_matter(text)
    lines = text.splitlines()

    profile: dict[str, Any] = {
        "name": "Hanbin Lee",
        "updated": current_update_date(),
        "contact": parse_contact(text),
        "about": [],
        "topics": [],
        "education": [],
        "peer_review": [],
    }

    sections = split_markdown_sections(lines)
    profile["about"], profile["topics"] = parse_about(sections.get("About", []))
    profile["education"] = parse_education(sections.get("Education", []))
    profile["peer_review"] = parse_peer_review(sections.get("Professional service", []))
    return profile


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def parse_contact(text: str) -> str:
    match = re.search(r"<([^<>\s]+@[^<>\s]+)>", text)
    return match.group(1).strip() if match else ""


def split_markdown_sections(lines: list[str]) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        if line.startswith("## "):
            current = line.removeprefix("## ").strip()
            sections[current] = []
        elif current:
            sections[current].append(line)
    return sections


def parse_about(lines: list[str]) -> tuple[list[str], list[str]]:
    paragraphs: list[str] = []
    topics: list[str] = []
    current: list[str] = []
    in_topic_list = False

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("![]"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.startswith("Contact:"):
            if current:
                paragraphs.append(" ".join(current))
            break
        if line.startswith("I'm currently working"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            in_topic_list = True
            continue
        if in_topic_list and line.startswith("- "):
            topics.append(line.removeprefix("- ").strip())
        elif not in_topic_list:
            current.append(line)

    if current:
        paragraphs.append(" ".join(current))
    return paragraphs, topics


def parse_education(lines: list[str]) -> list[dict[str, Any]]:
    education: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for raw in lines:
        line = raw.strip()
        if line.startswith("### "):
            current = {"institution": line.removeprefix("### ").strip(), "degrees": []}
            education.append(current)
        elif current and line.startswith("- "):
            current["degrees"].append(line.removeprefix("- ").strip())
    return education


def parse_peer_review(lines: list[str]) -> list[str]:
    text = "\n".join(lines)
    return [item.strip() for item in re.findall(r"_([^_]+)_", text)]


def parse_research(path: Path) -> list[Publication]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    publications: list[Publication] = []
    used_keys: set[str] = set()

    for section in data:
        section_name = str(section.get("name", "Publications"))
        for paper in section.get("papers") or []:
            title = str(paper.get("name", "")).strip()
            year = str(paper.get("year", "")).strip()
            key = unique_key(make_key(title, year), used_keys)
            publications.append(
                Publication(
                    key=key,
                    title=title,
                    journal=str(paper.get("journal", "")).strip(),
                    year=year,
                    doi=str(paper.get("doi", "")).strip(),
                    first_authors=str(paper.get("fauthor", "")).strip(),
                    other_authors=str(paper.get("author", "")).strip(),
                    section=section_name,
                )
            )
    return publications


def make_key(title: str, year: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title.lower())
    stem = "".join(words[:4]) or "publication"
    return f"lee{year}{stem}"


def unique_key(key: str, used_keys: set[str]) -> str:
    candidate = key
    suffix = 2
    while candidate in used_keys:
        candidate = f"{key}{suffix}"
        suffix += 1
    used_keys.add(candidate)
    return candidate


def build_bibliography(publications: list[Publication]) -> str:
    entries: list[str] = []
    for publication in publications:
        bib = doi_to_bibtex(publication)
        entries.append(bib if bib else fallback_bibtex(publication))
    return "\n\n".join(entries) + "\n"


def doi_to_bibtex(publication: Publication) -> str | None:
    doi = normalize_doi(publication.doi)
    if not doi:
        return None

    executable = shutil.which("doi2bib")
    if not executable:
        return None

    try:
        result = subprocess.run(
            [executable, doi],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None

    if result.returncode != 0 or "@" not in result.stdout:
        return None
    return replace_bibtex_key(result.stdout.strip(), publication.key)


def normalize_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = value.removeprefix("doi:")
    return value.strip().rstrip(".")


def replace_bibtex_key(entry: str, key: str) -> str:
    return re.sub(r"@\s*([A-Za-z]+)\s*\{\s*[^,]+,", r"@\1{" + key + ",", entry, count=1)


def fallback_bibtex(publication: Publication) -> str:
    fields = {
        "title": publication.title,
        "author": bibtex_authors(publication.display_authors),
        "journal": publication.journal,
        "year": publication.year,
        "doi": normalize_doi(publication.doi),
        "url": publication.doi_url,
    }
    body = "\n".join(
        f"  {name} = {{{escape_bibtex(value)}}},"
        for name, value in fields.items()
        if value
    )
    return f"@article{{{publication.key},\n{body}\n}}"


def bibtex_authors(display_authors: str) -> str:
    clean = display_authors.replace("*", "")
    clean = re.sub(r"\band\s+and\b", "and", clean)
    clean = re.sub(r"^and\s+", "", clean.strip())
    pieces: list[str] = []
    for part in re.split(r",|\band\b", clean):
        author = part.strip()
        if author:
            pieces.append(author)
    return " and ".join(pieces)


def display_authors(first_authors: str, other_authors: str) -> str:
    first = first_authors.strip()
    other = re.sub(r"^and\s+", "", other_authors.strip())
    if not first:
        return other
    if not other:
        return first
    return f"{first}, {other}"


def escape_markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("*", r"\*")


def escape_typst(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("[", r"\[")
        .replace("]", r"\]")
        .replace("#", r"\#")
        .replace("@", r"\@")
    )


def escape_bibtex(value: str) -> str:
    return value.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def build_quarto(profile: dict[str, Any], publications: list[Publication], bib_name: str) -> str:
    lines = [
        "---",
        "format:",
        "  typst:",
        "    toc: false",
        "---",
        "",
    ]

    lines.extend(build_document_header(profile))

    lines.extend(["## About", ""])
    for paragraph in profile["about"]:
        lines.extend([paragraph, ""])
    if profile["topics"]:
        lines.extend(["Current research topics:", ""])
        lines.extend(f"- {topic}" for topic in profile["topics"])
        lines.append("")

    lines.extend(["## Education", ""])
    for item in profile["education"]:
        lines.append(f"### {item['institution']}")
        lines.extend(f"- {degree}" for degree in item["degrees"])
        lines.append("")

    if profile["peer_review"]:
        lines.extend(["## Professional Service", "", "### Peer Review"])
        lines.extend(f"- {journal}" for journal in profile["peer_review"])
        lines.append("")

    lines.extend(["## Publications", "", r"\* denotes equal contribution.", ""])
    for section, grouped in group_publications(publications).items():
        lines.extend([f"### {section}", ""])
        for publication in grouped:
            authors = escape_markdown_text(publication.display_authors)
            doi = publication.doi_url
            lines.append(
                f"- **{authors}.** {publication.title}. "
                f"*{publication.journal}*, {publication.year}. [link]({doi})"
            )
        lines.append("")

    return "\n".join(lines)


def build_document_header(profile: dict[str, Any]) -> list[str]:
    updated = updated_text(profile.get("updated", ""))
    contact = profile.get("contact", "")
    return [
        "```{=typst}",
        f"#align(right)[{escape_typst(updated)}]",
        "#align(center)[",
        f"  #text(size: 20pt, weight: \"bold\")[{escape_typst(profile['name'])}]",
        "  #linebreak()",
        f"  #text(size: 10pt)[{escape_typst(contact)}]",
        "  #linebreak()",
        "  #text(size: 12pt)[Curriculum Vitae]",
        "]",
        "#v(1em)",
        "```",
        "",
    ]


def updated_text(updated: str) -> str:
    return f"Updated in {updated}" if updated else ""


def current_update_date() -> str:
    return date.today().strftime("%B, %Y")


def group_publications(publications: list[Publication]) -> dict[str, list[Publication]]:
    grouped: dict[str, list[Publication]] = {}
    for publication in publications:
        grouped.setdefault(publication.section, []).append(publication)
    return grouped


def render_pdf(qmd_path: Path, pdf_path: Path) -> None:
    subprocess.run(["quarto", "render", str(qmd_path)], check=True)
    rendered = qmd_path.with_suffix(".pdf")
    if rendered != pdf_path and rendered.exists():
        rendered.replace(pdf_path)


if __name__ == "__main__":
    main()
