# Module17 Troubleshooting Cheatsheet

## まず確認

```bash
docker compose ps
docker compose logs --tail=200 web-php8
docker compose logs --tail=200 db
git status
```

## Port already in use

```bash
lsof -i :8081
```

## Permission denied

```bash
ls -lah
whoami
id
```

## Xdebug

```bash
php -m | rg xdebug
php -i | rg xdebug
tail -100 /tmp/xdebug.log
```
