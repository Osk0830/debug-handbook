# Module23 APIデバッグ

API障害を、HTTP通信・クライアント・サーバー・外部依存の境界に分けて調査するための実践Moduleです。

## 学習目標

- HTTPリクエストとレスポンスを読める
- curlでAPIを再現できる
- ステータス・ヘッダー・ボディを分離して確認できる
- JSON、認証、CORSを切り分けられる
- PostmanやREST Clientで再現手順を保存できる
- PHP側で入力からレスポンスまで追跡できる
- Docker・Proxy・外部APIの問題を分離できる
- タイムアウト、リトライ、Rate Limitを判断できる

## Lesson一覧

- [APIデバッグの全体像](lessons/lesson01-api-debugging-overview.md)
- [HTTPリクエストとレスポンス](lessons/lesson02-http-request-response.md)
- [curl基礎](lessons/lesson03-curl-basics.md)
- [curlで通信を詳細観測する](lessons/lesson04-curl-advanced-observation.md)
- [HTTPステータスコードの切り分け](lessons/lesson05-status-codes.md)
- [ヘッダーとContent-Type](lessons/lesson06-headers-content-types.md)
- [JSONデバッグ](lessons/lesson07-json-debugging.md)
- [認証・認可のデバッグ](lessons/lesson08-authentication.md)
- [CORSとブラウザ固有問題](lessons/lesson09-cors.md)
- [PostmanとVS Code REST Client](lessons/lesson10-postman-rest-client.md)
- [PHPサーバー側のAPIデバッグ](lessons/lesson11-php-server-side-debugging.md)
- [外部API連携の切り分け](lessons/lesson12-external-api-debugging.md)
- [Docker・Proxy・ネットワーク](lessons/lesson13-docker-proxy-network.md)
- [タイムアウト・リトライ・Rate Limit](lessons/lesson14-timeout-retry-rate-limit.md)
- [API障害の体系的トラブルシューティング](lessons/lesson15-api-troubleshooting.md)
- [総合演習](lessons/lesson16-capstone.md)

## 補助教材

- [Lab01 curlでAPI障害を再現する](labs/lab01-curl-reproduction.md)
- [Lab02 認証・CORS・外部APIを切り分ける](labs/lab02-auth-cors-upstream.md)
- [Beginner Exercises](exercises/beginner.md)
- [Answers](exercises/answers.md)
- [Cheatsheet](cheatsheet.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)

## 学習の原則

```text
再現
→ 保存
→ 比較
→ 境界を分ける
→ ログと照合
→ 修正
→ 回帰テスト
```
