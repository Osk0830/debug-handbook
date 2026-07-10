# Module22 Exercise Answers

## Exercise02

```text
Browser
  │ HTTP
  ▼
Web Server
  ▼
PHP + Xdebug
  │ DBGp / TCP 9003
  ▼
VS Code PHP Debug
```

## Exercise03

```ini
[xdebug]
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=127.0.0.1
xdebug.client_port=9003
```

## Exercise04

```ini
[xdebug]
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=host.docker.internal
xdebug.client_port=9003
```

## Exercise05

```json
{
  "pathMappings": {
    "/var/www/html": "${workspaceFolder}"
  }
}
```

## Exercise06

- Step Over: 呼び出し先へ入らず次の行へ進む
- Step Into: 呼び出し先の関数・メソッドへ入る
- Step Out: 現在の関数を抜けて呼び出し元へ戻る

## Exercise07

```php
count($items)
json_last_error_msg()
$_SERVER['REQUEST_URI'] ?? null
$_SESSION['user_id'] ?? null
get_debug_type($value)
```

## Exercise08

```php
$id === 123 && $retryCount >= 2
```

## Exercise10

```text
対象コード
→ Xdebug読み込み
→ mode
→ 開始条件
→ VS Code待受
→ ホスト名
→ ポート
→ pathMappings
→ 実行可能行
```
