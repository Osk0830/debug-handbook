# Module14 Web Server Cheatsheet

```bash
curl -I URL
curl -L -I URL

tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

docker compose logs -f web-php8
```

## 404

```text
URL
  ↓
Method
  ↓
Route
  ↓
Rewrite
  ↓
DocumentRoot
```

## 502

```text
Nginx
  ↓
PHP-FPM
  ↓
Docker
  ↓
FastCGI設定
```
