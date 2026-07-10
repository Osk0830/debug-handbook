# Module24 ログ解析

障害時のログを、時刻・Request ID・サービス間の関係から読み解くための実践Moduleです。

## 学習目標

- ログの所在を設定から確認できる
- tail・less・grep・ripgrepを使い分けられる
- awk・sed・sort・uniqで集計できる
- jqで構造化ログを解析できる
- タイムゾーンをそろえて時系列を作れる
- Request IDで複数サービスを横断できる
- PHP、Nginx、Apache、Docker、MySQLのログを調べられる
- ローテーション・保持・マスキングを設計できる

## Lesson一覧

- [ログ解析の全体像](lessons/lesson01-log-analysis-overview.md)
- [ログの場所と情報源](lessons/lesson02-log-locations-and-sources.md)
- [tail・lessでログを読む](lessons/lesson03-tail-less-follow.md)
- [grep・ripgrepで絞り込む](lessons/lesson04-grep-ripgrep-search.md)
- [ログ形式を読み解く](lessons/lesson05-log-format-reading.md)
- [時刻・タイムゾーン・相関](lessons/lesson06-time-timezone-correlation.md)
- [Request ID・Trace IDでログをつなぐ](lessons/lesson07-request-id-trace-id.md)
- [awk・sed・cut・sort・uniq](lessons/lesson08-awk-sed-cut-sort-uniq.md)
- [jqで構造化ログを解析する](lessons/lesson09-jq-structured-logs.md)
- [PHP・アプリケーションログ](lessons/lesson10-php-application-logs.md)
- [Nginx・Apacheログ解析](lessons/lesson11-nginx-apache-logs.md)
- [Docker・journalctl・システムログ](lessons/lesson12-docker-journalctl-system-logs.md)
- [MySQLログ・スロークエリ](lessons/lesson13-mysql-slow-query-logs.md)
- [ログローテーションと保持](lessons/lesson14-log-rotation-retention.md)
- [ログのセキュリティと共有](lessons/lesson15-security-masking-and-sharing.md)
- [総合演習](lessons/lesson16-capstone.md)

## 補助教材

- [Lab01 500エラーを複数ログから追跡する](labs/lab01-trace-http-500.md)
- [Lab02 504とスロークエリを切り分ける](labs/lab02-timeout-and-slow-query.md)
- [Beginner Exercises](exercises/beginner.md)
- [Answers](exercises/answers.md)
- [Cheatsheet](cheatsheet.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)

## 学習の原則

```text
時刻を固定
→ 入口ログ
→ 識別子
→ 関連ログ
→ 正常比較
→ 原因
→ 再発防止
```
