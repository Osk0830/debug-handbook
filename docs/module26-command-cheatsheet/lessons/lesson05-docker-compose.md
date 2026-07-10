# Lesson05 Docker・Docker Compose

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## 状態確認

```bash
docker version
docker info
docker compose ps
docker ps -a
docker images
docker volume ls
docker network ls
```

**判断ポイント:** 最初にDocker Engineと対象コンテナの状態を確認する。

## 起動・停止

```bash
docker compose up -d
docker compose up -d --build
docker compose stop
docker compose down
docker compose down -v
```

**判断ポイント:** `down -v`はDBなどの永続データも削除するため注意する。

## ログ

```bash
docker compose logs
docker compose logs -f app
docker compose logs --tail=200 app
docker logs --since=10m CONTAINER
```

**判断ポイント:** 対象サービスと時間範囲を絞る。

## コンテナ内操作

```bash
docker compose exec app sh
docker compose exec app php -v
docker compose exec db mysql -uroot -p
docker compose run --rm app command
```

**判断ポイント:** `exec`は起動中コンテナ、`run --rm`は一時コンテナ。

## 調査・掃除

```bash
docker inspect CONTAINER
docker stats
docker system df
docker builder prune
docker system prune
```

**判断ポイント:** `prune`実行前に削除対象と再取得コストを確認する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
