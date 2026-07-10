# Module Template

## 新しいModuleの作成

Module21以降は、このテンプレートを基準に作ります。

```text
docs/moduleXX-name/
├── README.md
├── lessons/
│   ├── lesson01-topic.md
│   └── ...
├── labs/
│   ├── lab01-topic.md
│   └── ...
├── exercises/
│   ├── beginner.md
│   ├── intermediate.md
│   ├── advanced.md
│   └── answers.md
├── assets/
│   ├── images/
│   │   └── README.md
│   └── diagrams/
│       └── README.md
├── cheatsheet.md
├── faq.md
├── troubleshooting.md
└── resources.md
```

---

## README.mdの役割

Moduleの入口です。

必須内容:

- Moduleの目的
- 到達目標
- 前提知識
- 全体像
- Lesson一覧
- 推奨学習順
- 最低限試すこと
- 完了条件
- 次Moduleへの導線

---

## lessons/

概念・機能・実務フローをトピック別に分けます。

命名:

```text
lesson01-what-is-vscode.md
lesson02-install-and-initial-settings.md
```

原則として、番号は2桁、ファイル名は小文字英数字とハイフンを使います。

---

## labs/

複数Lessonの知識を組み合わせて手を動かす教材です。

例:

```text
lab01-search-and-terminal.md
lab02-debug-php-request.md
```

Labには次を含めます。

- 目的
- 前提
- シナリオ
- 手順
- 観測ポイント
- 完了条件
- 発展課題
- 記録テンプレート

---

## exercises/

難易度別の問題を置きます。

- `beginner.md`
- `intermediate.md`
- `advanced.md`
- `answers.md`

答えだけでなく、なぜその調査順になるかを解説します。

---

## cheatsheet.md

実務中に短時間で参照するページです。

長い説明はLessonへ移し、次を中心にします。

- コマンド
- ショートカット
- 判断フロー
- ステータス早見表
- よく使う設定例

---

## faq.md

学習中に出た質問を追加します。

```markdown
## Q. 質問

回答。

### 関連Lesson

- [LessonXX](lessons/lessonXX-topic.md)
```

---

## troubleshooting.md

症状から調査を開始できる形式にします。

```markdown
## 症状

## 最初に確認すること

## コマンド

## 結果別の判断

## 次の確認先
```

---

## resources.md

公式資料を中心にまとめます。

カテゴリ例:

- 公式ドキュメント
- 仕様
- 公式GitHub
- 補足記事
- 動画
- 書籍

---

## MkDocsへの追加

Module完成時に、次を更新します。

- `mkdocs.yml`
- ルート `README.md`
- `docs/index.md`
- `docs/project/BOOK_ARCHITECTURE.md`
- `docs/project/ROADMAP.md`
- `docs/project/CHANGELOG.md`

---

## コピー元

実ファイルのテンプレートは次に置きます。

```text
_base/module-template/
```
