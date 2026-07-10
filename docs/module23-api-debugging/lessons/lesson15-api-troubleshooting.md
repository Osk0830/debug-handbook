# API障害の体系的トラブルシューティング


## 5分診断

1. URLとMethod
2. DNS・接続先
3. Request Headers
4. Request Body
5. Response Status
6. Response Headers
7. Response Body
8. Request ID
9. サーバーログ
10. 直アクセスとの比較

## curlでは成功、アプリでは失敗

比較:

- URL
- Query encoding
- Headers
- Cookie
- Redirect
- Proxy
- TLS
- Timeout
- JSON serialization
- User-Agent

## ローカル成功、本番失敗

確認:

- 環境変数
- Secret
- DNS
- Firewall
- Proxy
- 証明書
- IP allowlist
- Timezone
- Clock skew
- API version

## 断続的失敗

- 複数インスタンス
- 接続プール
- Rate Limit
- Race condition
- Cache
- 負荷
- 外部API
- 特定データ

## 証拠セット

```text
timestamp
request_id
method
url
safe_headers
request_body_hash
status
response_headers
response_body
duration
server_log
```
