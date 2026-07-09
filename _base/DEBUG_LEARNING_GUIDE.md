# デバッグとCLI学習ガイド（このリポジトリ向け）

このガイドは、`rg`、`curl`、`docker compose`、SQL、Git応用、VS Codeデバッガを実務で使いこなすための実践トレーニング手順です。

## 目的

- 推測ではなく、事実ベースで素早く原因を絞り込めるようにする。
- 再現可能なコマンドで不具合を追えるようにする。
- CLI調査とステップ実行デバッグを行き来できるようにする。

## 前提環境

- アプリURL: http://localhost:8081/wedding/
- DB接続先: localhost:3306
- 主なコンテナ: `web-php8`, `db`, `mailhog`
- VS Codeデバッグ設定: `.vscode/launch.json`

## 日次ルーティン（30-45分）

1. 環境を起動し、状態を確認する。
2. 1つの調査テーマを決める（フォーム、API、SQL不整合など）。
3. まずCLIだけで調査する。
4. 次にVS Codeデバッガで同じ経路を追って比較する。
5. 原因・証拠・修正内容を短くメモする。

## フェーズ1: コマンド基礎

### 1) rg (ripgrep)

目的:

- ロジックの所在をすぐ見つける。
- 呼び出し経路や定数のつながりを素早く追う。

基本コマンド:

```bash
rg -n "execute.php|confirm.php|finish.php" inquiry data
rg -n "DB_HOST|DB_NAME|PDO|mysqli" app app2
rg --glob "*.php" -n "mail|send|subject" inquiry data
```

練習課題:

- 問い合わせフォームの入力画面から送信完了までの経路を追跡する。

到達目標:

- 3分以内に対象ファイルと実行順序を説明できる。

### 2) curl

目的:

- ブラウザなしでリクエストを再現する。
- ヘッダ、本文、ステータス差分を素早く確認する。

Core commands:

```bash
curl -I "http://localhost:8081/wedding/"
curl -v "http://localhost:8081/wedding/inquiry/"
curl -sS "http://localhost:8081/wedding/fair/" -o /tmp/fair.html
curl -sS -X POST "http://localhost:8081/wedding/inquiry/confirm.php" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "name=Test&email=test@example.com"
```

練習課題:

- 1つのエンドポイントで GET と POST の差分を確認する。

到達目標:

- ステータス、リダイレクト、レスポンス本文の違いを説明できる。

### 3) docker compose

目的:

- 開発環境の起動・停止・再起動を確実に行う。
- ログ確認とコンテナ内部確認を素早く行う。

Core commands:

```bash
docker compose up -d --build web-php8 db mailhog
docker compose ps
docker compose logs -f --tail=200 web-php8
docker compose exec web-php8 bash
docker compose restart web-php8
docker compose down
```

練習課題:

- `php.ini` を変更し、再起動後に反映を確認する。

到達目標:

- `php -i` とログで設定反映を検証できる。

### 4) SQL

目的:

- DB上の事実を直接確認する。
- 保存・更新挙動を推測で判断しない。

Core commands:

```bash
docker compose exec -it db mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME"
```

MySQL内で実行:

```sql
SHOW TABLES;
SELECT * FROM some_table ORDER BY id DESC LIMIT 20;
SELECT col1, col2 FROM some_table WHERE created_at >= NOW() - INTERVAL 1 DAY;
EXPLAIN SELECT col1 FROM some_table WHERE email = 'test@example.com';
```

練習課題:

- 1件のフォーム送信がどのテーブル・カラムに反映されるかを確認する。

到達目標:

- 問題の存在/解消を示すSQLを1本提示できる。

## フェーズ2: デバッグ向け Git 応用

### 優先して覚えるコマンド

```bash
git log --oneline --graph --decorate -n 30
git diff
git diff --staged
git blame path/to/file.php
git reflog -n 30
git restore --staged path/to/file.php
git restore path/to/file.php
git stash -p
git cherry-pick <commit>
git rebase -i HEAD~5
```

### bisect 練習

```bash
git bisect start
git bisect bad
git bisect good <known_good_commit>
# 各ステップで再現テストを実行
git bisect good  # or git bisect bad
git bisect reset
```

練習課題:

- 再現できる不具合を1つ選び、混入コミットを特定する。

到達目標:

- 候補コミットを絞り込み、原因コミットを1つ示せる。

## フェーズ3: VS Code デバッガ運用

## セットアップ確認

1. コンテナが起動していることを確認する。
2. VS Code で `Xdebug待ち受け (web-php8)` を開始する。
3. リクエスト経路上のファイルにブレークポイントを置く。
4. ブラウザまたは curl でリクエストを発火する。
5. `Variables`、`Watch`、`Call Stack` を確認する。
6. `Debug Console` で式評価する。

## よく使うデバッグ技法

- Conditional Breakpoint:
  - 条件一致時だけ停止する。
- Logpoint:
  - 停止せずに値だけ出力する。
- Step Over / Step Into / Step Out:
  - 内部実装が必要な場面だけ Step Into を使う。
- Watch expressions:
  - 重要な式を常時監視して変化を追う。

## トラブルシュート

ブレークポイントで停止しない場合:

1. xdebug モジュールの読込確認:

```bash
docker compose exec web-php8 php -m | rg -i xdebug
```

2. xdebug の実行時設定を確認:

```bash
docker compose exec web-php8 php -i | rg -n "xdebug.mode|xdebug.start_with_request|xdebug.client_host|xdebug.client_port"
```

3. ログ確認:

```bash
docker compose exec web-php8 tail -n 200 /tmp/xdebug.log
```

4. `.vscode/launch.json` のパスマッピング確認:

- `/var/www/html` -> `${workspaceFolder}`

## 2週間の学習プラン

### Week 1（基礎）

Day 1:

- inquiry/data の経路を rg で追跡。

Day 2:

- curl で GET/POST とヘッダ差分を確認。

Day 3:

- docker compose の起動・停止・ログ確認を反復。

Day 4:

- SQL の SELECT/WHERE/ORDER BY/EXPLAIN を反復。

Day 5:

- CLIのみで不具合調査を一通り実施。

Day 6:

- 同じ不具合を VS Code デバッガで追跡。

Day 7:

- メモを整理し、自分用コマンド集を作成。

### Week 2（応用）

Day 8:

- git reflog / restore を反復。

Day 9:

- git rebase -i / cherry-pick を反復。

Day 10:

- 用意した不具合で git bisect を実施。

Day 11:

- rg -> curl -> SQL -> デバッガ の統合フロー練習。

Day 12:

- 30分以内で1件解くタイムアタック。

Day 13:

- 領域を変えて反復（news/fair/inquiry）。

Day 14:

- ベストコマンドと判断フローを最終整理。

## すぐ使える判断フロー

1. まずコード位置を知りたい: `rg`
2. リクエストを再現したい: `curl`
3. 環境や設定が怪しい: `docker compose logs/exec`
4. データの事実を確認したい: SQL
5. 実行中の値変化を追いたい: VS Code デバッガ
6. いつ壊れたか履歴追跡したい: `git bisect` と `git reflog`

## バグ修正の完了条件

- 再現コマンド（curl もしくは URL + パラメータ）がある。
- 根本原因が、ログ・SQL・変数値などの証拠付きで説明されている。
- 修正は最小限で、git diff で確認済み。
- リグレッション確認が完了している。
- 開発メモに要点が残されている。
