# ログ解析チートシート

## 末尾・追跡

```bash
tail -n 100 app.log
tail -F app.log
less -S app.log
```

## 検索

```bash
rg -n -C 3 'ERROR|Exception|Fatal' app.log
rg 'request-id-123' logs/
zgrep 'ERROR' app.log.2.gz
```

## 件数集計

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
awk '$9 ~ /^5/ {print}' access.log
```

## JSONログ

```bash
jq -c 'select(.level == "error")' app.jsonl
jq -c 'select(.request_id == "abc123")' app.jsonl
jq -r '.status' access.jsonl | sort | uniq -c | sort -nr
```

## Docker

```bash
docker compose logs --tail=100 app
docker compose logs -f -t nginx app db
docker compose logs --since=30m app
```

## systemd

```bash
journalctl -u nginx --since "30 minutes ago"
journalctl -u php8.3-fpm -f
journalctl -p err..alert
```

## MySQL

```sql
SHOW FULL PROCESSLIST;
SHOW ENGINE INNODB STATUS\G
SHOW VARIABLES LIKE 'slow_query_log%';
```

## 時刻

```bash
date
date -u
docker compose exec app date
```

## 基本順序

```text
発生時刻
→ URL / 処理
→ Request ID
→ Access Log
→ Application Log
→ DB / External API
→ 正常比較
```
