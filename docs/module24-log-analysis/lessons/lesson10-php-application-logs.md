# PHP・アプリケーションログ


## PHP設定

```ini
log_errors=On
error_reporting=E_ALL
display_errors=Off
error_log=/var/log/php/error.log
```

本番でエラー詳細を画面表示せず、ログへ残します。

## error_log

```php
error_log('processing started');
```

構造化:

```php
error_log(json_encode([
    'timestamp' => date(DATE_ATOM),
    'level' => 'info',
    'request_id' => $requestId,
    'event' => 'order.created',
    'order_id' => $orderId,
], JSON_UNESCAPED_SLASHES));
```

## 例外

記録するもの:

- 例外クラス
- メッセージ
- コード
- ファイル・行
- stack trace
- request_id
- 安全化した入力
- 業務識別子

## ログレベル

```text
debug
info
notice
warning
error
critical
alert
emergency
```

すべてをerrorにすると重要度が分からなくなります。

## ログに出してはいけないもの

- Password
- Access Token
- Refresh Token
- Session ID
- Cookie全文
- クレジットカード番号
- 個人番号
- 秘密鍵
- 認証ヘッダー
