
# 第3章 rg・grep・find 完全攻略

> **目的**: 必要なコードや設定を数秒で見つけられるようになる。

---

# この章で身につくこと

- rg・grep・find の役割の違い
- 高速にコード検索する方法
- 実務で使う検索パターン
- Dockerコンテナ内での検索
- WordPress / PHP案件での検索テクニック

---

# 3つのコマンドの違い

|コマンド|得意分野|
|---|---|
|find|ファイルを探す|
|grep|ファイル内容を検索する|
|rg(ripgrep)|高速にファイル内容を検索する|

実務では **まず rg** を使うことがほとんどです。

---

# find

## PHPファイルを探す

```bash
find . -name "*.php"
```

## ログファイル

```bash
find . -name "*.log"
```

## ディレクトリだけ

```bash
find . -type d
```

## 10MB以上

```bash
find . -size +10M
```

---

# grep

```bash
grep "execute" file.php
grep -R "execute" .
grep -n "PDO" config.php
grep -i "mail" app.log
```

オプション

- -R : 再帰検索
- -n : 行番号
- -i : 大文字小文字無視

---

# rg 基本

```bash
rg execute
rg -n execute
rg -i mail
rg PDO app
```

---

# よく使うオプション

## 行番号

```bash
rg -n execute
```

## 前後3行

```bash
rg -C 3 execute
```

## 前だけ

```bash
rg -B 3 execute
```

## 後だけ

```bash
rg -A 5 execute
```

## PHPのみ

```bash
rg --glob "*.php" execute
```

## vendor除外

```bash
rg -g "!vendor" execute
```

## hidden含む

```bash
rg --hidden DB_HOST
```

## 全ファイル対象

```bash
rg -uu execute
```

---

# 実務で頻出

## メール送信

```bash
rg mail
rg sendMail
rg subject
```

## SQL

```bash
rg SELECT
rg PDO
rg prepare
```

## API

```bash
rg curl
rg fetch
rg axios
```

## WordPress

```bash
rg add_action
rg add_filter
rg register_post_type
```

## ルーティング

```bash
rg routes
rg execute.php
rg confirm.php
```

---

# 組み合わせ

PHPファイル一覧

```bash
rg --files | rg "\.php$"
```

検索件数

```bash
rg execute | wc -l
```

---

# Docker内検索

```bash
docker compose exec web-php8 bash
rg execute /var/www/html
```

---

# ケーススタディ

## ケース1

「問い合わせフォームでメールが飛ばない」

調査順

1. rg mail
2. rg subject
3. rg PHPMailer
4. rg send

---

## ケース2

「DB保存されない」

調査順

1. rg INSERT
2. rg prepare
3. rg execute
4. rg transaction

---

## ケース3

「APIだけ404」

調査順

1. rg route
2. rg rewrite
3. rg nginx
4. rg location

---

# ハンズオン

1. execute.phpを探す
2. confirm.phpを探す
3. PDO生成箇所を探す
4. mail送信処理を探す
5. vendor除外で検索
6. PHPだけ対象に検索
7. 前後3行付きで表示
8. 行番号付き表示
9. SQL実行箇所一覧を作る
10. Dockerコンテナ内で同じ検索

---

# タイムアタック

30秒以内で見つける

- DB接続
- Mail送信
- API呼び出し
- session_start
- include
- require
- Composer
- config
- .env参照

---

# 練習問題

1. findとrgの違いは？
2. grepよりrgが速い理由は？
3. --globは何をする？
4. -Cは何を表示する？
5. vendor除外する理由は？
6. -uuはいつ使う？

---

# チェックリスト

- [ ] findが使える
- [ ] grepが使える
- [ ] rgが使える
- [ ] PHPだけ検索できる
- [ ] vendor除外できる
- [ ] Docker内検索できる
- [ ] 30秒以内にDB接続箇所を探せる

---

# 次章予告

次章では HTTP の基礎を学びます。

ブラウザがどのようにリクエストを送り、サーバーがどう返しているのかを理解すると、curl や API デバッグが格段に分かりやすくなります。
