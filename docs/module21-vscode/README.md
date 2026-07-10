# Module21 VS Code実践デバッグ

> VS Codeを「コードを書くエディタ」ではなく、実務デバッグの司令塔として使いこなすためのモジュールです。

## Moduleのゴール

このModuleを終えると、次のことができるようになります。

- VS Code検索と `rg` を使い分けられる
- Explorer / Search / Problems / Terminal / Debugger の役割を説明できる
- `settings.json` / `launch.json` / `tasks.json` / `extensions.json` を使い分けられる
- GitLens / Error Lens / Copilot / Continue を実務デバッグに活用できる
- PHP / React / WordPress案件で、VS Codeを中心に調査フローを組み立てられる

## このModuleの位置づけ

Module01〜20で学んだCLI・Linux・HTTP・Docker・SQL・Git・Xdebugの知識を、VS Code上で統合します。

```text
Browser
  ↓
VS Code Search
  ↓
Terminal / rg / curl / Docker logs
  ↓
Debugger
  ↓
Git diff
  ↓
修正
  ↓
再確認
```

## Lesson一覧

1. [VS Codeとは](lessons/lesson01-what-is-vscode.md)
2. [インストールと初期設定](lessons/lesson02-install-and-initial-settings.md)
3. [画面構成](lessons/lesson03-ui-overview.md)
4. [Command Palette](lessons/lesson04-command-palette.md)
5. [Explorer](lessons/lesson05-explorer.md)
6. [検索完全攻略](lessons/lesson06-search.md)
7. [正規表現検索](lessons/lesson07-regex-search.md)
8. [Problems](lessons/lesson08-problems.md)
9. [Outlineとシンボル検索](lessons/lesson09-outline-symbols.md)
10. [統合ターミナル](lessons/lesson10-terminal.md)
11. [Debugger](lessons/lesson11-debugger.md)
12. [launch.json](lessons/lesson12-launch-json.md)
13. [tasks.json](lessons/lesson13-tasks-json.md)
14. [settings.json](lessons/lesson14-settings-json.md)
15. [Workspace](lessons/lesson15-workspace.md)
16. [Profile](lessons/lesson16-profile.md)
17. [Snippets](lessons/lesson17-snippets.md)
18. [拡張機能](lessons/lesson18-extensions.md)
19. [GitLens](lessons/lesson19-gitlens.md)
20. [Error Lens](lessons/lesson20-error-lens.md)
21. [GitHub Copilot](lessons/lesson21-copilot.md)
22. [Continue](lessons/lesson22-continue.md)
23. [AIとの付き合い方](lessons/lesson23-ai-guidelines.md)
24. [PHPケーススタディ](lessons/lesson24-case-study-php.md)
25. [Reactケーススタディ](lessons/lesson25-case-study-react.md)
26. [WordPressケーススタディ](lessons/lesson26-case-study-wordpress.md)
27. [パフォーマンス改善](lessons/lesson27-performance.md)
28. [チーム開発](lessons/lesson28-team-development.md)
29. [総合演習](lessons/lesson29-exercises.md)
30. [チートシート](lessons/lesson30-cheatsheet.md)

## 学習方法

各Lessonでは、以下を行います。

1. 概念を理解する
2. VS Code上で実際に操作する
3. CLIと比較する
4. 実案件を想定して調査する
5. 学習ログを残す

## このModuleで一番重要なこと

VS Codeを使いこなすとは、ショートカットを大量に覚えることではありません。

**コード・ログ・CLI・Git・Debuggerを1つの画面でつなぎ、証拠をもとに原因へ近づくこと**です。
