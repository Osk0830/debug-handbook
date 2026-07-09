# Module01 CLI チートシート

```bash
pwd
ls -lah
cd ..
cd -
echo $SHELL
echo $PATH
which php
type cd
history
```

## リダイレクト

```bash
command > output.log
command >> output.log
command 2> error.log
command > output.log 2>&1
```

## Docker

```bash
docker compose ps
docker compose exec web-php8 bash
docker compose logs -f web-php8
```
