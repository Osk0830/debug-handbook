# Lesson10 ログ解析・障害対応ワークフロー

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## ログ追跡

```bash
tail -f app.log
tail -n 200 app.log
rg -n 'ERROR|Exception|Fatal' logs/
rg -C 5 'request_id=abc123' logs/
```

**判断ポイント:** 時刻、Request ID、ユーザー、URLを軸に追う。

## 集計

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
rg -o 'status=[0-9]+' app.log | sort | uniq -c
cut -d' ' -f1 access.log | sort | uniq -c | sort -nr | head
```

**判断ポイント:** 形式が固定されたログでのみ列番号を信用する。

## 圧縮ログ

```bash
zgrep 'ERROR' app.log.1.gz
zcat access.log.*.gz | rg ' 500 '
gzcat access.log.1.gz | head   # macOS
```

**判断ポイント:** ローテーション済みログも調査対象に含める。

## 障害時の証拠保存

```bash
date
git rev-parse HEAD
docker compose ps
docker compose logs --since=30m > incident-logs.txt
curl -sS -D headers.txt -o body.txt URL
```

**判断ポイント:** 修正や再起動の前に、消える可能性がある証拠を保存する。

## 安全な調査順

```text
1. 影響範囲を確認
2. 発生時刻と直前変更を確認
3. ログ・メトリクス・リクエストを保存
4. レイヤーを切り分け
5. 暫定復旧
6. 原因修正
7. 再発確認と共有
```

**判断ポイント:** 復旧を優先する場面と、原因調査を優先する場面を区別する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
