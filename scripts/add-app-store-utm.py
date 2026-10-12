#!/usr/bin/env python3
"""Add UTM parameters to Shopify App Store links in HTML files.

Rewrites <a href="https://apps.shopify.com/..."> (any href to that host)
outside JSON-LD. Existing query parameters and fragments are kept. An href
that already has a utm_ query parameter is left unchanged.

utm_medium comes from the page path, first match wins:
  guides/                         -> guide
  tools/                          -> tool
  compare/ or a "-vs-" directory  -> compare
  /index.html (site root)         -> home
  everything else                 -> other

utm_campaign is the page directory slug. The site root uses "home".

Query separators are written as "&amp;" so the attribute matches the rest
of this site. Browsers decode that to "&".
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://apps.shopify.com/"

JSONLD_RE = re.compile(
    r'<script\b[^>]*\btype\s*=\s*(["\'])application/ld\+json\1[^>]*>.*?</script>',
    re.IGNORECASE | re.DOTALL,
)
HREF_RE = re.compile(
    r'href\s*=\s*(["\'])(' + re.escape(HOST) + r'[^"\']*)\1',
    re.IGNORECASE,
)
AMP_RE = re.compile(r"&amp;", re.IGNORECASE)


def classify(rel: Path) -> tuple[str, str]:
    parts = rel.parts
    if parts[-1] == "index.html" and len(parts) >= 2:
        slug = parts[-2]
    elif parts[-1] == "index.html":
        slug = "home"
    elif len(parts) >= 2:
        slug = parts[-2]
    else:
        slug = Path(parts[-1]).stem

    dirs = [part.lower() for part in parts[:-1]]
    if "guides" in dirs:
        medium = "guide"
    elif "tools" in dirs:
        medium = "tool"
    elif "compare" in dirs or any("-vs-" in directory for directory in dirs):
        medium = "compare"
    elif rel.as_posix() == "index.html":
        medium = "home"
    else:
        medium = "other"
    return medium, slug


def utm_query(medium: str, campaign: str) -> str:
    medium_value = quote(medium, safe="")
    campaign_value = quote(campaign, safe="-._~")
    return (
        "utm_source=momiji-site"
        f"&amp;utm_medium={medium_value}"
        f"&amp;utm_campaign={campaign_value}"
    )


def add_utm(raw_url: str, medium: str, campaign: str) -> str | None:
    if "#" in raw_url:
        before, fragment = raw_url.split("#", 1)
        fragment = "#" + fragment
    else:
        before, fragment = raw_url, ""

    if "?" in before:
        base, query = before.split("?", 1)
    else:
        base, query = before, ""

    if not base.lower().startswith(HOST):
        return None

    decoded_query = AMP_RE.sub("&", query)
    keys = [part.split("=", 1)[0] for part in decoded_query.split("&") if part]
    if any(key.lower().startswith("utm_") for key in keys):
        return None

    addition = utm_query(medium, campaign)
    if query:
        return f"{base}?{query}&amp;{addition}{fragment}"
    return f"{base}?{addition}{fragment}"


def split_jsonld(html: str) -> list[tuple[bool, str]]:
    parts: list[tuple[bool, str]] = []
    last = 0
    for match in JSONLD_RE.finditer(html):
        if match.start() > last:
            parts.append((False, html[last : match.start()]))
        parts.append((True, match.group(0)))
        last = match.end()
    if last < len(html):
        parts.append((False, html[last:]))
    return parts


def jsonld_blocks(html: str) -> list[str]:
    return [part for is_jsonld, part in split_jsonld(html) if is_jsonld]


def transform(html: str, medium: str, campaign: str) -> tuple[str, int, int]:
    changed = 0
    skipped = 0
    chunks: list[str] = []
    for is_jsonld, part in split_jsonld(html):
        if is_jsonld:
            chunks.append(part)
            continue

        def replace(match: re.Match[str]) -> str:
            nonlocal changed, skipped
            quote_char = match.group(1)
            updated = add_utm(match.group(2), medium, campaign)
            if updated is None:
                skipped += 1
                return match.group(0)
            changed += 1
            return f"href={quote_char}{updated}{quote_char}"

        chunks.append(HREF_RE.sub(replace, part))
    return "".join(chunks), changed, skipped


def strip_added(html: str, medium: str, campaign: str) -> str:
    addition = utm_query(medium, campaign)
    html = html.replace("&amp;" + addition, "")
    html = html.replace("?" + addition, "")
    return html


def self_test() -> None:
    assert classify(Path("guides/eudr-scope-2026-2027/index.html")) == (
        "guide",
        "eudr-scope-2026-2027",
    )
    assert classify(Path("guides/clp-vs-ghs/index.html")) == ("guide", "clp-vs-ghs")
    assert classify(Path("tools/po-box-address-checker/index.html")) == (
        "tool",
        "po-box-address-checker",
    )
    assert classify(Path("tools/index.html")) == ("tool", "tools")
    assert classify(Path("compare/article-vs-website-content-extractor/index.html")) == (
        "compare",
        "article-vs-website-content-extractor",
    )
    assert classify(Path("notes/rss-vs-apple-podcasts-scraper/index.html")) == (
        "compare",
        "rss-vs-apple-podcasts-scraper",
    )
    assert classify(Path("index.html")) == ("home", "home")
    assert classify(Path("access-audit/index.html")) == ("other", "access-audit")
    assert classify(Path("shopify-review/momiji-address-guard/index.html")) == (
        "other",
        "momiji-address-guard",
    )

    plain = add_utm(HOST + "foo", "guide", "bar")
    assert plain == (
        HOST + "foo?utm_source=momiji-site&amp;utm_medium=guide&amp;utm_campaign=bar"
    )
    queried = add_utm(HOST + "foo?x=1&amp;y=2#section", "tool", "bar")
    assert queried == (
        HOST
        + "foo?x=1&amp;y=2&amp;utm_source=momiji-site&amp;utm_medium=tool&amp;utm_campaign=bar#section"
    )
    fragment = add_utm(HOST + "foo#utm_source", "home", "home")
    assert fragment == (
        HOST
        + "foo?utm_source=momiji-site&amp;utm_medium=home&amp;utm_campaign=home#utm_source"
    )
    assert add_utm(HOST + "foo?utm_source=already", "guide", "bar") is None
    assert add_utm(HOST + "foo?x=1&amp;utm_medium=email#z", "guide", "bar") is None
    assert add_utm(HOST + "partners/momiji-shop", "other", "access-audit") == (
        HOST
        + "partners/momiji-shop?utm_source=momiji-site&amp;utm_medium=other&amp;utm_campaign=access-audit"
    )

    sample = """<script type="application/ld+json">
{"url":"https://apps.shopify.com/foo"}
</script>
<p><a class="cta" href="https://apps.shopify.com/foo">Install app</a></p>
<p><a href='https://apps.shopify.com/foo?ref=1#docs'>Docs</a></p>
<pre>{"appUrls":["https://apps.shopify.com/foo"]}</pre>
"""
    updated, changed, skipped = transform(sample, "guide", "sample-page")
    assert changed == 2 and skipped == 0
    assert jsonld_blocks(sample) == jsonld_blocks(updated)
    assert '{"url":"https://apps.shopify.com/foo"}' in updated
    assert '{"appUrls":["https://apps.shopify.com/foo"]}' in updated
    assert 'class="cta"' in updated
    assert ">Install app</a>" in updated
    assert strip_added(updated, "guide", "sample-page") == sample

    twice, changed_again, skipped_again = transform(updated, "guide", "sample-page")
    assert twice == updated
    assert changed_again == 0 and skipped_again == 2


def html_files() -> list[Path]:
    files = [
        path
        for path in ROOT.rglob("*.html")
        if ".git" not in path.relative_to(ROOT).parts
    ]
    return sorted(files)


def main() -> int:
    self_test()
    totals = {"files": 0, "changed_files": 0, "links": 0, "skipped": 0, "jsonld": 0}
    by_medium: dict[str, int] = {}
    planned: list[tuple[Path, str]] = []

    for path in html_files():
        original = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        medium, campaign = classify(rel)
        updated, changed, skipped = transform(original, medium, campaign)
        blocks_before = jsonld_blocks(original)
        blocks_after = jsonld_blocks(updated)
        totals["jsonld"] += len(blocks_before)
        if blocks_before != blocks_after:
            print(f"JSON-LD changed in {rel}", file=sys.stderr)
            return 1
        if updated != original and strip_added(updated, medium, campaign) != original:
            print(f"Non-link bytes changed in {rel}", file=sys.stderr)
            return 1
        totals["files"] += 1
        totals["links"] += changed
        totals["skipped"] += skipped
        if changed:
            totals["changed_files"] += 1
            by_medium[medium] = by_medium.get(medium, 0) + changed
            planned.append((path, updated))

    for path, updated in planned:
        path.write_text(updated, encoding="utf-8")

    print(f"html_files={totals['files']}")
    print(f"files_changed={totals['changed_files']}")
    print(f"links_changed={totals['links']}")
    print(f"links_skipped_existing_utm={totals['skipped']}")
    print(f"jsonld_blocks={totals['jsonld']}")
    print("jsonld_unchanged=true")
    for medium in ("guide", "tool", "compare", "home", "other"):
        print(f"medium_{medium}={by_medium.get(medium, 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
