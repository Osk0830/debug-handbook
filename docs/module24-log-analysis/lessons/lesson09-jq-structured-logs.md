# jqで構造化ログを解析する


## エラーだけ

```bash
jq -c 'select(.level == "error")' app.jsonl
```

## 時間範囲

```bash
jq -c '
  select(
    .timestamp >= "2026-07-10T14:00:00+09:00"
    and
    .timestamp < "2026-07-10T15:00:00+09:00"
  )
' app.jsonl
```

## Request ID

```bash
jq -c 'select(.request_id == "abc123")' app.jsonl
```

## 集計

```bash
jq -r '.status' access.jsonl | sort | uniq -c | sort -nr
```

## エラーコード別

```bash
jq -r 'select(.level == "error") | .error_code' app.jsonl \
  | sort | uniq -c | sort -nr
```

## null安全

```bash
jq -r '.user_id // "anonymous"' app.jsonl
```

## 複数条件

```bash
jq -c '
  select(
    .level == "error"
    and .service == "payment"
    and (.duration_ms // 0) > 1000
  )
' app.jsonl
```

## rawログが混ざる場合

すべての行がJSONでないと`jq`が失敗します。ログ出力形式を統一するか、JSON行だけを先に抽出します。
