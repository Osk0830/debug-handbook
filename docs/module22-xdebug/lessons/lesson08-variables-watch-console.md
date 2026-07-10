# 22-08 Variables・Watch・Debug Console

## Variables

停止中の現在スコープに存在する変数を表示します。

例:

```php
function updateUser(int $id, array $input): User
{
    $user = $this->repository->find($id);
    $validated = $this->validator->validate($input);

    return $this->repository->update($user, $validated);
}
```

確認できるもの:

- `$id`
- `$input`
- `$this`
- `$user`
- `$validated`

ただし、まだ実行されていない行の変数は存在しません。

---

## スーパーグローバル

Web処理では次を確認します。

```php
$_GET
$_POST
$_COOKIE
$_SESSION
$_SERVER
$_FILES
```

すべてを展開すると情報量が多いため、必要なキーへ絞ります。

```php
$_SERVER['REQUEST_METHOD']
$_SERVER['REQUEST_URI']
$_COOKIE['PHPSESSID'] ?? null
```

---

## Watch

常に確認したい式を登録します。

例:

```php
$id
$input['email'] ?? null
count($items)
$user?->getId()
$_SESSION['user_id'] ?? null
```

Watchは変数名だけでなく式を評価できます。

---

## 良いWatch式

```php
$order->getStatus()
count($errors)
array_keys($payload)
$index . ':' . ($item['id'] ?? 'none')
```

調査対象を短く表現します。

---

## 注意が必要なWatch式

副作用のある式を避けます。

```php
$repository->delete($id)
$mailer->send($message)
$service->execute()
```

デバッガによる評価で、実際に処理が実行される可能性があります。

原則として、Watchでは参照・計算だけを行います。

---

## Debug Console

停止中に式を評価できます。

例:

```php
$user
$user->getId()
count($items)
array_column($items, 'id')
json_encode($payload, JSON_PRETTY_PRINT)
```

---

## null安全な確認

```php
$user?->getProfile()?->getName()
```

配列:

```php
$payload['user']['email'] ?? null
```

---

## 型確認

```php
get_debug_type($value)
is_array($value)
is_object($value)
$value instanceof User
```

値が似ていても、型違いが不具合の原因になることがあります。

```php
0
'0'
false
null
''
```

---

## JSON確認

```php
json_last_error_msg()
json_encode($payload, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
```

デコード:

```php
json_decode($raw, true)
json_last_error_msg()
```

---

## 配列を絞り込む

巨大配列全体ではなく、必要な部分だけ評価します。

```php
array_slice($items, 0, 3)
array_column($items, 'id')
array_filter($items, fn ($item) => $item['status'] === 'error')
```

---

## オブジェクトの確認

ORMやフレームワークのオブジェクトは内部情報が多くなります。

公開メソッドやDTO変換を使います。

```php
$user->getId()
$user->getEmail()
$user->toArray()
```

---

## 変数が更新されるタイミング

黄色い実行位置は、**これから実行する行**を示します。

```php
$total = calculateTotal($items);
```

この行で停止した直後は、`$total`にはまだ新しい値が代入されていません。

Step Overした後に確認します。

---

## 実践チェック

フォーム送信時:

```php
$_SERVER['REQUEST_METHOD']
$_POST
$_FILES
$_SESSION
```

API:

```php
$rawBody
$payload
json_last_error_msg()
```

SQL:

```php
$sql
$params
$stmt->errorInfo()
```

---

## 演習

次の不具合を調査するWatch式を考えてください。

- `$items`の件数が想定と違う
- ユーザーIDが文字列になっている
- JSONデコードが失敗している
- セッションのログインIDが消えている
