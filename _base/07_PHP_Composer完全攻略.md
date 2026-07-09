
# 第7章 PHP・Composer 完全攻略

> **目的**: PHP実行環境とComposerを理解し、環境起因の不具合を切り分けられるようになる。

## この章で身につくこと

- PHPバージョン確認
- php.ini確認
- PHPモジュール確認
- Composerの仕組み
- オートロード
- 実務で使うComposerコマンド

---

## PHPバージョン

```bash
php -v
docker compose exec web-php8 php -v
```

---

## php.ini

```bash
php --ini
php -i
php -i | rg memory_limit
php -i | rg upload_max_filesize
php -i | rg post_max_size
php -i | rg max_execution_time
```

---

## PHPモジュール

```bash
php -m
php -m | rg xdebug
php -m | rg pdo
php -m | rg mysqli
```

---

## Composerとは

PHPのパッケージ管理ツールです。

重要ファイル

- composer.json
- composer.lock
- vendor/

---

## よく使うコマンド

```bash
composer install
composer update
composer require monolog/monolog
composer remove vendor/package
composer dump-autoload
composer validate
composer outdated
composer why monolog/monolog
composer why-not php 8.3
```

Docker内

```bash
docker compose exec web-php8 composer install
docker compose exec web-php8 composer dump-autoload
```

---

## install と update

- install: composer.lock通りにインストール
- update: バージョンを更新してcomposer.lockを書き換える

実務では通常 `install` を使います。

---

## dump-autoload

PSR-4や新しいクラスを認識させるために使用します。

---

## 実務シナリオ

### クラスが見つからない

1. namespace
2. use
3. composer.json
4. composer dump-autoload

### PHPだけエラー

```bash
php -v
php --ini
php -m
```

---

## ハンズオン

1. php -v
2. php --ini
3. php -m
4. xdebug確認
5. composer validate
6. composer install
7. composer dump-autoload
8. composer outdated
9. composer why を試す
10. vendor構成を見る

---

## 練習問題

1. installとupdateの違い
2. composer.lockを管理する理由
3. dump-autoloadはいつ使う？
4. php -mで何が分かる？
5. php --iniで何を確認する？
6. composer whyの用途は？

---

## チェックリスト

- [ ] PHPバージョン確認
- [ ] php.ini確認
- [ ] モジュール確認
- [ ] install/updateの違いを説明できる
- [ ] dump-autoloadを実行できる
- [ ] validateを実行できる

---

## 次章予告

第8章ではMySQL・SQL・EXPLAIN・インデックス・実践デバッグを学びます。
