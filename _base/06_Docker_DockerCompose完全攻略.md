
# 第6章 Docker / Docker Compose 完全攻略

> **目的**: Docker環境を理解し、コンテナ内部・ネットワーク・ログ・設定を根拠にデバッグできるようになる。

---

# この章で身につくこと

- Dockerの基本概念
- Image / Container / Volume / Network の違い
- docker と docker compose の違い
- コンテナへの接続
- ログ確認
- inspect による調査
- PHP・MySQL・MailHog の確認
- よくあるトラブルの切り分け

---

# Dockerとは

Dockerはアプリケーションを「コンテナ」という独立した環境で実行する仕組みです。

```
Host OS
 ├── Docker Engine
 │    ├── web-php8
 │    ├── db
 │    └── mailhog
```

---

# 用語

|用語|説明|
|---|---|
|Image|設計図|
|Container|実行中の環境|
|Volume|データ保存領域|
|Network|コンテナ同士の通信|

---

# docker と docker compose

- docker : 単一コンテナ操作
- docker compose : 複数コンテナをまとめて管理

普段の開発では compose を使うことが多いです。

---

# 起動・停止

```bash
docker compose up -d
docker compose down
docker compose stop
docker compose start
docker compose restart
```

---

# 状態確認

```bash
docker compose ps
docker ps
docker images
```

---

# ログ

```bash
docker compose logs
docker compose logs -f
docker compose logs --tail=200 web-php8
```

調査では `-f` と `--tail` をよく使います。

---

# コンテナへ入る

```bash
docker compose exec web-php8 bash
```

中で確認

```bash
pwd
php -v
php -m
php --ini
```

---

# inspect

```bash
docker inspect web-php8
```

確認できる情報

- IPアドレス
- マウント
- 環境変数
- ポート
- ネットワーク

---

# 環境変数

```bash
docker compose exec web-php8 env
```

---

# ファイルコピー

```bash
docker cp web-php8:/var/www/html/index.php .
docker cp index.php web-php8:/var/www/html/
```

---

# コンテナ情報

```bash
docker stats
docker top web-php8
```

---

# ネットワーク

一覧

```bash
docker network ls
```

詳細

```bash
docker network inspect <network>
```

---

# ボリューム

```bash
docker volume ls
docker volume inspect <volume>
```

---

# PHP確認

```bash
php -v
php -m
php --ini
```

Xdebug

```bash
php -m | rg xdebug
php -i | rg xdebug
```

---

# MySQL確認

```bash
docker compose exec db bash
mysql -u root -p
```

---

# MailHog

ブラウザ

```
http://localhost:8025
```

確認ポイント

- メールが届いているか
- 件名
- Body
- 添付

---

# 実務シナリオ

## PHPだけ500

1. compose ps
2. logs
3. exec
4. php -m
5. php --ini

---

## DB接続できない

1. compose ps
2. db起動確認
3. env確認
4. mysql接続
5. network確認

---

## Xdebug動かない

```bash
php -m | rg xdebug
php -i | rg xdebug
tail -100 /tmp/xdebug.log
```

---

# ハンズオン

1. 全コンテナ起動
2. 状態確認
3. web-php8へ入る
4. PHPバージョン確認
5. モジュール一覧
6. Xdebug確認
7. dbへ入る
8. MailHog確認
9. ログ監視
10. restartして再確認

---

# タイムアタック

30秒以内で

- PHPバージョン確認
- Xdebug確認
- コンテナログ確認
- DBへ入る
- MailHog確認

---

# 練習問題

1. ImageとContainerの違いは？
2. dockerとcomposeの違いは？
3. execは何をする？
4. inspectはいつ使う？
5. Volumeの役割は？
6. logs -fはいつ使う？
7. php -mで何が分かる？

---

# チェックリスト

- [ ] composeで起動できる
- [ ] logsが見られる
- [ ] execで入れる
- [ ] inspectを使える
- [ ] envを確認できる
- [ ] php -v を確認できる
- [ ] Xdebugを確認できる
- [ ] MailHogを確認できる

---

# コラム

**Dockerのトラブルは「アプリ」ではなく「環境」が原因のことが少なくありません。**

まずは

- コンテナは起動しているか
- ログに異常はないか
- PHP設定は正しいか
- ネットワークはつながっているか

を事実ベースで確認する習慣を付けましょう。

---

# 次章予告

第7章では PHP・Composer を学び、オートロード・依存関係・Composerコマンド・PHP設定・実務デバッグを深掘りします。
