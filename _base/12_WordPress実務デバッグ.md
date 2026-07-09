
# 第12章 WordPress実務デバッグ

> **目的**: WordPress案件で発生しやすい不具合を、テーマ・テンプレート・フック・管理画面・SQL・HTTPの観点から切り分けられるようになる。

---

# この章で身につくこと

- テンプレート階層
- functions.php の役割
- Action / Filter
- カスタム投稿
- カスタムフィールド
- 管理画面の調査
- プラグイン切り分け
- テーマ切り分け
- 本番反映時の確認事項

---

# WordPressのリクエスト

```text
Browser
 ↓
index.php
 ↓
wp-blog-header.php
 ↓
WP Core
 ↓
テーマ
 ↓
テンプレート
 ↓
HTML
```

---

# テンプレート階層

よく使うテンプレート

- front-page.php
- home.php
- archive.php
- single.php
- page.php
- search.php
- 404.php

確認方法

```bash
rg -n "get_header|get_footer|get_template_part" .
```

---

# functions.php

役割

- フック登録
- カスタム投稿
- 管理画面設定
- CSS / JS読み込み

検索

```bash
rg -n "add_action|add_filter|register_post_type|wp_enqueue" .
```

---

# Action と Filter

Action

```php
add_action(...)
```

Filter

```php
add_filter(...)
```

まずは「どこで登録されているか」を探すことが重要です。

---

# カスタム投稿

検索

```bash
rg -n "register_post_type" .
```

確認項目

- スラッグ
- rewrite
- supports

---

# カスタムフィールド

よく見るもの

- ACF
- post_meta

検索

```bash
rg -n "get_field|the_field|get_post_meta" .
```

---

# 管理画面

確認項目

- 投稿が公開済みか
- 下書きではないか
- カスタムフィールド
- メディア登録
- パーマリンク

---

# プラグイン切り分け

症状

- 管理画面だけ壊れる
- JSエラー
- 保存できない

手順

1. エラーログ確認
2. プラグイン停止
3. 再現確認
4. 一つずつ有効化

---

# テーマ切り分け

確認

```bash
rg -n "get_template_part" .
rg -n "locate_template" .
```

---

# DB調査

投稿確認

```sql
SELECT ID,post_title,post_status
FROM wp_posts
ORDER BY ID DESC
LIMIT 20;
```

メタ確認

```sql
SELECT *
FROM wp_postmeta
WHERE post_id=100;
```

---

# 実務シナリオ

## 投稿が表示されない

確認

1. post_status
2. WP_Query条件
3. カテゴリー
4. テンプレート
5. キャッシュ

---

## カスタム投稿だけ404

確認

- register_post_type
- rewrite
- パーマリンク更新

---

## ACFが表示されない

確認

- フィールド名
- post_id
- get_field()
- post_meta

---

# 本番反映

確認リスト

- DB更新
- uploads
- テーマ
- プラグイン
- .htaccess
- パーマリンク
- キャッシュ

---

# ハンズオン

1. register_post_typeを探す
2. add_actionを探す
3. add_filterを探す
4. get_fieldを探す
5. 投稿をSQLで確認
6. post_meta確認
7. テンプレート階層を説明する
8. functions.phpを読む
9. パーマリンク更新
10. キャッシュ削除

---

# タイムアタック

30分以内で

- テンプレート特定
- カスタム投稿定義
- functions.php
- 投稿SQL
- post_meta
- ACF取得

---

# 練習問題

1. front-page.phpとhome.phpの違いは？
2. ActionとFilterの違いは？
3. カスタム投稿が404になる原因は？
4. 投稿が表示されない時に最初に見るSQLは？
5. get_fieldとget_post_metaの違いは？

---

# チェックリスト

- [ ] テンプレート階層を説明できる
- [ ] functions.phpを読める
- [ ] Action / Filterを探せる
- [ ] カスタム投稿を確認できる
- [ ] SQLで投稿を確認できる
- [ ] 本番反映チェックができる

---

# コラム

WordPressの不具合は「テーマ」だけが原因とは限りません。

HTTP・SQL・PHP・テーマ・プラグイン・管理画面のどこで問題が起きているかを切り分けることが最重要です。

---

# 次章予告

第13章では React / API デバッグ編として、Network・状態管理・非同期処理・404・CORS・JSON解析を扱います。
