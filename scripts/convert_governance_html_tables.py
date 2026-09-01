#!/usr/bin/env python3
"""Convert HTML tables in governance credential docs to Markdown tables."""

from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path

FILES = [
    Path("docs/governance/business/digital-business-card-v1.md"),
    Path("docs/governance/business/municipal-services-digital-letter-of-authorization.md"),
    Path("docs/governance/business/rental-property-business-licence.md"),
]

BOOKMARK_REPLACEMENTS = {
    "#bookmark=id.d4k15yq1kvi3": "#attributes",
    "#bookmark=id.35ojgs4iy68y": "#credential-overview",
}

EMPTY_OVERVIEW_TABLE = re.compile(
    r"^\| Field \| Value \|\s*$\n"
    r"^\| --- \| --- \|\s*$\n"
    r"^\| \*\*",
    re.MULTILINE,
)


def convert_inline_html(html: str) -> str:
    text = html.strip()
    text = re.sub(r"<br\s*/?\s*>\s*</?\s*br\s*>", "<br>", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\s*/?\s*>", "<br>", text, flags=re.IGNORECASE)

    while re.search(r"<ul\b", text, flags=re.IGNORECASE):
        text = re.sub(
            r"<ul>\s*(.*?)\s*</ul>",
            lambda match: "<br>".join(
                f"- {convert_inline_html(item.strip())}"
                for item in re.findall(r"<li>(.*?)</li>", match.group(1), flags=re.IGNORECASE | re.DOTALL)
            ),
            text,
            count=1,
            flags=re.IGNORECASE | re.DOTALL,
        )

    text = re.sub(
        r"<code>(.*?)</code>",
        lambda match: f"`{match.group(1).strip()}`",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",
        lambda match: f"[{convert_inline_html(match.group(2))}]({match.group(1)})",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<em>(.*?)</em>",
        lambda match: f"_{convert_inline_html(match.group(1))}_",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    text = text.replace("<br>", "%%LINEBREAK%%")
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("%%LINEBREAK%%", "<br>")
    text = re.sub(r"\s*\n\s*", " ", text)
    text = unescape(text)
    text = re.sub(r" +", " ", text)
    return text.strip()


def table_to_markdown(table_html: str) -> str:
    rows: list[tuple[str, str]] = []
    for row_html in re.findall(r"<tr>(.*?)</tr>", table_html, flags=re.IGNORECASE | re.DOTALL):
        header = re.search(r"<th[^>]*>(.*?)</th>", row_html, flags=re.IGNORECASE | re.DOTALL)
        cell = re.search(r"<td[^>]*>(.*?)</td>", row_html, flags=re.IGNORECASE | re.DOTALL)
        if not header or not cell:
            continue
        key = convert_inline_html(header.group(1))
        value = convert_inline_html(cell.group(1))
        if not key.endswith(":") and key not in {"Credential", "Issuer", "Schema"}:
            key = key.rstrip(":")
        rows.append((key, value))

    if not rows:
        return table_html

    lines = [f"- **{normalize_label(key)}**: {value}" for key, value in rows]
    return "\n".join(lines)


def normalize_label(label: str) -> str:
    label = label.strip()
    if label.startswith("**") and label.endswith("**"):
        label = label[2:-2]
    return label.rstrip(":")


def convert_tables(content: str) -> str:
    def replace_table(match: re.Match[str]) -> str:
        return table_to_markdown(match.group(0))

    return re.sub(r"<table>.*?</table>", replace_table, content, flags=re.IGNORECASE | re.DOTALL)


def fix_overview_tables(content: str) -> str:
    return EMPTY_OVERVIEW_TABLE.sub("| | |\n| --- | --- |\n| **", content)


def fix_misc(content: str) -> str:
    for old, new in BOOKMARK_REPLACEMENTS.items():
        content = content.replace(old, new)
    content = re.sub(r"<br\s*/?\s*>\s*</?\s*br\s*>", "<br>", content, flags=re.IGNORECASE)
    content = content.replace("Licence/code>", "</code>")
    return content


def process_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    updated = original
    updated = convert_tables(updated)
    updated = fix_misc(updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        print(f"updated {path}")
    else:
        print(f"unchanged {path}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for relative in FILES:
        process_file(root / relative)
    return 0


if __name__ == "__main__":
    sys.exit(main())
