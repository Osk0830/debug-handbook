#!/usr/bin/env python3
"""既存のmkdocs.ymlを保持したままModule26のnavを追記する。"""
from pathlib import Path
import shutil
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "mkdocs.yml")
if not path.exists():
    raise SystemExit(f"not found: {path}")

text = path.read_text(encoding="utf-8")
marker = "- Module26 コマンドチートシート:"
if marker in text:
    print("Module26 navigation already exists. No changes made.")
    raise SystemExit(0)

backup = path.with_suffix(path.suffix + ".before-module26")
shutil.copy2(path, backup)

block = "- Module26 コマンドチートシート:\n  - 概要: module26-command-cheatsheet/README.md\n  - Lesson01 CLI・ファイル・テキスト操作: module26-command-cheatsheet/lessons/lesson01-cli-files-and-text.md\n  - 'Lesson02 検索: rg・grep・find': module26-command-cheatsheet/lessons/lesson02-search-rg-grep-find.md\n  - Lesson03 HTTP・curl・ネットワーク: module26-command-cheatsheet/lessons/lesson03-http-curl-network.md\n  - Lesson04 プロセス・ポート・システム: module26-command-cheatsheet/lessons/lesson04-process-port-system.md\n  - Lesson05 Docker・Docker Compose: module26-command-cheatsheet/lessons/lesson05-docker-compose.md\n  - Lesson06 Git・GitHub: module26-command-cheatsheet/lessons/lesson06-git-github.md\n  - Lesson07 PHP・Composer・WordPress: module26-command-cheatsheet/lessons/lesson07-php-composer-wordpress.md\n  - Lesson08 Node.js・フロントエンド: module26-command-cheatsheet/lessons/lesson08-node-frontend.md\n  - Lesson09 MySQL・SQL: module26-command-cheatsheet/lessons/lesson09-mysql-sql.md\n  - Lesson10 ログ解析・障害対応ワークフロー: module26-command-cheatsheet/lessons/lesson10-logs-incident-workflow.md\n  - Lab01 障害調査コマンド実践: module26-command-cheatsheet/labs/lab01-incident-command-workflow.md\n  - Lab02 ローカル環境診断: module26-command-cheatsheet/labs/lab02-local-environment-diagnosis.md\n  - 演習: module26-command-cheatsheet/exercises/beginner.md\n  - 解答: module26-command-cheatsheet/exercises/answers.md\n  - Cheatsheet: module26-command-cheatsheet/cheatsheet.md\n  - FAQ: module26-command-cheatsheet/faq.md\n  - Troubleshooting: module26-command-cheatsheet/troubleshooting.md\n  - Resources: module26-command-cheatsheet/resources.md\n"
if not text.endswith("\n"):
    text += "\n"
path.write_text(text + block, encoding="utf-8")
print(f"Updated: {path}")
print(f"Backup:  {backup}")
