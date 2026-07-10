# Docker・journalctl・システムログ


## Docker Compose

```bash
docker compose logs
docker compose logs --tail=100 app
docker compose logs -f app
docker compose logs --since=30m app
docker compose logs -t app
```

## 複数サービス

```bash
docker compose logs -t nginx app db
```

時刻付きで同時表示し、処理順を確認します。

## コンテナ状態

```bash
docker compose ps
docker inspect <container>
docker stats
```

## OOM・再起動

```bash
docker inspect <container> \
  --format '{{.State.Status}} {{.State.OOMKilled}} {{.State.ExitCode}}'
```

## journalctl

```bash
journalctl -u nginx --since "30 minutes ago"
journalctl -u php8.3-fpm -f
journalctl -p err..alert
journalctl --since "2026-07-10 14:00" --until "2026-07-10 15:00"
```

## Kernel

```bash
journalctl -k
dmesg | tail
```

OOM Killer、ディスク、ネットワークなど、アプリ外の原因を確認します。
