# Module22 Xdebug完全攻略

> **この章のテーマ**
>
> PHPの処理を「読む」のではなく、実行中の状態を観測しながら原因を特定できるようになる。

---

## この章で学ぶこと

この章では、VS CodeとXdebugを使ったPHPデバッグを、導入から実務運用まで体系的に学びます。

- Xdebugが動く仕組み
- PHP・Xdebug・VS Codeの役割分担
- ローカル環境への導入
- Docker環境への導入
- `php.ini` / Xdebug設定
- VS CodeのPHP Debug拡張
- `launch.json`
- ブレークポイント
- Step Over / Step Into / Step Out
- Variables / Watch / Call Stack
- Conditional Breakpoint / Hit Count / Logpoint
- Webリクエストのデバッグ
- CLI・バッチ・テストのデバッグ
- Dockerの`pathMappings`
- 「ブレークポイントで止まらない」問題の切り分け
- WordPress・API・フォーム処理の実践デバッグ

---

## Xdebugを使う目的

PHPの不具合調査では、次のようなコードを追加しがちです。

```php
var_dump($user);
exit;
```

あるいは、

```php
error_log(print_r($data, true));
```

これらは便利ですが、複雑な処理では次の問題が起きます。

- 調査用コードを何度も追加・削除する
- 処理を途中で止めるため、後続処理を確認できない
- 呼び出し元を追いにくい
- ループ内の特定ケースだけを調べにくい
- オブジェクトの状態を継続して観測しにくい
- 調査コードを消し忘れる

Xdebugを使うと、ソースコードを変更せずに処理を止め、その瞬間の状態を観測できます。

```text
Browser / curl / CLI
        │
        ▼
      PHP
        │
        ▼
     Xdebug
        │ DBGp
        ▼
VS Code PHP Debug
```

---

## Lesson一覧

- [Lesson01 Xdebugの仕組み](lessons/lesson01-xdebug-architecture.md)
- [Lesson02 導入前の環境確認](lessons/lesson02-environment-check.md)
- [Lesson03 ローカル環境へのインストール](lessons/lesson03-local-installation.md)
- [Lesson04 Docker環境へのインストール](lessons/lesson04-docker-installation.md)
- [Lesson05 Xdebug設定](lessons/lesson05-xdebug-configuration.md)
- [Lesson06 VS Codeとlaunch.json](lessons/lesson06-vscode-launch-json.md)
- [Lesson07 ブレークポイントと基本操作](lessons/lesson07-breakpoints-and-stepping.md)
- [Lesson08 Variables・Watch・Debug Console](lessons/lesson08-variables-watch-console.md)
- [Lesson09 Call Stack](lessons/lesson09-call-stack.md)
- [Lesson10 条件付きブレークポイント](lessons/lesson10-advanced-breakpoints.md)
- [Lesson11 Webリクエストのデバッグ](lessons/lesson11-web-debugging.md)
- [Lesson12 CLI・バッチ・テストのデバッグ](lessons/lesson12-cli-debugging.md)
- [Lesson13 DockerとpathMappings](lessons/lesson13-path-mappings.md)
- [Lesson14 実務ケース](lessons/lesson14-real-world-cases.md)
- [Lesson15 接続トラブルシューティング](lessons/lesson15-debug-connection-troubleshooting.md)
- [Lesson16 総合演習](lessons/lesson16-capstone.md)

## 補助教材

- [Lab01 ローカルPHPをXdebugで停止する](labs/lab01-local-xdebug.md)
- [Lab02 Docker環境のXdebug接続を切り分ける](labs/lab02-docker-debug-workflow.md)
- [Beginner Exercises](exercises/beginner.md)
- [Answers](exercises/answers.md)
- [Cheatsheet](cheatsheet.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)


## 推奨環境

- macOS / Linux / Windows
- PHP 8系
- Xdebug 3系
- VS Code
- 拡張機能: PHP Debug
- Docker Composeを利用する場合はDocker Desktop

本章ではXdebug 3系を前提にします。

Xdebug 2系の設定例としてよく見かける次の項目は、Xdebug 3系では使用しません。

```ini
xdebug.remote_enable
xdebug.remote_host
xdebug.remote_port
xdebug.remote_autostart
```

Xdebug 3系では、主に次の設定を使用します。

```ini
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=host.docker.internal
xdebug.client_port=9003
```

---

## 最初に覚える診断コマンド

```bash
php --version
php --ini
php -m | grep -i xdebug
php --ri xdebug
```

`ripgrep`を使う場合:

```bash
php -m | rg -i xdebug
php -i | rg 'xdebug.mode|xdebug.client_|xdebug.start_with_request'
```

Docker環境:

```bash
docker compose ps
docker compose exec php php --version
docker compose exec php php --ini
docker compose exec php php --ri xdebug
```

サービス名が`php`でない場合は、実際のサービス名に読み替えてください。

---

## 学習時の原則

### 1. ブレークポイントは仮説の場所に置く

無計画に大量のブレークポイントを置くのではなく、次の境界を優先します。

- 入力を受け取る場所
- バリデーション直前・直後
- 条件分岐
- 外部API呼び出し前後
- SQL実行前後
- 戻り値を返す直前
- 例外が発生する可能性のある場所

### 2. 値だけでなく経路を見る

変数が間違っているとき、原因がその行にあるとは限りません。

`Call Stack`を使い、どこからどの引数で呼ばれたのかを確認します。

### 3. 設定問題とコード問題を分離する

ブレークポイントで止まらないときは、コードの問題とは限りません。

```text
Xdebug未導入
  ↓
Xdebug無効
  ↓
VS Code未待受
  ↓
接続先ホスト不一致
  ↓
ポート不一致
  ↓
pathMappings不一致
  ↓
対象コードが実行されていない
```

この順番で切り分けます。

---

## 完了チェック

- [ ] Xdebugの通信の流れを説明できる
- [ ] Xdebugが読み込まれているか確認できる
- [ ] `xdebug.mode`を確認できる
- [ ] VS Codeでデバッグ待受を開始できる
- [ ] ブレークポイントで処理を止められる
- [ ] Step系操作を使い分けられる
- [ ] VariablesとWatchを使える
- [ ] Call Stackから呼び出し元を追える
- [ ] 条件付きブレークポイントを使える
- [ ] Dockerの`pathMappings`を設定できる
- [ ] CLIスクリプトをデバッグできる
- [ ] 止まらない原因を段階的に切り分けられる
