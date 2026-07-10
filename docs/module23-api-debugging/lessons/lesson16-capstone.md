# 総合演習


## 症状

注文APIがブラウザからだけ失敗します。

```text
POST /api/orders
Browser: CORS error
curl: 201 Created
```

さらに、まれに同じ注文が2件作成されます。

## 課題

1. Networkタブでpreflightを確認する
2. OPTIONSをcurlで再現する
3. CORSレスポンスヘッダーを確認する
4. credentials利用有無を確認する
5. POSTリクエストを保存する
6. Request IDを付ける
7. サーバーログと照合する
8. リトライ設定を確認する
9. Idempotency Keyの有無を確認する
10. 重複防止テストを書く

## OPTIONS例

```bash
curl -i   -X OPTIONS   -H 'Origin: http://localhost:3000'   -H 'Access-Control-Request-Method: POST'   -H 'Access-Control-Request-Headers: content-type,authorization,idempotency-key'   http://localhost:8080/api/orders
```

## POST例

```bash
curl -i   -X POST   -H 'Origin: http://localhost:3000'   -H 'Content-Type: application/json'   -H 'Idempotency-Key: order-debug-001'   --data @order.json   http://localhost:8080/api/orders
```

## 完了条件

- CORS問題とAPIロジック問題を分離できる
- 同じリクエストを再現できる
- 重複生成の原因を説明できる
- 再発防止策をテストへ落とせる
