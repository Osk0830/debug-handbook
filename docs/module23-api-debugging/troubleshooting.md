# APIデバッグ Troubleshooting

## 最小診断

```bash
curl -v http://localhost:8080/health
curl -sS -D response.headers -o response.body http://localhost:8080/api/target
cat response.headers
jq . response.body
```

## 切り分け

```text
クライアント
→ DNS
→ TLS
→ Proxy
→ Web Server
→ Application
→ Database
→ External API
```

## 比較表

| 比較 | 分かること |
|---|---|
| Browser vs curl | CORS・Cookie・ブラウザ制約 |
| Proxy経由 vs 直アクセス | Nginx・LB・rewrite |
| Host vs Container | Dockerネットワーク |
| Local vs Production | 環境変数・Secret・Firewall |
| 正常データ vs 異常データ | 入力依存 |
| 正常時刻 vs 障害時刻 | 負荷・Rate Limit・外部依存 |

詳細は[Lesson15](lessons/lesson15-api-troubleshooting.md)を参照してください。
