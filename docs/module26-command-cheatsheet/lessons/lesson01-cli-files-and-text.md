# Lesson01 CLI・ファイル・テキスト操作

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## 現在地と一覧

```bash
pwd
ls -la
ls -lah
tree -L 2
```

**判断ポイント:** 作業対象を誤らないため、破壊的操作の前に必ず現在地と対象を確認する。

## ファイルの確認

```bash
file path/to/file
stat path/to/file
wc -l path/to/file
head -n 20 path/to/file
tail -n 50 path/to/file
```

**判断ポイント:** `file`で形式、`stat`で時刻・権限、`wc`で規模を把握する。

## コピー・移動・削除

```bash
cp -iv source target
cp -a source_dir backup_dir
mv -iv old new
rm -i file
rm -rf directory
```

**判断ポイント:** `rm -rf`は最終手段。実行前に`pwd`と`ls`で対象を確認する。

## 差分確認

```bash
diff -u before.txt after.txt
cmp file1 file2
comm -3 <(sort a.txt) <(sort b.txt)
```

**判断ポイント:** 内容差分には`diff -u`、バイナリ同一性には`cmp`を使う。

## テキスト加工

```bash
sort input.txt
sort input.txt | uniq -c | sort -nr
cut -d, -f1,3 data.csv
tr '[:lower:]' '[:upper:]'
sed -n '20,40p' file.txt
awk '{print $1, $NF}' file.txt
```

**判断ポイント:** 元ファイルを書き換える前に、まず標準出力で結果を確認する。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
