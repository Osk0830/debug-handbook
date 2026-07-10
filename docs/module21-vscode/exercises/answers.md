# Answers

## 問題1

VS Codeはコードを読みながら検索する、差分を見る、Debuggerを使う作業が得意です。CLIはログ加工、大量検索、集計、自動化が得意です。

## 問題2

例:

- ワークスペース全体検索が使える
- Gitリポジトリを認識できる
- Workspace設定が適用される
- importやシンボル解析の範囲が正しくなる
- Terminalの開始位置をプロジェクトルートにできる

## 問題3

User設定:

- 個人のフォントサイズ
- 個人のテーマ

Workspace設定:

- チーム共通のPrettier指定
- 案件固有の検索除外

## 問題4

- Problems: リンター、型、構文などの問題一覧
- Output: 拡張機能やタスクが出力したログ
- Terminal: シェルコマンドを対話的に実行する場所

## 問題5

Command Paletteでコマンド名を検索して実行します。

```text
Preferences: Open User Settings (JSON)
Preferences: Open Keyboard Shortcuts
Terminal: Create New Terminal
Developer: Reload Window
```

## 問題6

プロジェクトにより異なります。役割をファイル名だけで決めず、内容も確認してください。

## 問題7

例:

```text
src/**/*.ts
```

TSXも含める場合:

```text
src/**/*.{ts,tsx}
```

## 問題8

```text
**/node_modules/**,**/vendor/**,**/dist/**
```

## 問題9

```regex
console\.(log|warn|error)\(
```

## 問題10

```regex
https?://
```

`?`により直前の`s`が0回または1回になります。

## 問題11

```regex
\b(TODO|FIXME|HACK)\b
```

## 問題12

1. VS Code Search: 前後コードを視覚的に確認しやすい
2. `rg`: `-c`で件数集計しやすい
3. VS Code Search: Replace Previewがある
4. `rg`: パイプや`xargs`へ渡しやすい

## 問題13

例:

1. `git status`
2. 検索だけ実行
3. 件数・対象ファイル確認
4. Include / Exclude設定
5. Replace Preview
6. 少数箇所で試す
7. 置換実行
8. Format / Lint / Test
9. `git diff`

## 問題14

例:

- スコープを理解して変数名を変更する
- import元を追跡してクラス名を変更する
- コメントや文字列を除外して識別子だけ変更する

## 問題15

案件ごとに異なります。評価ポイントは、画面文言から検索を開始し、条件分岐、関数、呼び出し元へ検索をつなげられていることです。


# Lesson08以降の解答方針

演習は単一のコマンド名ではなく、次の観点で評価します。

- 現象と期待結果が区別されている
- 静的診断と実行時エラーが区別されている
- 正常系との比較がある
- 仮説ごとに検証方法がある
- 修正前後のテストとGit差分を確認している
- 秘密情報や本番データを不適切に扱っていない
- AIや拡張の表示だけで原因を断定していない
