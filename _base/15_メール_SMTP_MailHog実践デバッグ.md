
# 第15章 メール・SMTP・MailHog実践デバッグ

> **目的**: 「メールが届かない」を論理的に切り分け、送信処理からSMTPまで調査できるようになる。

---

# この章で身につくこと

- メール送信の流れ
- SMTPの基本
- MailHogの使い方
- PHPからのメール送信確認
- PHPMailerの調査
- SMTP設定の確認
- メールデバッグの手順

---

# メール送信の流れ

```text
Browser
 ↓
PHP
 ↓
Mailer(PHPMailer等)
 ↓
SMTP
 ↓
MailHog / Mail Server
 ↓
受信者
```

---

# SMTPとは

SMTP(Simple Mail Transfer Protocol)はメール送信のためのプロトコルです。

主な設定項目

- Host
- Port
- Username
- Password
- Encryption(TLS/SSL)

---

# MailHog

ローカル開発ではMailHogを利用することが多いです。

確認画面

```text
http://localhost:8025
```

確認項目

- 件名
- 宛先
- 差出人
- 本文
- 添付ファイル

---

# コード検索

送信処理

```bash
rg -n "mail|send|PHPMailer|SMTP|subject|Body" .
```

---

# ログ確認

```bash
docker compose logs -f mailhog
docker compose logs -f web-php8
```

---

# PHP設定

```bash
php -i | rg sendmail
php -m
```

---

# curlでフォーム再現

```bash
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
--data "name=Test&email=test@example.com" \
http://localhost:8081/wedding/inquiry/confirm.php
```

---

# 実務シナリオ

## DB保存されるがメールだけ届かない

確認順

1. curlで再現
2. PHPログ
3. Mail送信処理へ到達しているか
4. MailHog
5. SMTP設定

---

## MailHogに届かない

確認

```bash
docker compose ps
docker compose logs -f mailhog
```

---

## 本番だけ届かない

確認

- SMTP Host
- Port
- TLS
- 認証情報
- SPF
- DKIM
- DMARC

---

# よくある原因

- 宛先が空
- SMTP認証失敗
- ポート違い
- TLS設定違い
- 添付サイズ超過
- バリデーションで送信されていない

---

# ハンズオン

1. MailHogを開く
2. curlでフォーム送信
3. MailHogで確認
4. 件名確認
5. 宛先確認
6. 本文確認
7. docker logs確認
8. rgで送信処理検索
9. SMTP設定確認
10. Xdebugで送信直前停止

---

# タイムアタック

30分以内で

- Mail送信処理を探す
- MailHog確認
- SMTP設定確認
- curl再現
- ログ確認

---

# 練習問題

1. MailHogの役割は？
2. SMTPとは？
3. DB保存されるのにメールだけ届かない場合の調査順は？
4. rgで送信処理を探すコマンドを書いてください。
5. 本番だけ届かない原因を3つ挙げてください。

---

# チェックリスト

- [ ] MailHogを確認できる
- [ ] SMTP設定を理解した
- [ ] ログを確認できる
- [ ] curlで送信再現できる
- [ ] メール処理を検索できる

---

# コラム

メール障害は「送信されていない」のか、「送信されたが届いていない」のかを最初に切り分けることが重要です。

まずはPHPの処理、次にSMTP、最後に受信環境を確認しましょう。

---

# 次章予告

第16章ではパフォーマンス改善・SQL高速化・N+1問題・キャッシュ・プロファイリングを学びます。
