# Lab01 SearchとTerminal

## 目的

同じ調査をVS Code Searchと`rg`で実行し、結果の見やすさ、絞り込み、加工の違いを体験します。

## 所要時間

30〜45分

## 準備

```bash
mkdir -p ~/debug-handbook-labs/vscode-search/src \
  ~/debug-handbook-labs/vscode-search/tests \
  ~/debug-handbook-labs/vscode-search/vendor/sample
cd ~/debug-handbook-labs/vscode-search
```

次のファイルを作成します。

```bash
cat > src/user.js <<'EOF'
export function getUser(id) {
  console.log('getUser', id); // TODO: remove debug output
  return { id, name: 'Alice' };
}
EOF

cat > src/profile.js <<'EOF'
export function getProfile(userId) {
  console.warn('temporary profile warning'); // FIXME
  return fetch(`https://example.com/users/${userId}`);
}
EOF

cat > tests/user.test.js <<'EOF'
console.log('test only');
EOF

cat > vendor/sample/library.js <<'EOF'
console.error('vendor error');
EOF

git init
git add .
git commit -m "Add VS Code search lab"
code .
```

Gitのユーザー設定がない環境では、コミットは省略して構いません。

## 課題1 通常検索

VS Code Searchで`getUser`を検索します。

記録:

```text
一致件数:
一致ファイル:
定義と利用のどちらが見つかったか:
```

CLIでも実行します。

```bash
rg -n "getUser" .
```

## 課題2 Include

VS Code Searchで`console`を検索し、Includeへ次を指定します。

```text
src/**
```

CLI:

```bash
rg -n "console" src
```

検索結果がどう変わったか記録します。

## 課題3 Exclude

ワークスペース全体を対象にしながら、次を除外します。

```text
**/tests/**,**/vendor/**
```

CLI:

```bash
rg -n "console" . -g '!tests/**' -g '!vendor/**'
```

## 課題4 正規表現

次をまとめて検索します。

```regex
console\.(log|warn|error)\(
```

CLI:

```bash
rg -n 'console\.(log|warn|error)\(' .
```

## 課題5 TODO系コメント

```regex
\b(TODO|FIXME|HACK)\b
```

`src/**`に限定して検索してください。

## 課題6 URL

URL候補を検索します。

```regex
https?://[^\s"'<>`]+
```

一致したURLが本当に外部通信先か、コード周辺も確認します。

## 課題7 件数集計

CLIでファイルごとの`console`件数を表示します。

```bash
rg -c "console" .
```

VS Code Searchの表示と比較してください。

## 課題8 Search Editor

Command Paletteから新しいSearch Editorを開き、デバッグ出力の検索結果を表示します。

```text
Search: Open New Search Editor
```

結果を残したまま、各ファイルを開いて確認します。

## 課題9 置換Preview

`console.log`を`logger.debug`へ置換する設定を作ります。ただし実行前にPreviewし、次を確認してください。

- testsやvendorを除外できているか
- 引数が保持されるか
- `logger`が未定義であり、そのまま置換すると壊れること

この課題では置換を実行しません。**機械的に置換できても、意味的に正しいとは限らない**ことを確認します。

## 振り返り

次に答えてください。

1. コードを読みながら調べやすかったのはどちらか
2. 件数を集計しやすかったのはどちらか
3. Include / Excludeの書き方はどう違ったか
4. 正規表現の結果に誤検出はあったか
5. 一括置換を実行しなかった理由は何か

## 完了条件

- Searchと`rg`の両方で同じ調査を実施した
- Include / Excludeを使った
- 正規表現を3種類以上試した
- Search Editorを開いた
- 置換Previewの危険性を説明できた
