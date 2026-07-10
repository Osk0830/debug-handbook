# ログ解析 Troubleshooting

## ログが見つからない

1. 実行中プロセスを確認
2. 設定ファイルを確認
3. stdout / stderrを確認
4. Docker / systemdを確認
5. volumeを確認
6. ローテーション済みファイルを確認
7. 権限を確認

## ログはあるが原因が分からない

```text
時刻
→ Request ID
→ 前後行
→ Call Stack
→ 下流サービス
→ 正常時比較
```

## 断続的障害

- 複数インスタンス
- 特定コンテナ
- 特定データ
- 負荷
- Rate Limit
- DB Lock
- 外部API
- Cache
- 再起動

インスタンス名・コンテナID・ホスト名もログへ含めます。

## ログが大きすぎる

- 時間範囲を狭める
- `rg`で識別子検索
- `zgrep`で圧縮ログ検索
- `awk`で必要列だけ抽出
- 一時ファイルへ絞り込み結果を保存

詳細は[Lesson01](lessons/lesson01-log-analysis-overview.md)と[Lesson16](lessons/lesson16-capstone.md)を参照してください。
