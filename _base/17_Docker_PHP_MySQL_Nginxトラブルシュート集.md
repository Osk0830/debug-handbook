
# 第17章 Docker・PHP・MySQL・Nginx トラブルシュート集

> **目的**: 実務で頻繁に遭遇する環境トラブルを、原因ごとに切り分けて解決できるようになる。

---

# この章で身につくこと

- 障害の切り分け手順
- Docker環境の確認
- PHP・MySQL・Nginxの典型的な障害
- よくあるエラーメッセージの意味
- 調査テンプレート

---

# トラブルシュートの原則

1. 現象を整理する
2. 再現する
3. ログを見る
4. 設定を見る
5. コードを見る
6. 修正後に再確認する

---

# まず確認するコマンド

```bash
docker compose ps
docker compose logs -f
docker compose exec web-php8 bash
docker stats
git status
```

---

# ケース1 コンテナが起動しない

確認

```bash
docker compose ps
docker compose logs
```

原因例

- ポート競合
- イメージビルド失敗
- volume設定
- .env誤り

---

# ケース2 Port already in use

確認

```bash
lsof -i :8081
```

対処

- プロセス停止
- ポート変更

---

# ケース3 MySQLにつながらない

確認

```bash
docker compose ps
docker compose logs db
```

接続確認

```bash
docker compose exec db mysql -uroot -p
```

---

# ケース4 Permission denied

確認

```bash
ls -lah
chmod
chown
```

Docker内

```bash
id
whoami
```

---

# ケース5 Xdebugが動かない

```bash
php -m | rg xdebug
php -i | rg xdebug
tail -100 /tmp/xdebug.log
```

確認

- port
- host
- pathMappings

---

# ケース6 502 Bad Gateway

確認順

1. PHP-FPM
2. Nginxログ
3. Docker
4. FastCGI設定

---

# ケース7 404

確認

- URL
- Rewrite
- location
- ルーティング
- ファイル存在

---

# ケース8 500

確認

```bash
docker compose logs -f web-php8
tail -100 error.log
```

---

# ケース9 composer install失敗

確認

```bash
composer validate
composer diagnose
composer install -vvv
```

---

# ケース10 .envが反映されない

確認

```bash
env
printenv
docker compose config
```

---

# ログ調査テンプレート

```bash
docker compose logs --tail=200 web-php8
docker compose logs --tail=200 db
docker compose logs --tail=200 mailhog
```

---

# 障害切り分けフローチャート

```text
現象
 ↓
HTTP
 ↓
Docker
 ↓
ログ
 ↓
設定
 ↓
SQL
 ↓
Xdebug
 ↓
Git
 ↓
修正
```

---

# ハンズオン

1. コンテナ停止・起動
2. logs確認
3. db接続
4. php -m確認
5. env確認
6. docker stats確認
7. 404を調査
8. 500を調査
9. composer validate
10. git status確認

---

# 練習問題

1. 500で最初に見るものは？
2. Port already in useの原因は？
3. 502の原因を3つ挙げる
4. composer diagnoseは何に使う？
5. .envが反映されない時の確認項目は？
6. Docker logsとerror.logの違いは？

---

# チェックリスト

- [ ] docker compose logsを使える
- [ ] dbへ接続できる
- [ ] php設定を確認できる
- [ ] Xdebugを確認できる
- [ ] composer診断できる
- [ ] 障害を順番に切り分けられる

---

# コラム

障害対応で一番重要なのは「焦って設定を変えない」ことです。

**ログ → 設定 → コード**の順番を崩さないだけで、多くの障害は短時間で解決できます。

---

# 次章予告

第18章では実務ケーススタディ集として、実際の障害を題材に「調査 → 原因特定 → 修正」までを一連の流れで学びます。
