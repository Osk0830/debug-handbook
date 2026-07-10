# ログ形式を読み解く


## Nginx combined形式

```text
127.0.0.1 - - [10/Jul/2026:14:20:01 +0900] "GET /api/users HTTP/1.1" 500 128 "-" "curl/8.7.1"
```

代表フィールド:

1. client IP
2. user
3. timestamp
4. request line
5. status
6. response size
7. referer
8. user agent

## PHPログ

```text
[10-Jul-2026 14:20:01 Asia/Tokyo] PHP Fatal error: Uncaught TypeError ...
```

確認:

- severity
- exception class
- message
- file
- line
- stack trace

## JSON Lines

```json
{"timestamp":"2026-07-10T14:20:01+09:00","level":"error","request_id":"abc123","message":"payment failed"}
```

1行1JSONなら`jq`で扱えます。

```bash
jq -c 'select(.level == "error")' app.jsonl
```

## Key-Value

```text
time=2026-07-10T14:20:01+09:00 level=error request_id=abc123 status=500
```

## 形式を先に理解する

列位置を誤ると、ステータス・サイズ・時刻を取り違えます。

ログ設定を確認し、フィールド定義を書き出してから集計します。
