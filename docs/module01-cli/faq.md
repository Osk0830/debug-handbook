# Module01 FAQ

## Q. CLIは全部暗記する必要がありますか？

ありません。最初は `pwd` / `ls` / `cd` だけで十分です。

## Q. command not found が出ました。

以下を確認します。

```bash
which command_name
echo $PATH
```

原因候補:

- インストールされていない
- PATHが通っていない
- コマンド名が違う

## Q. Docker内かホスト側か分からなくなりました。

以下を確認します。

```bash
pwd
php -v
hostname
```
