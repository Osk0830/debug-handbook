# HTTPステータスコードの切り分け


## 2xx

- 200: 成功
- 201: 作成成功
- 202: 非同期受付
- 204: ボディなし成功

`204`なのにJSONを期待してパースエラーになるケースがあります。

## 3xx

- 301/308: 恒久リダイレクト
- 302/303/307: 一時リダイレクト

メソッド維持の違いに注意します。

## 4xx

- 400: リクエスト形式
- 401: 認証不足・失敗
- 403: 認証済みだが禁止
- 404: リソース・ルートなし
- 405: Method Not Allowed
- 409: 状態競合
- 415: Unsupported Media Type
- 422: 入力値エラー
- 429: Rate Limit

## 5xx

- 500: アプリ例外
- 502: 上流から不正応答
- 503: 一時利用不可
- 504: 上流タイムアウト

## 調査のコツ

ステータスだけで判断しません。

```bash
curl -sS -D - -o response.json http://localhost:8080/api/users
cat response.json | jq .
```

確認:

- エラーコード
- エラーメッセージ
- Request ID
- Validation errors
- Retry-After
- WWW-Authenticate
