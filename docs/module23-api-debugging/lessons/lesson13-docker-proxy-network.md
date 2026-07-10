# Docker・Proxy・ネットワーク


## コンテナ内から確認

```bash
docker compose exec app curl -v http://api:8080/health
```

サービス名はComposeネットワーク内のDNS名として使えます。

## localhostの意味

- ホストOSのlocalhost
- コンテナ自身のlocalhost
- 別コンテナのlocalhost

は別です。

## 名前解決

```bash
docker compose exec app getent hosts api
```

## Nginx経由と直アクセスを比較

```bash
curl -i http://localhost:8080/api/health
docker compose exec app curl -i http://api:8080/health
```

差があればProxy設定を確認します。

## Proxyで見る項目

- upstream
- Host
- X-Forwarded-For
- X-Forwarded-Proto
- timeout
- body size
- buffering
- path rewrite

## 502/504

```text
502: 上流へ接続できない・不正応答
504: 上流応答待ちタイムアウト
```

Nginxログ、アプリログ、コンテナ状態を同じ時刻で照合します。
