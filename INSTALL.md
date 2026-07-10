# Module26反映手順

ZIPをリポジトリ直下へ展開したあと、次を実行します。

```bash
bash scripts/install_module26.sh .
```

このスクリプトは現在の`mkdocs.yml`を保持したままModule26を追記し、
`mkdocs.yml.before-module26`へバックアップを作ります。

すでにModule26が登録済みの場合は重複追記しません。

## 手動確認

```bash
git status
git diff -- mkdocs.yml
mkdocs build --strict
```
