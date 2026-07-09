# Module12 WordPress Cheatsheet

```bash
rg -n "get_header|get_footer|get_template_part" .
rg -n "add_action|add_filter" .
rg -n "register_post_type" .
rg -n "get_field|the_field|get_post_meta" .
```

```sql
SELECT ID, post_title, post_status
FROM wp_posts
ORDER BY ID DESC
LIMIT 20;

SELECT *
FROM wp_postmeta
WHERE post_id = 100;
```
