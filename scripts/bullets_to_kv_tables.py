#!/usr/bin/env python3
"""Convert key/value bullet lists back to two-column markdown tables."""

from __future__ import annotations

import re
import sys
from pathlib import Path

FILES = [
    Path("docs/governance/business/digital-business-card-v1.md"),
    Path("docs/governance/business/municipal-services-digital-letter-of-authorization.md"),
    Path("docs/governance/business/rental-property-business-licence.md"),
]

KV_BULLET = re.compile(r"^- \*\*(.+?)\*\*: (.*)$")
BLOCK = re.compile(
    r"(?:^- \*\*.+?\*\*: .*(?:\n|$))+(?:\n)?",
    re.MULTILINE,
)


def bullets_to_table(block: str) -> str:
    rows: list[str] = []
    for line in block.strip().splitlines():
        match = KV_BULLET.match(line)
        if not match:
            continue
        label = match.group(1).strip()
        value = match.group(2).strip()
        rows.append(f"| **{label}** | {value} |")
    if not rows:
        return block
    return "| | |\n| --- | --- |\n" + "\n".join(rows) + "\n"


def convert(content: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return bullets_to_table(match.group(0))

    return BLOCK.sub(replace, content)


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
