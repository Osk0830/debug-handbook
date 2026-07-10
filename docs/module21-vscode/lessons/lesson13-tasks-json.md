# Lesson13 tasks.jsonで定型作業を自動化する

## このLessonのゴール

- TaskとTerminalコマンドの違いを説明できる
- ビルド・lint・テストをTask化できる
- problemMatcherでエラーをProblemsへ連携できる

## はじめに

`.vscode/tasks.json` は、繰り返し実行するコマンドを名前付きの手順として共有する仕組みです。単なるショートカットではなく、依存関係、バックグラウンド実行、エラー解析を定義できます。

## Taskの基本

Taskは `label`、`type`、`command` を中心に定義します。npm scriptsがある場合は重複したロジックをtasks.jsonへ書かず、`npm run lint` のように既存の入口を呼び出します。

## 例: lint Task

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "lint",
      "type": "shell",
      "command": "npm run lint",
      "group": "test",
      "problemMatcher": "$eslint-stylish"
    }
  ]
}
```

## problemMatcher

コマンド出力からファイル、行、列、重大度、メッセージを抽出し、Problemsへ表示します。既製matcherが合わない場合は正規表現で定義します。まず実際の出力形式を固定してからmatcherを作ります。

## 依存関係

`dependsOn` で複数Taskを順番または並列に実行できます。例として、型チェック、lint、テストをまとめた `verify` Taskを作れます。失敗時に後続を実行すべきかも考慮します。

## preLaunchTask

launch.jsonの `preLaunchTask` からビルドやコンテナ起動確認を呼べます。ただし毎回重い処理を実行するとデバッグ開始が遅くなるため、必要な最小単位にします。

## 共有時の注意

OS固有コマンド、絶対パス、ローカルだけのツールへ依存するとチームで動きません。READMEに前提コマンドを記載し、CIと同じ入口を再利用します。

## ハンズオン

1. プロジェクトのlintコマンドをTask化します。
2. `Terminal: Run Task` から実行します。
3. Problemsへ結果が出るようproblemMatcherを設定します。
4. lintとテストをまとめた `verify` Taskを作ります。
5. 別のTerminalから同じコマンドを実行し、結果が一致するか確認します。

## 確認問題

1. Task化に適したコマンドの特徴は何ですか。
2. problemMatcherの役割は何ですか。
3. npm scriptsとtasks.jsonへ同じ処理を二重に書かない理由は何ですか。

## まとめ

このLessonでは、**13 tasks.jsonで定型作業を自動化する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson14 settings.json](lesson14-settings-json.md) へ進みます。
