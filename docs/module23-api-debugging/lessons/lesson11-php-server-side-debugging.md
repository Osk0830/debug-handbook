# PHPサーバー側のAPIデバッグ


## 入力取得

```php
$method = $_SERVER['REQUEST_METHOD'] ?? '';
$uri = $_SERVER['REQUEST_URI'] ?? '';
$contentType = $_SERVER['CONTENT_TYPE'] ?? '';
$rawBody = file_get_contents('php://input');
```

## ヘッダー

```php
$headers = function_exists('getallheaders') ? getallheaders() : [];
```

環境差があるため、フレームワークのRequestオブジェクトがあれば優先します。

## JSON

```php
try {
    $payload = json_decode($rawBody, true, flags: JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    http_response_code(400);
}
```

## ログ

秘密情報を除外します。

```php
$safeHeaders = $headers;
unset($safeHeaders['Authorization'], $safeHeaders['Cookie']);
```

## Xdebugとの連携

ブレークポイント候補:

1. Request生成直後
2. JSON decode直後
3. Validation直後
4. Service入口
5. 外部API呼び出し前後
6. Repository直前
7. Response生成直前

## レスポンス

```php
http_response_code(422);
header('Content-Type: application/json; charset=UTF-8');
echo json_encode([
    'error' => [
        'code' => 'VALIDATION_ERROR',
        'details' => $errors,
    ],
], JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
```
