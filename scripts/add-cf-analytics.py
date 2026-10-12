#!/usr/bin/env python3
"""Insert the Cloudflare Web Analytics beacon immediately before </body>.

Idempotent: a page that already contains the beacon is left unchanged.
JSON-LD and every other part of the page are not modified.
"""

from __future__ import annotations

import sys
from pathlib import Path

BEACON = (
    "<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"10aeccbd602743299692f41113bc3b55\"}'></script>"
)

SKIP_DIRS = {".git"}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def html_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".html", ".htm"}:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        pages.append(path)
    return sorted(pages)


def insert_beacon(text: str) -> str | None:
    """Return new page text, or None when the beacon is already present."""
    if BEACON in text:
        return None
    idx = text.rfind("</body>")
    if idx < 0:
        raise ValueError("missing </body>")
    line_start = text.rfind("\n", 0, idx) + 1
    indent = text[line_start:idx]
    if indent.strip():
        raise ValueError("</body> is not alone on its line")
    return text[:line_start] + f"{indent}{BEACON}\n" + text[line_start:]


def beacon_immediately_before_body(text: str) -> bool:
    if text.count(BEACON) != 1:
        return False
    idx = text.rfind("</body>")
    if idx < 0:
        return False
    line_start = text.rfind("\n", 0, idx) + 1
    indent = text[line_start:idx]
    prev_end = line_start - 1
    if prev_end < 0:
        return False
    prev_start = text.rfind("\n", 0, prev_end) + 1
    return text[prev_start:prev_end] == f"{indent}{BEACON}"


def main() -> int:
    root = repo_root()
    pages = html_pages(root)
    updated = 0
    already = 0
    errors: list[str] = []

    for path in pages:
        rel = path.relative_to(root)
        text = path.read_bytes().decode("utf-8")
        try:
            updated_text = insert_beacon(text)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if updated_text is None:
            already += 1
            continue
        path.write_bytes(updated_text.encode("utf-8"))
        updated += 1

    tagged = 0
    for path in pages:
        rel = path.relative_to(root)
        text = path.read_bytes().decode("utf-8")
        if beacon_immediately_before_body(text):
            tagged += 1
        else:
            errors.append(f"{rel}: beacon is not exactly once immediately before </body>")

    print(f"html_pages={len(pages)}")
    print(f"updated={updated}")
    print(f"already_present={already}")
    print(f"tagged={tagged}")
    if errors or tagged != len(pages):
        for err in errors:
            print(err, file=sys.stderr)
        print("tagged count does not equal HTML page count", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
