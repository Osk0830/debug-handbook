# JSONデバッグ


## 構文確認

```bash
jq . response.json
```

Compact:

```bash
jq -c . response.json
```

特定項目:

```bash
jq '.data.users[] | {id, email}' response.json
```

## PHP

```php
$raw = file_get_contents('php://input');

try {
    $payload = json_decode($raw, true, flags: JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    // エラー処理
}
```

## よくある問題

- 末尾カンマ
- シングルクォート
- 不正なUTF-8
- 数値と文字列の違い
- `null`とキー不存在
- 巨大整数
- 空レスポンス
- HTMLエラーページをJSONとして解析

## Content-Typeも確認

```bash
curl -sS -D response.headers -o response.body http://localhost:8080/api/users
rg -i '^content-type:' response.headers
```

## jqで型を確認

```bash
jq '.id | type' response.json
```

## 差分

```bash
jq -S . expected.json > expected.sorted.json
jq -S . actual.json > actual.sorted.json
diff -u expected.sorted.json actual.sorted.json
```
