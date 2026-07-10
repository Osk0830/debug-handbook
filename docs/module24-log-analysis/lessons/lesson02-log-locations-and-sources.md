# ログの場所と情報源


## PHP

設定確認:

```bash
php -i | rg 'error_log|log_errors'
```

代表例:

```text
/var/log/php/error.log
/var/log/php8.3-fpm.log
/var/log/php-fpm/error.log
```

Dockerではファイルではなくstdout / stderrへ出している場合があります。

## Nginx

```text
/var/log/nginx/access.log
/var/log/nginx/error.log
```

設定確認:

```bash
nginx -T | rg 'access_log|error_log'
```

## Apache

```text
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/httpd/access_log
/var/log/httpd/error_log
```

## Docker

```bash
docker compose logs
docker compose logs app
docker logs <container>
```

## systemd

```bash
journalctl -u nginx
journalctl -u php8.3-fpm
```

## MySQL

```bash
mysql -e "SHOW VARIABLES LIKE '%log%';"
```

確認対象:

- error log
- slow query log
- general log
- binary log

## ログの場所を決めつけない

パッケージ、OS、コンテナ、構成管理によって場所は変わります。

```text
設定ファイル
→ 実行中プロセス
→ stdout / stderr
→ volume
→ ローテーション設定
```

の順で確認します。
