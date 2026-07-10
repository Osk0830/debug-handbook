# Lab01 500エラーを複数ログから追跡する

## シナリオ

`GET /api/users/123`が500を返します。

構成:

```text
Nginx → PHP-FPM → MySQL
```

## 手順

1. curlで再現する
2. 発生時刻を記録する
3. Access Logから対象リクエストを探す
4. Request IDを取得する
5. Nginx Error Logを検索する
6. PHPログをRequest IDで検索する
7. 例外クラスとstack traceを確認する
8. SQL・対象IDを安全に確認する
9. 正常IDの処理と比較する
10. 調査記録を作る

## 完了条件

- 500の事実と根本原因を区別できる
- 入口からDBまで時系列で説明できる
- 共有用ログがマスキングされている
