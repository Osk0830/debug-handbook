# Module25 Cheatsheet

## デバッグ基本フロー

```text
再現 → 観測 → 仮説 → 検証 → 修正 → 再確認 → 共有
```

## 最初に確認する情報

- 発生時刻
- URL / 操作
- ユーザー・権限
- 入力値
- 期待値と実際値
- HTTPステータス
- Request ID
- 直前の変更

## 基本コマンド

```bash
curl -i URL
curl -sS URL | jq .
docker compose ps
docker compose logs --tail=200 SERVICE
git diff
git log --oneline --decorate -20
git bisect start
rg -n 'ERROR|Exception|Fatal'
tail -f /path/to/log
```
