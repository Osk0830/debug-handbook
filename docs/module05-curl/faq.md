# Module05 FAQ

## Q. `-I` と `-i` の違いは？

`-I` はヘッダーだけ取得します。`-i` は本文にヘッダーも含めて表示します。

## Q. 302の遷移先を見るには？

```bash
curl -I URL
```

または

```bash
curl -L -I URL
```

## Q. Cookieを保持するには？

```bash
curl -c cookie.txt URL
curl -b cookie.txt URL
```
