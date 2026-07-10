# Module22 Beginner Exercises

## Exercise01 実行環境を特定する

次を実行し、PHPの実体、バージョン、読み込み中のiniを記録してください。

```bash
which php
php --version
php --ini
php --ri xdebug
```

## Exercise02 Xdebugの接続方向

ブラウザ、Webサーバー、PHP、Xdebug、VS Codeの関係を図にしてください。

## Exercise03 最小設定

次の条件を満たすXdebug設定を書いてください。

- Xdebug 3
- ステップデバッグ
- 常時開始
- ローカルPHP
- ポート9003

## Exercise04 Docker設定

Dockerコンテナ内のPHPから、ホストOS上のVS Codeへ接続する設定を書いてください。

## Exercise05 launch.json

コンテナ内の`/var/www/html`と、VS Codeの`${workspaceFolder}`を対応させてください。

## Exercise06 Step操作

`Step Over`、`Step Into`、`Step Out`の違いを説明してください。

## Exercise07 Watch

次を確認するWatch式を書いてください。

- 配列の件数
- JSONエラー
- リクエストURI
- セッションのユーザーID
- 値の型

## Exercise08 条件付き停止

IDが123、かつ再試行回数が2以上の場合だけ停止する条件を書いてください。

## Exercise09 Web API

JSON APIをcurlで呼び出し、生データ、デコード結果、バリデーション結果を追ってください。

## Exercise10 接続障害

ブレークポイントで止まらない場合の確認順序を、9段階で書いてください。
