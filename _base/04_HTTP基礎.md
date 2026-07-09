
# 第4章 HTTP基礎

> **目的**: ブラウザとサーバーの通信を理解し、HTTPを根拠にデバッグできるようになる。

---

# この章で身につくこと

- HTTPとは何か
- リクエストとレスポンス
- URLの構造
- HTTPメソッド
- ステータスコード
- HTTPヘッダー
- CookieとSession
- ブラウザ開発者ツールの見方

---

# HTTPとは

HTTP(HyperText Transfer Protocol)はブラウザとサーバーが通信するためのルールです。

```
Browser
   │ Request
   ▼
Server
   │
Application
   │
Database
   │
Response
   ▼
Browser
```

デバッグでは、この流れのどこで問題が起きているかを切り分けます。

---

# URLの構造

```
https://example.com:443/news?id=100#top
```

|要素|例|
|---|---|
|スキーム|https|
|ホスト|example.com|
|ポート|443|
|パス|/news|
|クエリ|id=100|
|フラグメント|#top|

---

# HTTPメソッド

|メソッド|用途|
|---|---|
|GET|取得|
|POST|登録・送信|
|PUT|更新|
|PATCH|部分更新|
|DELETE|削除|

実務では GET と POST を最も多く扱います。

---

# GETとPOST

## GET

- URLにパラメータ
- ブックマーク可能
- 検索・一覧取得向き

例

```
/news?id=10
```

## POST

- Bodyにデータ
- フォーム送信
- ログイン
- 問い合わせ

---

# リクエスト

リクエストには次の情報が含まれます。

- URL
- Method
- Header
- Body

---

# レスポンス

レスポンスには次の情報が含まれます。

- Status Code
- Header
- Body

---

# よく見るステータスコード

|コード|意味|
|---:|---|
|200|成功|
|201|作成成功|
|204|本文なし|
|301|恒久的リダイレクト|
|302|一時リダイレクト|
|304|キャッシュ利用|
|400|リクエスト不正|
|401|認証必要|
|403|権限なし|
|404|見つからない|
|405|メソッド不正|
|419|CSRF失敗(環境依存)|
|429|アクセス過多|
|500|サーバーエラー|
|502|Bad Gateway|
|503|サービス停止|

---

# HTTPヘッダー

よく見るヘッダー

- Host
- Content-Type
- Content-Length
- Accept
- Authorization
- Cookie
- Set-Cookie
- Location
- Cache-Control
- User-Agent
- Referer
- Origin

---

# Content-Type

代表例

```
text/html
application/json
application/x-www-form-urlencoded
multipart/form-data
image/png
```

---

# CookieとSession

Cookie

- ブラウザに保存
- IDなど小さい情報

Session

- サーバー側に保存
- CookieのSession IDと紐付く

ログイン状態の維持に利用されます。

---

# リダイレクト

```
302
 ↓
Location: /login
```

302が返ってきたら、Locationヘッダーを確認します。

---

# ブラウザ開発者ツール

Networkタブで確認する項目

- Method
- URL
- Status
- Request Headers
- Response Headers
- Payload
- Response
- Timing

---

# 実務シナリオ

## フォーム送信後に302

確認すること

1. Location
2. Cookie
3. Session
4. PHPログ

---

## APIが404

確認すること

1. URL
2. Method
3. Route
4. Rewrite設定

---

## 500エラー

確認すること

1. Response
2. PHPログ
3. Dockerログ
4. SQLログ

---

# ハンズオン

1. Chrome DevToolsを開く
2. Networkタブを表示
3. ページを再読み込み
4. 200の通信を確認
5. Request Headersを読む
6. Response Headersを読む
7. Cookieを見る
8. Payloadを見る
9. 302通信を探す
10. 404通信を探す

---

# 練習問題

1. GETとPOSTの違いは？
2. 302の意味は？
3. 500なら最初に何を見る？
4. CookieとSessionの違いは？
5. Content-Typeは何を表す？
6. 401と403の違いは？
7. Locationヘッダーは何に使う？

---

# チェックリスト

- [ ] URLの構造を説明できる
- [ ] GETとPOSTを説明できる
- [ ] ステータスコードを理解した
- [ ] Headerを確認できる
- [ ] CookieとSessionを理解した
- [ ] DevToolsで通信を追える

---

# コラム

**デバッグの第一歩は「コードを見ること」ではありません。**

まずHTTP通信を確認してください。

通信が正常なのか、URLが違うのか、302なのか、500なのか。

これが分かるだけで調査範囲は大きく絞れます。

---

# 次章予告

第5章では **curl完全攻略** として、ブラウザを使わずにHTTP通信を再現・検証する方法を学びます。
