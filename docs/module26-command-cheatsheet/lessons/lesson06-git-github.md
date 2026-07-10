# Lesson06 Git・GitHub

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## 状態と差分

```bash
git status
git diff
git diff --staged
git diff main...HEAD
git log --oneline --decorate --graph -20
```

**判断ポイント:** 変更前後とステージ済み・未ステージを分けて確認する。

## ブランチ

```bash
git branch
git switch -c feature/name
git switch main
git fetch --prune
git pull --ff-only
```

**判断ポイント:** `pull --ff-only`で意図しないマージコミットを防げる。

## コミット調査

```bash
git show COMMIT
git blame -L 20,40 path/to/file
git log -S 'keyword' -- path/to/file
git log -G 'regex' -- path/to/file
```

**判断ポイント:** `-S`は文字列の増減、`-G`は差分内容の正規表現検索。

## 取り消し

```bash
git restore path/to/file
git restore --staged path/to/file
git revert COMMIT
git reset --soft HEAD~1
```

**判断ポイント:** 共有済み履歴は原則`revert`。`reset`は影響範囲を理解して使う。

## 原因コミット

```bash
git bisect start
git bisect bad
git bisect good GOOD_COMMIT
git bisect good   # または bad
git bisect reset
```

**判断ポイント:** 再現判定を自動化できると`git bisect run`も使える。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
