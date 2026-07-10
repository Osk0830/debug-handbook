# Lesson03 HTTP・curl・ネットワーク

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## 基本リクエスト

```bash
curl -i https://example.com
curl -sS https://example.com
curl -I https://example.com
curl -L https://example.com
curl -v https://example.com
```

**判断ポイント:** `-i`はヘッダー込み、`-I`はHEAD、`-L`はリダイレクト追従。

## JSON API

```bash
curl -sS https://api.example.com/items | jq .
curl -sS -X POST https://api.example.com/items \
  -H 'Content-Type: application/json' \
  -d '{"name":"sample"}'
```

**判断ポイント:** HTTPメソッド、URL、ヘッダー、ボディを分けて確認する。

## 認証

```bash
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/me
curl -u user:password https://example.com/private
```

**判断ポイント:** トークンをシェル履歴や共有ログへ残さない。

## 時間計測

```bash
curl -o /dev/null -sS \
  -w 'status=%{http_code} dns=%{time_namelookup} connect=%{time_connect} start=%{time_starttransfer} total=%{time_total}\n' \
  https://example.com
```

**判断ポイント:** DNS、接続、最初の1byte、総時間を分ける。

## 名前解決・ポート

```bash
dig example.com
nslookup example.com
nc -vz localhost 8080
lsof -nP -iTCP:8080 -sTCP:LISTEN
```

**判断ポイント:** 接続不能は、DNS・経路・ポート待受・アプリの順に切り分ける。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
