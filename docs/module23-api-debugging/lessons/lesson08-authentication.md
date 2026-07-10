# 認証・認可のデバッグ


## Basic認証

```bash
curl -i -u 'demo:demo' http://localhost:8080/private
```

## Bearer Token

```bash
curl -i   -H "Authorization: Bearer $ACCESS_TOKEN"   http://localhost:8080/api/me
```

## Cookie

```bash
curl -c cookies.txt -b cookies.txt   -X POST   --data 'email=user@example.com&password=secret'   http://localhost:8080/login
```

続けて:

```bash
curl -b cookies.txt http://localhost:8080/account
```

## 401と403

- 401: 認証できていない
- 403: 認証済みだが権限不足

## JWTの確認項目

- issuer
- audience
- subject
- expiration
- not before
- signature
- key rotation
- clock skew

トークンをオンラインの第三者サービスへ貼り付けないでください。

## CSRF

Cookie認証の更新系リクエストでは、CSRFトークンが必要なことがあります。

確認:

- Cookie
- hidden field
- custom header
- SameSite属性
- Origin / Referer
