
# 第16章 パフォーマンス改善・SQL高速化・キャッシュ

> **目的**: 「動く」だけではなく「速く動く」ための調査・改善方法を身につける。

---

# この章で身につくこと

- パフォーマンス調査の考え方
- ボトルネックの見つけ方
- SQL高速化
- EXPLAINの読み方
- インデックスの基本
- N+1問題
- PHP・HTTP・ブラウザのキャッシュ
- 計測して改善する習慣

---

# 基本原則

**推測ではなく計測する。**

悪い例

```
たぶんSQLが遅い
```

良い例

```
Networkで3.2秒
SQLは2.8秒
PHPは0.2秒
HTML生成0.2秒
```

---

# ボトルネックを切り分ける

```text
Browser
 ↓
HTTP
 ↓
Web Server
 ↓
PHP
 ↓
SQL
 ↓
Response
```

どこが遅いかを特定します。

---

# Chrome DevTools

Networkタブで確認

- DNS
- Connect
- SSL
- Waiting(TTFB)
- Download

---

# curlで計測

```bash
curl -s -o /dev/null \
-w "status:%{http_code}\nTTFB:%{time_starttransfer}\nTotal:%{time_total}\n" \
http://localhost:8081/
```

---

# SQL計測

まずは

```sql
EXPLAIN
SELECT *
FROM users
WHERE email='test@example.com';
```

確認項目

- type
- key
- rows
- Extra

---

# インデックス

確認

```sql
SHOW INDEX FROM users;
```

インデックス候補

- WHERE
- JOIN
- ORDER BY

---

# N+1問題

悪い例

```text
Users取得
↓
UserごとにOrders取得
↓
100件なら101回SQL
```

改善

```text
JOIN
または
IN句
```

---

# LIMIT

一覧では必要件数だけ取得します。

```sql
LIMIT 20;
```

---

# SELECT *

必要な列だけ取得します。

悪い例

```sql
SELECT *
```

良い例

```sql
SELECT id,name
```

---

# PHP

確認

```bash
php -i | rg memory_limit
php -i | rg opcache
```

---

# OPcache

有効確認

```bash
php -i | rg opcache.enable
```

---

# Docker

リソース確認

```bash
docker stats
```

CPU・Memoryが不足していないか確認します。

---

# キャッシュ

種類

- Browser Cache
- HTTP Cache
- OPcache
- Redis
- CDN

---

# 実務シナリオ

## 一覧画面が遅い

確認順

1. Network
2. SQL
3. EXPLAIN
4. rows
5. インデックス

---

## APIが重い

確認

- SQL回数
- N+1
- JSONサイズ
- キャッシュ

---

## WordPressが遅い

確認

- WP_Query
- Plugin
- Object Cache
- SQL

---

# ハンズオン

1. curlで時間計測
2. EXPLAIN実行
3. SHOW INDEX
4. docker stats
5. Network確認
6. LIMIT追加
7. SELECT * を修正
8. rows比較
9. OPcache確認
10. キャッシュ削除後比較

---

# タイムアタック

30分以内で

- EXPLAIN確認
- rows確認
- Index確認
- curl計測
- docker stats確認

---

# 練習問題

1. EXPLAINは何を見る？
2. N+1問題とは？
3. SELECT * を避ける理由は？
4. LIMITを使う理由は？
5. OPcacheとは？
6. curlでレスポンス時間を測る方法は？

---

# チェックリスト

- [ ] curlで時間計測できる
- [ ] EXPLAINを読める
- [ ] SHOW INDEXを使える
- [ ] N+1問題を説明できる
- [ ] docker statsを確認できる
- [ ] ボトルネックを切り分けられる

---

# コラム

速いシステムは「速いコード」ではなく、「遅い場所を正しく見つける調査」ができています。

改善前と改善後を必ず計測し、数字で効果を確認しましょう。

---

# 次章予告

第17章では Docker・PHP・MySQL・Nginx を中心に、実務で遭遇しやすいトラブルシュート集を扱います。
