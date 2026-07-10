# MySQLログ・スロークエリ


## 状態確認

```sql
SHOW VARIABLES LIKE 'slow_query_log';
SHOW VARIABLES LIKE 'slow_query_log_file';
SHOW VARIABLES LIKE 'long_query_time';
SHOW GLOBAL STATUS LIKE 'Slow_queries';
```

## 実行中SQL

```sql
SHOW FULL PROCESSLIST;
```

## InnoDB

```sql
SHOW ENGINE INNODB STATUS\G
```

確認:

- deadlock
- lock wait
- transaction
- buffer pool
- latest foreign key error

## Slow Query Log

```bash
mysqldumpslow /path/to/slow.log
```

代表オプション:

```bash
mysqldumpslow -s t -t 20 /path/to/slow.log
```

## Docker

```bash
docker compose logs db
docker compose exec db mysql -e "SHOW FULL PROCESSLIST"
```

## 注意

General Logは大量出力・性能影響があります。常時有効にせず、調査目的と時間範囲を限定します。

## SQLだけで完結しない

遅いSQLの前に、アプリが同じSQLを何百回も発行していることがあります。Request ID・処理名・件数と合わせて調査します。
