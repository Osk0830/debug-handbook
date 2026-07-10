#!/usr/bin/env python3
"""
docs/module22-* ～ docs/module25-* を走査し、
実在するMarkdownだけを mkdocs.yml の nav に追加します。

- 既存設定を保持
- Module26の直前へ追加
- 重複登録を防止
- mkdocs.yml.before-modules22-25 を作成
"""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import sys


MODULE_NAMES = {
    22: "Module22 Xdebug",
    23: "Module23 APIデバッグ",
    24: "Module24 ログ解析",
    25: "Module25 実践デバッグ100本ノック",
}

SPECIAL_LABELS = {
    "README.md": "概要",
    "cheatsheet.md": "Cheatsheet",
    "faq.md": "FAQ",
    "troubleshooting.md": "Troubleshooting",
    "resources.md": "Resources",
}

SECTION_ORDER = ("lessons", "labs", "exercises")
ROOT_ORDER = ("README.md",)


def yaml_quote(value: str) -> str:
    """YAMLキーとして安全な文字列へ変換する。"""
    if (
        ":" in value
        or "#" in value
        or value.startswith(("-", "?", "!", "&", "*", "{", "[", "@", "`"))
        or value.strip() != value
    ):
        return "'" + value.replace("'", "''") + "'"
    return value


def first_heading(path: Path) -> str | None:
    """Markdownの最初のH1を取得する。"""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^#\s+(.+?)\s*$", line)
            if match:
                return match.group(1).strip()
    except UnicodeDecodeError:
        return None
    return None


def natural_key(path: Path) -> list[object]:
    """lesson2よりlesson10が後になる自然順ソート。"""
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.as_posix())
    ]


def label_for(path: Path, module_dir: Path) -> str:
    rel = path.relative_to(module_dir)

    if rel.as_posix() in SPECIAL_LABELS:
        return SPECIAL_LABELS[rel.as_posix()]

    heading = first_heading(path)
    if heading:
        return heading

    stem = path.stem.replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() for word in stem.split())


def collect_markdown(module_dir: Path) -> list[Path]:
    result: list[Path] = []

    for filename in ROOT_ORDER:
        path = module_dir / filename
        if path.is_file():
            result.append(path)

    for section in SECTION_ORDER:
        section_dir = module_dir / section
        if section_dir.is_dir():
            result.extend(sorted(section_dir.glob("*.md"), key=natural_key))

    for filename in ("cheatsheet.md", "faq.md", "troubleshooting.md", "resources.md"):
        path = module_dir / filename
        if path.is_file():
            result.append(path)

    # 上記以外のMarkdownも漏らさない
    known = {p.resolve() for p in result}
    extras = [
        p for p in module_dir.rglob("*.md")
        if p.resolve() not in known
    ]
    result.extend(sorted(extras, key=natural_key))

    return result


def find_module_dir(docs_dir: Path, module_no: int) -> Path:
    candidates = sorted(
        [p for p in docs_dir.glob(f"module{module_no}-*") if p.is_dir()],
        key=natural_key,
    )

    if not candidates:
        raise SystemExit(
            f"Module{module_no} directory not found under {docs_dir}\n"
            f"Expected: docs/module{module_no}-*/"
        )

    if len(candidates) > 1:
        names = "\n".join(f"  - {p}" for p in candidates)
        raise SystemExit(
            f"Multiple Module{module_no} directories found:\n{names}\n"
            "Please leave only the intended directory."
        )

    return candidates[0]


def build_block(docs_dir: Path) -> str:
    lines: list[str] = []

    for module_no in range(22, 26):
        module_dir = find_module_dir(docs_dir, module_no)
        markdown_files = collect_markdown(module_dir)

        if not markdown_files:
            raise SystemExit(f"No Markdown files found: {module_dir}")

        lines.append(f"- {yaml_quote(MODULE_NAMES[module_no])}:")
        for path in markdown_files:
            label = label_for(path, module_dir)
            nav_path = path.relative_to(docs_dir).as_posix()
            lines.append(f"  - {yaml_quote(label)}: {nav_path}")

    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    config = repo_root / "mkdocs.yml"
    docs_dir = repo_root / "docs"

    if not config.is_file():
        raise SystemExit(f"mkdocs.yml not found: {config}")
    if not docs_dir.is_dir():
        raise SystemExit(f"docs directory not found: {docs_dir}")

    original = config.read_text(encoding="utf-8")

    existing = [
        no for no in range(22, 26)
        if re.search(rf"(?m)^-\s+Module{no}\b", original)
    ]
    if existing:
        joined = ", ".join(f"Module{no}" for no in existing)
        raise SystemExit(
            f"Already registered in mkdocs.yml: {joined}\n"
            "No changes were made. Remove duplicate/incomplete entries first."
        )

    block = build_block(docs_dir)

    module26_match = re.search(
        r"(?m)^-\s+Module26(?:\s|:)",
        original,
    )
    if not module26_match:
        raise SystemExit(
            "Module26 entry was not found in mkdocs.yml.\n"
            "No changes were made."
        )

    updated = (
        original[:module26_match.start()]
        + block
        + original[module26_match.start():]
    )

    backup = repo_root / "mkdocs.yml.before-modules22-25"
    shutil.copy2(config, backup)
    config.write_text(updated, encoding="utf-8")

    print("Updated mkdocs.yml")
    print(f"Backup: {backup}")
    print("")
    print("Added:")
    for no in range(22, 26):
        module_dir = find_module_dir(docs_dir, no)
        count = len(collect_markdown(module_dir))
        print(f"  Module{no}: {count} pages ({module_dir.name})")
    print("")
    print("Next:")
    print("  mkdocs build --strict")
    print("  git diff -- mkdocs.yml")


if __name__ == "__main__":
    main()
