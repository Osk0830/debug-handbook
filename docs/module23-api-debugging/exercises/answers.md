# Module23 Exercise Answers

## Exercise01

```bash
curl -sS \
  -D response.headers \
  -o response.body \
  http://localhost:8080/api/users
```

## Exercise02

```bash
curl -i \
  -H 'Content-Type: application/json' \
  --data @request.json \
  http://localhost:8080/api/users
```

## Exercise03

```bash
jq '.data[] | {id, email}' response.json
```

## Exercise04

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  http://localhost:8080/api/me
```

## Exercise05

```bash
curl -c cookies.txt -b cookies.txt \
  --data 'email=user@example.com&password=secret' \
  http://localhost:8080/login

curl -b cookies.txt http://localhost:8080/account
```

## Exercise06

```bash
curl -i -X OPTIONS \
  -H 'Origin: http://localhost:3000' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type,authorization' \
  http://localhost:8080/api/users
```

## Exercise08

```bash
docker compose exec app curl -i http://api:8080/health
```

## Exercise09

```bash
curl -sS -o /dev/null \
  -w 'dns=%{time_namelookup} connect=%{time_connect} ttfb=%{time_starttransfer} total=%{time_total}\n' \
  http://localhost:8080/api/users
```
