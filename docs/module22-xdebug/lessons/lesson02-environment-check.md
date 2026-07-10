# 22-02 導入前の環境確認

## 最初にPHPの実体を確認する

Xdebug導入でよくある失敗は、**別のPHPへXdebugをインストールすること**です。

PHPが複数存在する環境では、CLI・Webサーバー・Dockerコンテナが別々のPHPを使うことがあります。

---

## CLIのPHP

```bash
which php
php --version
php --ini
```

確認例:

```text
/usr/local/bin/php
PHP 8.3.x (cli)
Loaded Configuration File: /usr/local/etc/php/8.3/php.ini
```

macOSで複数候補を確認:

```bash
type -a php
```

---

## 読み込まれている設定ファイル

```bash
php --ini
```

確認する項目:

```text
Configuration File (php.ini) Path
Loaded Configuration File
Scan for additional .ini files in
Additional .ini files parsed
```

Xdebug専用設定は、追加iniディレクトリへ配置されることがあります。

例:

```text
/usr/local/etc/php/8.3/conf.d/ext-xdebug.ini
```

---

## Webサーバー側のPHP

CLIでXdebugが有効でも、Webアクセス側で無効なことがあります。

一時的な確認ファイル:

```php
<?php

phpinfo();
```

ブラウザで表示し、次を確認します。

- PHP Version
- Server API
- Loaded Configuration File
- Additional `.ini` files parsed
- Xdebugセクション

> `phpinfo()`は環境情報を大量に公開します。確認後は必ず削除してください。

より安全な確認例:

```php
<?php

header('Content-Type: text/plain; charset=UTF-8');

echo 'PHP_VERSION=' . PHP_VERSION . PHP_EOL;
echo 'PHP_SAPI=' . PHP_SAPI . PHP_EOL;
echo 'php.ini=' . (php_ini_loaded_file() ?: 'none') . PHP_EOL;
echo 'xdebug=' . (extension_loaded('xdebug') ? 'loaded' : 'not loaded') . PHP_EOL;
```

---

## Docker環境

サービス一覧:

```bash
docker compose ps
docker compose config --services
```

PHPサービスが`php`の場合:

```bash
docker compose exec php which php
docker compose exec php php --version
docker compose exec php php --ini
docker compose exec php php -m | grep -i xdebug
```

PHP-FPMの設定確認:

```bash
docker compose exec php php-fpm -i | grep -i xdebug
```

CLIとFPMで異なる設定を読む構成もあるため注意してください。

---

## Xdebugの既存状態を確認

```bash
php -m | grep -i xdebug
php --ri xdebug
```

`php --ri xdebug`で情報が表示されれば、拡張は読み込まれています。

設定だけ確認:

```bash
php -i | grep -E 'xdebug.mode|xdebug.client_host|xdebug.client_port|xdebug.start_with_request'
```

`rg`版:

```bash
php -i | rg 'xdebug.mode|xdebug.client_host|xdebug.client_port|xdebug.start_with_request'
```

---

## アーキテクチャ確認

macOS Apple Siliconでは、PHPと拡張のアーキテクチャ不一致が問題になることがあります。

```bash
uname -m
file "$(which php)"
```

例:

```text
arm64
```

Rosetta経由のx86_64 PHPとarm64拡張を混在させないようにします。

---

## PHP APIバージョン

PHP拡張は対象PHPのAPIバージョンに依存します。

```bash
php -i | grep 'PHP API'
php-config --extension-dir
```

Xdebugの共有ライブラリ確認:

```bash
find "$(php-config --extension-dir)" -name '*xdebug*' -maxdepth 1
```

---

## ポート9003の使用状況

VS Code起動前:

```bash
lsof -nP -iTCP:9003
```

VS Codeで待受開始後:

```bash
lsof -nP -iTCP:9003 -sTCP:LISTEN
```

Linux:

```bash
ss -lntp | grep 9003
```

---

## 環境確認シート

```text
PHP実行場所:
[ ] ホストOS
[ ] Dockerコンテナ
[ ] 仮想マシン
[ ] リモートサーバー

実行方法:
[ ] Browser / PHP-FPM
[ ] Apache mod_php
[ ] CLI
[ ] Queue / Worker
[ ] PHPUnit

PHPバージョン:
PHP SAPI:
php.ini:
追加ini:
Xdebugバージョン:
VS Codeを動かす場所:
接続ポート:
```

---

## 演習

次の結果を取得し、CLIとWebで同じPHPを使っているか判断してください。

```bash
which php
php --version
php --ini
php --ri xdebug
```
