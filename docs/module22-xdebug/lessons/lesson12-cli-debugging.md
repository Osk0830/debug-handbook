# 22-12 CLI・バッチ・テストのデバッグ

## CLIもXdebugで止められる

PHP CLIプロセスにもXdebugが読み込まれていれば、VS Codeへ接続できます。

確認:

```bash
php --ri xdebug
```

---

## 常時開始設定

```ini
xdebug.start_with_request=yes
```

VS Codeで待受開始後:

```bash
php script.php
```

---

## トリガー設定

```ini
xdebug.start_with_request=trigger
```

実行:

```bash
XDEBUG_TRIGGER=1 php script.php
```

Docker:

```bash
docker compose exec \
  -e XDEBUG_TRIGGER=1 \
  php php script.php
```

---

## 引数付きスクリプト

```bash
XDEBUG_TRIGGER=1 php import.php --file=data.csv --dry-run
```

確認:

```php
$argv
$argc
getopt('', ['file:', 'dry-run'])
```

---

## 標準入力

```bash
cat data.json | XDEBUG_TRIGGER=1 php process.php
```

PHP:

```php
$input = stream_get_contents(STDIN);
```

停止中に`$input`を確認します。

---

## バッチ処理

大量データでは条件付きブレークポイントを使います。

```php
foreach ($rows as $index => $row) {
    process($row);
}
```

条件:

```php
$index === 499
```

または:

```php
($row['id'] ?? null) === 12345
```

---

## PHPUnit

例:

```bash
XDEBUG_TRIGGER=1 ./vendor/bin/phpunit tests/UserServiceTest.php
```

Docker:

```bash
docker compose exec \
  -e XDEBUG_TRIGGER=1 \
  php ./vendor/bin/phpunit tests/UserServiceTest.php
```

対象テストを絞ります。

```bash
./vendor/bin/phpunit --filter testUpdateUser
```

すべてのテストでデバッグを有効にすると遅くなるため、失敗ケースへ絞ります。

---

## Composer Script

```json
{
  "scripts": {
    "debug:test": "XDEBUG_TRIGGER=1 phpunit"
  }
}
```

OS差異を避けるなら、シェルスクリプトやCompose環境変数を使います。

---

## Queue Worker

Workerは長時間起動しています。

設定変更後はWorkerを再起動します。

例:

```bash
docker compose restart worker
```

Supervisor利用時はSupervisor配下のプロセスを再起動します。

Worker内部のPHPにXdebugが読み込まれているか確認してください。

```bash
docker compose exec worker php --ri xdebug
```

---

## Cron

Cronは通常のログインシェルと環境変数が異なります。

確認項目:

- 実行されるPHPの絶対パス
- `php.ini`
- `XDEBUG_TRIGGER`
- 実行ユーザー
- ネットワーク
- カレントディレクトリ

デバッグ用に同じコマンドを手動実行し、再現します。

---

## VS Codeから現在ファイルを起動

`launch.json`:

```json
{
  "name": "Debug current PHP script",
  "type": "php",
  "request": "launch",
  "program": "${file}",
  "cwd": "${workspaceFolder}",
  "runtimeArgs": [
    "-dxdebug.mode=debug",
    "-dxdebug.start_with_request=yes"
  ],
  "args": []
}
```

引数:

```json
"args": [
  "--file",
  "data/sample.csv",
  "--dry-run"
]
```

---

## 無限ループ・常駐処理

```php
while (true) {
    $job = receiveJob();
    process($job);
}
```

通常ブレークポイントでは何度も止まります。

条件付きブレークポイント:

```php
$job?->getId() === 'target-job-id'
```

---

## 演習

CSVインポートの300件目でのみ価格が0になります。

次を使って原因を特定してください。

- CLIトリガー
- 引数確認
- 条件付きブレークポイント
- Watch
- Call Stack
