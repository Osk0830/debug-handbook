# HTTPリクエストとレスポンス


## リクエストの構造

```http
POST /api/users?notify=1 HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Authorization: Bearer TOKEN

{"name":"Taro","email":"taro@example.com"}
```

構成要素:

- Request Line
- Headers
- 空行
- Body

## レスポンスの構造

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/123

{"id":123,"name":"Taro"}
```

## メソッド

| Method | 主な用途 |
|---|---|
| GET | 取得 |
| POST | 作成・処理実行 |
| PUT | 全体更新 |
| PATCH | 部分更新 |
| DELETE | 削除 |
| HEAD | ヘッダーのみ |
| OPTIONS | 対応メソッドやCORS確認 |

## 安全性と冪等性

- GETは原則として状態を変更しない
- PUT・DELETEは同じ操作を繰り返しても結果が同じになる設計が望ましい
- POSTは重複実行に注意する
- 決済・注文ではIdempotency Keyを検討する

## 観測コマンド

```bash
curl -i http://localhost:8080/api/users/123
```

詳細:

```bash
curl -v http://localhost:8080/api/users/123
```

ヘッダーのみ:

```bash
curl -I http://localhost:8080/api/users/123
```

## 注意

`curl -v`は認証情報を表示する場合があります。共有ログへ貼る前に必ずマスキングしてください。
