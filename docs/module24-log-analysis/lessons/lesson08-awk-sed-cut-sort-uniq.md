# awk・sed・cut・sort・uniq


## ステータス件数

Nginx combined形式でステータスが9列目の場合:

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

## URL別件数

```bash
awk '{print $7}' access.log | sort | uniq -c | sort -nr | head
```

## 500だけ

```bash
awk '$9 == 500 {print}' access.log
```

## IP別件数

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head
```

## cut

区切り文字が明確なログ:

```bash
cut -d',' -f1,4 app.csv
```

## sed

秘密情報をマスキング:

```bash
sed -E 's/(Authorization: Bearer )[A-Za-z0-9._-]+/\1***MASKED***/g' debug.log
```

## 注意

空白区切りのログでも、引用符内に空白があります。単純な列番号が常に正しいとは限りません。

本格的な集計ではログ形式をJSON化するか、専用パーサーを検討します。
