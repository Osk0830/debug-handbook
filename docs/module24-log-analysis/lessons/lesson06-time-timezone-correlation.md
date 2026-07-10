# 時刻・タイムゾーン・相関


## 時刻がずれる原因

- UTCとJST
- コンテナのタイムゾーン
- DBのタイムゾーン
- ブラウザ時刻
- サマータイム
- NTPずれ
- ミリ秒・秒の違い

## 現在時刻

```bash
date
date -u
```

Docker:

```bash
docker compose exec app date
docker compose exec app date -u
```

MySQL:

```sql
SELECT NOW(), UTC_TIMESTAMP(), @@session.time_zone, @@global.time_zone;
```

## ISO 8601

推奨例:

```text
2026-07-10T14:20:01.123+09:00
2026-07-10T05:20:01.123Z
```

## 時間窓

ユーザー報告が14:20の場合、まず前後数分を取ります。

```text
14:18:00 ～ 14:22:00
```

非同期処理ではさらに広げます。

## 相関のコツ

```text
Access Log 14:20:01 request_id=abc
Application 14:20:01.120 request_id=abc
SQL Slow Log 14:20:02
Upstream timeout 14:20:31
Nginx 504 14:20:31
```

同じ時刻・識別子をつなぎ、処理の順序を再構成します。
