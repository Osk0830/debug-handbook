# Lesson09 MySQL・SQL

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## 接続

```bash
mysql -h 127.0.0.1 -P 3306 -u user -p database
mysql --protocol=TCP -h localhost -u user -p
```

**判断ポイント:** socket接続とTCP接続の違いに注意する。

## 状態確認

```sql
SELECT VERSION();
SELECT DATABASE();
SHOW TABLES;
SHOW FULL PROCESSLIST;
SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'time_zone';
```

**判断ポイント:** 接続先DB、文字コード、タイムゾーンを最初に確認する。

## データ確認

```sql
SELECT COUNT(*) FROM users;
SELECT * FROM users ORDER BY id DESC LIMIT 20;
SELECT id, email FROM users WHERE email IS NULL;
```

**判断ポイント:** 更新前に同じWHERE条件でSELECTし、対象件数を確認する。

## 実行計画

```sql
EXPLAIN SELECT * FROM users WHERE email = 'a@example.com';
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 10;
SHOW INDEX FROM users;
```

**判断ポイント:** 走査行数、使用インデックス、temporary/filesortを確認する。

## バックアップ

```bash
mysqldump -h 127.0.0.1 -u user -p database > backup.sql
mysql -h 127.0.0.1 -u user -p database < backup.sql
```

**判断ポイント:** 復元先を誤らないよう、DB名と接続先を声に出して確認する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
