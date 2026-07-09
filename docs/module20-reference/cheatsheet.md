# Module20 Reference Cheatsheet

## 最初に打つ5コマンド

```bash
git status
docker compose ps
docker compose logs --tail=100 web-php8
curl -I http://localhost:8081/
rg -n "keyword" .
```

## 500

```text
HTTP
  ↓
Docker logs
  ↓
PHP logs
  ↓
rg
  ↓
SQL
  ↓
Xdebug
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
Web Server
```
