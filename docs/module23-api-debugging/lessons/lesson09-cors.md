# CORSとブラウザ固有問題


## curlで成功、ブラウザで失敗

この場合、サーバー処理ではなくCORSやブラウザ制約の可能性があります。

## Preflight

```bash
curl -i   -X OPTIONS   -H 'Origin: https://frontend.example'   -H 'Access-Control-Request-Method: POST'   -H 'Access-Control-Request-Headers: content-type,authorization'   http://localhost:8080/api/users
```

確認するレスポンス:

```text
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
Access-Control-Allow-Credentials
Access-Control-Max-Age
```

## Credentials

Cookie送信時:

```javascript
fetch(url, {
  credentials: 'include'
});
```

`Access-Control-Allow-Origin: *`とcredentialsは組み合わせられません。

## Origin

Originはscheme・host・portの組み合わせです。

```text
http://localhost:3000
http://localhost:8080
```

は別Originです。

## Networkタブ

確認:

- OPTIONSの有無
- Request Headers
- Response Headers
- blocked reason
- mixed content
- SameSite Cookie
