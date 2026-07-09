# Lesson13 Docker内でCLIを使う

## ゴール

Dockerコンテナ内で基本的なCLI操作ができるようになる。

## 基本

```bash
docker compose ps
docker compose exec web-php8 bash
```

コンテナ内:

```bash
pwd
ls -lah
php -v
php -m
exit
```

## 実務ではいつ使う？

- PHPバージョン確認
- 拡張モジュール確認
- アプリ内ファイル確認
- Xdebug確認

## よくある失敗

ホスト側で実行しているのか、コンテナ内で実行しているのか分からなくなる。

`pwd` と `php -v` で確認します。

## ハンズオン

```bash
docker compose ps
docker compose exec web-php8 bash
pwd
ls -lah
php -v
exit
```

## 演習

1. コンテナ内に入るコマンドを書いてください。
2. コンテナ内でPHPバージョンを見るコマンドは？

## 模範解答

1. `docker compose exec web-php8 bash`
2. `php -v`

## 次へ進む条件

- [ ] Dockerコンテナ内で `pwd` を実行できる
