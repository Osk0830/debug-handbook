# 外部API連携の切り分け


## 境界を分ける

```text
自分のClientコード
→ DNS/TLS
→ Proxy
→ 外部API
→ Response解析
→ 自分の業務ロジック
```

## 保存する情報

- URL
- Method
- 安全化したHeaders
- Body
- Status
- Response Headers
- Response Body
- 接続時間
- 応答時間
- Retry回数
- Request ID

## curlで再現

アプリが送った通信を、秘密情報を差し替えてcurlへ落とします。

## TLS確認

```bash
curl -v https://api.example.com/health
```

証明書検証を無効にする`-k`は、原因確認の一時用途に限定します。

## タイムアウト

- connect timeout
- read timeout
- total timeout

どの段階で止まったかを区別します。

## Stub / Mock

外部APIが不安定な場合:

- 固定JSON
- Mock Server
- WireMock
- ローカルStub
- 記録済みレスポンス

外部依存を切り離し、自分のコードだけを再現可能にします。
