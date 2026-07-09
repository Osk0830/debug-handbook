
# 第1章 CLI入門

> 目的: CLIを使って実務で調査・デバッグを始められるようになる。

## この章で身につくこと

- CLIとは何か
- シェルとは何か
- pwd / ls / cd
- 相対パス・絶対パス
- 標準入力・標準出力・標準エラー
- パイプとリダイレクト
- history・which・type
- 環境変数
- 実務でのCLI活用

---

## CLIとは

CLI(Command Line Interface)は、キーボードからコマンドを入力してコンピュータを操作する仕組みです。

GUIよりも高速で再現性があり、サーバーやDocker環境でも同じ操作ができます。

---

## シェル

現在のシェル確認

```bash
echo $SHELL
```

代表例

- bash
- zsh
- fish

---

## 現在地

```bash
pwd
```

---

## 一覧表示

```bash
ls
ls -l
ls -la
ls -lah
```

---

## ディレクトリ移動

```bash
cd
cd ..
cd ../..
cd ~
cd -
```

---

## パス

絶対パス

```
/Users/username/project
```

相対パス

```
../src
```

---

## タブ補完

Tabキーで入力補完できます。

---

## 履歴

```bash
history
```

検索

```
Ctrl+r
```

---

## コマンドを調べる

```bash
man ls
ls --help
which php
type cd
```

---

## 標準入出力

```bash
ls > files.txt
ls >> files.txt
ls notfound 2> error.log
```

---

## パイプ

```bash
cat app.log | grep ERROR
rg ERROR app.log | wc -l
```

---

## 環境変数

```bash
env
printenv
echo $PATH
```

---

## 実務例

Dockerへ入る

```bash
docker compose exec web-php8 bash
```

ログ監視

```bash
tail -f storage/logs/app.log
```

PHPファイル数

```bash
find . -name "*.php" | wc -l
```

---

## ハンズオン

1. pwdを実行
2. ls -lah
3. cdで移動
4. history表示
5. Ctrl+rで検索
6. PATH表示
7. files.txtへ出力
8. catで確認

---

## 練習問題

1. pwdとlsの違い
2. cd -の意味
3. stdoutとstderrの違い
4. >と>>の違い
5. whichとtypeの違い

---

## チェックリスト

- [ ] pwdが使える
- [ ] lsオプションを理解した
- [ ] cdで迷わない
- [ ] パイプを使える
- [ ] リダイレクトを使える
- [ ] PATHを説明できる

---

## 参考

https://linuxcommand.org/

https://www.gnu.org/software/bash/manual/

https://code.visualstudio.com/docs/terminal/basics
