# タイムアウト・リトライ・Rate Limit


## タイムアウトを分解する

- DNS
- TCP connect
- TLS handshake
- request upload
- server processing
- first byte
- response download

curl:

```bash
curl -sS -o /dev/null   -w 'dns=%{time_namelookup}
connect=%{time_connect}
tls=%{time_appconnect}
ttfb=%{time_starttransfer}
total=%{time_total}
'   https://api.example.com/health
```

## Retry

安全にリトライしやすい:

- GET
- HEAD
- 冪等なPUT
- Idempotency Key付きPOST

危険:

- 決済
- 注文
- メール送信
- 在庫減算

## 429

確認:

```text
Retry-After
RateLimit-Limit
RateLimit-Remaining
RateLimit-Reset
```

## Backoff

```text
1秒 → 2秒 → 4秒 → 8秒
```

Jitterを加え、同時再試行を避けます。

## デバッグ時の注意

ブレークポイント停止中に外部通信やProxyがタイムアウトすることがあります。呼び出し前後で停止位置を分けます。
