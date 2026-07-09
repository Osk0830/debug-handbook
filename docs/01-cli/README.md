# Module 01: CLI入門

> **ゴール:** ターミナルを怖がらず、実務で調査・デバッグを始められるようになる。

---

## この章で身につくこと

この章を終えると、以下ができるようになります。

- CLIとは何か説明できる
- ターミナルとシェルの違いを説明できる
- `pwd` / `ls` / `cd` を使ってプロジェクト内を移動できる
- 相対パス・絶対パスを使い分けられる
- 標準入力・標準出力・標準エラーの意味を理解できる
- パイプ `|` とリダイレクト `>` / `>>` を使える
- `history` / `Ctrl + r` で過去のコマンドを再利用できる
- `which` / `type` / `man` / `--help` でコマンドを調べられる
- Dockerコンテナ内でも最低限のCLI操作ができる

---

## この章を学ぶ前に

必要な前提知識はほとんどありません。

ただし、次のどれかを使える状態にしておくと学習しやすいです。

- macOS標準のターミナル
- VS Codeの統合ターミナル
- iTerm2
- Git Bash
- Dockerコンテナ内のbash

---

## 実務ではいつ使う？

CLIは、ほぼすべての実務調査の入口です。

例えば、次のような場面で使います。

- Dockerコンテナの状態確認
- PHPバージョン確認
- ログ確認
- ファイル検索
- Git操作
- SQL接続
- API確認
- 本番サーバーでの障害調査

ブラウザやエディタだけで調査しようとすると、どうしても「見えている範囲」だけに頼りがちです。

CLIを使えると、**環境・ログ・通信・履歴・データ**を直接確認できます。

---

## 学習時間の目安

|項目|時間|
|---|---:|
|読む|30分|
|ハンズオン|60分|
|復習|20分|
|合計|約110分|

一度で完璧に覚える必要はありません。

毎日少しずつ打つことが大事です。

---

## まず結論: 最初に覚える3つ

CLI初心者が最初に覚えるべきコマンドはこの3つです。

```bash
pwd
ls
cd
```

この3つだけで、ターミナル上で「今どこにいるか」「何があるか」「どこへ移動するか」が分かります。

---

## CLIとは

CLIは **Command Line Interface** の略です。

GUIではボタンやメニューをクリックして操作します。

CLIでは、キーボードでコマンドを入力して操作します。

```text
GUI: Finderでフォルダを開く
CLI: cd project
```

どちらも「フォルダを開く」という目的は同じです。

違うのは操作方法です。

---

## なぜCLIを使うのか

CLIには次の利点があります。

### 1. 速い

慣れると、GUIで何度もクリックするより速く操作できます。

### 2. 再現性がある

コマンドはそのままメモやREADMEに残せます。

```bash
docker compose logs -f web-php8
```

この1行を共有すれば、他の人も同じ調査ができます。

### 3. 自動化できる

コマンドはシェルスクリプトやCI/CDに組み込めます。

### 4. サーバーでも使える

本番サーバーにはGUIがないことが多いです。

その場合、CLIが必須です。

---

## ターミナルとシェル

混同しやすいですが、ターミナルとシェルは別物です。

|用語|役割|
|---|---|
|ターミナル|文字を入力・表示するアプリ|
|シェル|入力されたコマンドを解釈して実行するプログラム|

代表的なシェル:

- bash
- zsh
- fish

現在のシェルを確認します。

```bash
echo $SHELL
```

---

## VS Code統合ターミナル

VS Codeでは、画面下部にターミナルを開けます。

ショートカット:

