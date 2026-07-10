# 22-03 ローカル環境へのインストール

## インストール方法を選ぶ

Xdebugの導入方法はPHPの導入方法に合わせます。

- Homebrew PHP
- PECL
- OSパッケージ
- 手動ビルド
- Windows DLL

本章では代表例を扱います。

---

## PECLで導入

前提確認:

```bash
php --version
pecl version
phpize --version
php-config --version
```

インストール:

```bash
pecl install xdebug
```

インストール後に表示される共有ライブラリのパスを確認します。

例:

```text
Installing '/path/to/php/extensions/.../xdebug.so'
```

---

## ini設定

例:

```ini
zend_extension=xdebug
```

フルパス指定が必要な環境:

```ini
zend_extension=/path/to/php/extensions/no-debug-non-zts-xxxxxxxx/xdebug.so
```

Xdebugは通常の`extension`ではなく、`zend_extension`で読み込みます。

```ini
; 推奨
zend_extension=xdebug

; 避ける
extension=xdebug
```

---

## Homebrew PHP

PHPの設定場所を確認:

```bash
brew --prefix
brew --prefix php
php --ini
```

追加設定ディレクトリ例:

```text
/opt/homebrew/etc/php/8.3/conf.d/
```

Xdebug設定ファイル例:

```bash
touch /opt/homebrew/etc/php/8.3/conf.d/99-xdebug.ini
```

内容:

```ini
zend_extension=xdebug

[xdebug]
xdebug.mode=debug,develop
xdebug.start_with_request=yes
xdebug.client_host=127.0.0.1
xdebug.client_port=9003
xdebug.log_level=0
```

Webサーバーを再起動:

```bash
brew services restart php
```

バージョン付きサービスの場合:

```bash
brew services restart php@8.3
```

---

## Ubuntu / Debian系

パッケージ例:

```bash
sudo apt update
sudo apt install php-xdebug
```

特定バージョン:

```bash
sudo apt install php8.3-xdebug
```

設定確認:

```bash
php --ini
php --ri xdebug
```

PHP-FPM再起動例:

```bash
sudo systemctl restart php8.3-fpm
```

Apache利用時:

```bash
sudo systemctl restart apache2
```

---

## インストール後の確認

```bash
php --version
```

表示例:

```text
with Xdebug v3.x.x
```

詳細:

```bash
php --ri xdebug
```

モジュール:

```bash
php -m | grep -i xdebug
```

---

## 二重読み込み

次のような警告が出る場合:

```text
Cannot load Xdebug - it was already loaded
```

複数のiniで`zend_extension=xdebug`を記述している可能性があります。

```bash
php --ini
grep -R "zend_extension.*xdebug" /path/to/php/conf.d
```

`rg`:

```bash
rg 'zend_extension\s*=.*xdebug' /path/to/php
```

1か所だけにします。

---

## PHP更新後に消えた場合

PHPのマイナーバージョン更新後、拡張ディレクトリが変わる場合があります。

確認:

```bash
php-config --extension-dir
php --ri xdebug
```

必要に応じて、現在のPHPに対して再インストールします。

```bash
pecl uninstall xdebug
pecl install xdebug
```

---

## 確認用スクリプト

```php
<?php

printf("PHP: %s\n", PHP_VERSION);
printf("SAPI: %s\n", PHP_SAPI);
printf("php.ini: %s\n", php_ini_loaded_file() ?: 'none');
printf(
    "Xdebug: %s\n",
    extension_loaded('xdebug') ? phpversion('xdebug') : 'not loaded'
);
```

実行:

```bash
php check-xdebug.php
```

---

## 演習

1. 自分のPHPが読み込む`php.ini`を確認する。
2. Xdebug専用iniの場所を確認する。
3. `php --ri xdebug`でバージョンを確認する。
4. 二重読み込みがないことを確認する。
