# 目的別クイックリファレンス

## 今いる場所を確認したい

```bash
pwd
ls -la
```

## コードから文字列を探したい

```bash
rg -n 'keyword'
rg -C 3 'keyword'
rg 'keyword' -g '*.php'
```

## APIレスポンスを確認したい

```bash
curl -i URL
curl -sS URL | jq .
curl -v URL
```

## ポートを使っているプロセスを知りたい

```bash
lsof -nP -iTCP:PORT -sTCP:LISTEN
```

## Dockerコンテナの状態を確認したい

```bash
docker compose ps
docker compose logs --tail=200 SERVICE
docker compose exec SERVICE sh
```

## Gitの変更内容を確認したい

```bash
git status
git diff
git diff --staged
git log --oneline --graph -20
```

## PHP環境を確認したい

```bash
php -v
php --ini
php -m
php -l file.php
```

## Node.js環境を確認したい

```bash
node -v
pnpm -v
pnpm why PACKAGE
```

## SQLが遅い理由を確認したい

```sql
EXPLAIN SELECT ...;
EXPLAIN ANALYZE SELECT ...;
SHOW INDEX FROM table_name;
```

## ログからエラーを探したい

```bash
rg -n 'ERROR|Exception|Fatal' logs/
tail -f app.log
```

## 破壊的操作の前

```text
1. pwd / 接続先 / ブランチを確認
2. 読み取りコマンドで対象を確認
3. バックアップまたは復旧方法を確認
4. 実行結果を記録
```
