# APIデバッグ チートシート

## GET

```bash
curl -i 'http://localhost:8080/api/users?id=123'
```

## JSON POST

```bash
curl -i \
  -H 'Content-Type: application/json' \
  --data @request.json \
  http://localhost:8080/api/users
```

## HeadersとBodyを分離

```bash
curl -sS \
  -D response.headers \
  -o response.body \
  http://localhost:8080/api/users
```

## 詳細

```bash
curl -v http://localhost:8080/api/users
```

## Timing

```bash
curl -sS -o /dev/null \
  -w 'status=%{http_code} connect=%{time_connect} ttfb=%{time_starttransfer} total=%{time_total}\n' \
  http://localhost:8080/api/users
```

## JSON

```bash
jq . response.json
jq -S . response.json
jq '.data[] | {id, name}' response.json
```

## Bearer

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" http://localhost:8080/api/me
```

## Cookie

```bash
curl -c cookies.txt -b cookies.txt http://localhost:8080/login
```

## CORS preflight

```bash
curl -i -X OPTIONS \
  -H 'Origin: http://localhost:3000' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type,authorization' \
  http://localhost:8080/api/users
```

## Docker

```bash
docker compose exec app curl -v http://api:8080/health
```

## 確認順序

```text
URL
→ Method
→ Headers
→ Body
→ Status
→ Response Headers
→ Response Body
→ Request ID
→ Server Log
→ Upstream
```
