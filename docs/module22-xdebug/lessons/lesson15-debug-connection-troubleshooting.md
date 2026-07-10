# 22-15 ブレークポイントで止まらないとき

## 切り分け順序

```text
1. 対象コードが実行されているか
2. 対象PHPにXdebugが読み込まれているか
3. debugモードが有効か
4. デバッグ開始条件を満たしているか
5. VS Codeが待ち受けているか
6. ホスト名を解決できるか
7. ポートへ接続できるか
8. pathMappingsが正しいか
9. ブレークポイントが実行可能行か
```

---

## 1. 対象コードが実行されているか

一時ログ:

```php
error_log(__FILE__ . ':' . __LINE__);
```

curlで対象URL確認:

```bash
curl -i http://localhost:8080/target
```

別環境・別コンテナ・キャッシュ済みレスポンスを見ていないか確認します。

---

## 2. Xdebug読み込み

```bash
php --ri xdebug
```

Docker:

```bash
docker compose exec php php --ri xdebug
```

Web側はPHP-FPMの設定も確認します。

```bash
docker compose exec php php-fpm -i | grep -i xdebug
```

---

## 3. mode

```bash
php -i | grep xdebug.mode
```

期待:

```text
xdebug.mode => debug
```

`XDEBUG_MODE`確認:

```bash
env | grep XDEBUG_MODE
```

---

## 4. 開始条件

```bash
php -i | grep xdebug.start_with_request
```

`trigger`の場合:

```bash
XDEBUG_TRIGGER=1 php script.php
```

Webリクエストにもトリガーが付いているか確認します。

---

## 5. VS Code待受

F5で`Listen for Xdebug`を開始します。

ポート確認:

```bash
lsof -nP -iTCP:9003 -sTCP:LISTEN
```

別アプリが9003を使っていないか確認します。

---

## 6. ホスト名

Docker:

```bash
docker compose exec php php -r \
  'echo gethostbyname("host.docker.internal"), PHP_EOL;'
```

解決されない場合、Compose:

```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

---

## 7. ポート接続

コンテナに`nc`がある場合:

```bash
docker compose exec php nc -vz host.docker.internal 9003
```

VS Codeが待受中に実行します。

macOSのファイアウォールやセキュリティソフトも確認します。

---

## 8. Xdebugログ

```ini
xdebug.log=/tmp/xdebug.log
xdebug.log_level=7
```

```bash
docker compose exec php tail -f /tmp/xdebug.log
```

見る内容:

- 接続先
- 接続成功・失敗
- IDE key
- ファイルパス
- ブレークポイント解決

---

## 9. pathMappings

PHP側:

```php
error_log(__FILE__);
```

Compose:

```bash
docker compose config
```

`launch.json`:

```json
{
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}"
  }
}
```

---

## 10. 実行可能行

避ける:

- 空行
- コメント
- 宣言途中
- 実行されない分岐
- 最適化や生成コードの対応しない位置

関数内部の確実に実行される代入・return・呼び出し行へ移動します。

---

## CLIだけ止まる / Webだけ止まらない

CLIとFPMで設定が異なります。

```bash
php --ini
php-fpm -i | grep 'Loaded Configuration File'
```

Docker内:

```bash
docker compose exec php php --ini
docker compose exec php php-fpm -i | grep -E 'Loaded Configuration|xdebug'
```

---

## Webだけ止まる / CLIだけ止まらない

CLIのPHP実体が別かもしれません。

```bash
which php
type -a php
php --ini
```

---

## 接続できるが別ファイルが開く

- 同名ファイルが複数ある
- volumeとローカルコピーがずれている
- `pathMappings`が広すぎる
- VS Codeで開くルートが違う
- シンボリックリンク

`__FILE__`とGit管理ファイルの絶対パスを比較します。

---

## すぐ切断される

- PHP処理がすぐ終了
- ブレークポイント行を通っていない
- Fatal Error
- タイムアウト
- Worker再起動漏れ
- 別ポート
- 複数のVS Codeウィンドウが競合

XdebugログとPHPエラーログを同時に確認します。

---

## 遅い

- `xdebug.start_with_request=yes`
- IDEが待ち受けていない
- `client_host`へ到達できない
- 接続タイムアウト
- `develop`や`coverage`を常時有効
- 巨大変数を展開
- Logpoint大量出力

必要時だけ`trigger`で有効にします。

---

## 最終診断コマンド集

```bash
php --version
php --ini
php --ri xdebug
php -i | rg '^xdebug\.'
lsof -nP -iTCP:9003
```

Docker:

```bash
docker compose ps
docker compose exec php php --version
docker compose exec php php --ini
docker compose exec php php --ri xdebug
docker compose exec php php -i | rg '^xdebug\.'
docker compose exec php tail -100 /tmp/xdebug.log
```

---

## 5分診断チェックリスト

- [ ] URLは正しい
- [ ] 対象コードを通る
- [ ] 対象PHPにXdebugがある
- [ ] `xdebug.mode=debug`
- [ ] 開始条件を満たす
- [ ] VS Codeが9003で待受中
- [ ] コンテナからホスト名を解決できる
- [ ] Xdebugログに接続試行がある
- [ ] `pathMappings`が正しい
- [ ] ブレークポイントが実行可能行
