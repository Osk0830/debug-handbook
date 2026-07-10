# ログローテーションと保持


## なぜ必要か

ログを無制限に残すとディスクを圧迫し、サービス停止につながります。

## logrotate

設定例:

```conf
/var/log/myapp/*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
```

## copytruncateの注意

アプリを再起動せずローテーションできますが、切り替え中にログ欠落の可能性があります。

可能なら、アプリへシグナルを送りファイルを開き直す方式を検討します。

## Docker

Docker logging driverのローテーション例:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "5"
  }
}
```

## 保持期間

決める要素:

- 障害調査期間
- 法令・契約
- 個人情報
- ストレージ費用
- セキュリティ
- 監査要件

## ローテーション確認

```bash
logrotate -d /etc/logrotate.conf
```

実行前にdry-run相当で確認します。
