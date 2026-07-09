
# 第8章 MySQL・SQL 実践デバッグ

> **目的**: SQLを使って「データの事実」を確認し、アプリケーションの不具合を根拠を持って切り分けられるようになる。

---

# この章で身につくこと

- MySQLへの接続
- SELECT / INSERT / UPDATE / DELETE
- WHERE / ORDER BY / LIMIT
- JOIN
- GROUP BY / HAVING
- EXPLAIN
- インデックスの考え方
- 実務での調査フロー

---

# なぜSQLが重要なのか

バグ調査では「画面」を信じるのではなく、**DBの中身**を確認します。

例:
- 本当に保存されている？
- 更新された？
- 想定外の値が入っていない？

---

# 接続

```bash
docker compose exec db bash
mysql -u root -p
```

または

```bash
docker compose exec db mysql -uroot -p
```

---

# データベース選択

```sql
SHOW DATABASES;
USE database_name;
SHOW TABLES;
```

---

# テーブル構造

```sql
DESCRIBE users;
SHOW CREATE TABLE users;
SHOW INDEX FROM users;
```

---

# SELECT

```sql
SELECT * FROM users;
SELECT id,name FROM users;
```

条件

```sql
SELECT *
FROM users
WHERE id = 1;
```

---

# ORDER BY

```sql
SELECT *
FROM users
ORDER BY created_at DESC;
```

---

# LIMIT

```sql
SELECT *
FROM users
ORDER BY id DESC
LIMIT 10;
```

---

# INSERT

```sql
INSERT INTO users(name,email)
VALUES('Song','test@example.com');
```

---

# UPDATE

```sql
UPDATE users
SET name='ChatGPT'
WHERE id=1;
```

---

# DELETE

```sql
DELETE
FROM users
WHERE id=1;
```

---

# LIKE

```sql
SELECT *
FROM users
WHERE email LIKE '%gmail.com';
```

---

# JOIN

```sql
SELECT
u.id,
u.name,
o.id
FROM users u
INNER JOIN orders o
ON u.id=o.user_id;
```

LEFT JOIN

```sql
SELECT *
FROM users u
LEFT JOIN orders o
ON u.id=o.user_id;
```

---

# GROUP BY

```sql
SELECT
status,
COUNT(*)
FROM orders
GROUP BY status;
```

---

# HAVING

```sql
SELECT
status,
COUNT(*)
FROM orders
GROUP BY status
HAVING COUNT(*) > 10;
```

---

# EXPLAIN

```sql
EXPLAIN
SELECT *
FROM users
WHERE email='test@example.com';
```

見るポイント

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

考え方

- WHERE
- JOIN
- ORDER BY

で使う列に作成されることが多いです。

---

# 実務シナリオ

## フォーム送信後

1. 保存テーブル確認
2. 最新10件取得
3. 値を確認

```sql
SELECT *
FROM inquiry
ORDER BY id DESC
LIMIT 10;
```

---

## 「更新されない」

```sql
SELECT *
FROM users
WHERE id=100;
```

UPDATE後に再度SELECTします。

---

## 「遅い」

まず

```sql
EXPLAIN
SELECT ...
```

を確認します。

---

# Docker環境

DBへ接続

```bash
docker compose exec db mysql -uroot -p
```

---

# ハンズオン

1. SHOW DATABASES
2. SHOW TABLES
3. DESCRIBE
4. SELECT
5. WHERE
6. ORDER BY
7. LIMIT
8. JOIN
9. GROUP BY
10. EXPLAIN

---

# タイムアタック

30秒以内で

- テーブル一覧
- 最新10件
- メール検索
- インデックス確認
- EXPLAIN

---

# 練習問題

1. WHEREとHAVINGの違いは？
2. INNER JOINとLEFT JOINの違いは？
3. LIMITは何をする？
4. EXPLAINは何のため？
5. SHOW INDEXで何が分かる？
6. ORDER BY DESCとは？

---

# チェックリスト

- [ ] DBへ接続できる
- [ ] SELECTできる
- [ ] JOINを書ける
- [ ] GROUP BYを書ける
- [ ] EXPLAINを実行できる
- [ ] インデックスを確認できる

---

# コラム

**「保存されていないと思う」は禁物です。**

まずSQLで確認しましょう。

画面表示・API・キャッシュの問題なのか、DB保存の問題なのかを切り分けるだけで、調査時間は大幅に短縮できます。

---

# 次章予告

第9章では Git 完全攻略として、`diff`・`blame`・`reflog`・`restore`・`rebase`・`bisect` を使った実践的なデバッグを学びます。
