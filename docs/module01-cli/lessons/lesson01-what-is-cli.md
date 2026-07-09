# Lesson01 CLIとは

## ゴール

CLIを使う理由を説明できるようになる。

## このLessonで身につくこと

- CLIとGUIの違い
- なぜCLIが実務で重要なのか
- デバッグでCLIが役立つ場面

## 実務ではいつ使う？

- Dockerコンテナを操作するとき
- Gitで差分や履歴を見るとき
- ログを見るとき
- SQLに接続するとき
- 本番サーバーで障害調査するとき

## 基本

CLIは **Command Line Interface** の略です。

GUIではクリックで操作します。CLIではコマンドで操作します。

```text
GUI: Finderでフォルダを開く
CLI: cd project
```

CLIの強みは、操作をそのまま記録・共有・再実行できることです。

```bash
docker compose logs -f web-php8
```

この1行を共有すれば、他の人も同じ調査ができます。

## よくある失敗

GUIで開いているフォルダと、ターミナルの現在地が違うことがあります。

作業前に必ず確認します。

```bash
pwd
```

## ハンズオン

```bash
pwd
ls -lah
echo $SHELL
```

## 演習

1. CLIとGUIの違いを自分の言葉で説明してください。
2. CLIがデバッグに向いている理由を3つ挙げてください。

## 模範解答

1. GUIはクリックで操作し、CLIはコマンドで操作する。
2. 再現性がある、ログに残せる、自動化しやすい。

## FAQ

### Q. CLIは全部暗記しないとダメですか？

いいえ。最初は `pwd`、`ls`、`cd` だけで十分です。

## 関連リンク

- https://linuxcommand.org/
- https://code.visualstudio.com/docs/terminal/basics

## 学習ログ

```markdown
## 学習日

## 試したコマンド

## 分からなかったこと

## 実務で使えそうな場面
```

## 次へ進む条件

- [ ] CLIとGUIの違いを説明できる
- [ ] `pwd` を実行できる
