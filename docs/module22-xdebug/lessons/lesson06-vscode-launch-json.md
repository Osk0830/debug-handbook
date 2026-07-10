# 22-06 VS Codeとlaunch.json

## PHP Debug拡張

VS Codeの拡張機能で次を検索します。

```text
PHP Debug
```

拡張ID:

```text
xdebug.php-debug
```

---

## 最小の`launch.json`

プロジェクト直下:

```text
.vscode/launch.json
```

内容:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Listen for Xdebug",
      "type": "php",
      "request": "launch",
      "port": 9003
    }
  ]
}
```

---

## 起動方法

1. VS Codeで「実行とデバッグ」を開く
2. `Listen for Xdebug`を選択
3. F5を押す
4. ステータスバーがデバッグ状態になる
5. ブラウザやcurlから対象処理を実行する

---

## Dockerの`pathMappings`

コンテナ内:

```text
/var/www/html
```

ホスト側:

```text
${workspaceFolder}
```

設定:

```json
{
  "name": "Listen for Xdebug (Docker)",
  "type": "php",
  "request": "launch",
  "port": 9003,
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}"
  }
}
```

左右を逆にしないでください。

```text
"コンテナ内のパス": "VS Code側のパス"
```

---

## 複数プロジェクト

```json
{
  "pathMappings": {
    "/var/www/app": "${workspaceFolder}/app",
    "/var/www/shared": "${workspaceFolder}/shared"
  }
}
```

---

## `stopOnEntry`

エントリポイント付近で停止します。

```json
{
  "stopOnEntry": true
}
```

ブレークポイントが解決できないときの確認に使えます。

通常運用では`false`または省略します。

---

## `log`

PHP Debug拡張側の通信ログを表示します。

```json
{
  "log": true
}
```

Xdebugログと合わせて確認すると、接続のどちら側で失敗しているか分かります。

---

## `ignore`

ベンダーコードなどへのStep Intoを抑制します。

```json
{
  "ignore": [
    "**/vendor/**/*.php"
  ]
}
```

ただし、ライブラリ内部を調査したいときは一時的に外します。

---

## 複数構成

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Listen for Xdebug - Local",
      "type": "php",
      "request": "launch",
      "port": 9003
    },
    {
      "name": "Listen for Xdebug - Docker",
      "type": "php",
      "request": "launch",
      "port": 9003,
      "pathMappings": {
        "/var/www/html": "${workspaceFolder}"
      }
    }
  ]
}
```

---

## CLIファイルをVS Codeから実行

```json
{
  "name": "Debug current PHP file",
  "type": "php",
  "request": "launch",
  "program": "${file}",
  "cwd": "${fileDirname}",
  "port": 0,
  "runtimeArgs": [
    "-dxdebug.mode=debug",
    "-dxdebug.start_with_request=yes"
  ]
}
```

`port: 0`は、拡張側が利用可能なポートを選び、その情報をPHPへ渡す用途で使われます。

環境や拡張バージョンにより挙動を確認してください。

---

## Workspaceの基準位置

`${workspaceFolder}`は、VS Codeで開いたフォルダです。

次の開き方では基準が変わります。

```text
project/
└── app/
```

`project`を開く:

```json
"/var/www/html": "${workspaceFolder}/app"
```

`app`を開く:

```json
"/var/www/html": "${workspaceFolder}"
```

---

## 設定例の完成形

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Listen for Xdebug (Docker)",
      "type": "php",
      "request": "launch",
      "port": 9003,
      "pathMappings": {
        "/var/www/html": "${workspaceFolder}"
      },
      "ignore": [
        "**/vendor/**/*.php"
      ],
      "log": false
    }
  ]
}
```

---

## 演習

1. `.vscode/launch.json`を作成する。
2. Dockerコンテナ内のドキュメントルートを確認する。
3. `pathMappings`を設定する。
4. F5で待受を開始する。
5. `lsof`で9003番ポートを確認する。
