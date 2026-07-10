# Lesson02 学習環境の確認

## ゴール

教材を進めるために必要なコマンドとアプリが使えるか確認します。

## 確認コマンド

```bash
git --version
docker --version
docker compose version
curl --version
rg --version
code --version
python --version
node --version
```

## 推奨確認

```bash
which git
which docker
which curl
which rg
which code
```

## 確認結果テンプレート

```markdown
|Tool|Version|Path|Status|
|---|---|---|---|
|Git||||
|Docker||||
|curl||||
|ripgrep||||
|VS Code||||
|Python||||
|Node.js||||
```

## 注意

全Moduleを始める前に全ツールが必要なわけではありません。

Module01〜05では、まず次があれば進められます。

- Terminal
- Git
- curl
- ripgrep
- VS Code

## 次へ進む条件

- [ ] `git --version` が実行できる
- [ ] `curl --version` が実行できる
- [ ] `rg --version` が実行できる
- [ ] VS Codeを起動できる
