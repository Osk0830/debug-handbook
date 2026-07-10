# 22-07 ブレークポイントと基本操作

## ブレークポイント

エディタ左端の行番号付近をクリックすると赤い丸が表示されます。

処理がその行へ到達すると停止します。

---

## 最初に止める場所

フォーム処理:

```php
$request = $_POST;
```

API:

```php
$payload = json_decode(file_get_contents('php://input'), true);
```

サービス:

```php
$result = $service->execute($input);
```

SQL直前:

```php
$stmt->execute($params);
```

戻り値直前:

```php
return $response;
```

---

## Continue

```text
F5
```

次のブレークポイントまで処理を続行します。

---

## Step Over

```text
F10
```

現在行を実行し、次の行へ進みます。

関数呼び出しがあっても、通常は関数内部へ入りません。

```php
$total = calculateTotal($items);
$response = buildResponse($total);
```

`calculateTotal()`の内部を調べず、戻り値だけ確認したい場合に使います。

---

## Step Into

```text
F11
```

呼び出している関数の内部へ入ります。

```php
$total = calculateTotal($items);
```

`calculateTotal()`のロジックを追いたい場合に使います。

---

## Step Out

```text
Shift + F11
```

現在の関数の残りを実行し、呼び出し元へ戻ります。

ライブラリ内部へ誤って入った場合にも便利です。

---

## Restart

デバッグセッションを再開始します。

ただしWebリクエストの場合、VS Code側だけ再起動しても同じHTTPリクエストが自動送信されるとは限りません。

ブラウザ更新やcurl再実行が必要です。

---

## Stop

現在のデバッグセッションを終了します。

PHP処理自体が中断される場合があるため、更新処理の途中で止めるときは注意します。

---

## ブレークポイントの状態

### 赤い実線の丸

有効なブレークポイント。

### 薄い丸・未検証表示

IDEが実行ファイルとの対応を確認できていない可能性があります。

主な原因:

- デバッグセッションが未接続
- `pathMappings`不一致
- 対象ファイルが読み込まれていない
- 実行不能行
- 別のコピーを編集している

---

## 1行ずつ進めすぎない

すべてをStep Intoすると調査が遅くなります。

基本方針:

```text
大きな境界まではContinue
  ↓
対象関数の入口で停止
  ↓
通常はStep Over
  ↓
怪しい関数だけStep Into
  ↓
不要な階層へ入ったらStep Out
```

---

## 例: 金額計算の不具合

```php
function calculateTotal(array $items): int
{
    $subtotal = calculateSubtotal($items);
    $tax = calculateTax($subtotal);
    $discount = calculateDiscount($items);

    return $subtotal + $tax - $discount;
}
```

確認手順:

1. 関数入口で停止
2. `$items`を確認
3. `calculateSubtotal()`をStep Over
4. `$subtotal`を確認
5. 値が不正なら関数へ戻ってStep Into
6. `$tax`と`$discount`を順に確認
7. return直前の式を評価

---

## 副作用に注意

次の処理をStep Overすると、実際に実行されます。

```php
$mailer->send($message);
$repository->delete($id);
$payment->capture($amount);
```

デバッグ中でも、メール・削除・決済などの副作用は発生します。

安全策:

- 開発環境を使う
- テスト用データを使う
- 外部サービスをモックする
- トランザクションを使う
- 実行前にブレークポイントで入力値を確認する

---

## 演習

次のコードをデバッグし、どの操作を使うか説明してください。

```php
$user = findUser($id);
$permission = resolvePermission($user);
$result = updateProfile($user, $input);
sendNotification($user, $result);
```
