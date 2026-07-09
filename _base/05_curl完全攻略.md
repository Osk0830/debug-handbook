
# 第5章 curl完全攻略

> **目的**: ブラウザを使わずにHTTP通信を再現し、APIやフォームの不具合をCLIだけで切り分けられるようになる。

---

# この章で身につくこと

- curlの役割
- GET / POST / PUT / DELETE の実行
- ヘッダー・Cookie・JSON送信
- リダイレクト・レスポンス解析
- APIデバッグ
- Docker環境での疎通確認

---

# curlとは

curlはHTTP/HTTPSをはじめとする通信をCLIから実行できるツールです。

実務では

- API疎通確認
- フォーム送信再現
- リダイレクト調査
- レスポンス確認
- CI/CDやシェルスクリプト

で頻繁に利用します。

---

# 最初の一歩

```bash
curl http://localhost:8081/wedding/
```

HTMLが返ってくれば通信成功です。

---

# レスポンスヘッダーだけ取得

```bash
curl -I http://localhost:8081/wedding/
```

確認ポイント

- HTTP Status
- Server
- Content-Type
- Location
- Set-Cookie

---

# 詳細ログを見る

```bash
curl -v http://localhost:8081/wedding/
```

`>` は送信内容、`<` は受信内容を表します。

---

# リダイレクトを追う

```bash
curl -L http://localhost:8081/wedding/
```

302や301の遷移先まで取得します。

---

# POST

```bash
curl \
-X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
--data "name=Song&email=test@example.com" \
http://localhost:8081/wedding/inquiry/confirm.php
```

---

# JSON送信

```bash
curl \
-H "Content-Type: application/json" \
-d '{"name":"Song"}' \
https://example.com/api
```

---

# PUT・DELETE

```bash
curl -X PUT https://example.com/api/1
curl -X DELETE https://example.com/api/1
```

---

# ヘッダー追加

```bash
curl \
-H "Authorization: Bearer TOKEN" \
-H "Accept: application/json"
```

---

# Cookie

保存

```bash
curl -c cookie.txt URL
```

利用

```bash
curl -b cookie.txt URL
```

---

# ファイルアップロード

```bash
curl \
-F "image=@sample.jpg" \
https://example.com/upload
```

---

# 保存

```bash
curl -o result.html URL
```

ファイル名そのまま

```bash
curl -O URL
```

---

# HTTPコードだけ取得

```bash
curl \
-s \
-o /dev/null \
-w "%{http_code}\n" \
URL
```

---

# レスポンス時間

```bash
curl \
-s \
-o /dev/null \
-w "%{time_total}\n" \
URL
```

---

# 実務シナリオ

## 問い合わせフォーム

1. GET確認
2. POST送信
3. Status確認
4. Location確認
5. Cookie確認
6. MailHog確認

---

## OAuth

- code
- state
- redirect_uri

が正しいか確認する。

---

## API

確認する項目

- URL
- Method
- Header
- Body
- Status
- Response

---

# Docker

コンテナ内から実行

```bash
docker compose exec web-php8 bash

curl http://localhost/
```

---

# よく使うオプション

|オプション|意味|
|---|---|
|-I|ヘッダーのみ|
|-i|ヘッダー付き|
|-v|詳細表示|
|-L|リダイレクト追従|
|-H|ヘッダー追加|
|-d|Body送信|
|-F|multipart|
|-o|保存|
|-O|元ファイル名保存|
|-w|情報表示|
|-c|Cookie保存|
|-b|Cookie送信|

---

# ハンズオン

1. localhostへGET
2. Header確認
3. HTML保存
4. POST送信
5. JSON送信
6. Cookie保存
7. Cookie利用
8. HTTPコード取得
9. レスポンス時間取得
10. Docker内で実行

---

# タイムアタック

30秒以内で

- Header確認
- 302確認
- Cookie取得
- JSON送信
- POST再現

---

# 練習問題

1. -Iと-iの違い
2. -Lは何をする？
3. Cookieを保持する方法は？
4. Bearer認証はどう送る？
5. HTTPコードだけ取得するには？
6. HTMLを保存するには？

---

# チェックリスト

- [ ] GETできる
- [ ] POSTできる
- [ ] JSON送信できる
- [ ] Headerを追加できる
- [ ] Cookieを扱える
- [ ] 302を追える
- [ ] HTTPコードを取得できる
- [ ] Docker内から疎通確認できる

---

# コラム

ブラウザでしか再現できないと思っている現象の多くは、curlでも再現できます。

まずcurlで再現できるか試す癖を付けると、デバッグ速度が大きく向上します。

---

# 次章予告

第6章では Docker / Docker Compose を深掘りし、コンテナ・ネットワーク・ログ・ボリューム・exec・inspect を使った実践的なデバッグ方法を学びます。
