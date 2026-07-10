# Xdebugチートシート

## 確認

```bash
php --version
php --ini
php -m | grep -i xdebug
php --ri xdebug
php -i | rg '^xdebug\.'
```

Docker:

```bash
docker compose exec php php --version
docker compose exec php php --ini
docker compose exec php php --ri xdebug
```

---

## Xdebug最小設定

ローカル:

```ini
[xdebug]
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=127.0.0.1
xdebug.client_port=9003
```

Docker:

```ini
[xdebug]
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=host.docker.internal
xdebug.client_port=9003
```

ログ:

```ini
xdebug.log=/tmp/xdebug.log
xdebug.log_level=7
```

---

## VS Code

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Listen for Xdebug",
      "type": "php",
      "request": "launch",
      "port": 9003,
      "pathMappings": {
        "/var/www/html": "${workspaceFolder}"
      }
    }
  ]
}
```

---

## キー操作

| 操作 | キー |
|---|---|
| Continue | F5 |
| Step Over | F10 |
| Step Into | F11 |
| Step Out | Shift+F11 |
| Stop | Shift+F5 |

---

## CLIトリガー

```bash
XDEBUG_TRIGGER=1 php script.php
```

Docker:

```bash
docker compose exec -e XDEBUG_TRIGGER=1 php php script.php
```

PHPUnit:

```bash
XDEBUG_TRIGGER=1 ./vendor/bin/phpunit --filter testName
```

---

## ポート

```bash
lsof -nP -iTCP:9003 -sTCP:LISTEN
```

Linux:

```bash
ss -lntp | grep 9003
```

コンテナから:

```bash
docker compose exec php nc -vz host.docker.internal 9003
```

---

## ホスト名

```bash
docker compose exec php php -r \
  'echo gethostbyname("host.docker.internal"), PHP_EOL;'
```

Linux Compose:

```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

---

## よく使うWatch

```php
$_GET
$_POST
$_SESSION
$_SERVER['REQUEST_URI'] ?? null
$payload
json_last_error_msg()
count($items)
get_debug_type($value)
$stmt->errorInfo()
```

---

## 止まらないとき

```text
対象コード
→ Xdebug読み込み
→ mode=debug
→ start条件
→ VS Code待受
→ host
→ port
→ Xdebug log
→ pathMappings
→ 実行可能行
```
