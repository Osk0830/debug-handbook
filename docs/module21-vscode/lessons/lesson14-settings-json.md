# Lesson14 settings.jsonを安全に管理する

## このLessonのゴール

- User設定とWorkspace設定を使い分けられる
- 言語別設定と設定優先順位を理解できる
- チーム共有すべき設定を判断できる

## はじめに

VS Codeの設定は、見た目だけでなく保存、整形、除外、言語解析、Terminalなど開発結果へ影響します。個人の好みとプロジェクトの再現性を分離することが重要です。

## 設定スコープ

User設定は自分の全プロジェクトへ、Workspace設定は現在のプロジェクトへ適用されます。Remote環境やProfileにもスコープがあります。設定画面のスコープ表示を確認してください。

## 設定優先順位

一般に、より具体的なスコープが優先されます。Userで有効なのにプロジェクトで動かない場合は、Workspace設定や言語別設定による上書きを確認します。

## 言語別設定

```json
{
  "editor.formatOnSave": true,
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },
  "[php]": {
    "editor.defaultFormatter": "bmewburn.vscode-intelephense-client"
  }
}
```
フォーマッターIDは実際に導入している拡張へ合わせます。

## 共有向きの設定

フォーマット、改行、除外、ファイル関連付け、テスト探索など、成果物の一貫性に関わる設定は共有候補です。テーマ、フォントサイズ、UI配置は個人設定向きです。

## 設定の調査方法

設定UIで項目名を検索し、歯車から「Copy Setting as JSON」を使うと正確なキーを取得できます。設定変更後はModifiedフィルターで変更箇所を確認します。

## 設定事故を避ける

設定を大量にコピーせず、目的と副作用を1項目ずつ確認します。`files.exclude` と `search.exclude`、`editor.formatOnSave` と `codeActionsOnSave` など、似た設定の役割を混同しないようにします。

## ハンズオン

1. UserとWorkspaceのsettings.jsonを開きます。
2. 個人設定と共有設定を分類します。
3. Markdownだけ折り返す言語別設定を追加します。
4. Settings UIのModifiedフィルターで変更を確認します。
5. Workspace設定をGit差分で確認し、プロジェクトに必要な項目だけ残します。

## 確認問題

1. User設定とWorkspace設定の判断基準は何ですか。
2. 言語別設定が必要な例を挙げてください。
3. 設定変更後にModifiedフィルターを見る理由は何ですか。

## まとめ

このLessonでは、**14 settings.jsonを安全に管理する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson15 Workspace](lesson15-workspace.md) へ進みます。
