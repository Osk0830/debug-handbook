# ログ解析の全体像


ログ解析の目的は、文字列を眺めることではありません。

**障害が発生した時刻・処理・入力・サービス間の関係を、証拠から再構成すること**です。

```text
User Request
  ↓
Load Balancer / CDN
  ↓
Nginx / Apache
  ↓
PHP Application
  ↓
Database / Cache / External API
```

## 最初に固定する情報

- 発生日時
- タイムゾーン
- 対象URL・処理名
- ユーザーまたは対象データ
- HTTPステータス
- Request ID / Trace ID
- 対象環境
- 再現率
- 正常時との違い

## 基本フロー

```text
症状を言語化
→ 時間範囲を絞る
→ 入口ログを探す
→ 識別子を得る
→ 関連ログを横断する
→ 正常と異常を比較
→ 根本原因を特定
→ 再発防止へ反映
```

## ログの種類

| 種類 | 主な用途 |
|---|---|
| Access Log | 誰がいつ何へアクセスしたか |
| Error Log | サーバー・アプリの異常 |
| Application Log | 業務処理・例外・状態 |
| Audit Log | 誰が何を変更したか |
| Database Log | SQL・接続・遅延 |
| Container Log | stdout / stderr |
| System Log | OS・サービス・カーネル |
| Security Log | 認証・拒否・攻撃兆候 |

## 原則

- 推測より時刻と識別子
- 1行だけで判断しない
- 前後関係を見る
- 正常系と比較する
- タイムゾーンを明示する
- 秘密情報を共有しない
