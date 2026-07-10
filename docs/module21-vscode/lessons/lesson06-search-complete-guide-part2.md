
# Lesson06 Search 完全攻略（Part2）

> Module21 VS Code実践

## このPartで学ぶこと

- Globパターン
- Regex検索
- Match Case / Whole Word
- Search Editor
- Replaceの安全な使い方
- ripgrepとの関係

---

# Globとは

Globは検索対象ファイルを絞るためのパターンです。

## よく使う例

```text
**/*.php
```

PHPのみ

```text
src/**
```

src配下

```text
app/**/*.php
```

app配下のPHP

```text
**/*Controller.php
```

Controllerだけ

```text
**/*Repository.php
```

Repositoryだけ

---

# Glob実務例

WordPress

```text
wp-content/themes/**
```

React

```text
src/components/**
```

Laravel

```text
app/Http/**
```

---

# Regex検索

検索欄右側の `.*` をONにすると正規表現検索になります。

例

```regex
get[A-Z]\w+
```

一致例

```
getUser
getProfile
getReserveData
```

---

数字だけ探す

```regex
\d+
```

メールアドレス候補

```regex
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

---

# Match Case

例

検索

```
User
```

Match Case OFF

```
user
USER
User
```

全部一致。

大文字小文字を区別したい調査ではONにします。

---

# Whole Word

検索

```
id
```

OFF

```
id
user_id
id_value
```

ON

```
id
```

だけ。

変数名調査では非常に便利です。

---

# Search Editor

大量検索では Search Editor を使います。

Command Palette

```
Search: Open New Search Editor
```

検索結果をエディタとして保存できます。

メリット

- 比較できる
- メモを書ける
- Git管理できる

---

# Replace

Replaceは必ず

1. Search
2. 件数確認
3. Preview
4. Replace

の順で実施します。

「Replace All」をいきなり押さないこと。

---

# VS Codeとripgrep

VS Codeの全文検索は高速検索エンジンを利用しています。

CLIで確認したい場合

```bash
rg "register_post_type" .
```

検索結果が大量ならCLI、

コードを追うならVS Code、

という使い分けがおすすめです。

---

# ケーススタディ

現象

```
予約画面だけ500
```

調査

1. Searchで reserveConfirm
2. Controllerを特定
3. Service検索
4. Repository検索
5. Debugger停止
6. Git Diff確認

---

# ハンズオン

- Search Editorを開く
- `Route::` を検索
- Regexで `get[A-Z]\w+` を検索
- `**/*Controller.php` に絞る
- rgでも同じ検索を実行して結果を比較する

---

# チェックリスト

- [ ] Globを書ける
- [ ] Regex検索を使える
- [ ] Whole Wordを説明できる
- [ ] Search Editorを開ける
- [ ] rgとの使い分けを説明できる

Part3では

- Go to Definition
- Peek
- Symbol Search
- Workspace Symbol
- Call Hierarchy
- Type Hierarchy

を扱います。
