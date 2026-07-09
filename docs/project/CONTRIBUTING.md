# CONTRIBUTING

## 基本方針

この教材は、まず全体を作成し、その後に学習しながら改善していきます。

## 更新の流れ

1. 学習する
2. 分からない箇所をメモする
3. 該当Lessonに追記する
4. FAQまたはTroubleshootingにも必要なら追加する
5. コミットする

## コミット単位

おすすめの単位:

- Module単位
- Lesson単位
- FAQ追加
- Case Study追加
- MkDocs設定修正

## コミット例

```bash
git add .
git commit -m "Expand Module01 CLI pwd lesson"
git push
```

```bash
git add .
git commit -m "Add WordPress form debugging case study"
git push
```

## 追記先の判断

|追加したい内容|追記先|
|---|---|
|理解補足|該当Lesson|
|よくある質問|faq.md|
|症状別対応|troubleshooting.md|
|コマンド|cheatsheet.md|
|実案件|case study|
|全体方針|docs/project/PROJECT.md|
|書き方ルール|docs/project/STYLE_GUIDE.md|

## 注意

- 危険なコマンドには注意書きを入れる
- 本番情報・秘密情報・認証情報は書かない
- 実案件の内容は個人情報や社名を伏せる
- コマンドはコピペ可能にする
