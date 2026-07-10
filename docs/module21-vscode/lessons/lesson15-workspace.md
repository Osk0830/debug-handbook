# Lesson15 Workspaceを理解する

## このLessonのゴール

- フォルダーとWorkspaceの違いを説明できる
- Multi-root Workspaceを構成できる
- Workspace Trustを安全に判断できる

## はじめに

VS Codeでは単一フォルダーを開くだけでも作業できますが、複数リポジトリやフロントエンド・バックエンドをまとめて扱う場合はWorkspaceが役立ちます。一方で、設定やTaskの適用範囲が広がるため、信頼境界を意識します。

## フォルダーと.code-workspace

`.code-workspace` ファイルには、含めるフォルダーとWorkspace全体の設定を保存できます。リポジトリ自体へ置く場合と、親ディレクトリへ個人用として置く場合を使い分けます。

## Multi-root Workspace

複数のフォルダーを1つのウィンドウで扱えます。検索ではフォルダー単位のInclude/Excludeが可能です。同名ファイルが多い場合は、検索結果のルート名を必ず確認します。

## 例

```json
{
  "folders": [
    { "name": "frontend", "path": "../frontend" },
    { "name": "api", "path": "../api" }
  ],
  "settings": {
    "search.exclude": {
      "**/node_modules": true,
      "**/vendor": true
    }
  }
}
```

## Workspace Trust

未確認のリポジトリを開くときはRestricted Modeを利用します。Task、Debugger、拡張機能、設定はコマンド実行につながるため、信頼する前に `.vscode`、package scripts、設定ファイルを確認します。

## チーム共有

複数リポジトリを常に同じ組み合わせで扱う場合は共有候補です。ただし各メンバーのディレクトリ構成が異なると壊れます。相対パス、命名、セットアップ手順を揃えます。

## ハンズオン

1. 2つのサンプルフォルダーをMulti-root Workspaceへ追加します。
2. Workspaceへ名前を付けて保存します。
3. 全体検索し、どのルートの結果か確認します。
4. `.code-workspace` の相対パスと設定を読みます。
5. 信頼前に確認すべきファイルをチェックリスト化します。

## 確認問題

1. Multi-root Workspaceが適するプロジェクト例は何ですか。
2. Workspace Trustは何を防ぐための機能ですか。
3. Workspaceファイル共有時に絶対パスが問題になる理由は何ですか。

## まとめ

このLessonでは、**15 Workspaceを理解する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson16 Profiles](lesson16-profile.md) へ進みます。
