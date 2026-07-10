# Lab02 認証・CORS・外部APIを切り分ける

## シナリオ

ブラウザでは401またはCORSエラー、サーバー側では外部APIが504になることがあります。

## 手順

1. curlでAPIへ直接アクセス
2. Bearer Token有無を比較
3. Token期限を確認
4. OPTIONSを再現
5. Allow-OriginとCredentialsを確認
6. Cookie属性を確認
7. アプリから外部APIへの通信を保存
8. コンテナ内から外部APIへcurl
9. connectとTTFBを測定
10. timeout箇所を特定

## 完了条件

- 認証失敗とCORS失敗を区別できる
- 自分のAPIと外部APIの障害を分離できる
- 504の発生段階を説明できる
