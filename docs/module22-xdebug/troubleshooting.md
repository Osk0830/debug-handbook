# Module22 Troubleshooting

Xdebugで止まらない場合は、推測で設定を増やさず、次の順番で確認します。

```text
対象コードが実行される
  ↓
対象PHPにXdebugが読み込まれる
  ↓
xdebug.modeにdebugが含まれる
  ↓
開始条件を満たす
  ↓
VS Codeが9003番で待ち受ける
  ↓
XdebugからVS Codeへ到達できる
  ↓
pathMappingsで同じファイルへ対応する
  ↓
実行可能行へブレークポイントを置く
```

## 最小診断

```bash
php --version
php --ini
php --ri xdebug
php -i | rg '^xdebug\.'
lsof -nP -iTCP:9003 -sTCP:LISTEN
```

Docker:

```bash
docker compose ps
docker compose exec php php --ri xdebug
docker compose exec php php -i | rg '^xdebug\.'
docker compose exec php tail -100 /tmp/xdebug.log
```

詳しい切り分けは
[Lesson15 デバッグ接続のトラブルシューティング](lessons/lesson15-debug-connection-troubleshooting.md)
を参照してください。
