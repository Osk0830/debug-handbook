# 総合演習


## 症状

14:20頃、注文APIが一部ユーザーだけ504になりました。

構成:

```text
Nginx
→ PHP API
→ MySQL
→ External Payment API
```

## 与えられた情報

- ユーザー報告時刻: 14:20 JST
- URL: `POST /api/orders`
- Nginx status: 504
- Request ID: `req-7f3a`
- 再現率: 約10%

## 課題

1. JSTとUTCを確認する
2. Nginx access logからRequest IDを探す
3. Nginx error logの前後を確認する
4. PHPログをRequest IDで検索する
5. 外部API開始・終了ログを確認する
6. MySQL slow logを同時刻で確認する
7. 正常リクエストと時間を比較する
8. どの区間で時間を消費したか示す
9. 秘密情報をマスキングした調査資料を作る
10. 再発防止策を提案する

## 期待する時系列例

```text
14:20:00.100 Nginx request accepted
14:20:00.140 PHP order processing started
14:20:00.300 MySQL completed
14:20:00.350 Payment API started
14:20:30.350 Upstream timeout
14:20:30.351 Nginx 504
```

## 完了条件

- 複数ログから1本の時系列を作れる
- 504の発生場所と根本原因を区別できる
- 正常系との差分を説明できる
- 安全な共有用ログを作れる
