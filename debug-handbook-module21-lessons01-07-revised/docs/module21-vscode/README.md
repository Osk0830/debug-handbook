# Module21 VS Code実践デバッグ

## このModuleの目的

VS Codeを単なるテキストエディタではなく、**検索・調査・実行・デバッグ・差分確認を一か所で回すための実務環境**として使いこなします。

デバッグでは、コードを最初から読むよりも、現象から証拠を集め、関係する場所へ素早く到達することが重要です。このModuleでは、次の流れをVS Code上で再現できるようにします。

```text
現象を確認する
  ↓
検索で候補を絞る
  ↓
コードと設定を読む
  ↓
TerminalやDebuggerで検証する
  ↓
Git差分で修正範囲を確認する
```

## Lesson01〜07で学ぶこと

1. VS Codeの役割とCLIとの使い分け
2. インストール、初期設定、設定の同期方法
3. 画面構成とデバッグ時の導線
4. Command Paletteを使った機能呼び出し
5. Explorerによるプロジェクト構造の把握
6. ワークスペース全体検索と絞り込み
7. 正規表現検索による高度な調査

## 前提環境

- macOSまたはWindows
- VS Code Stable
- Git
- 任意のサンプルプロジェクト
- CLIで `pwd`、`ls`、`cd`、`rg` を実行できること

本教材のコマンド例はmacOS/Linuxを基本とします。WindowsではPowerShellまたはWSLへ読み替えてください。

## 学習方法

各Lessonは次の順序で進めます。

1. ゴールを確認する
2. 機能の役割を理解する
3. 実務例を読む
4. ハンズオンを実行する
5. 確認問題に答える

ショートカットを一度に暗記する必要はありません。まずは「どの場面で何を使うか」を判断できることを優先します。

## Lesson一覧

- [Lesson01 VS Codeとは](lessons/lesson01-what-is-vscode.md)
- [Lesson02 インストールと初期設定](lessons/lesson02-install-and-initial-settings.md)
- [Lesson03 画面構成](lessons/lesson03-ui-overview.md)
- [Lesson04 Command Palette](lessons/lesson04-command-palette.md)
- [Lesson05 Explorer](lessons/lesson05-explorer.md)
- [Lesson06 Search完全攻略 Part1](lessons/lesson06-search-complete-guide-part1.md)
- [Lesson06 Search完全攻略 Part2](lessons/lesson06-search-complete-guide-part2.md)
- [Lesson07 正規表現検索](lessons/lesson07-regex-search.md)

## 補助教材

- [Lab01 SearchとTerminal](labs/lab01-search-and-terminal.md)
- [Beginner Exercises](exercises/beginner.md)
- [Answers](exercises/answers.md)
- [Cheatsheet](cheatsheet.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)

## 到達基準

Lesson07終了時点で、次の操作を自力で行えることを目標にします。

- プロジェクトをフォルダ単位で開ける
- VS Codeの主要エリアを説明できる
- Command Paletteから目的の機能を探せる
- Explorerで構成ファイルと入口ファイルを見つけられる
- SearchのInclude / Excludeで結果を絞れる
- 正規表現で関数名、ログ出力、URL、設定値などを検索できる
- VS Code Searchと`rg`を状況に応じて使い分けられる
