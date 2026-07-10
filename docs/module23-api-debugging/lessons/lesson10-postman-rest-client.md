# PostmanとVS Code REST Client


## Postmanの用途

- CollectionでAPI群を整理
- EnvironmentでURLやトークンを切り替え
- Pre-request Script
- Test Script
- Request履歴
- チーム共有

## 秘密情報

トークン・パスワードをCollectionへ直書きしないでください。

## REST Client

`.http`ファイル例:

```http
@baseUrl = http://localhost:8080
@token = replace-me

### Health
GET {{baseUrl}}/health

### Create user
POST {{baseUrl}}/api/users
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "name": "Taro",
  "email": "taro@example.com"
}
```

## リクエストをコード管理する利点

- 再現手順になる
- レビューできる
- 仕様変更を追跡できる
- CIへ移植しやすい
- curlへ変換しやすい

## 注意

`.http`へ本物の秘密情報をコミットしないでください。環境変数やgitignore対象ファイルへ分離します。
