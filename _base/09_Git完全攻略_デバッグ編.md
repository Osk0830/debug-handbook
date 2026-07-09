
# 第9章 Git完全攻略（デバッグ編）

> **目的**: Gitを「ソースコード管理ツール」ではなく、「原因調査ツール」として使いこなせるようになる。

---

# この章で身につくこと

- Gitの履歴を読む
- 差分を確認する
- いつ壊れたかを特定する
- 安全に変更を戻す
- bisectで原因コミットを探す
- rebase・cherry-pickの基本

---

# Gitはデバッグツール

実務では

- いつ壊れた？
- 誰が変更した？
- 何が変わった？

を調べるためにGitを使います。

---

# 状態確認

```bash
git status
```

まず最初に実行する習慣を付けましょう。

---

# 差分

作業ツリー

```bash
git diff
```

ステージ済み

```bash
git diff --staged
```

特定ファイル

```bash
git diff app/Controller/User.php
```

---

# 履歴

```bash
git log
git log --oneline
git log --graph --decorate
git log -n 20
git log -p
```

---

# コミット内容

```bash
git show
git show HEAD
git show <commit>
```

---

# 誰が変更した？

```bash
git blame app/Controller/User.php
```

確認ポイント

- コミット
- 作者
- 日時

---

# reflog

```bash
git reflog
```

HEADの移動履歴を確認できます。

---

# restore

変更取り消し

```bash
git restore file.php
```

ステージ解除

```bash
git restore --staged file.php
```

---

# reset と revert

reset

- ローカル履歴を書き換える

revert

- 打ち消しコミットを作る

共有ブランチでは通常 `revert` を使います。

---

# stash

```bash
git stash
git stash list
git stash pop
git stash -p
```

---

# cherry-pick

```bash
git cherry-pick <commit>
```

特定コミットだけ取り込みます。

---

# rebase

```bash
git rebase -i HEAD~5
```

できること

- コミット順変更
- squash
- reword
- drop

※共有ブランチでは慎重に。

---

# bisect

```bash
git bisect start
git bisect bad
git bisect good <good_commit>
```

各ステップでテスト

```bash
git bisect good
git bisect bad
```

終了

```bash
git bisect reset
```

---

# 実務シナリオ

## 今日から500エラー

1. git log
2. git diff
3. git blame
4. git bisect

---

## CSSだけ崩れた

```bash
git diff
git log -- css/
```

---

## developだけ壊れた

```bash
git log develop
git log feature
git diff develop..feature
```

---

# ハンズオン

1. status確認
2. diff確認
3. show確認
4. blame実行
5. reflog確認
6. restore実行
7. stash作成
8. stash復元
9. rebase -i を読む
10. bisectを最後まで実施

---

# タイムアタック

30秒以内で

- 差分確認
- コミット履歴
- 誰が変更したか
- HEAD履歴
- 原因コミット候補を表示

---

# 練習問題

1. diffとshowの違い
2. blameは何に使う？
3. reflogとlogの違い
4. restoreとresetの違い
5. revertはいつ使う？
6. bisectの目的は？
7. rebaseを共有ブランチで注意する理由

---

# チェックリスト

- [ ] statusを最初に確認できる
- [ ] diffを読める
- [ ] showを使える
- [ ] blameで変更者を探せる
- [ ] reflogを確認できる
- [ ] restoreを安全に使える
- [ ] bisectで原因コミットを探せる

---

# コラム

**「いつから壊れた？」が分かれば、調査時間は劇的に短縮できます。**

推測ではなく、Gitの履歴を使って事実を積み重ねる習慣を身につけましょう。

---

# 次章予告

第10章では VS Code・Xdebug を使い、ブレークポイント・Watch・Call Stack・Conditional Breakpoint・Logpoint を使った実践デバッグを学びます。
