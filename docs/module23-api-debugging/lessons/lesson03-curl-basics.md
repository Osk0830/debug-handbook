# curl基礎


## GET

```bash
curl -i 'http://localhost:8080/api/users?id=123'
```

Queryを安全に組み立てる:

```bash
curl -G   --data-urlencode 'keyword=PHP デバッグ'   --data-urlencode 'page=1'   http://localhost:8080/api/search
```

## JSON POST

```bash
curl -i   -X POST   -H 'Content-Type: application/json'   --data '{"name":"Taro","email":"taro@example.com"}'   http://localhost:8080/api/users
```

ファイルから送信:

```bash
curl -i   -H 'Content-Type: application/json'   --data @request.json   http://localhost:8080/api/users
```

## フォーム

```bash
curl -i   -X POST   --data 'name=Taro'   --data 'email=taro@example.com'   http://localhost:8080/contact
```

## Multipart

```bash
curl -i   -F 'title=sample'   -F 'image=@./sample.jpg'   http://localhost:8080/api/uploads
```

## レスポンス保存

```bash
curl -sS   -D response-headers.txt   -o response-body.json   http://localhost:8080/api/users/123
```

## 終了コード確認

```bash
curl -fsS http://localhost:8080/health
echo $?
```

`-f`はHTTP 400以上を失敗として扱いますが、エラーボディ確認時には外すことがあります。
