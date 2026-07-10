# Module26 コマンドチートシート

> デバッグ時に「何を確認したいか」からコマンドを逆引きする、Debug Handbookの最終リファレンスです。

## 学習目標

- CLI、検索、HTTP、プロセス、Docker、Git、PHP、Node.js、MySQL、ログの基本コマンドを使い分ける
- 読み取り・変更・破壊的操作を区別する
- コマンド結果を証拠として残す
- 障害時に安全な順序で調査する

## Lesson一覧

1. [CLI・ファイル・テキスト操作](lessons/lesson01-cli-files-and-text.md)
2. [検索：rg・grep・find](lessons/lesson02-search-rg-grep-find.md)
3. [HTTP・curl・ネットワーク](lessons/lesson03-http-curl-network.md)
4. [プロセス・ポート・システム](lessons/lesson04-process-port-system.md)
5. [Docker・Docker Compose](lessons/lesson05-docker-compose.md)
6. [Git・GitHub](lessons/lesson06-git-github.md)
7. [PHP・Composer・WordPress](lessons/lesson07-php-composer-wordpress.md)
8. [Node.js・フロントエンド](lessons/lesson08-node-frontend.md)
9. [MySQL・SQL](lessons/lesson09-mysql-sql.md)
10. [ログ解析・障害対応ワークフロー](lessons/lesson10-logs-incident-workflow.md)

## 補助教材

- [目的別クイックリファレンス](cheatsheet.md)
- [Lab01 障害調査コマンド実践](labs/lab01-incident-command-workflow.md)
- [Lab02 ローカル環境診断](labs/lab02-local-environment-diagnosis.md)
- [演習問題](exercises/beginner.md)
- [解答例](exercises/answers.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Resources](resources.md)

## 重要な原則

```text
確認 → 絞り込み → 記録 → 変更 → 再確認
```

`rm -rf`、`docker compose down -v`、`git reset --hard`、SQLの`UPDATE`・`DELETE`などは、
対象を確認せずに実行しないでください。
