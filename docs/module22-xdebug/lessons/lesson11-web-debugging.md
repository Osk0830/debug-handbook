# 22-11 Webリクエストのデバッグ

## 基本フロー

```text
VS Codeで待受
  ↓
ブレークポイント設定
  ↓
ブラウザまたはcurlでリクエスト
  ↓
PHPで停止
  ↓
Request確認
  ↓
Serviceへ進む
  ↓
Response確認
```

---

## GET

```bash
curl -i 'http://localhost:8080/users?id=123'
```

確認:

```php
$_GET
$_SERVER['REQUEST_URI']
$_SERVER['QUERY_STRING']
```

---

## POSTフォーム

```bash
curl -i \
  -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'name=Taro&email=taro@example.com' \
  http://localhost:8080/users
```

確認:

```php
$_POST
$_SERVER['CONTENT_TYPE']
$_SERVER['REQUEST_METHOD']
```

---

## JSON API

```bash
curl -i \
  -X POST \
  -H 'Content-Type: application/json' \
  --data '{"name":"Taro","email":"taro@example.com"}' \
  http://localhost:8080/api/users
```

PHP:

```php
$raw = file_get_contents('php://input');
$payload = json_decode($raw, true);
```

確認:

```php
$raw
$payload
json_last_error_msg()
```

---

## Cookie・Session

Cookie付き:

```bash
curl -i \
  -b 'PHPSESSID=example-session-id' \
  http://localhost:8080/account
```

確認:

```php
$_COOKIE
session_id()
$_SESSION
```

ブラウザのCookieとPHPセッションの対応を確認します。

---

## ファイルアップロード

```bash
curl -i \
  -X POST \
  -F 'title=sample' \
  -F 'image=@./sample.jpg' \
  http://localhost:8080/upload
```

確認:

```php
$_POST
$_FILES
$_FILES['image']['error'] ?? null
```

---

## リダイレクト

```bash
curl -i http://localhost:8080/login
```

追従:

```bash
curl -i -L http://localhost:8080/login
```

デバッグでは、最初は`-L`を付けずに各レスポンスを分離します。

確認:

- HTTPステータス
- `Location`
- Cookie
- セッション更新
- リダイレクト前の分岐

---

## ブレークポイントの置き場所

```text
public/index.php
  ↓
Router / Middleware
  ↓
Controller
  ↓
Validation
  ↓
Service
  ↓
Repository
  ↓
Response
```

すべてへ置かず、境界に置きます。

1. Controller入口
2. Service入口
3. SQL直前
4. Response直前

---

## 一度に複数リクエストが来る場合

Webページの表示で、次も同時に発生することがあります。

- favicon
- CSS / JavaScript
- API
- 画像
- Ajax
- Service Worker

PHPを通るリクエストだけが対象ですが、複数APIが同時に動く場合は混乱します。

対策:

- 条件付きブレークポイント
- `$_SERVER['REQUEST_URI']`で絞る
- curlで対象APIだけ再現する
- ブラウザのNetworkからリクエストをコピーする

---

## トリガー方式

`xdebug.start_with_request=trigger`の場合:

CLI:

```bash
XDEBUG_TRIGGER=1 php script.php
```

Webではブラウザ拡張を使うか、トリガーCookieを設定します。

curl例:

```bash
curl -i \
  -b 'XDEBUG_TRIGGER=1' \
  http://localhost:8080/api/users
```

環境のXdebug設定に合わせてトリガー方法を確認してください。

---

## タイムアウト

ブレークポイントで長時間停止すると、次がタイムアウトする可能性があります。

- ブラウザ
- Nginx / Apache
- PHP-FPM
- リバースプロキシ
- 外部API
- DBロック待ち

更新処理を止める場合は、トランザクションやロックにも注意します。

---

## 演習

JSON APIへ不正なメールアドレスを送信し、次を確認してください。

1. 生のリクエストボディ
2. JSONデコード結果
3. バリデーション入力
4. エラー配列
5. HTTPステータス
6. レスポンスJSON
