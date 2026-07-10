#!/usr/bin/env bash
set -euo pipefail

repo_root="${1:-.}"
cd "$repo_root"

test -f mkdocs.yml || { echo "mkdocs.yml not found: $PWD" >&2; exit 1; }
test -d docs/module26-command-cheatsheet || {
  echo "docs/module26-command-cheatsheet not found: $PWD" >&2
  exit 1
}

python3 scripts/apply_module26_nav.py mkdocs.yml

if command -v mkdocs >/dev/null 2>&1; then
  mkdocs build --strict
else
  echo "mkdocs command not found. Navigation was updated; run mkdocs build later."
fi
