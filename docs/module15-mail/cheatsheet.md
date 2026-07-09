# Module15 Mail Cheatsheet

```bash
rg -n "mail|send|PHPMailer|SMTP|subject|Body" .
docker compose logs -f mailhog
docker compose logs -f web-php8
```

MailHog:

```text
http://localhost:8025
```

## 調査順

```text
POST
  ↓
PHP処理
  ↓
Mail処理
  ↓
MailHog
  ↓
SMTP
  ↓
受信環境
```
