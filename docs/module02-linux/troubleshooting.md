# Module02 Troubleshooting

## ファイルが見つからない

```bash
pwd
ls -lah
find . -name "filename"
```

## 権限エラー

```bash
ls -lah
chmod 644 file.php
chmod 755 script.sh
```

## ログが見つからない

```bash
find . -name "*.log"
docker compose logs -f web-php8
```
