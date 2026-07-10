# Troubleshooting

## command not found

```bash
type -a command
which command
echo "$PATH" | tr ':' '\n'
```

インストール有無とPATHを確認します。

## Permission denied

```bash
ls -l path
stat path
id
```

安易に`chmod 777`を使わず、所有者・グループ・必要権限を確認します。

## No such file or directory

```bash
pwd
ls -la
find . -name 'filename'
```

相対パス、カレントディレクトリ、大文字小文字を確認します。

## Address already in use

```bash
lsof -nP -iTCP:PORT -sTCP:LISTEN
ps -p PID -o pid,ppid,user,command
```

既存プロセスを終了するか、使用ポートを変更します。

## Dockerへ接続できない

```bash
docker version
docker info
docker context ls
```

Docker Desktop / Engineの起動状態とcontextを確認します。

## Gitで作業内容を失いそう

```bash
git status
git diff
git stash push -u -m 'temporary backup'
```

変更を保存してから、resetやswitchを実行します。
