# tail・lessでログを読む


## 末尾を確認

```bash
tail -n 100 app.log
```

リアルタイム追跡:

```bash
tail -f app.log
```

ファイル再作成にも追従:

```bash
tail -F app.log
```

ログローテーションがある環境では`-F`が便利です。

## 複数ファイル

```bash
tail -F nginx-access.log php-error.log
```

## less

```bash
less app.log
```

便利な操作:

| キー | 動作 |
|---|---|
| `/error` | 前方検索 |
| `?error` | 後方検索 |
| `n` | 次の一致 |
| `N` | 前の一致 |
| `G` | 末尾 |
| `g` | 先頭 |
| `F` | 追跡モード |
| `Ctrl+C` | 追跡解除 |
| `q` | 終了 |

## 長い1行

JSONログなどは横スクロールしやすくします。

```bash
less -S app.log
```

## 圧縮ログ

```bash
zless app.log.2.gz
zgrep 'ERROR' app.log.2.gz
```

## 最初から全量を開かない

時間・識別子・エラー語で絞ってから読みます。

```bash
rg '2026-07-10 14:3[0-9]' app.log
```
