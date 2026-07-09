# BOOK ARCHITECTURE

## 全体構成

この教材は 20 Module 構成です。

|Module|Title|役割|
|---:|---|---|
|01|CLI|全体の土台|
|02|Linux|ファイル操作・ログ確認|
|03|ripgrep / grep / find|コード探索|
|04|HTTP|通信理解|
|05|curl|HTTP再現|
|06|Docker|環境調査|
|07|PHP Debug|PHP調査|
|08|SQL|DB事実確認|
|09|Git|履歴調査|
|10|VS Code / Xdebug|実行時デバッグ|
|11|Debug Flow|統合調査フロー|
|12|WordPress|WP案件調査|
|13|React / API|フロント・API調査|
|14|Web Server|Nginx / Apache|
|15|Mail|メール送信調査|
|16|Performance|速度改善|
|17|Troubleshooting|症状別対応|
|18|Case Study|実務ケース|
|19|Debug Drills|反復演習|
|20|Reference|チートシート|

## Module構成

各Moduleは原則として以下の構成にします。

```text
moduleXX-name/
├── README.md
├── lessons/
├── labs/
├── exercises/
├── cheatsheet.md
├── faq.md
├── troubleshooting.md
├── resources.md
└── assets/
```

## Lesson構成

各Lessonは原則として以下を含めます。

1. ゴール
2. このLessonで身につくこと
3. 実務ではいつ使う？
4. 基本
5. 実務メモ
6. よくある失敗
7. ハンズオン
8. 演習
9. 模範解答
10. FAQ
11. 学習ログ
12. 次へ進む条件

## Lab構成

Labは「実際に手を動かす」ためのページです。

1. 目的
2. 手順
3. チェックポイント
4. 発展課題
5. 記録テンプレート

## Exercise構成

Exerciseは「自分で考える」ためのページです。

1. 問題
2. ヒント
3. 解答
4. 解説
5. 実務ポイント

## Reference方針

Referenceは「困った時に最初に開く」ことを目的にします。

- コマンド索引
- 障害別フロー
- HTTPステータス表
- SQL確認表
- Git操作表
- Docker調査表

## 重要な設計方針

- 読む順番が分かる
- 後から加筆しやすい
- MkDocsで検索しやすい
- Lesson単位で改善できる
- 実案件を追加しやすい
