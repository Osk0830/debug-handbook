# Request ID・Trace IDでログをつなぐ


## Request ID

1リクエストを複数ログで追跡する識別子です。

```text
X-Request-ID: 4c9a...
```

## 生成

入口で受け取り、なければ生成します。

PHP例:

```php
$requestId = $_SERVER['HTTP_X_REQUEST_ID'] ?? bin2hex(random_bytes(16));
header('X-Request-ID: ' . $requestId);
```

## ログへ含める

```php
error_log(json_encode([
    'level' => 'error',
    'request_id' => $requestId,
    'message' => 'order failed',
]));
```

## 下流へ伝播

外部APIや別サービスへ送ります。

```http
X-Request-ID: 4c9a...
```

## Trace IDとの違い

分散トレーシングでは、Trace ID・Span IDを使って複数サービス間の処理を表現します。

```text
Trace
 ├─ Web
 ├─ API
 ├─ Database
 └─ External API
```

## 検索

```bash
rg '4c9a...' logs/
docker compose logs | rg '4c9a...'
```

## 個人情報を識別子にしない

メールアドレスや電話番号をRequest IDとして使わず、推測困難なランダム値を使います。
