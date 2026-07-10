# 22-05 Xdebug設定

## 最小構成

ホストOS上のPHP:

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

---

## 開発向け推奨例

```ini
[xdebug]
xdebug.mode=debug,develop
xdebug.start_with_request=trigger

xdebug.client_host=host.docker.internal
xdebug.client_port=9003

xdebug.discover_client_host=0

xdebug.log=/tmp/xdebug.log
xdebug.log_level=7

xdebug.max_nesting_level=512
xdebug.var_display_max_children=128
xdebug.var_display_max_data=2048
xdebug.var_display_max_depth=5
```

---

## `xdebug.mode`

```ini
xdebug.mode=debug,develop
```

設定後はPHPプロセスの再起動が必要です。

確認:

```bash
php -i | grep xdebug.mode
```

環境変数が優先される場合:

```bash
env | grep XDEBUG_MODE
```

Docker:

```bash
docker compose exec php env | grep XDEBUG_MODE
```

---

## `xdebug.start_with_request`

### 常時開始

```ini
xdebug.start_with_request=yes
```

### トリガー時だけ

```ini
xdebug.start_with_request=trigger
```

CLI:

```bash
XDEBUG_TRIGGER=1 php script.php
```

Docker:

```bash
docker compose exec -e XDEBUG_TRIGGER=1 php php script.php
```

Webではブラウザ拡張やCookieを使用できます。

---

## `xdebug.client_host`

Xdebugが接続するIDEのホストです。

ホストOS上のPHP:

```ini
xdebug.client_host=127.0.0.1
```

Docker Desktop:

```ini
xdebug.client_host=host.docker.internal
```

固定IPを直接書く方法は環境変更に弱いため、可能なら名前解決を使います。

---

## `xdebug.client_port`

Xdebug 3系の既定値:

```ini
xdebug.client_port=9003
```

VS Code側の`port`と一致させます。

---

## `xdebug.discover_client_host`

```ini
xdebug.discover_client_host=1
```

HTTPリクエストの送信元情報から接続先を推測します。

プロキシ・ロードバランサー・Docker環境では、意図しないIPを取得する可能性があります。

まずは明示的な`client_host`を推奨します。

---

## ログ

```ini
xdebug.log=/tmp/xdebug.log
xdebug.log_level=7
```

接続失敗の調査で有効です。

例:

```text
Connecting to configured address/port: host.docker.internal:9003
Could not connect to debugging client
```

調査後はログレベルを下げます。

```ini
xdebug.log_level=0
```

---

## IDE Key

```ini
xdebug.idekey=VSCODE
```

単一開発環境では必須でない場合が多いですが、プロキシや複数IDEを使う構成で識別に使われます。

---

## 表示制限

巨大な配列や深いオブジェクトを展開すると、IDEが重くなることがあります。

```ini
xdebug.var_display_max_children=128
xdebug.var_display_max_data=2048
xdebug.var_display_max_depth=5
```

値を大きくしすぎないようにします。

---

## 設定反映

CLIはコマンドごとに新しいプロセスです。

PHP-FPM:

```bash
sudo systemctl restart php8.3-fpm
```

Docker:

```bash
docker compose restart php
```

設定ファイルやイメージ変更時:

```bash
docker compose up -d --build --force-recreate php
```

---

## 設定確認コマンド

```bash
php --ri xdebug
```

絞り込み:

```bash
php -i | rg '^xdebug\.(mode|start_with_request|client_host|client_port|log|log_level)'
```

Docker:

```bash
docker compose exec php php -i \
  | rg '^xdebug\.(mode|start_with_request|client_host|client_port|log|log_level)'
```

---

## 演習

次の要件を満たす設定を書いてください。

- Xdebug 3
- ステップデバッグ
- トリガー時のみ開始
- DockerコンテナからホストOSへ接続
- ポート9003
- 接続ログを`/tmp/xdebug.log`へ出力
