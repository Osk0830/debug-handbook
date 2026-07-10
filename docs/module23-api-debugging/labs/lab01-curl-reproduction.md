# Lab01 curlでAPI障害を再現する

## 目的

ブラウザやアプリで発生したAPI障害を、curlだけで再現可能にします。

## シナリオ

`POST /api/users`が422を返します。

## 手順

1. URLとMethodを記録
2. Request Headersを保存
3. Request BodyをJSONファイルへ保存
4. curlへ変換
5. Response HeadersとBodyを分離
6. `jq`でエラー内容を確認
7. 正常データと差分比較
8. Request IDを付与
9. サーバーログと照合
10. 再現コマンドを`.md`または`.http`へ保存

## 完了条件

- 他の開発者が同じ障害を再現できる
- 秘密情報が除外されている
- 正常・異常の差分が説明できる
