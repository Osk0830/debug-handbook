# Lab01 CLI Basics

## 目的

CLIで現在地確認・移動・一覧表示ができるようになる。

## 手順

```bash
pwd
ls -lah
cd ..
pwd
cd -
pwd
```

## チェックポイント

- `pwd` の結果が変わる
- `cd -` で戻れる
- `ls -lah` で隠しファイルも見える

## 発展

Dockerコンテナ内でも同じ操作をしてください。

```bash
docker compose exec web-php8 bash
pwd
ls -lah
exit
```
