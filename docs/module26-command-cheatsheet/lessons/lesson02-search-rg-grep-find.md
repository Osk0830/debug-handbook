# Lesson02 検索：rg・grep・find

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## プロジェクト内検索

```bash
rg 'ERROR|Exception|Fatal'
rg -n 'function_name'
rg -i 'timeout'
rg -C 3 'keyword'
rg -l 'deprecated'
```

**判断ポイント:** `rg`はGit管理対象やignore設定を考慮しながら高速検索できる。

## ファイル種類を限定

```bash
rg 'TODO' -g '*.php'
rg 'fetch\(' -g '*.{js,ts,tsx}'
rg 'password' -g '!vendor/**' -g '!node_modules/**'
```

**判断ポイント:** 検索範囲を絞るほどノイズが減り、判断が速くなる。

## grepでログ検索

```bash
grep -n 'ERROR' app.log
grep -E 'ERROR|WARN' app.log
grep -B 3 -A 5 'request_id=abc' app.log
grep -v 'healthcheck' access.log
```

**判断ポイント:** ログでは発生時刻、Request ID、URLを組み合わせる。

## findでファイル検索

```bash
find . -type f -name '*.log'
find . -type f -mtime -1
find . -type f -size +10M
find . -type d -empty
```

**判断ポイント:** `find`の`-exec rm`は、先に`-print`で対象を確認してから使う。

## 組み合わせ

```bash
find . -type f -name '*.php' -print0 | xargs -0 rg -n 'TODO'
rg -l 'oldName' | xargs sed -n '1,20p'
```

**判断ポイント:** 空白を含むパスには`-print0`と`xargs -0`を使う。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
