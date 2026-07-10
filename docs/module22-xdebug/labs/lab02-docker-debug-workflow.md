# Lab02 Docker環境のXdebug接続を切り分ける

## 目的

Docker環境で起きる接続問題を、ログとコマンドで段階的に切り分けます。

## 前提

```text
コンテナ内: /var/www/html
ホスト側: ${workspaceFolder}
VS Code: ホストOS上
```

## 手順

1. コンテナ内で`php --ri xdebug`
2. `xdebug.client_host`を確認
3. `host.docker.internal`の名前解決を確認
4. VS Codeで9003番ポートを待ち受ける
5. コンテナから9003番へ接続確認
6. Xdebugログを有効化
7. Webリクエストを送信
8. ログの接続先を確認
9. `pathMappings`を設定
10. 実行可能行へブレークポイントを移動

## launch.json

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
      }
    }
  ]
}
```

## 完了条件

- 接続障害とパス障害を区別できる
- Xdebugログから接続先を説明できる
- 未検証ブレークポイントを解消できる
