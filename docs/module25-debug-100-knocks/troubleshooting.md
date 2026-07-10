# Module25 Troubleshooting

## 調査が行き詰まったとき

1. 期待値と実際値を再確認する
2. 再現手順を最小化する
3. 正常ケースとの差分を一つだけ探す
4. レイヤーを分ける
5. 仮説を文章にする
6. 変更を戻して観測し直す

## レイヤー分解

```text
Browser
→ Network
→ Web Server
→ Application
→ Database
→ External Service
```

各境界で「入力」と「出力」を確認します。
