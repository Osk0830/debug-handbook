# 22-14 WordPress・API・フォーム実践

## ケース1: WordPressの保存処理

### 症状

管理画面で投稿を保存しても、カスタムフィールドが保存されない。

### ブレークポイント候補

```php
add_action('save_post', 'save_custom_fields');
```

```php
function save_custom_fields(int $postId): void
{
    // 入口
}
```

### 確認項目

```php
$postId
$_POST
wp_is_post_revision($postId)
defined('DOING_AUTOSAVE')
current_user_can('edit_post', $postId)
```

### よくある原因

- nonce不一致
- autosaveでreturn
- revisionでreturn
- 権限判定
- input名の不一致
- サニタイズ後に空
- フック優先度
- 別プラグインによる上書き

---

## ケース2: REST APIが400になる

### 入口

```php
$raw = file_get_contents('php://input');
$payload = json_decode($raw, true);
```

### 確認

```php
$raw
$payload
json_last_error_msg()
$_SERVER['CONTENT_TYPE'] ?? null
```

### 境界

```text
Request
  ↓
JSON decode
  ↓
Validation
  ↓
Service
  ↓
Repository
  ↓
Response
```

400が返る直前だけでなく、入力がどこで欠落したかを追います。

---

## ケース3: フォーム確認画面と完了画面で値が消える

### 確認ポイント

```php
$_POST
$_SESSION
session_id()
$_COOKIE
```

### 処理経路

```text
input.php
  ↓ POST
confirm.php
  ↓ POST / Session
complete.php
```

### よくある原因

- hidden input不足
- session_start()漏れ
- Cookie属性
- ドメイン・パス不一致
- HTTP/HTTPS混在
- リダイレクト前後でセッション更新失敗
- 二重送信対策のタイミング

---

## ケース4: SQL更新件数が0

```php
$stmt = $pdo->prepare($sql);
$stmt->execute($params);
$rowCount = $stmt->rowCount();
```

確認:

```php
$sql
$params
$stmt->errorInfo()
$rowCount
```

追加確認:

- WHERE条件
- IDの型
- 対象行の存在
- 同じ値への更新
- トランザクション
- 接続先DB
- レプリカ参照
- コミット漏れ

---

## ケース5: 外部APIレスポンスが空

```php
$response = $client->request('GET', $url, $options);
$body = (string) $response->getBody();
$data = json_decode($body, true);
```

確認:

```php
$url
$options
$response->getStatusCode()
$response->getHeaders()
$body
json_last_error_msg()
```

デバッガで長時間止めると外部通信がタイムアウトするため、呼び出し前後にブレークポイントを分けます。

---

## ケース6: WordPress Ajax

確認:

```php
$_REQUEST['action'] ?? null
is_user_logged_in()
check_ajax_referer(...)
```

フック:

```php
wp_ajax_example
wp_ajax_nopriv_example
```

ログイン状態により呼ばれるフックが変わります。

---

## ケース7: 404画像のフォールバック

サーバー側で画像URLを生成している場合:

```php
$imageUrl = buildImageUrl($image);
```

確認:

- 元データ
- パス結合
- URLエンコード
- ベースURL
- CDN設定
- null時の分岐
- ファイル存在判定

クライアント側404はブラウザNetworkと組み合わせます。

---

## 実務デバッグテンプレート

```text
症状:
再現条件:
期待結果:
実際結果:

入口:
最初の正常値:
最初の異常値:
正常→異常の境界:

使用した証拠:
[ ] HTTP
[ ] Variables
[ ] Watch
[ ] Call Stack
[ ] SQL
[ ] Log
[ ] Git diff

原因:
修正:
再発防止:
```

---

## 演習

WordPressのAjax検索で、未ログイン時だけ0が返ります。

確認するフック、変数、ブレークポイント位置を整理してください。
