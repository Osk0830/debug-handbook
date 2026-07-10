# Module21 Troubleshooting

## `code: command not found`

### 確認

```bash
command -v code
```

### macOS

Command Paletteから次を実行します。

```text
Shell Command: Install 'code' command in PATH
```

Terminalを完全に開き直して確認します。

```bash
code --version
```

シェル設定でPATHを上書きしている場合は、`.zshrc`や`.zprofile`も確認します。

## Search結果が0件になる

確認項目:

1. 正しいフォルダを開いているか
2. Match Case、Whole Word、Regexが意図せず有効でないか
3. Includeが狭すぎないか
4. Excludeへ対象が入っていないか
5. `.gitignore`対象ではないか
6. 検索語に全角・半角や見えない空白がないか

まず検索オプションをすべて解除し、短い固有語で再検索します。

## Searchが遅い

### 原因候補

- `node_modules`、`vendor`、`dist`、ログを含む
- ホームディレクトリ全体を開いている
- ネットワークドライブや同期フォルダ上にある
- 巨大ファイルが存在する

### 対応

Workspaceのルートを狭め、`search.exclude`を設定します。

```json
{
  "search.exclude": {
    "**/node_modules": true,
    "**/vendor": true,
    "**/dist": true,
    "**/coverage": true,
    "**/*.log": true
  }
}
```

## 設定を変更しても反映されない

1. UserとWorkspaceのどちらへ設定したか確認
2. 設定画面で`Modified in Workspace`などの表示を確認
3. JSONの構文エラーを確認
4. `Developer: Reload Window`を実行
5. 拡張機能が設定を上書きしていないか確認

## 保存時に意図しないフォーマットが走る

複数フォーマッタが競合している可能性があります。

1. `Format Document With...`を実行
2. `Configure Default Formatter...`を選ぶ
3. 言語ごとの`editor.defaultFormatter`を確認
4. ESLintとPrettierの責務を整理する

例:

```json
{
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

## Explorerでファイルが見えない

`files.exclude`により非表示の可能性があります。Settingsで`files.exclude`を検索してください。Searchには存在するがExplorerにない場合、この設定を疑います。

## ファイルをクリックするとタブが置き換わる

Previewタブです。ファイルをダブルクリックして固定するか、設定を変更します。

```json
{
  "workbench.editor.enablePreview": false
}
```

## 正規表現がエラーになる

- `(`、`[`、`{`の閉じ忘れ
- `\`の不足
- 文字として探したい`.`や`(`を未エスケープ
- 使用中エンジンが非対応の記法

パターンを小さくして、段階的に追加します。

```regex
console
console\.
console\.log
console\.log\(
```

## 一括置換で想定外の箇所まで変わった

未保存ならUndoを試します。Git管理下なら差分を確認します。

```bash
git diff --stat
git diff
```

その変更だけを破棄できる状況なら、VS CodeのSource Controlからファイル単位・hunk単位で戻します。ほかの未コミット変更がある場合、安易な`git reset --hard`は使わないでください。

## 拡張機能導入後にVS Codeが不安定

1. `Developer: Reload Window`
2. 最近入れた拡張を無効化
3. `Help: Start Extension Bisect`で原因候補を絞る
4. Outputの該当チャンネルを確認
5. 再現手順とVS Codeバージョンを記録
