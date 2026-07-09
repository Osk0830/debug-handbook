# Module03 FAQ

## Q. grep と rg はどちらを使えばいいですか？

普段は `rg` を優先します。高速で、`.gitignore` も考慮されます。

## Q. find と rg の違いは？

`find` はファイル名や属性を探します。`rg` はファイルの中身を探します。

## Q. vendor を除外したいです。

```bash
rg -g "!vendor" "keyword"
```
