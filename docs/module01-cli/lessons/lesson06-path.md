# Lesson06 相対パスと絶対パス

## ゴール

相対パスと絶対パスを説明できるようになる。

## 基本

絶対パス:

```text
/Users/song/projects/debug-handbook
```

相対パス:

```text
../docs
./README.md
```

## 記号

|表記|意味|
|---|---|
|`.`|現在のディレクトリ|
|`..`|親ディレクトリ|
|`~`|ホームディレクトリ|

## 実務ではいつ使う？

- include / require のパス確認
- Dockerのpath mapping
- Git操作
- VS Codeのデバッグ設定

## よくある失敗

ホスト側のパスとコンテナ内のパスを混同する。

例:

```text
Host: /Users/song/project
Container: /var/www/html
```

## ハンズオン

```bash
pwd
ls ./README.md
cd ..
ls ../
```

## 演習

1. `.` と `..` の違いは？
2. 絶対パスと相対パスの違いは？

## 模範解答

1. `.` は現在、`..` は親。
2. 絶対パスはルートから、相対パスは現在地から指定する。

## 次へ進む条件

- [ ] 相対パスを説明できる
- [ ] Dockerのホストパスとコンテナパスの違いを意識できる
