# Lesson09 リダイレクト

## ゴール

コマンドの出力をファイルへ保存できるようになる。

## 基本

```bash
ls > files.txt
ls >> files.txt
ls not-found 2> error.log
command > output.log 2>&1
```

## 違い

|記号|意味|
|---|---|
|`>`|上書き|
|`>>`|追記|
|`2>`|標準エラーを保存|
|`2>&1`|標準エラーを標準出力へまとめる|

## 実務ではいつ使う？

- 調査ログを残す
- 実行結果を共有する
- エラー内容を保存する

## ハンズオン

```bash
ls -lah > files.txt
cat files.txt
pwd >> files.txt
cat files.txt
```

## 演習

1. `>` と `>>` の違いは？
2. エラーだけ保存するには？

## 模範解答

1. 上書きと追記。
2. `2> error.log`

## 次へ進む条件

- [ ] 出力とエラーを保存できる
