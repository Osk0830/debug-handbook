# curlで通信を詳細観測する


## タイミング

```bash
curl -sS -o /dev/null   -w 'status=%{http_code}
connect=%{time_connect}
ttfb=%{time_starttransfer}
total=%{time_total}
'   http://localhost:8080/api/users
```

## リダイレクト

追従しない:

```bash
curl -i http://localhost:8080/login
```

追従する:

```bash
curl -i -L http://localhost:8080/login
```

デバッグではまず追従せず、各レスポンスの`Location`とCookieを確認します。

## DNSを固定

```bash
curl --resolve example.test:443:127.0.0.1 https://example.test/api/health
```

## 接続先を確認

```bash
curl -v http://localhost:8080/api/health
```

## 圧縮

```bash
curl --compressed -i http://localhost:8080/api/users
```

## タイムアウト

```bash
curl   --connect-timeout 3   --max-time 10   http://localhost:8080/api/users
```

## リトライ

```bash
curl   --retry 3   --retry-all-errors   --retry-delay 1   http://localhost:8080/api/users
```

更新系APIへ無条件リトライを設定すると重複処理の危険があります。
