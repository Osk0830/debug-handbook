# Lab02 504とスロークエリを切り分ける

## シナリオ

一覧APIが時々504になります。

## 手順

1. Nginxの`request_time`を確認
2. `upstream_response_time`を確認
3. PHP処理開始・終了時刻を確認
4. MySQL Slow Query Logを確認
5. `SHOW FULL PROCESSLIST`を確認
6. `SHOW ENGINE INNODB STATUS`を確認
7. DockerのCPU・メモリを確認
8. 正常リクエストと比較
9. SQLの遅延と待ち時間を分離
10. 改善案を作成

## 完了条件

- Nginx timeoutとSQL遅延の関係を説明できる
- Lock wait、N+1、大量データを区別できる
- タイムアウト値を上げるだけで終わらせない