```text
Ctrl + `
```

macOSでも同じです。

実務では、VS Codeでコードを見ながら同じ画面でCLI調査できるため便利です。

---

## pwd: 現在地を確認する

```bash
pwd
```

`pwd` は **print working directory** の略です。

今いるディレクトリを表示します。

例:

```bash
/Users/song/projects/debug-handbook
```

### 実務ポイント

`rm` や `git` など影響の大きいコマンドを打つ前は、必ず `pwd` を確認します。

```bash
pwd
git status
```

---

## ls: 中身を見る

```bash
ls
```

よく使う形:

```bash
ls -l
ls -la
ls -lah
```

|オプション|意味|
|---|---|
|`-l`|詳細表示|
|`-a`|隠しファイルも表示|
|`-h`|サイズを読みやすく表示|

一番よく使うのはこれです。

```bash
ls -lah
```

### 見るポイント

```text
drwxr-xr-x  10 song  staff   320B Jul  9  docs
-rw-r--r--   1 song  staff   1.2K Jul  9  README.md
```

- 先頭が `d` ならディレクトリ
- 先頭が `-` ならファイル
- サイズ
- 更新日時
- ファイル名

---

## cd: 移動する

```bash
cd docs
```

親ディレクトリへ戻る:

```bash
cd ..
```

2階層戻る:

```bash
cd ../..
```

ホームへ戻る:

```bash
cd ~
```

直前の場所へ戻る:

```bash
cd -
```

### 実務ポイント

`cd -` はかなり便利です。

```bash
cd docs/01-cli
cd -
```

行ったり来たりする時に使います。

---

## 絶対パスと相対パス

### 絶対パス

ルートから始まる完全な場所です。

```bash
/Users/song/projects/debug-handbook/docs
```

### 相対パス

今いる場所を基準にした場所です。

```bash
../docs
./README.md
```

|表記|意味|
|---|---|
|`.`|現在のディレクトリ|
|`..`|親ディレクトリ|
|`~`|ホームディレクトリ|

---

## tab補完

途中まで入力して `Tab` を押すと補完できます。

例:

```bash
cd Doc<Tab>
```

存在する候補があれば補完されます。

### この章だけは絶対やる

**Tab補完を使う癖をつけてください。**

入力ミスが減ります。

長いファイル名も怖くなくなります。

---

## history: 履歴を見る

```bash
history
```

過去に打ったコマンドが表示されます。

再実行:

```bash
!123
```

ただし、最初は `!番号` の再実行は慎重に使いましょう。

---

## Ctrl + r: 履歴検索

```text
Ctrl + r
```

過去に実行したコマンドを検索できます。

例:

```text
(reverse-i-search)`docker':
```

ここで `logs` などを入力すると、過去の `docker compose logs ...` を探せます。

### 実務ポイント

長いコマンドを毎回手で打たないこと。

`Ctrl + r` で呼び出すだけでかなり速くなります。

---

## clear: 画面をクリアする

```bash
clear
```

ショートカット:

```text
Ctrl + l
```

---

## man と --help

コマンドの使い方を調べます。

```bash
man ls
```

または

```bash
ls --help
```

macOSでは `--help` がLinuxと挙動違いの場合があります。

その場合は `man` を使います。

---

## which: コマンドの実体を探す

```bash
which php
which git
which docker
```

例:

```bash
/usr/bin/git
```

---

## type: コマンドの種類を調べる

```bash
type cd
type ls
```

`cd` はシェル組み込み、`ls` は実行ファイルやaliasの場合があります。

---

## PATHとは

`PATH` は、コマンドを探す場所の一覧です。

```bash
echo $PATH
```

シェルは `PATH` に登録されたディレクトリを順番に探して、コマンドを実行します。

### よくあるトラブル

```text
command not found
```

これは、多くの場合

- インストールされていない
- PATHが通っていない
- コマンド名が違う

のどれかです。

---

## 標準入力・標準出力・標準エラー

CLIには3つの基本的な入出力があります。

|名前|番号|意味|
|---|---:|---|
|stdin|0|標準入力|
|stdout|1|標準出力|
|stderr|2|標準エラー|

普通に表示される結果は stdout です。

エラーは stderr です。

---

## リダイレクト

標準出力をファイルに保存します。

```bash
ls > files.txt
```

追記します。

```bash
ls >> files.txt
```

エラーだけ保存します。

```bash
ls not-found 2> error.log
```

標準出力とエラーを両方保存します。

```bash
command > output.log 2>&1
```

---

## パイプ

前のコマンドの結果を次のコマンドへ渡します。

```bash
ls | wc -l
```

ログからERRORだけ探す:

```bash
cat app.log | grep ERROR
```

ただし、後の章では `cat | grep` より `rg` を使う場面が増えます。

---

## ワイルドカード

```bash
*.php
*.md
*.log
```

例:

```bash
ls *.md
```

---

## クォート

スペースや特殊文字を扱う時に使います。

```bash
echo "hello world"
echo 'hello world'
```

ダブルクォートは変数展開されます。

```bash
name=Song
echo "Hello $name"
```

シングルクォートは変数展開されません。

```bash
echo 'Hello $name'
```

---

## 環境変数

一覧:

```bash
env
```

個別表示:

```bash
echo $HOME
echo $SHELL
echo $PATH
```

一時的に設定:

```bash
APP_ENV=local php script.php
```

---

## Dockerコンテナ内でCLIを使う

コンテナに入ります。

```bash
docker compose exec web-php8 bash
```

中で確認します。

```bash
pwd
ls -lah
php -v
php -m
```

### あなたへのアドバイス

あなたの案件では `web-php8` / `db` / `mailhog` のようなコンテナ名がよく出てきます。

まずは以下を毎回打てるようにしておくと強いです。

```bash
docker compose ps
docker compose exec web-php8 bash
docker compose logs -f web-php8
```

---

## 実務での使いどころ

