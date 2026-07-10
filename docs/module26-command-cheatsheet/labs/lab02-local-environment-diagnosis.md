# Lab02 ローカル環境診断

## 目的

新しいMacで開発環境が正しく構築されているか、コマンドだけで診断します。

## 確認対象

```bash
sw_vers
uname -m
brew --version
asdf --version
node -v
python --version
php -v
docker version
git --version
gh --version
```

## 課題

1. コマンドの実体を`type -a`で確認する
2. PATHを1行ずつ表示する
3. asdfの現在バージョンを確認する
4. Docker Engineへ接続する
5. ポート8081と3306の使用状況を確認する
6. 結果を診断レポートへまとめる
