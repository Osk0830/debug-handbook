
# 第14章 Nginx・Apache・Webサーバーデバッグ

> **目的**: Webサーバーの役割を理解し、404・500・リダイレクト・HTTPS・リバースプロキシなどの問題を切り分けられるようになる。

---

# この章で身につくこと

- Webサーバーの役割
- NginxとApacheの違い
- リバースプロキシ
- リダイレクト
- HTTPS
- アクセスログ・エラーログ
- よくあるWebサーバートラブル

---

# Webサーバーとは

ブラウザからのHTTPリクエストを受け取り、適切なアプリケーションへ渡す役割を持ちます。

```text
Browser
   │
 HTTP Request
   │
Nginx / Apache
   │
PHP-FPM
   │
Application
   │
MySQL
```

---

# NginxとApache

|項目|Nginx|Apache|
|---|---|---|
|得意|静的配信・リバースプロキシ|モジュール豊富|
|設定|nginx.conf|httpd.conf /.htaccess|
|PHP|PHP-FPM経由|mod_php または PHP-FPM|

---

# よく確認するHTTPステータス

- 200 OK
- 301 Moved Permanently
- 302 Found
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable

---

# リバースプロキシ

```text
Browser
  ↓
Nginx
  ↓
PHP
```

Nginxが入口となり、PHPやNode.jsへリクエストを転送します。

---

# 設定ファイル

Nginx

```text
/etc/nginx/nginx.conf
/etc/nginx/conf.d/
```

Apache

```text
httpd.conf
.htaccess
```

---

# ログ

Docker環境

```bash
docker compose logs -f web-php8
```

Nginx

```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

Apache

```bash
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
```

---

# access.log

確認項目

- URL
- Method
- Status
- IP
- User-Agent
- Response Size

---

# error.log

確認項目

- PHP Error
- Rewrite Error
- Permission Error
- FastCGI Error

---

# HTTPS

確認

```bash
curl -I https://example.com
```

確認ポイント

- Location
- Strict-Transport-Security
- Certificate

---

# Rewrite

404の時は

- rewrite
- location
- DocumentRoot
- index.php

を確認します。

---

# 実務シナリオ

## 404

確認順

1. URL
2. rewrite
3. location
4. ファイル存在
5. ルーティング

---

## 502

確認順

1. PHP-FPM起動
2. FastCGI設定
3. Docker状態
4. エラーログ

---

## 301ループ

確認

- HTTPS
- Location
- リバースプロキシ
- APP_URL
- X-Forwarded-Proto

---

# Docker

設定確認

```bash
docker compose ps
docker compose logs -f
docker compose exec web-php8 bash
```

---

# ハンズオン

1. access.log確認
2. error.log確認
3. curl -I実行
4. 404再現
5. 500再現
6. rewrite確認
7. HTTPS確認
8. docker logs確認
9. Nginx設定確認
10. Apache設定確認

---

# タイムアタック

30分以内で

- 404原因候補
- 500原因候補
- access.log確認
- error.log確認
- curlでHeader確認

---

# 練習問題

1. NginxとApacheの違いは？
2. access.logとerror.logの違いは？
3. 502 Bad Gatewayの原因を3つ挙げる
4. rewrite設定は何のため？
5. 301と302の違いは？
6. リバースプロキシとは？

---

# チェックリスト

- [ ] access.logを読める
- [ ] error.logを読める
- [ ] curl -IでHeader確認できる
- [ ] 404を切り分けられる
- [ ] 500を切り分けられる
- [ ] Dockerログと組み合わせて調査できる

---

# コラム

Webサーバーの障害は「アプリが悪い」と決めつけないことが重要です。

HTTP・Webサーバー・PHP・アプリ・DBのどこで止まっているかを順番に切り分けることが、最短で原因へたどり着く近道です。

---

# 次章予告

第15章では Mail・SMTP・MailHog を使ったメール送信デバッグを学びます。
