# Module03 Troubleshooting

## 検索結果が多すぎる

```bash
rg --glob "*.php" "keyword"
rg -g "!vendor" "keyword"
```

## 隠しファイルも検索したい

```bash
rg --hidden "keyword"
```

## .gitignore対象も検索したい

```bash
rg -uu "keyword"
```
