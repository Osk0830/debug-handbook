# Lesson06 Search完全攻略 Part1

## ゴール

- Search Viewでワークスペース全体を検索できる
- 検索語を現象から組み立てられる
- Include / Excludeを使ってノイズを減らせる
- Explorerで順番に読むより速く目的のコードへ到達できる

## Searchはデバッグの入口

未知のコードを最初から読むのは非効率です。実務では現象に含まれる手掛かりを検索し、関係箇所だけを読みます。

```text
画面の文言
URL
エラーメッセージ
API名
CSSクラス
関数名
設定キー
```

これらは検索語になります。

## Search Viewを開く

```text
macOS: Cmd + Shift + F
Windows/Linux: Ctrl + Shift + F
```

主な項目:

- Search: 検索文字列
- Replace: 置換文字列
- Files to include: 検索対象
- Files to exclude: 除外対象
- Results: 結果一覧

## 最初の検索語を選ぶ

### 良い検索語

- エラー全文の特徴的な部分
- 画面にしか出ない固有文言
- URLのパス
- APIエンドポイント
- 設定キー

### ノイズが多い検索語

```text
id
name
data
error
user
```

一般語は大量に一致します。まず固有語で位置を特定し、その周辺から関数名や変数名へ検索をつなげます。

## 検索の連鎖

画面に「予約内容を確認できません」と表示された場合:

```text
"予約内容を確認できません"
  ↓
メッセージを出している条件分岐
  ↓
呼び出しているAPI関数名
  ↓
API URL
  ↓
レスポンス処理
```

1回の検索で原因へ到達しようとせず、**検索結果から次の検索語を得る**のが実務的です。

## Match Case / Whole Word / Regex

検索欄右側の切り替え:

| 機能 | 用途 |
|---|---|
| Match Case | 大文字・小文字を区別 |
| Match Whole Word | 単語単位で一致 |
| Use Regular Expression | 正規表現を使用 |

例として`User`を検索すると、Match Caseが無効な場合は`user`や`USER`も候補になります。

`id`をWhole Wordで検索すると、`user_id`との一致を避けられる場合があります。ただし言語や単語境界の扱いにより結果は変わるため、結果を必ず確認します。

## Files to include

検索対象をGlobで絞ります。

```text
src/**
```

```text
**/*.php
```

```text
**/*Controller.php
```

複数指定:

```text
**/*.php,**/*.js,**/*.ts
```

### 実務例

WordPressテーマのみ:

```text
wp-content/themes/my-theme/**
```

LaravelのController:

```text
app/Http/Controllers/**/*.php
```

Reactコンポーネント:

```text
src/components/**/*.{js,jsx,ts,tsx}
```

## Files to exclude

依存物、生成物、キャッシュを除外します。

```text
**/node_modules/**,**/vendor/**,**/dist/**,**/build/**,**/coverage/**
```

検索結果が多すぎる場合、検索語を複雑にする前に対象範囲を見直します。

## `.gitignore`と検索除外

VS Code Searchは設定により`.gitignore`や`search.exclude`を利用します。検索結果に出ない場合は、検索欄の設定やWorkspace設定を確認します。

一時的に除外設定を無視して検索する場合もありますが、巨大な依存フォルダを含めると検索が遅くなるため注意してください。

## Search結果の読み方

結果はファイル単位でまとまります。

確認する順番:

1. 一致件数
2. 一致したファイル数
3. パス
4. 前後のコード
5. 同じ語が定義と利用のどちらにあるか

同名関数が複数ある場合、`src`、`tests`、`vendor`、`dist`などのパスを見て優先度を判断します。

## 実務ケース1: WordPress

カスタム投稿タイプの定義を探す:

```text
register_post_type(
```

フックを探す:

```text
add_action(
```

テンプレート階層の候補を絞る:

```text
single-
archive-
```

Include:

```text
wp-content/themes/my-theme/**/*.php
```

## 実務ケース2: Laravel

URLからルートを探す:

```text
Route::
```

またはURLの一部:

```text
/reservations
```

次にController名、Service名、Repository名へ検索をつなげます。

## 実務ケース3: React

画面文言を検索し、コンポーネントを特定します。次にprops名、API関数、state更新箇所を追います。

```text
予約内容
```

Include:

```text
src/**/*.{ts,tsx}
```

## ハンズオン

サンプルプロジェクトで次を実行してください。

1. `TODO`を全体検索する
2. `src/**`だけに絞る
3. テストファイルを除外する
4. 大文字・小文字を区別して検索する
5. 検索結果から別の識別子を選び、2回目の検索を行う

調査記録として、検索語、件数、次に選んだ検索語を書き残してください。

## 確認問題

1. 一般語より固有文言を優先する理由は何ですか。
2. Include / Excludeを使う主な目的は何ですか。
3. 1回の検索で原因が分からない場合、次に何をしますか。

## まとめ

- 現象に含まれる固有情報を検索語へ変換する
- Searchから次のSearchへ連鎖させる
- Include / Excludeで検索対象を管理する
- 件数だけでなくパスと前後コードを読む
