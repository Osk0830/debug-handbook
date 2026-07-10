# 22-01 Xdebugの仕組み

## Xdebugとは

XdebugはPHPの拡張機能です。

PHPコードを実行するエンジンそのものではなく、PHPの実行に介入し、デバッグに必要な情報を外部へ送ります。

主な機能は次のとおりです。

- ステップデバッグ
- スタックトレースの強化
- コードカバレッジ
- プロファイリング
- 関数トレース

本章の中心は**ステップデバッグ**です。

---

## VS CodeだけではPHPを止められない

VS Codeはデバッグ画面を提供しますが、PHP内部の実行状態を単独では取得できません。

それぞれの役割は次のとおりです。

| 要素 | 役割 |
|---|---|
| PHP | PHPコードを実行する |
| Xdebug | PHPの実行状態を取得し、IDEへ接続する |
| PHP Debug拡張 | Xdebugとの通信をVS Codeへ橋渡しする |
| VS Code | ブレークポイント・変数・スタックを表示する |

---

## 接続方向を理解する

重要なのは、通常のWebアクセスとXdebugの接続方向が異なる点です。

### Webアクセス

```text
Browser
  │ HTTP
  ▼
Web Server
  │
  ▼
PHP
```

### Xdebug接続

```text
PHP / Xdebug
  │ 接続
  ▼
VS Code
```

Xdebugは、VS Codeが待ち受けているポートへ接続します。

そのためDocker環境では、コンテナからホストOSへ到達できるホスト名を設定する必要があります。

---

## DBGp

XdebugとIDEはDBGpというプロトコルを使って通信します。

通常、利用者がDBGpを直接操作することはありません。

ただし次の理解は重要です。

- VS Codeは待ち受け側
- Xdebugは接続側
- 接続ポートの既定値は`9003`
- PHPの実行開始時に接続を試みる
- IDEと接続できない場合も、通常はPHP処理自体は続行する

---

## 1回のデバッグセッション

```text
1. VS Codeで「Listen for Xdebug」を開始
2. PHP Debug拡張が9003番ポートを待ち受ける
3. ブラウザやcurlからPHPへアクセス
4. PHPがコードを実行
5. XdebugがVS Codeへ接続
6. ファイルパスをIDEへ通知
7. ブレークポイントのある行で停止
8. VS Codeから実行継続・ステップ操作
9. PHP処理が完了
10. デバッグ接続が終了
```

---

## `xdebug.start_with_request`

デバッグ接続をいつ開始するかを決める設定です。

### `yes`

すべてのリクエストでデバッグ接続を試みます。

```ini
xdebug.start_with_request=yes
```

学習環境では分かりやすい設定です。

ただし、常に接続を試すため、IDEが起動していない場合にわずかな待ち時間が発生することがあります。

### `trigger`

特定のトリガーがある場合だけ開始します。

```ini
xdebug.start_with_request=trigger
```

WebではCookieやクエリ、CLIでは環境変数などを使います。

例:

```bash
XDEBUG_TRIGGER=1 php script.php
```

日常運用では`trigger`が便利です。

---

## `xdebug.mode`

Xdebugの機能を指定します。

```ini
xdebug.mode=debug
```

複数指定:

```ini
xdebug.mode=debug,develop
```

代表的なモード:

| mode | 用途 |
|---|---|
| `debug` | ステップデバッグ |
| `develop` | 開発向けエラー表示や補助情報 |
| `coverage` | コードカバレッジ |
| `profile` | プロファイリング |
| `trace` | 関数トレース |
| `off` | 無効 |

機能を増やすほどオーバーヘッドも増えるため、必要なモードだけを有効にします。

---

## ブレークポイントが止まる条件

ブレークポイントで止まるには、少なくとも次の条件が必要です。

1. 対象PHPプロセスにXdebugが読み込まれている
2. `xdebug.mode`に`debug`が含まれている
3. デバッグ開始条件を満たしている
4. XdebugからVS Codeへ接続できる
5. VS Codeの待受ポートと一致している
6. Xdebugが通知するパスをVS Codeが解決できる
7. 対象の行が実際に実行される
8. 実行可能な行にブレークポイントがある

---

## 実行可能な行

次のような行は、ブレークポイントを置いても期待どおりに止まらない場合があります。

```php
<?php

// コメントだけの行

function calculate(
    int $price,
    int $quantity
): int {
    return $price * $quantity;
}
```

関数宣言の途中やコメントではなく、実際に命令が実行される行へ置きます。

```php
return $price * $quantity;
```

---

## 章末演習

1. XdebugとVS Codeの役割の違いを説明してください。
2. XdebugからVS Codeへ接続する理由を説明してください。
3. `xdebug.start_with_request=yes`と`trigger`の違いを説明してください。
4. ブレークポイントで止まるための条件を5つ挙げてください。
