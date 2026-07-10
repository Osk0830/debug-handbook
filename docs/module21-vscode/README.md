# Module21 VS Code実践デバッグ

## このModuleの目的

VS Codeを単なるテキストエディタではなく、**検索・調査・実行・デバッグ・差分確認を一か所で回すための実務環境**として使いこなします。

```text
現象を確認する
  ↓
検索とProblemsで候補を絞る
  ↓
シンボル・設定・履歴を読む
  ↓
TerminalとDebuggerで検証する
  ↓
最小修正を行う
  ↓
テストとGit差分で確認する
```

## 学習範囲

- Lesson01〜07: 基本操作、Explorer、全体検索、正規表現検索
- Lesson08〜18: Problems、コード移動、Terminal、Debugger、設定、自動化、拡張管理
- Lesson19〜23: Git履歴、診断表示、AI支援と利用ルール
- Lesson24〜26: PHP、React、WordPressのケーススタディ
- Lesson27〜30: 性能改善、チーム運用、総合演習、チートシート

## 前提環境

- macOS、Windows、またはLinux
- VS Code Stable
- Git
- 任意のサンプルプロジェクト
- CLIの基本操作

コマンド例はmacOS/Linuxを基本とします。ショートカットはmacOSとWindows/Linuxを併記します。

## Lesson一覧

- [Lesson01 VS Codeとは](lessons/lesson01-what-is-vscode.md)
- [Lesson02 インストールと初期設定](lessons/lesson02-install-and-initial-settings.md)
- [Lesson03 画面構成](lessons/lesson03-ui-overview.md)
- [Lesson04 Command Palette](lessons/lesson04-command-palette.md)
- [Lesson05 Explorer](lessons/lesson05-explorer.md)
- [Lesson06 Search完全攻略 Part1](lessons/lesson06-search-complete-guide-part1.md)
- [Lesson06 Search完全攻略 Part2](lessons/lesson06-search-complete-guide-part2.md)
- [Lesson07 正規表現検索](lessons/lesson07-regex-search.md)
- [Lesson08 Problemsパネルでエラーを集約する](lessons/lesson08-problems.md)
- [Lesson09 Outlineとシンボル検索でコードを俯瞰する](lessons/lesson09-outline-symbols.md)
- [Lesson10 統合Terminalで検証を回す](lessons/lesson10-terminal.md)
- [Lesson11 Debugger基礎](lessons/lesson11-debugger.md)
- [Lesson12 launch.jsonを理解する](lessons/lesson12-launch-json.md)
- [Lesson13 tasks.jsonで定型作業を自動化する](lessons/lesson13-tasks-json.md)
- [Lesson14 settings.jsonを安全に管理する](lessons/lesson14-settings-json.md)
- [Lesson15 Workspaceを理解する](lessons/lesson15-workspace.md)
- [Lesson16 Profilesで環境を分離する](lessons/lesson16-profile.md)
- [Lesson17 Snippetsで安全に定型入力する](lessons/lesson17-snippets.md)
- [Lesson18 Extensionsを選定・管理する](lessons/lesson18-extensions.md)
- [Lesson19 GitLensで変更理由を追う](lessons/lesson19-gitlens.md)
- [Lesson20 Error Lensで診断を見逃さない](lessons/lesson20-error-lens.md)
- [Lesson21 GitHub Copilotをデバッグへ使う](lessons/lesson21-copilot.md)
- [Lesson22 Continueなど外部AI拡張を評価する](lessons/lesson22-continue.md)
- [Lesson23 AI利用ガイドラインを作る](lessons/lesson23-ai-guidelines.md)
- [Lesson24 ケーススタディ: PHPの500エラーを追う](lessons/lesson24-case-study-php.md)
- [Lesson25 ケーススタディ: Reactの表示不具合を追う](lessons/lesson25-case-study-react.md)
- [Lesson26 ケーススタディ: WordPressの表示崩れを追う](lessons/lesson26-case-study-wordpress.md)
- [Lesson27 VS Codeのパフォーマンスを改善する](lessons/lesson27-performance.md)
- [Lesson28 チームでVS Code設定を運用する](lessons/lesson28-team-development.md)
- [Lesson29 総合演習](lessons/lesson29-exercises.md)
- [Lesson30 VS Codeデバッグ・チートシート](lessons/lesson30-cheatsheet.md)

## 補助教材

- [Lab01 SearchとTerminal](labs/lab01-search-and-terminal.md)
- [Beginner Exercises](exercises/beginner.md)
- [Answers](exercises/answers.md)
- [Cheatsheet](cheatsheet.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)

## 到達基準

Module21終了時点で、次のことを自力で行えることを目標にします。

- 検索、Problems、Outline、Terminal、Debuggerを適切な順番で使える
- `launch.json`、`tasks.json`、`settings.json` の役割を説明できる
- 拡張機能とWorkspace設定の問題を切り分けられる
- Git履歴から変更背景を調べられる
- AI支援を情報管理と検証ルールの下で利用できる
- PHP、React、WordPressの障害をレイヤーごとに調査できる
- 調査結果を事実・仮説・検証結果に分けて報告できる
