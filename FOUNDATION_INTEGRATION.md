# Foundation Patch 反映手順

## 追加されるもの

- `docs/module00-learning-guide/`
- `docs/project/WRITING_GUIDELINES.md`
- `docs/project/MODULE_TEMPLATE.md`
- `docs/project/README.md`
- `docs/references/`
- `docs/assets/`
- `_base/module-template/`

## mkdocs.ymlへ追加

`nav:` の先頭付近へ追加します。

```yaml
  - Module00 学習ガイド:
      - Overview: module00-learning-guide/README.md
      - この教材の読み方: module00-learning-guide/lessons/lesson01-how-to-use-this-book.md
      - 学習環境の確認: module00-learning-guide/lessons/lesson02-environment-check.md
      - 毎日の学習ルーティン: module00-learning-guide/lessons/lesson03-daily-routine.md
      - 学習ログの残し方: module00-learning-guide/lessons/lesson04-learning-log.md
      - 実案件を教材へ戻す方法: module00-learning-guide/lessons/lesson05-feedback-loop.md
      - Cheatsheet: module00-learning-guide/cheatsheet.md
      - FAQ: module00-learning-guide/faq.md
      - Troubleshooting: module00-learning-guide/troubleshooting.md
      - Resources: module00-learning-guide/resources.md

  - Project:
      - Overview: project/README.md
      - PROJECT: project/PROJECT.md
      - Book Architecture: project/BOOK_ARCHITECTURE.md
      - Style Guide: project/STYLE_GUIDE.md
      - Writing Guidelines: project/WRITING_GUIDELINES.md
      - Module Template: project/MODULE_TEMPLATE.md
      - Contributing: project/CONTRIBUTING.md
      - Roadmap: project/ROADMAP.md
      - Changelog: project/CHANGELOG.md

  - References:
      - Overview: references/README.md
      - CLI / Linux: references/cli-linux.md
      - Git: references/git.md
      - Docker: references/docker.md
      - PHP / Xdebug: references/php-xdebug.md
      - MySQL / SQL: references/mysql-sql.md
      - HTTP / curl: references/http-curl.md
      - VS Code: references/vscode.md
      - WordPress: references/wordpress.md
      - React / JavaScript: references/react-javascript.md
```

`docs_dir: docs` を使っているため、nav内では `docs/` を付けません。

## README.mdへ追加

Module一覧の先頭へ:

```markdown
|00|[学習ガイド](docs/module00-learning-guide/README.md)|
```

Module一覧の後へ:

```markdown
## Project Documents

- [教材設計](docs/project/README.md)
- [執筆ガイド](docs/project/WRITING_GUIDELINES.md)
- [Moduleテンプレート](docs/project/MODULE_TEMPLATE.md)
- [公式リファレンス](docs/references/README.md)
```

## 構文・表示確認

```bash
mkdocs build --strict
mkdocs serve
```

## コミット例

```bash
git add .
git commit -m "Add handbook architecture and module template"
git push
```
