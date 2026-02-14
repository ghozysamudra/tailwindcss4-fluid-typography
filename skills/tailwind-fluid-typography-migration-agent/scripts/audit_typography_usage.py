#!/usr/bin/env python3
"""Audit legacy Tailwind text-size chains for migration planning.

Finds class/className/template class attributes containing text-size utilities and
responsive variants, then prints JSON findings.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TEXT_TOKEN = re.compile(r"^(?:sm:|md:|lg:|xl:|2xl:)?text-(?:xs|sm|base|lg|xl|[2-9]xl)$")

ATTR_RE = re.compile(
    r"(?:class|className)\s*=\s*(?:\"([^\"]+)\"|\{`([^`]+)`\})",
    re.MULTILINE,
)


def scan_file(file_path: Path) -> list[dict]:
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    findings: list[dict] = []

    for match in ATTR_RE.finditer(content):
        class_value = match.group(1) or match.group(2) or ""
        tokens = class_value.split()
        text_tokens = [token for token in tokens if TEXT_TOKEN.match(token)]

        if len(text_tokens) < 2:
            continue

        line = content.count("\n", 0, match.start()) + 1
        findings.append(
            {
                "file": str(file_path),
                "line": line,
                "text_tokens": text_tokens,
                "class_value": class_value,
            }
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit Tailwind typography utility chains"
    )
    parser.add_argument("path", help="Root path to scan")
    parser.add_argument(
        "--include",
        nargs="*",
        default=[".astro", ".tsx", ".jsx", ".html", ".vue"],
        help="File extensions to scan",
    )
    args = parser.parse_args()

    root = Path(args.path).resolve()
    exts = set(args.include)

    all_findings: list[dict] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in exts:
            continue
        all_findings.extend(scan_file(path))

    output = {
        "root": str(root),
        "count": len(all_findings),
        "findings": all_findings,
    }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
