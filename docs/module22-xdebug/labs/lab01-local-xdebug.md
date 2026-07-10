# Lab01 ローカルPHPをXdebugで停止する

## 目的

ローカルPHP、Xdebug、VS Codeの接続を最小構成で成立させます。

## 手順

1. `php --ri xdebug`で読み込みを確認する
2. `xdebug.mode=debug`を設定する
3. `xdebug.start_with_request=yes`を設定する
4. VS CodeへPHP Debug拡張を導入する
5. `.vscode/launch.json`を作成する
6. サンプルPHPへブレークポイントを置く
7. F5で待受を開始する
8. PHPを実行する
9. Variables、Watch、Call Stackを確認する

## サンプル

```php
<?php

function calculate(int $price, int $quantity): int
{
    $subtotal = $price * $quantity;
    $tax = (int) floor($subtotal * 0.1);

    return $subtotal + $tax;
}

echo calculate(1200, 3), PHP_EOL;
```

## 完了条件

- ブレークポイントで停止する
- Step IntoとStep Overを使える
- `$subtotal`と`$tax`を確認できる
- 呼び出し元へ戻れる
