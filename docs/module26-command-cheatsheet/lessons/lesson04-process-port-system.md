# Lesson04 プロセス・ポート・システム

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## プロセス確認

```bash
ps aux
ps aux | rg 'php|node|nginx'
pgrep -af php
top
```

**判断ポイント:** PID、CPU、メモリ、実行コマンドを確認する。

## 終了

```bash
kill PID
kill -TERM PID
kill -KILL PID
pkill -f 'pattern'
```

**判断ポイント:** まずTERMで正常終了を試し、KILLは最後に使う。

## ポート確認

```bash
lsof -nP -iTCP -sTCP:LISTEN
lsof -nP -iTCP:3000
netstat -an | grep LISTEN
```

**判断ポイント:** Macでは`lsof`が実用的。ポート競合時はPIDと実行元を確認する。

## ディスク・メモリ

```bash
df -h
du -sh .
du -sh * | sort -h
free -h
vm_stat
```

**判断ポイント:** Linuxでは`free`、macOSでは`vm_stat`を使う。

## 環境情報

```bash
uname -a
sw_vers
cat /etc/os-release
env | sort
which php
type -a node
```

**判断ポイント:** ローカルとCI・コンテナで差がある場合、OS・PATH・バージョンを比較する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
