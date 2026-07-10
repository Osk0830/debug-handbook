# 22-13 DockerとpathMappings

## pathMappingsが必要な理由

Xdebugは、PHPが実行しているファイルのパスをVS Codeへ通知します。

コンテナ内:

```text
/var/www/html/src/UserService.php
```

ホスト側:

```text
/Users/name/project/src/UserService.php
```

パスが異なるため、VS Codeは同じファイルだと判断できません。

---

## 基本設定

```json
{
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}"
  }
}
```

変換:

```text
/var/www/html/src/UserService.php
        ↓
${workspaceFolder}/src/UserService.php
```

---

## コンテナ内パスを確認

```bash
docker compose exec php pwd
docker compose exec php ls -la
```

PHPから:

```bash
docker compose exec php php -r 'echo __DIR__, PHP_EOL;'
```

対象ファイル:

```php
error_log(__FILE__);
```

またはブレークポイント前に一時確認:

```php
var_dump(__FILE__);
```

---

## Composeのvolume確認

```yaml
services:
  php:
    volumes:
      - ./app:/var/www/html
```

この場合:

```json
{
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}/app"
  }
}
```

VS Codeで`app`フォルダ自体を開いている場合:

```json
{
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}"
  }
}
```

---

## よくある逆指定

誤り:

```json
{
  "pathMappings": {
    "${workspaceFolder}": "/var/www/html"
  }
}
```

正しい考え方:

```text
Xdebugが通知するパス → VS Codeで開いているパス
```

---

## サブディレクトリ

```yaml
volumes:
  - ./backend:/app
```

VS Codeでリポジトリルートを開く:

```json
{
  "pathMappings": {
    "/app": "${workspaceFolder}/backend"
  }
}
```

---

## シンボリックリンク

実行時パスがシンボリックリンク解決後のパスになる場合があります。

確認:

```bash
docker compose exec php readlink -f /var/www/html
```

XdebugログやPHP Debugログで通知パスを確認し、そのパスへマッピングします。

---

## 複数volume

```yaml
volumes:
  - ./app:/var/www/app
  - ./packages/shared:/var/www/shared
```

```json
{
  "pathMappings": {
    "/var/www/app": "${workspaceFolder}/app",
    "/var/www/shared": "${workspaceFolder}/packages/shared"
  }
}
```

---

## vendor

ホスト側に`vendor`が存在しない、またはコンテナ内だけにある場合、vendor内で停止しても対応ファイルを開けません。

対策:

- ホスト側にも同じvendorを用意する
- vendorへStep Intoしない
- `ignore`設定を使う
- コンテナへ接続するVS Code Dev Containersを使う

---

## Dev Containers

VS Code自体がコンテナ側のファイルを開く構成では、パスが一致し、`pathMappings`が不要になることがあります。

ただしXdebugがどこで動き、PHP Debugがどこで待ち受けているかを確認してください。

---

## 診断手順

1. ブレークポイントが未検証か確認
2. `__FILE__`で実行パス確認
3. Composeのvolume確認
4. `${workspaceFolder}`の実体確認
5. `pathMappings`の左右確認
6. VS Codeを再読込
7. デバッグセッションを再開始
8. リクエストを再送信

---

## 演習

次の構成の`pathMappings`を書いてください。

```text
ホスト:
project/backend/public/index.php

コンテナ:
/srv/app/public/index.php

VS Code:
projectを開いている
```
