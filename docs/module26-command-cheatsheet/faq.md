# FAQ

## コマンドは暗記する必要がありますか

すべて暗記する必要はありません。よく使う基本形と、`--help`・`man`で調べる習慣を身につけます。

```bash
command --help
man command
type -a command
```

## macOSとLinuxでコマンドが違う場合はどうしますか

BSD系とGNU系でオプションが異なることがあります。OS、コマンドの実体、バージョンを確認してください。

```bash
uname -a
type -a sed
sed --version
```

## コマンド実行結果を残す方法はありますか

標準出力と標準エラーをファイルへ保存します。

```bash
command > result.txt 2>&1
command 2>&1 | tee result.txt
```

## 本番で実行してよいか迷います

読み取り専用か、変更するか、データを削除するかを分類してください。不明なコマンドは本番で試さず、検証環境で確認します。
