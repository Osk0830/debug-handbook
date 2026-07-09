
# 第10章 VS Code・Xdebug 完全攻略

> **目的**: `echo` や `var_dump()` に頼らず、実行中の処理を追跡して原因を特定できるようになる。

---

# この章で身につくこと

- VS Codeデバッガの基本
- Xdebugの仕組み
- ブレークポイント
- Step Over / Into / Out
- Variables / Watch / Call Stack
- Conditional Breakpoint
- Logpoint
- Debug Console
- PHPデバッグの実践フロー

---

# デバッグとは

デバッグとは「コードを止めて、その瞬間の状態を確認すること」です。

コードを読むだけでは分からない

- 変数
- 引数
- 戻り値
- 分岐

を実際に確認できます。

---

# Xdebugとは

PHP用のデバッガです。

流れ

```
Browser
   │
HTTP Request
   │
PHP
   │
Xdebug
   │
VS Code
```

---

# 起動確認

```bash
docker compose exec web-php8 php -m | rg xdebug
```

設定確認

```bash
docker compose exec web-php8 php -i | rg xdebug
```

---

# launch.json

確認ポイント

- port
- pathMappings
- hostname

例

```json
"pathMappings": {
    "/var/www/html": "${workspaceFolder}"
}
```

---

# ブレークポイント

行番号をクリックして設定します。

処理がその行で停止します。

---

# Step Over (F10)

現在の行だけ実行します。

関数の中には入りません。

---

# Step Into (F11)

関数の中へ入ります。

ライブラリの処理も追えます。

---

# Step Out (Shift+F11)

現在の関数を最後まで実行し、呼び出し元へ戻ります。

---

# Continue (F5)

次のブレークポイントまで実行します。

---

# Variables

現在のスコープに存在する変数を確認します。

見るポイント

- POST値
- Session
- オブジェクト
- 戻り値

---

# Watch

毎回見たい値を登録します。

例

```
$_POST
$user
$result
$count
```

---

# Call Stack

現在どの順番で呼ばれているか確認します。

例

```
index.php
 ↓
controller
 ↓
service
 ↓
repository
```

---

# Debug Console

停止中にPHP式を評価できます。

例

```php
$user
count($items)
$_SESSION
```

---

# Conditional Breakpoint

条件を満たしたときだけ停止

例

```php
$id == 100
```

ループ処理で非常に便利です。

---

# Logpoint

停止せずログだけ出力します。

例

```
User ID: {id}
```

本番に近い調査でも役立ちます。

---

# 実務シナリオ

## フォーム送信

ブレークポイント

```
confirm.php
 ↓
execute.php
 ↓
INSERT
 ↓
Mail送信
```

確認

- POST
- Validation
- SQL
- Mail

---

## API

止める場所

- Controller
- Service
- Repository

確認

- Request
- Response
- SQL

---

## Session

確認

```php
$_SESSION
```

Cookieとの対応も確認します。

---

# 停止しない場合

1.

```bash
php -m | rg xdebug
```

2.

```bash
php -i | rg xdebug
```

3.

```bash
tail -100 /tmp/xdebug.log
```

4.

pathMappings確認

---

# ハンズオン

1. launch.json確認
2. Xdebug有効確認
3. Breakpoint設定
4. GET実行
5. POST実行
6. Variables確認
7. Watch追加
8. Step Into
9. Step Out
10. Logpointを試す

---

# タイムアタック

30秒以内で

- Xdebug確認
- Breakpoint設置
- Variables確認
- Call Stack確認
- Debug Console評価

---

# 練習問題

1. Step OverとStep Intoの違いは？
2. VariablesとWatchの違いは？
3. Conditional Breakpointはいつ使う？
4. Logpointの利点は？
5. pathMappingsは何のため？
6. デバッグが止まらない時に最初に確認することは？

---

# チェックリスト

- [ ] Xdebugが有効か確認できる
- [ ] Breakpointを設定できる
- [ ] Step系を使い分けられる
- [ ] Variablesを読める
- [ ] Watchを使える
- [ ] Call Stackを読める
- [ ] Logpointを使える

---

# コラム

**デバッガは「答え」を教えてくれるツールではありません。**

「実際に何が起きているか」を確認するためのツールです。

HTTP・Docker・SQL・Gitと組み合わせることで、初めて強力な武器になります。

---

# 次章予告

第11章では「実践デバッグフロー」として、

**HTTP → curl → Docker → ログ → rg → SQL → Xdebug → Git**

を組み合わせて、実際の障害を解く流れを学びます。
