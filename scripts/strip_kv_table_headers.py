#!/usr/bin/env python3
"""Convert two-column key/value markdown tables to bullet lists."""

from __future__ import annotations

import re
import sys
from pathlib import Path

FILES = [
    Path("docs/governance/business/digital-business-card-v1.md"),
    Path("docs/governance/business/municipal-services-digital-letter-of-authorization.md"),
    Path("docs/governance/business/rental-property-business-licence.md"),
]

TABLE_START = re.compile(
    r"^\| \| \|$\n^\| --- \| --- \|$\n((?:^\| .+\|$\n?)+)",
    re.MULTILINE,
)
ROW = re.compile(r"^\| (.+?) \| (.+?) \|$")


def normalize_label(cell: str) -> str:
    label = cell.strip()
    if label.startswith("**") and label.endswith("**"):
        label = label[2:-2]
    return label.rstrip(":")


def table_to_bullets(block: str) -> str:
    bullets: list[str] = []
    for line in block.strip().splitlines():
        match = ROW.match(line)
        if not match:
            continue
        label = normalize_label(match.group(1))
        value = match.group(2).strip()
        bullets.append(f"- **{label}**: {value}")
    return "\n".join(bullets) + "\n"


def convert(content: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return table_to_bullets(match.group(1))

    return TABLE_START.sub(replace, content)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for relative in FILES:
        path = root / relative
        original = path.read_text(encoding="utf-8")
        updated = convert(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            print(f"updated {relative}")
        else:
            print(f"unchanged {relative}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
