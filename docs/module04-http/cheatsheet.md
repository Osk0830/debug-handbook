# Module04 HTTP チートシート

## よく見るステータス

|Code|意味|最初に見る場所|
|---:|---|---|
|200|成功|Response|
|301|恒久リダイレクト|Location|
|302|一時リダイレクト|Cookie / Session / Location|
|400|リクエスト不正|Payload|
|401|認証必要|Authorization|
|403|権限なし|認証・権限|
|404|見つからない|URL / Route / Rewrite|
|405|Method不正|GET / POST|
|500|サーバーエラー|PHPログ|
|502|Bad Gateway|PHP-FPM / Web Server|
|503|停止|Docker / Web Server|

## Networkで見るもの

- Method
- URL
- Status
- Request Headers
- Response Headers
- Payload
- Response
- Timing
