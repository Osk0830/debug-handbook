# Answers

## 1

```bash
lsof -nP -iTCP:8081 -sTCP:LISTEN
```

## 2

```bash
docker compose logs --since=30m > docker-logs.txt 2>&1
```

## 3

```bash
rg -n 'TODO' -g '*.php'
```

## 4

```bash
curl -o /dev/null -sS -w 'status=%{http_code} total=%{time_total}\n' URL
```

## 5

```bash
git log -S 'keyword' --oneline
```

## 6

```bash
find . -type f -name '*.log' -size +10M -print
```

## 7

```sql
SELECT DATABASE(), VERSION();
```

## 8

```bash
pnpm why PACKAGE
```

## 9

```bash
zgrep ' 500 ' access.log.1.gz
```

## 10

```bash
{
  date
  git rev-parse HEAD
  docker compose ps
  docker compose logs --since=30m
} > incident-evidence.txt 2>&1
```
