#!/usr/bin/env python3
"""Dependency-free structural checks for the Clear Story Presentations Agent Skill.

Usage: python3 scripts/check_skill.py

This is **not** a model-quality evaluation, security audit or slide-rendering test.
It checks structure, metadata, links and evaluation fixture completeness only.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def file_text(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        ERRORS.append(f"Missing required file: {relative}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeError, OSError) as exc:
        ERRORS.append(f"Unreadable UTF-8 text file {relative}: {exc}")
        return ""


def parse_frontmatter(raw: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", raw, re.S)
    if not match:
        ERRORS.append("SKILL.md has no YAML frontmatter bounded by --- lines")
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        m = re.fullmatch(r"([a-z][a-z0-9-]*):\s*(.*?)\s*", line)
        if not m:
            ERRORS.append(f"Unsupported or malformed frontmatter entry: {line!r}")
            continue
        key, value = m.groups()
        # Supports the project's simple single-line YAML scalar metadata.
        if value[:1] in ('"', "'") and value[-1:] == value[:1]:
            value = value[1:-1]
        if key in data:
            ERRORS.append(f"Duplicate frontmatter field: {key}")
        data[key] = value
    return data


main = file_text("SKILL.md")
if main:
    front = parse_frontmatter(main)
    name = front.get("name", "")
    description = front.get("description", "")
    check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)),
          f"Invalid skill name: {name!r}")
    check(len(name) <= 64, "Skill name exceeds 64 characters")
    check(name == ROOT.name, f"Skill name {name!r} != folder {ROOT.name!r}")
    check(1 <= len(description) <= 1024,
          f"Skill description must contain 1–1024 characters; got {len(description)}")
    check(0 < len(main.splitlines()) < 500,
          "SKILL.md should be present and below 500 lines")
    check("when" in description.lower() or "use for" in description.lower(),
          "Description should specify when the skill applies")

# Validate all local Markdown hyperlinks across project documentation, skipping
# fenced-code samples (which include deliberately generic example paths).
doc_paths = [ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md"))
doc_paths += sorted((ROOT / "docs").glob("*.md"))
doc_paths += sorted((ROOT / "examples").glob("*.md"))
doc_paths += sorted(ROOT.glob("*.md"))
doc_paths = list(dict.fromkeys(doc_paths))
for path in doc_paths:
    try:
        source = path.read_text(encoding="utf-8")
    except Exception as exc:
        ERRORS.append(f"Cannot read {path.relative_to(ROOT)}: {exc}")
        continue
    source = re.sub(r"(?ms)^```.*?^```\s*$", "", source)
    # Standard Markdown links, including relative anchors; ignores images as URL-only.
    for target in re.findall(r"!?(?:\[[^\]\n]*\])\(([^)\n]+)\)", source):
        target = target.strip().split(" ")[0].strip("<>")
        parsed = urlparse(target)
        if parsed.scheme in ("http", "https", "mailto") or target.startswith("#"):
            continue
        if parsed.scheme or target.startswith("//"):
            continue
        candidate = (path.parent / unquote(parsed.path)).resolve()
        if not candidate.is_relative_to(ROOT.resolve()) or not candidate.exists():
            ERRORS.append(f"Broken relative link in {path.relative_to(ROOT)}: {target}")

for rel in sorted(set(re.findall(r"`((?:references|evals|scripts)/[^`\n ]+)`", main))):
    if not (ROOT / rel).is_file() and not (ROOT / rel).is_dir():
        ERRORS.append(f"SKILL.md mentions missing resource: {rel}")

references = sorted((ROOT / "references").glob("*.md"))
check(len(references) == 11, f"Expected 11 focused reference files, got {len(references)}")
for path in references:
    check(len(path.read_text(encoding="utf-8").strip()) >= 250,
          f"Reference appears empty: {path.name}")

for rel in ["README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md",
            "CHANGELOG.md", "docs/EVALUATION.md", "docs/SOURCES.md",
            ".github/workflows/check-skill.yml", "examples/launch-decision-storyboard.md"]:
    file_text(rel)

cases = []
raw = file_text("evals/evals.json")
if raw:
    try:
        parsed = json.loads(raw)
        check(parsed.get("skill_name") == ROOT.name,
              "Eval file skill_name must match directory")
        cases = parsed.get("evals", [])
        check(isinstance(cases, list), "evals must be an array")
        if isinstance(cases, list):
            check(len(cases) >= 9, f"Expected 9+ evaluation cases; got {len(cases)}")
            ids = []
            for i, case in enumerate(cases):
                if not isinstance(case, dict):
                    ERRORS.append(f"Eval {i} must be a JSON object")
                    continue
                for field in ("id", "prompt", "expected_behavior"):
                    check(isinstance(case.get(field), str) and len(case[field].strip()) > 9,
                          f"Eval {i} missing meaningful {field}")
                ids.append(case.get("id"))
            check(len(ids) == len(set(ids)), "Evaluation case ids must be unique")
    except (ValueError, TypeError) as exc:
        ERRORS.append(f"Invalid evals/evals.json: {exc}")

check("MIT License" in file_text("LICENSE"), "Expected an MIT LICENSE file")

if ERRORS:
    print("FAIL — package validation")
    for error in ERRORS:
        print(f"  ERROR: {error}")
    sys.exit(1)
print(f"PASS — structural validation: {len(references)} references, "
      f"{len(cases)} manual evaluation cases, {len(doc_paths)} documentation files")
print("NOTE — No model output, link reachability or slide rendering was evaluated.")
for warning in WARNINGS:
    print(f"  WARNING: {warning}")
