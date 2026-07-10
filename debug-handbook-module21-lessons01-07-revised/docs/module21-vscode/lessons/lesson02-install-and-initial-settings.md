# Lesson02 インストールと初期設定

## ゴール

- VS Codeを安全に導入できる
- User設定とWorkspace設定の違いを説明できる
- 最低限の設定と拡張機能を自分で管理できる

## Stable版を使う

通常の業務ではVS Code Stableを使用します。Insiders版は新機能を早く試せますが、業務環境の再現性を優先する場合はStable版が適しています。

インストール後、Command Paletteから次を確認します。

```text
Help: About
```

バージョン、コミット、OS、CPUアーキテクチャが表示されます。不具合報告時に必要になる情報です。

## `code`コマンドを使えるようにする

macOSではCommand Paletteを開き、次を実行します。

```text
Shell Command: Install 'code' command in PATH
```

Terminalを開き直して確認します。

```bash
code --version
code .
```

`command not found`になる場合は[トラブルシューティング](../troubleshooting.md)を参照してください。

## 設定の3つの範囲

| 種類 | 適用範囲 | 主な用途 |
|---|---|---|
| Default | VS Code標準 | 参照用 |
| User | すべてのプロジェクト | 個人の見た目・操作 |
| Workspace | 現在のプロジェクト | チーム共通の規約 |

Workspace設定は通常、プロジェクト内の`.vscode/settings.json`へ保存されます。

```text
project/
└── .vscode/
    └── settings.json
```

## 推奨User設定

次は一例です。値はチームルールに合わせて調整してください。

```json
{
  "editor.fontSize": 13,
  "editor.lineHeight": 1.7,
  "editor.wordWrap": "wordWrapColumn",
  "editor.wordWrapColumn": 100,
  "editor.minimap.enabled": false,
  "editor.formatOnSave": true,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "workbench.startupEditor": "none",
  "terminal.integrated.scrollback": 10000
}
```

### 設定をJSONで開く

Command Paletteから次を実行します。

```text
Preferences: Open User Settings (JSON)
```

GUI設定とJSON設定は同じ内容を別の方法で編集しています。設定名を正確に確認したい場合はGUI、まとめて管理したい場合はJSONが便利です。

## Workspace設定の例

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/.git": true,
    "**/node_modules": true,
    "**/vendor": false
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/vendor": true,
    "**/dist": true
  }
}
```

`files.exclude`はExplorer上の表示、`search.exclude`は検索対象に影響します。役割を混同しないでください。

## 拡張機能の選び方

言語や案件に応じて導入します。

| 用途 | 代表例 |
|---|---|
| Git履歴 | GitLens |
| エラーの行内表示 | Error Lens |
| JavaScript / TypeScript検査 | ESLint |
| フォーマット | Prettier |
| PHP補完 | PHP Intelephense |
| Python | Python |
| コンテナ | Docker / Dev Containers |

同じ役割のフォーマッタやリンターを複数有効にすると競合しやすいため、言語ごとに担当を決めます。

## 拡張機能をCLIで管理する

一覧を保存できます。

```bash
code --list-extensions > extensions.txt
```

別環境で一括インストールする例です。

```bash
while IFS= read -r extension; do
  code --install-extension "$extension"
done < extensions.txt
```

空行やコメントを含む管理ファイルを使う場合は、スクリプト側で除外処理を追加してください。

## 設定をGit管理するときの判断

### Git管理に向くもの

- `.vscode/settings.json`
- `.vscode/extensions.json`
- `.vscode/tasks.json`
- `.vscode/launch.json`
- チームで共有するスニペット

### Git管理に向かないもの

- 個人の画面テーマ
- 個人のフォントサイズ
- 秘密情報を含む設定
- ローカル固有の絶対パス

`.vscode/settings.json`を無条件で`.gitignore`へ入れるのではなく、共有価値で判断します。

## ハンズオン

1. `code --version`を実行する
2. User Settings(JSON)を開く
3. `editor.minimap.enabled`を`false`にする
4. サンプルプロジェクトに`.vscode/settings.json`を作る
5. `code --list-extensions`で拡張一覧を保存する

## 確認問題

1. User設定とWorkspace設定の違いは何ですか。
2. `files.exclude`と`search.exclude`の違いは何ですか。
3. 拡張機能の競合を避けるには何を確認すべきですか。

## まとめ

- 業務ではStable版を基本にする
- User設定は個人全体、Workspace設定はプロジェクト単位
- 設定・拡張機能は再現できる形で管理する
- チーム共有設定へ秘密情報やローカル固有パスを書かない
