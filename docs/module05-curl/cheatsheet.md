# Module05 curl チートシート

```bash
curl URL
curl -I URL
curl -i URL
curl -v URL
curl -L URL
curl -o result.html URL
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" --data "name=Test&email=test@example.com" URL
curl -H "Content-Type: application/json" -d '{"name":"Test"}' URL
curl -c cookie.txt URL
curl -b cookie.txt URL
curl -s -o /dev/null -w "%{http_code} %{time_total}\n" URL
```
