# PROJECT

## プロジェクト名

Debug Handbook

## 目的

Debug Handbook は、実務で使えるデバッグ力を身につけるためのハンズオン教材です。

単なるコマンド集ではなく、以下を重視します。

- 現象を整理する
- 証拠を集める
- 仮説を立てる
- 検証する
- 最小限で修正する
- 再確認する
- 学びを教材へ戻す

## 想定読者

- PHP / WordPress / React / Docker を実務で扱うエンジニア
- CLIやデバッグに苦手意識がある人
- 「なんとなく直す」から卒業したい人
- 実案件で原因切り分けを速くしたい人

## 対象技術

- CLI
- Linux
- ripgrep / grep / find
- HTTP
- curl
- Docker / Docker Compose
- PHP / Composer
- MySQL / SQL
- Git
- VS Code / Xdebug
- WordPress
- React / API
- Nginx / Apache
- Mail / SMTP / MailHog
- Performance
- Troubleshooting

## 基本方針

### 1. 推測で直さない

悪い例:

```text
たぶんここが原因だと思う
↓
修正
↓
直らない
↓
別の場所を修正
```

良い例:

```text
現象
↓
証拠
↓
仮説
↓
検証
↓
修正
↓
再確認
```

### 2. 手を動かす

この教材は読むだけでは完了しません。

各Moduleで最低1つはコマンドや確認作業を実行します。

### 3. 学習しながら育てる

最初から完璧を目指しません。

学習中に分からなかったこと、実案件でハマったことを教材へ追加していきます。

## 学習サイクル

```text
Learn
  ↓
Try
  ↓
Break
  ↓
Debug
  ↓
Review
  ↓
Apply
```

## 教材の更新方針

- 疑問点は該当Lessonへ追記する
- よく使うコマンドはcheatsheetへ追記する
- よくある失敗はfaq/troubleshootingへ追記する
- 実案件で遭遇した障害はcase studyへ追記する
- 判断フローはdebug flow/referenceへ追記する

## この教材で最も重要な言葉

**推測ではなく、証拠で判断する。**
