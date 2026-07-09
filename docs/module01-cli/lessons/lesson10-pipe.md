# Lesson10 パイプ

## ゴール

コマンドの結果を次のコマンドへ渡せるようになる。

## 基本

```bash
ls | wc -l
cat app.log | grep ERROR
```

## 実務ではいつ使う？

- ログの絞り込み
- 件数カウント
- コマンド結果の加工

## よく使う組み合わせ

```bash
history | grep docker
ls -lah | wc -l
```

## ハンズオン

```bash
ls | wc -l
history | grep cd
```

## 演習

1. パイプは何をしますか？
2. `ls | wc -l` は何を数えますか？

## 模範解答

1. 前の出力を次の入力へ渡す。
2. `ls` の出力行数。

## 次へ進む条件

- [ ] パイプを使って件数を数えられる
