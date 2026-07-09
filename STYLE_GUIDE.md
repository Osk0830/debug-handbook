# STYLE_GUIDE.md

## ファイル命名

- module: `module01-cli`
- lesson: `lesson01-what-is-cli.md`
- lab: `lab01-terminal-basics.md`
- exercise: `beginner.md`, `intermediate.md`, `advanced.md`, `answers.md`

## 見出しルール

- `#` はページタイトルのみ
- `##` は主要セクション
- `###` は補足セクション

## コードブロック

コマンドは必ず fenced code block を使います。

```bash
pwd
ls -lah
```

SQLは `sql`、JavaScriptは `js`、PHPは `php` を指定します。

## 各Lessonの推奨構成

1. ゴール
2. このLessonで身につくこと
3. 実務ではいつ使う？
4. 基本
5. なぜそうなる？
6. よくある失敗
7. ハンズオン
8. 演習
9. 模範解答
10. FAQ
11. 関連リンク
12. 学習ログ
13. 次へ進む条件

## コラム表記

実務的な補足は以下のように書きます。

> **実務メモ**
> ここに補足を書く。

## 注意表記

危険な操作は明確に警告します。

> **注意**
> `rm -rf` は実行前に必ず `pwd` を確認します。
