# 22-16 総合演習

## 演習環境

次の処理を想定します。

```text
POST /api/orders
  ↓
OrderController
  ↓
OrderValidator
  ↓
OrderService
  ↓
PriceCalculator
  ↓
OrderRepository
  ↓
JSON Response
```

症状:

> 特定の商品を3個以上注文すると、合計金額が100円少なくなる。

---

## サンプルコード

```php
<?php

final class PriceCalculator
{
    public function calculate(array $items): int
    {
        $subtotal = 0;

        foreach ($items as $item) {
            $lineTotal = $item['price'] * $item['quantity'];

            if ($item['quantity'] >= 3) {
                $lineTotal -= 100;
            }

            $subtotal += $lineTotal;
        }

        return $subtotal;
    }
}
```

仕様:

> 3個以上の場合、注文全体から100円引き。ただし割引は1回だけ。

現在のコードでは、対象商品ごとに100円引かれます。

---

## 課題1: 再現条件を固定する

リクエスト例:

```bash
curl -i \
  -X POST \
  -H 'Content-Type: application/json' \
  --data '{
    "items": [
      {"id": 1, "price": 1000, "quantity": 3},
      {"id": 2, "price": 500, "quantity": 4}
    ]
  }' \
  http://localhost:8080/api/orders
```

期待:

```text
3000 + 2000 - 100 = 4900
```

実際:

```text
3000 - 100 + 2000 - 100 = 4800
```

---

## 課題2: ブレークポイントを設計する

次の場所へ置いてください。

1. Controller入口
2. Validator直後
3. PriceCalculator入口
4. ループ内部
5. return直前

各場所で確認する値を決めます。

---

## 課題3: Watch

次を登録してください。

```php
count($items)
$subtotal
$lineTotal
$item['id']
$item['quantity']
```

---

## 課題4: 条件付きブレークポイント

商品IDが2のときだけ停止:

```php
$item['id'] === 2
```

---

## 課題5: Call Stack

ループ内で停止し、呼び出し経路を記録してください。

```text
PriceCalculator->calculate()
OrderService->create()
OrderController->store()
```

実際の構成に合わせて記録します。

---

## 課題6: 修正

例:

```php
final class PriceCalculator
{
    public function calculate(array $items): int
    {
        $subtotal = 0;
        $hasBulkItem = false;

        foreach ($items as $item) {
            $subtotal += $item['price'] * $item['quantity'];

            if ($item['quantity'] >= 3) {
                $hasBulkItem = true;
            }
        }

        if ($hasBulkItem) {
            $subtotal -= 100;
        }

        return $subtotal;
    }
}
```

仕様が「合計数量3個以上」なのか「いずれかの商品が3個以上」なのかで条件は変わります。

デバッグで現象を理解した後、仕様を確認して修正します。

---

## 課題7: テスト

```php
public function test_bulk_discount_is_applied_once(): void
{
    $calculator = new PriceCalculator();

    $actual = $calculator->calculate([
        ['id' => 1, 'price' => 1000, 'quantity' => 3],
        ['id' => 2, 'price' => 500, 'quantity' => 4],
    ]);

    self::assertSame(4900, $actual);
}
```

追加ケース:

- 割引対象なし
- 対象商品1件
- 対象商品複数
- 空配列
- 数量0
- 負数
- 不正な型

---

## 総合演習B: Xdebug接続障害

症状:

> Docker内のPHPへアクセスできるが、ブレークポイントで止まらない。

設定:

```ini
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=127.0.0.1
xdebug.client_port=9003
```

Dockerでは`127.0.0.1`は通常コンテナ自身です。

次を実施してください。

1. `php --ri xdebug`
2. VS Code待受確認
3. Xdebugログ有効化
4. 接続先の確認
5. `host.docker.internal`へ修正
6. 名前解決確認
7. `pathMappings`確認
8. 再リクエスト

---

## 総合演習C: セッション不具合

症状:

> フォーム確認画面では値があるが、完了画面でログイン情報だけ消える。

確認対象:

```php
session_id()
$_COOKIE
$_SESSION
session_status()
```

Call Stackとリダイレクト前後を使い、値が消える境界を特定してください。

---

## 提出用デバッグ記録

```markdown
# デバッグ記録

## 症状

## 再現手順

## 期待結果

## 実際結果

## 仮説

## ブレークポイント

## 確認した変数

## Call Stack

## 最初に異常になった場所

## 根本原因

## 修正内容

## テスト

## 再発防止
```

---

## 章の完了条件

- [ ] Xdebugの接続方向を説明できる
- [ ] ローカルとDockerへ導入できる
- [ ] Xdebug設定を確認できる
- [ ] `launch.json`を作成できる
- [ ] `pathMappings`を設定できる
- [ ] Step操作を使い分けられる
- [ ] Variables・Watch・Consoleを使える
- [ ] Call Stackで原因範囲を絞れる
- [ ] 条件付きブレークポイントを使える
- [ ] Web・CLI・テストをデバッグできる
- [ ] 止まらない問題を順番に切り分けられる
