# ログのセキュリティと共有


## ログは機密情報になり得る

デバッグログには、入力値・URL・Cookie・Token・個人情報が含まれます。

## マスキング対象

- Authorization
- Cookie
- Set-Cookie
- password
- token
- secret
- email
- phone
- card number
- address
- session id

## 共有前チェック

```text
[ ] Tokenを削除
[ ] Cookieを削除
[ ] パスワードを削除
[ ] 個人情報を匿名化
[ ] 内部IP・ホスト名の扱いを確認
[ ] 必要な時間範囲だけ抜粋
[ ] 保管先の権限を確認
```

## grepで検査

```bash
rg -i 'authorization|cookie|password|token|secret' debug-bundle/
```

## マスキング例

```bash
sed -E \
  's/(Bearer )[A-Za-z0-9._-]+/\1***MASKED***/g' \
  original.log > shared.log
```

## 改ざんしない

マスキング以外の内容を変更すると、証拠としての価値が下がります。

原本を安全に保管し、共有版を別ファイルとして作ります。