### 1. まず現在地確認

```bash
pwd
ls -lah
git status
```

### 2. Dockerの状態確認

```bash
docker compose ps
```

### 3. ログ確認

```bash
docker compose logs -f web-php8
```

### 4. PHP確認

```bash
docker compose exec web-php8 php -v
```

---

## よくある失敗

### 失敗1: 今いる場所を確認せずに操作する

危険です。

```bash
rm -rf *
```

を打つ前に、必ず `pwd` します。

### 失敗2: 長いパスを手入力する

Tab補完を使いましょう。

### 失敗3: エラーを読まない

エラーメッセージは答えです。

読まずに検索する前に、まずそのまま読みます。

### 失敗4: GUIとCLIの現在地が違う

VS Codeで開いているフォルダと、ターミナルの現在地が違うことがあります。

```bash
pwd
```

で確認します。

---

## これだけは試してみて

この章では、最低限これだけは手を動かしてください。

```bash
pwd
ls -lah
cd ..
cd -
history
echo $SHELL
echo $PATH
which php
type cd
```

Docker環境がある場合:

```bash
docker compose ps
docker compose exec web-php8 bash
pwd
ls -lah
php -v
exit
```

---

## ハンズオン 01: プロジェクト内を移動する

### 手順

```bash
pwd
ls -lah
cd docs
pwd
ls -lah
cd ..
pwd
```

### 確認

- `pwd` の表示が変わること
- `ls` の結果が場所によって変わること

---

## ハンズオン 02: 出力をファイルに保存する

```bash
ls -lah > files.txt
cat files.txt
```

追記します。

```bash
pwd >> files.txt
cat files.txt
```

---

## ハンズオン 03: パイプを使う

```bash
ls -lah | wc -l
```

Markdownファイル数を数えます。

```bash
ls *.md | wc -l
```

---

## ハンズオン 04: エラーを保存する

```bash
ls not-found 2> error.log
cat error.log
```

---

## ハンズオン 05: Docker内で同じことをする

```bash
docker compose exec web-php8 bash
pwd
ls -lah
php -v
exit
```

---

## 実務課題

あなたの実際の案件リポジトリで、以下をメモしてください。

```markdown
## リポジトリ名

## プロジェクトルートの絶対パス

## よく使うディレクトリ

## Dockerコンテナ名

## よく見るログ

## よく使うコマンド
```

---

## 復習クイズ

### Q1

`pwd` は何の略で、何を表示しますか？

### Q2

`ls -lah` の `l` `a` `h` はそれぞれ何を意味しますか？

### Q3

`cd -` は何をしますか？

### Q4

`>` と `>>` の違いは何ですか？

### Q5

`which php` と `type php` の違いは何ですか？

### Q6

`command not found` が出た時に考える原因を3つ挙げてください。

### Q7

Dockerコンテナ内に入るコマンドを書いてください。

---

## 模範解答

### A1

`print working directory` の略で、現在いるディレクトリを表示します。

### A2

- `l`: 詳細表示
- `a`: 隠しファイルも表示
- `h`: ファイルサイズを読みやすく表示

### A3

直前にいたディレクトリへ戻ります。

### A4

- `>` は上書き
- `>>` は追記

### A5

`which` は実行ファイルの場所を探します。  
`type` はシェル組み込み・alias・実行ファイルなど、コマンドの種類も確認できます。

### A6

- インストールされていない
- PATHが通っていない
- コマンド名が違う

### A7

例:

```bash
docker compose exec web-php8 bash
```

---

## 学習ログ

```markdown
## 学習日

## 理解度
★★★★★

## 試したコマンド

## 分からなかったこと

## 実務で使えそうな場面

## 次回復習日
```

---

## この章で一番重要

**CLIは暗記ではなく、毎日打って慣れるものです。**

最初は `pwd` / `ls` / `cd` だけで十分です。

その3つが自然に使えるようになると、Docker・Git・SQL・ログ調査が一気に楽になります。

---

## 関連リンク

- [The Linux Command Line](https://linuxcommand.org/)
- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [Zsh Documentation](https://zsh.sourceforge.io/Doc/)
- [VS Code Integrated Terminal](https://code.visualstudio.com/docs/terminal/basics)
- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/)
- [Docker Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/)

---

## 次に進む条件

以下ができれば、第2章へ進んでOKです。

- [ ] `pwd` / `ls -lah` / `cd` を迷わず使える
- [ ] 相対パスと絶対パスを説明できる
- [ ] `>` / `>>` の違いを説明できる
- [ ] `history` / `Ctrl + r` を使える
- [ ] `which` / `type` でコマンドを確認できる
- [ ] Dockerコンテナ内で `pwd` / `ls` / `php -v` を実行できる