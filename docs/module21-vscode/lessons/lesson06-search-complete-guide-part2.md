# Lesson06 Search完全攻略 Part2

## ゴール

- Globパターンを組み合わせて検索対象を精密に指定できる
- Search Editorで調査結果を残せる
- 一括置換を安全に実施できる
- VS Code Searchと`rg`を使い分けられる

## Globの基本

Globはファイル名やパスをパターンで指定する記法です。

| パターン | 意味 |
|---|---|
| `*` | 同じ階層の任意文字列 |
| `**` | 複数階層を含む任意パス |
| `?` | 任意の1文字 |
| `{a,b}` | aまたはb |
| `[0-9]` | 指定範囲の1文字 |

## よく使うパターン

すべてのPHPファイル:

```text
**/*.php
```

`src`配下すべて:

```text
src/**
```

Controllerだけ:

```text
**/*Controller.php
```

JavaScriptとTypeScript系:

```text
**/*.{js,jsx,ts,tsx}
```

テストファイル:

```text
**/*.{test,spec}.{js,jsx,ts,tsx}
```

## IncludeとExcludeの設計

調査対象が明確ならIncludeを狭くします。

```text
app/Http/Controllers/**
```

対象が広く、ノイズだけ分かっているならExcludeを使います。

```text
**/vendor/**,**/node_modules/**,**/storage/**
```

両方を使う例:

```text
Include: app/**/*.php
Exclude: app/Generated/**,app/Cache/**
```

## Search Editor

通常のSearch結果はSide Barに表示されます。長い調査ではSearch Editorを使うと、結果をエディタとして保持できます。

Command Palette:

```text
Search: Open New Search Editor
```

用途:

- 複数検索の結果を比較する
- 調査対象を残したままコードを読む
- 結果を保存してレビュー材料にする
- 検索結果内をさらに検索する

Search Editorに表示された結果は、元ファイルへのリンクとして利用できます。

## 置換の安全手順

一括置換は次の順番で行います。

1. Gitの作業ツリーを確認
2. 検索だけ実行
3. 対象件数とファイルを確認
4. Include / Excludeを指定
5. Replace Previewで差分確認
6. 置換実行
7. フォーマット、テスト、Git差分確認

```bash
git status
git diff --stat
```

### 危険な例

`color`を`themeColor`へ全体置換すると、次まで変わる可能性があります。

```text
background-color
border-color
discoloration
```

Whole Word、正規表現、対象ファイルの絞り込みを利用します。

## Capture Groupを使った置換

正規表現で一致部分を保持しながら置換できます。

検索:

```regex
console\.log\((.+)\);
```

置換:

```text
logger.debug($1);
```

`$1`は最初の括弧で捕捉した内容です。構文の入れ子や複数行には単純な正規表現が向かない場合があります。ASTベースのリファクタリングや言語機能を優先すべきケースもあります。

## Preserve Case

置換時に大文字・小文字の形を維持する機能があります。ただし識別子の命名規則を完全に理解するものではないため、Previewを必ず確認します。

## VS Code Searchと`rg`

VS Codeの検索は、コードを見ながら結果を移動するのに向いています。`rg`は結果の加工、件数集計、他コマンドとの連携に向いています。

### VS Code向き

- 一致箇所を順に開く
- 前後コードを読む
- 置換Previewを確認する
- Search Editorに残す

### `rg`向き

```bash
rg -n "register_post_type" .
rg -l "TODO" src
rg -c "console\.log" src
rg "ERROR|WARN" logs/app.log
```

- `-n`: 行番号
- `-l`: ファイル名だけ
- `-c`: ファイルごとの件数

## CLI結果をVS Codeで開く

一致したファイルをVS Codeで開く例:

```bash
rg -l "deprecatedFunction" src | xargs code
```

ファイル名に空白が含まれる環境では、NULL区切りなど安全な方法を検討してください。

特定ファイルの行番号を開く:

```bash
code -g src/app.ts:120:5
```

## 検索が遅いとき

確認項目:

- リポジトリルートより上を開いていないか
- `node_modules`や`vendor`を含めていないか
- ネットワークドライブ上ではないか
- 巨大ログや生成物があるか
- シンボリックリンクをたどっていないか

検索対象を明示的に狭めることが最優先です。

## ハンズオン

1. `**/*.{js,ts}`をIncludeに指定して検索する
2. `**/*.test.*`をExcludeへ追加する
3. Search Editorを開き、結果を保持する
4. 置換Previewだけを実行し、実際には置換しない
5. 同じ検索を`rg -n`でも実行して結果を比較する

## 確認問題

1. `*`と`**`の違いは何ですか。
2. 一括置換前にGit状態を確認する理由は何ですか。
3. Search Editorが通常のSearch結果より便利な場面を1つ挙げてください。
4. VS Code Searchより`rg`が向く作業を1つ挙げてください。

## まとめ

- Globで検索対象を正確に指定する
- 長い調査はSearch Editorへ残す
- 一括置換はPreview、テスト、Git差分までを1セットにする
- 結果閲覧はVS Code、加工と集計は`rg`が得意
