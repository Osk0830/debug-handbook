# Exercise 01: CLI入門

## 課題1

プロジェクトルートで以下を実行してください。

```bash
pwd
ls -lah
```

結果から分かったことを書いてください。

## 課題2

`docs/01-cli` へ移動し、戻ってください。

```bash
cd docs/01-cli
pwd
cd -
pwd
```

## 課題3

ファイル一覧を `files.txt` に保存してください。

```bash
ls -lah > files.txt
cat files.txt
```

## 課題4

存在しないファイルを参照して、エラーを `error.log` に保存してください。

```bash
ls not-found 2> error.log
cat error.log
```