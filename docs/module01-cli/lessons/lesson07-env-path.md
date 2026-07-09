# Lesson07 環境変数とPATH

## ゴール

環境変数とPATHの役割を理解する。

## 基本

```bash
env
printenv
echo $PATH
echo $HOME
echo $SHELL
```

## PATHとは

シェルがコマンドを探すディレクトリ一覧です。

## 実務ではいつ使う？

- `command not found` の調査
- PHP / Composer / Node の場所確認
- Dockerコンテナ内の環境確認

## よくある失敗

インストール済みなのに `command not found` が出る場合、PATHが通っていない可能性があります。

## ハンズオン

```bash
echo $PATH
which php
which git
```

## 演習

1. PATHは何のためにありますか？
2. `command not found` の原因を3つ挙げてください。

## 模範解答

1. コマンドを探す場所を指定するため。
2. 未インストール、PATH未設定、コマンド名ミス。

## 次へ進む条件

- [ ] `echo $PATH` を実行できる
- [ ] `which` と組み合わせて調査できる
