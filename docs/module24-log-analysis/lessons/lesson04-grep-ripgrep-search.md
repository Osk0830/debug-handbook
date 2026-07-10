# grep・ripgrepで絞り込む


## 基本検索

```bash
grep 'ERROR' app.log
rg 'ERROR' app.log
```

## 大文字小文字を無視

```bash
rg -i 'error|exception|fatal' app.log
```

## 前後行

```bash
grep -C 3 'request-id-123' app.log
rg -C 3 'request-id-123' app.log
```

## 行番号

```bash
rg -n 'PDOException' app.log
```

## 複数ファイル

```bash
rg 'request-id-123' logs/
```

## 除外

```bash
rg 'ERROR' logs/ -g '!access.log'
```

## 完全一致に近づける

```bash
rg '\b500\b' access.log
```

単純な`500`ではURLやサイズにも一致する可能性があります。

## 固定文字列

```bash
rg -F '[payment.failed]' app.log
```

## 検索条件を段階化する

```text
日付
→ URL
→ ステータス
→ Request ID
→ 例外名
→ 対象ID
```

一度に複雑な正規表現を書かず、結果を見ながら狭めます。
