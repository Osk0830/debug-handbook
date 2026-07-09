# Module16 Performance Cheatsheet

## curl計測

```bash
curl -s -o /dev/null \
  -w "status:%{http_code}\nTTFB:%{time_starttransfer}\nTotal:%{time_total}\n" \
  http://localhost:8081/
```

## SQL

```sql
EXPLAIN
SELECT *
FROM users
WHERE email = 'test@example.com';

SHOW INDEX FROM users;
```

## Docker

```bash
docker stats
```

## 調査順

```text
Browser
  ↓
Network
  ↓
curl
  ↓
PHP
  ↓
SQL
  ↓
Docker Resource
```
