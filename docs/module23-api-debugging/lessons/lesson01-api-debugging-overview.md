# APIデバッグの全体像


APIデバッグでは、コードだけでなく通信の境界を観測します。

```text
Client
  ↓ Request
Web Server / Reverse Proxy
  ↓
Application
  ↓
Database / External API
  ↑
Response
```

## 基本原則

1. 再現条件を固定する
2. リクエストを保存する
3. ステータス・ヘッダー・ボディを分けて確認する
4. クライアント側とサーバー側を分離する
5. 外部依存を切り分ける
6. 推測ではなく証拠で狭める

## 最初に記録する項目

- URL
- HTTPメソッド
- Query String
- Request Headers
- Request Body
- Response Status
- Response Headers
- Response Body
- 実行時刻
- Request ID / Trace ID
- 認証方式
- 再現率

## 典型的な問題

| 症状 | 主な確認対象 |
|---|---|
| 400 | 入力形式、必須項目、Content-Type |
| 401 | Authorization、Cookie、トークン期限 |
| 403 | 権限、CSRF、IP制限 |
| 404 | URL、ルーティング、HTTPメソッド |
| 405 | 許可メソッド |
| 409 | 重複、競合、状態遷移 |
| 422 | バリデーション |
| 429 | Rate Limit |
| 500 | アプリケーション例外 |
| 502/503/504 | Proxy、上流、タイムアウト |

## デバッグの順序

```text
再現
→ 通信を保存
→ クライアントを単純化
→ サーバーログ照合
→ アプリ内部を追跡
→ 外部依存を分離
→ 修正
→ 回帰テスト
```
