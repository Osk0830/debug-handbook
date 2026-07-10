
# Lesson06 Search 完全攻略（Part1）

> **Module21 VS Code実践**

## ゴール

このLessonでは VS Code の Search を使って、
「コードを読む」のではなく「目的のコードへ最短で到達する」ための考え方を身につけます。

このPartでは以下を扱います。

- Search View
- Explorerとの違い
- Include / Exclude
- 大規模案件での検索戦略
- WordPress・React・PHP案件での検索例

---

# なぜSearchが重要なのか

初心者は Explorer を開いて順番にファイルを読もうとします。

```
index.php
 ↓
require
 ↓
include
 ↓
また読む
```

実務ではほぼ逆です。

```
Search
 ↓
候補抽出
 ↓
絞り込み
 ↓
該当ファイル
 ↓
Debugger
```

検索はデバッグの入口です。

---

# Search View

macOS

```
⌘ + Shift + F
```

Windows

```
Ctrl + Shift + F
```

開くと

- Search
- Replace
- Files to include
- Files to exclude
- Results

が表示されます。

---

# Explorerとの違い

Explorer は

「場所を知っている」

ときに使います。

Search は

「場所を知らない」

ときに使います。

実務では

Search → Explorer

の順になることが圧倒的に多いです。

---

# Include

例

```
src/**
```

```
app/**
```

```
components/**
```

```
**/*.php
```

```
**/*.ts
```

```
**/*.scss
```

複数指定

```
**/*.php,**/*.js
```

---

# Exclude

```
**/node_modules/**
```

```
vendor/**
```

```
dist/**
```

```
coverage/**
```

---

# Include + Exclude

Include

```
app/**
```

Exclude

```
app/cache/**
```

不要な検索結果を減らせます。

---

# 実案件例（WordPress）

まず

```
register_post_type(
```

検索。

次に

```
register_taxonomy(
```

さらに

```
add_action(
```

これだけでサイト構造をかなり把握できます。

---

# 実案件例（Laravel）

```
Route::
```

↓

```
Controller
```

↓

```
Service
```

↓

```
Repository
```

の順で追うと処理を理解しやすくなります。

---

# ハンズオン

1. 任意のプロジェクトを開く
2. `register_post_type(` または `Route::` を検索
3. Include を `app/**` に限定
4. Exclude に `vendor/**` を追加
5. 検索件数の変化を確認する

---

# チェックリスト

- [ ] Search View を開ける
- [ ] Include を使える
- [ ] Exclude を使える
- [ ] Explorerとの違いを説明できる
- [ ] Search→Debugger の流れを説明できる

---

Part2では以下を扱います。

- Glob完全攻略
- Regex検索
- Search Editor
- Replace
- ripgrepとの関係
- 実務ケーススタディ
