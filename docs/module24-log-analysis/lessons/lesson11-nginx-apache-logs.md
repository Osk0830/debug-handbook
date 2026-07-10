# Nginx・Apacheログ解析


## Nginx access log

```bash
tail -F /var/log/nginx/access.log
```

500:

```bash
awk '$9 ~ /^5/ {print}' /var/log/nginx/access.log
```

## Nginx error log

```bash
rg -i 'error|crit|alert|emerg' /var/log/nginx/error.log
```

代表的な語:

```text
upstream timed out
connect() failed
no live upstreams
client intended to send too large body
permission denied
rewrite or internal redirection cycle
```

## Apache

```bash
tail -F /var/log/apache2/access.log
tail -F /var/log/apache2/error.log
```

## Proxy時間

Nginxで次をログに含めると有効です。

```text
$request_time
$upstream_connect_time
$upstream_header_time
$upstream_response_time
$request_id
```

## 413

```text
client intended to send too large body
```

`client_max_body_size`を確認します。

## 502・504

- PHP-FPMが停止
- Unix socket権限
- upstream名・ポート
- timeout
- アプリ処理遅延
- コンテナ再起動
