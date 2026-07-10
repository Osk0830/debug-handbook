# Project Documentation

このディレクトリは、Debug Handbook全体の設計・執筆・運用ルールを管理します。

## 最初に読むファイル

1. [PROJECT.md](PROJECT.md)
2. [BOOK_ARCHITECTURE.md](BOOK_ARCHITECTURE.md)
3. [STYLE_GUIDE.md](STYLE_GUIDE.md)
4. [WRITING_GUIDELINES.md](WRITING_GUIDELINES.md)
5. [MODULE_TEMPLATE.md](MODULE_TEMPLATE.md)
6. [ROADMAP.md](ROADMAP.md)
7. [CHANGELOG.md](CHANGELOG.md)

## 各ファイルの役割

|ファイル|役割|
|---|---|
|`PROJECT.md`|教材の目的・対象読者・基本方針|
|`BOOK_ARCHITECTURE.md`|全体構成とModuleの役割|
|`STYLE_GUIDE.md`|見出し・コード・表記のルール|
|`WRITING_GUIDELINES.md`|内容品質・調査・執筆のルール|
|`MODULE_TEMPLATE.md`|新しいModuleを作る際の標準形|
|`ROADMAP.md`|今後の作業計画|
|`CHANGELOG.md`|教材全体の変更履歴|

## 方針

Module01〜20は既存教材として維持します。

Module21以降は、以下の標準構成を適用します。

```text
moduleXX-name/
├── README.md
├── lessons/
├── labs/
├── exercises/
├── assets/
│   ├── images/
│   └── diagrams/
├── cheatsheet.md
├── faq.md
├── troubleshooting.md
└── resources.md
```

既存Moduleを一度に作り直すのではなく、学習・改訂時に段階的に新基準へ寄せます。
