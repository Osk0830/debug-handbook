# Module01 CLI入門

## Moduleのゴール

CLIを使って、実務調査の入口に立てるようになること。

このModuleを終えると、以下ができるようになります。

- ターミナルを開ける
- 現在地を確認できる
- ディレクトリを移動できる
- ファイル一覧を確認できる
- 標準出力・標準エラーの違いを説明できる
- パイプとリダイレクトを使える
- Dockerコンテナ内でも基本操作ができる

## Lesson一覧

1. [CLIとは](lessons/lesson01-what-is-cli.md)
2. [TerminalとShell](lessons/lesson02-terminal-shell.md)
3. [pwd](lessons/lesson03-pwd.md)
4. [ls](lessons/lesson04-ls.md)
5. [cd](lessons/lesson05-cd.md)
6. [相対パスと絶対パス](lessons/lesson06-path.md)
7. [環境変数とPATH](lessons/lesson07-env-path.md)
8. [標準入力・標準出力・標準エラー](lessons/lesson08-stdin-stdout-stderr.md)
9. [リダイレクト](lessons/lesson09-redirection.md)
10. [パイプ](lessons/lesson10-pipe.md)
11. [履歴と補完](lessons/lesson11-history-completion.md)
12. [コマンドの調べ方](lessons/lesson12-help-man-which-type.md)
13. [Docker内CLI](lessons/lesson13-cli-in-docker.md)
14. [総復習](lessons/lesson14-review.md)

## これだけは試す

```bash
pwd
ls -lah
cd ..
cd -
history
echo $SHELL
echo $PATH
```

Docker環境がある場合:

```bash
docker compose ps
docker compose exec web-php8 bash
pwd
ls -lah
php -v
exit
```
