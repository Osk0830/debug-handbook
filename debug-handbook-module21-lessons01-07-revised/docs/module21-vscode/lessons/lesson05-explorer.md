# Lesson05 Explorer

## ゴール

- Explorerからプロジェクトの種類と主要構成を推測できる
- ファイルを順番に読む前に、入口・設定・依存関係を見つけられる
- 誤操作を避けながらファイルを作成・移動・比較できる

## Explorerの役割

Explorerはファイルを開くためだけの画面ではありません。プロジェクトの構造を俯瞰し、調査の起点を決めるために使います。

最初に見る代表ファイル:

| ファイル | 判断できること |
|---|---|
| `README.md` | 起動方法、構成、制約 |
| `package.json` | Node依存、scripts |
| `composer.json` | PHP依存、autoload |
| `compose.yml` | コンテナ、ポート、Volume |
| `.env.example` | 必要な環境変数 |
| `.gitignore` | 生成物、秘密情報、管理対象外 |
| `phpunit.xml` / `vitest.config.*` | テスト構成 |
| `tsconfig.json` | TypeScript設定、path alias |

## 構成からフレームワークを推測する

### WordPress

```text
wp-content/
├── themes/
├── plugins/
└── uploads/
```

### Laravel

```text
app/
routes/
resources/
config/
storage/
artisan
```

### React / Vite

```text
src/
public/
package.json
vite.config.*
```

構成を把握すると、どこを検索対象に含め、どこを除外すべきか判断しやすくなります。

## 開く順番

未知の案件では、次の順序が有効です。

1. `README.md`
2. 依存管理ファイル
3. 起動設定
4. エントリーポイント
5. ルーティング
6. 対象機能の実装

いきなり`src`配下を上から読むと、全体像を失いやすくなります。

## Explorerの基本操作

- 新規ファイル・フォルダ作成
- 名前変更
- 削除
- ドラッグによる移動
- 右クリックからTerminalを開く
- ファイルの相対パスをコピー
- Finder / Explorerで表示

### パスをコピーする

右クリックから次を使い分けます。

- Copy Path: 絶対パス
- Copy Relative Path: ワークスペースからの相対パス

Issue、レビュー、チャットでは相対パスの方が共有しやすい場合が多いです。

```text
src/components/Header.tsx
```

## Compact Folders

子フォルダが1つだけ続く場合、Explorerは複数階層を1行にまとめることがあります。

```text
src/components/common
```

階層を個別に見たい場合:

```json
{
  "explorer.compactFolders": false
}
```

## Auto Reveal

開いているファイルをExplorer上でも自動選択する設定です。

```json
{
  "explorer.autoReveal": true
}
```

巨大リポジトリではツリーが頻繁に移動して見づらい場合があります。その場合は無効化も検討します。

## ファイルを比較する

Explorerで1つ目のファイルを右クリックし、比較対象として選択します。次に2つ目を右クリックして比較すると、差分エディタを開けます。

用途:

- 環境別設定の比較
- 旧テンプレートと新テンプレートの比較
- 類似コンポーネントの差分確認

## 誤操作を防ぐ

ファイル移動・名前変更はimport、autoload、URL、ビルド設定へ影響します。

実行前に確認すること:

```bash
git status
git diff --stat
```

実行後:

```bash
git status
git diff --find-renames
```

VS Code上の表示だけでなく、Gitが変更をどう認識しているか確認します。

## Timeline

ファイルを選択した際、TimelineにGit履歴や保存履歴が表示されることがあります。直近の変更経緯を追う入口として便利ですが、詳細な履歴調査はGitLensや`git log`も併用します。

## ハンズオン

任意のプロジェクトを開き、次を記録してください。

1. プロジェクトの種類
2. 依存管理ファイル
3. 起動コマンドが定義されたファイル
4. エントリーポイント
5. ルーティングまたはURL定義
6. 生成物・依存物として検索から除外すべきフォルダ

次に、2つの設定ファイルをExplorerから比較してください。

## 確認問題

1. 未知の案件で最初に`README.md`を見る理由は何ですか。
2. `Copy Path`と`Copy Relative Path`の違いは何ですか。
3. ファイル移動後にGit差分を確認する理由は何ですか。

## まとめ

- Explorerは構造把握と調査計画のために使う
- README、依存管理、起動設定、入口の順で確認する
- ファイル移動や名前変更はGit差分とセットで確認する
- パス共有には相対パスが便利
