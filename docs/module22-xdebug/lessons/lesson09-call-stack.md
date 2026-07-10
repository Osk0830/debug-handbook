# 22-09 Call Stackと処理経路

## Call Stackとは

現在の処理が、どの関数・メソッドを経由して到達したかを表示します。

例:

```text
public/index.php
App\Kernel->handle()
UserController->update()
UserService->updateProfile()
UserRepository->save()
```

一番上が現在位置で、その下に呼び出し元が並びます。

---

## なぜ変数だけでは足りないのか

同じメソッドが複数箇所から呼ばれる場合があります。

```php
$userService->update($input);
```

呼び出し元:

- 管理画面
- 公開API
- バッチ
- テスト
- Queue Worker

値が不正でも、メソッド内部ではなく呼び出し元の組み立てが原因かもしれません。

---

## フレームを切り替える

Call Stackの別フレームを選択すると、その時点のローカル変数を確認できます。

現在:

```php
UserRepository->save($user)
```

1つ上:

```php
UserService->updateProfile($id, $input)
```

さらに上:

```php
UserController->update($request)
```

これにより、

- Controllerが渡した入力
- Serviceで加工した値
- Repositoryへ渡ったオブジェクト

を比較できます。

---

## 例外発生時

```php
throw new RuntimeException('User not found');
```

例外位置だけでなく、Call Stackを上へたどります。

確認項目:

1. どの入口から呼ばれたか
2. どの引数が渡されたか
3. どの分岐を通ったか
4. 例外が想定内か
5. 捕捉される設計か

---

## 再帰

```php
function walk(Node $node): void
{
    foreach ($node->children as $child) {
        walk($child);
    }
}
```

Call Stackに同じ関数が繰り返し表示されます。

確認する値:

- 深さ
- 現在ノード
- 親ノード
- 終了条件

Watch例:

```php
$node->id
count($node->children)
```

---

## コールバック

```php
$result = array_map(
    fn (array $item) => normalize($item),
    $items
);
```

Call Stackを見ると、内部関数やコールバックを経由していることが分かります。

無関係な内部処理へ入った場合はStep Outを使います。

---

## フレームワーク

フレームワークではスタックが長くなります。

```text
vendor/
  ↓
Middleware
  ↓
Router
  ↓
Controller
  ↓
Service
  ↓
Repository
```

最初からすべてを読む必要はありません。

まず自分のコードの最上位フレームを探します。

---

## 問題の境界を見つける

各フレームの値を比較し、正常から異常へ変わった境界を探します。

```text
Controller: 正常
  ↓
Service入口: 正常
  ↓
Service加工後: 異常
  ↓
Repository: 異常
```

この場合、Service内の加工処理へ調査範囲を絞れます。

---

## 実践フロー

1. 不具合が現れる下流で停止
2. 現在の値を確認
3. Call Stackを1つ上へ移動
4. 渡す直前の値を確認
5. 正常なフレームまで上る
6. 正常→異常へ変化した境界を特定
7. その範囲だけStep実行する

---

## 演習

Repositoryへ空のメールアドレスが渡っています。

```text
UserController->update()
UserService->normalizeInput()
UserRepository->save()
```

Call Stackを使い、どの順番で何を確認するか説明してください。
