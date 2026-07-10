# 22-04 Docker環境へのインストール

## Dockerではイメージへ組み込む

コンテナ内へ手動インストールしても、コンテナを作り直すと消えます。

XdebugはDockerfileへ記述し、再現可能なイメージとして管理します。

---

## 公式PHPイメージの例

```dockerfile
FROM php:8.3-fpm

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug

COPY ./docker/php/xdebug.ini /usr/local/etc/php/conf.d/99-xdebug.ini
```

`xdebug.ini`:

```ini
[xdebug]
xdebug.mode=debug,develop
xdebug.start_with_request=yes
xdebug.client_host=host.docker.internal
xdebug.client_port=9003
xdebug.log=/tmp/xdebug.log
xdebug.log_level=7
```

---

## イメージ再ビルド

```bash
docker compose build --no-cache php
docker compose up -d
```

サービス名が不明な場合:

```bash
docker compose config --services
```

---

## 確認

```bash
docker compose exec php php --version
docker compose exec php php -m | grep -i xdebug
docker compose exec php php --ri xdebug
```

設定値:

```bash
docker compose exec php php -i \
  | grep -E 'xdebug.mode|xdebug.client_host|xdebug.client_port|xdebug.start_with_request'
```

---

## `host.docker.internal`

DockerコンテナからホストOS上のVS Codeへ接続するために使います。

```ini
xdebug.client_host=host.docker.internal
```

Docker Desktopでは一般に利用できます。

Linuxで名前解決できない場合は、Composeへ次を追加します。

```yaml
services:
  php:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

確認:

```bash
docker compose exec php getent hosts host.docker.internal
```

イメージに`getent`がない場合:

```bash
docker compose exec php php -r \
  'echo gethostbyname("host.docker.internal"), PHP_EOL;'
```

---

## 開発環境だけ有効にする

本番イメージへXdebugを含めない構成が理想です。

### 開発用Dockerfile

```dockerfile
FROM php:8.3-fpm AS base

# 共通拡張を導入

FROM base AS development

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug

COPY ./docker/php/xdebug.ini /usr/local/etc/php/conf.d/99-xdebug.ini

FROM base AS production

# Xdebugを含めない
```

Compose:

```yaml
services:
  php:
    build:
      context: .
      target: development
```

---

## 環境変数で設定する

`XDEBUG_MODE`は`xdebug.mode`を上書きできます。

```yaml
services:
  php:
    environment:
      XDEBUG_MODE: debug,develop
```

CLIで一時的に無効化:

```bash
docker compose exec -e XDEBUG_MODE=off php php script.php
```

一時的に有効化:

```bash
docker compose exec \
  -e XDEBUG_MODE=debug \
  -e XDEBUG_TRIGGER=1 \
  php php script.php
```

---

## 設定ファイルが反映されない場合

コンテナ内のファイル確認:

```bash
docker compose exec php ls -la /usr/local/etc/php/conf.d
docker compose exec php cat /usr/local/etc/php/conf.d/99-xdebug.ini
```

マウント確認:

```bash
docker compose config
docker inspect <container-name>
```

コンテナ再作成:

```bash
docker compose up -d --build --force-recreate php
```

---

## Alpine系

必要なビルド依存関係が異なります。

```dockerfile
FROM php:8.3-fpm-alpine

RUN apk add --no-cache --virtual .build-deps $PHPIZE_DEPS linux-headers \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && apk del .build-deps
```

---

## ログ確認

```bash
docker compose exec php tail -f /tmp/xdebug.log
```

ファイルがない場合:

```bash
docker compose exec php sh -lc 'touch /tmp/xdebug.log && chmod 666 /tmp/xdebug.log'
```

通常、`/tmp`は書き込み可能ですが、実行ユーザーやセキュリティ設定を確認してください。

---

## 演習

1. DockerfileにXdebugを追加する。
2. イメージを再ビルドする。
3. `php --ri xdebug`を実行する。
4. `host.docker.internal`が解決できるか確認する。
5. Xdebugログを表示する。
