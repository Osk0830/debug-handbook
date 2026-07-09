# Module03 検索チートシート

```bash
find . -name "*.php"
find . -name "*.log"
find . -type d
find . -size +10M

grep -R "execute" .
grep -n "PDO" config.php
grep -i "error" app.log

rg -n "execute"
rg -i "mail"
rg --glob "*.php" "PDO"
rg -g "!vendor" "register_post_type"
rg -C 3 "INSERT"
rg --files | rg "\.php$"
```
