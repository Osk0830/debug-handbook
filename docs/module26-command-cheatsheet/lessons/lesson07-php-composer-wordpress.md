# Lesson07 PHP・Composer・WordPress

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## PHP基本

```bash
php -v
php --ini
php -m
php -l path/to/file.php
php -r 'echo PHP_VERSION, PHP_EOL;'
```

**判断ポイント:** CLIとWebで異なるphp.iniを使う場合がある。

## Composer

```bash
composer --version
composer validate
composer install
composer update vendor/package
composer dump-autoload -o
composer diagnose
```

**判断ポイント:** `install`はlockに従い、`update`はlockを書き換える。

## PHP実行・ログ

```bash
php script.php
php -d display_errors=1 -d error_reporting=E_ALL script.php
tail -f /path/to/php-error.log
```

**判断ポイント:** 本番では画面表示せず、ログへ安全に出力する。

## WP-CLI

```bash
wp core version
wp plugin list
wp theme list
wp option get siteurl
wp cache flush
wp rewrite flush
```

**判断ポイント:** 本番操作前に対象URL・環境・バックアップを確認する。

## WordPress調査

```bash
wp plugin deactivate plugin-slug
wp theme activate twentytwentysix
wp db query 'SELECT option_name FROM wp_options LIMIT 10;'
wp search-replace 'old.example.com' 'new.example.com' --dry-run
```

**判断ポイント:** `search-replace`は必ず`--dry-run`で影響を確認する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
