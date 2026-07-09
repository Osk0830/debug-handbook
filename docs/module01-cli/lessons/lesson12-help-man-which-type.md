# Lesson12 コマンドの調べ方

## ゴール

分からないコマンドを自分で調べられるようになる。

## 基本

```bash
man ls
ls --help
which php
type cd
```

## 実務ではいつ使う？

- オプションを確認する
- コマンドの場所を確認する
- aliasや組み込みコマンドを見分ける

## which と type

```bash
which php
type php
type cd
```

`type` は、alias・シェル組み込み・実行ファイルの違いも確認できます。

## ハンズオン

```bash
which git
type git
type cd
```

## 演習

1. `which` は何をしますか？
2. `type` が便利な理由は？

## 模範解答

1. 実行ファイルの場所を表示する。
2. コマンドの種類まで分かる。

## 次へ進む条件

- [ ] `which` と `type` を使い分けられる
