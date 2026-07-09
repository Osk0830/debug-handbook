# NEXT_STEPS.md

## すぐにやること

- [ ] `.DS_Store` をGit管理から外す
- [ ] `README.md` の改行を修正する
- [ ] `mkdocs.yml` を正しいYAML形式に修正する
- [ ] `mkdocs serve` でローカル表示確認する

## コマンド

```bash
git rm --cached .DS_Store
git add .gitignore README.md mkdocs.yml NEXT_STEPS.md
git commit -m "Fix repository metadata and MkDocs config"
git push
```

## MkDocs確認

```bash
pip install mkdocs-material
mkdocs serve
```

ブラウザで以下を開きます。

```text
http://127.0.0.1:8000/
```

## 次フェーズ

- Module01から学習開始
- 学習中に分からなかった点を該当Lessonに追記
- 実案件で使ったコマンドをcheatsheetへ追加
- ハマった内容をcase studyへ追加
