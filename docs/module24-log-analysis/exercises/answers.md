# Module24 Exercise Answers

## Exercise01

```bash
tail -n 100 app.log
tail -F app.log
```

## Exercise02

```bash
rg -C 3 'ERROR' app.log
```

## Exercise03

```bash
zgrep 'PDOException' app.log.2.gz
```

## Exercise04

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

## Exercise05

```bash
jq -c 'select(.level == "error")' app.jsonl
```

## Exercise06

```bash
rg 'req-123' logs/
```

## Exercise07

```bash
docker compose logs -f -t nginx app db
```

## Exercise08

```sql
SHOW FULL PROCESSLIST;
SHOW ENGINE INNODB STATUS\G
```

## Exercise09

```bash
sed -E \
  's/(Bearer )[A-Za-z0-9._-]+/\1***MASKED***/g' \
  original.log > shared.log
```

## Exercise10

まず14:18〜14:22程度を対象にし、Access Log、Error Log、Application Log、DB・外部APIログの順にRequest IDで横断します。
