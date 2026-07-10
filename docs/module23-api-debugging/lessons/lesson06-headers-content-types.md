# ヘッダーとContent-Type


## Request Headers

```bash
curl -i   -H 'Accept: application/json'   -H 'Content-Type: application/json'   -H 'X-Request-ID: debug-001'   --data @request.json   http://localhost:8080/api/users
```

## AcceptとContent-Type

- `Content-Type`: 送信ボディの形式
- `Accept`: 受け取りたい形式

JSON文字列を送っても、`Content-Type`が違えばサーバーが解析しない場合があります。

## 代表的な形式

```text
application/json
application/x-www-form-urlencoded
multipart/form-data
text/plain
application/xml
```

`multipart/form-data`のboundaryは、curlの`-F`に生成させます。手動指定しない方が安全です。

## キャッシュ関連

```text
Cache-Control
ETag
If-None-Match
Last-Modified
If-Modified-Since
```

304を調べる場合:

```bash
curl -i   -H 'If-None-Match: "etag-value"'   http://localhost:8080/api/users/123
```

## Proxy関連

```text
Host
X-Forwarded-For
X-Forwarded-Proto
X-Forwarded-Host
Forwarded
```

アプリがHTTPS判定を誤る場合は、Proxyからのヘッダーと信頼設定を確認します。
