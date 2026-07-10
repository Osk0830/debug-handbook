# Lesson03 画面構成

## ゴール

- VS Codeの主要エリアを説明できる
- デバッグ時にどの画面へ移動すべきか判断できる
- PanelとSide Barの違いを理解する

## 画面全体

VS Codeは主に次の領域で構成されます。

```text
┌ Activity Bar ┬ Side Bar ┬──── Editor Group ────┐
│              │          │                      │
│ Explorer     │ Files    │ source code          │
│ Search       │ Results  │ diff / settings      │
│ Source Ctrl  │ Changes  │                      │
├──────────────┴──────────┴──────────────────────┤
│ Panel: Problems / Output / Debug Console / Terminal │
└────────────────────────────────────────────────┘
 Status Bar
```

## Activity Bar

画面左端のアイコン列です。

- Explorer
- Search
- Source Control
- Run and Debug
- Extensions

アイコンが見つからない場合はActivity Barを右クリックし、表示項目を確認します。

## Side Bar

Activity Barで選択した機能の詳細を表示します。Explorerならファイルツリー、Searchなら検索フォームと結果、Source Controlなら変更ファイル一覧が表示されます。

Side Barの表示切り替え:

```text
macOS: Cmd + B
Windows/Linux: Ctrl + B
```

## Editor Group

ファイル、設定、差分、Search Editorなどを表示する中心領域です。分割表示すると、実装と呼び出し元、修正前と修正後を並べて確認できます。

代表操作:

- エディタを右へ分割
- タブを別グループへ移動
- 差分エディタを開く
- Previewタブを固定する

### Previewタブ

Explorerでファイルを1回クリックすると、タブ名が斜体になる場合があります。これはPreview状態です。別ファイルを開くと同じタブが置き換わります。

固定する方法:

- ファイルをダブルクリックする
- タブをダブルクリックする
- 編集を開始する

## Panel

画面下部または右側に表示されます。

| タブ | 用途 |
|---|---|
| Problems | リンター、型、構文エラーの一覧 |
| Output | 拡張機能やタスクの出力 |
| Debug Console | デバッグ中の式評価や出力 |
| Terminal | シェルコマンドの実行 |

Panelの表示切り替え:

```text
macOS: Cmd + J
Windows/Linux: Ctrl + J
```

## Status Bar

画面下端には現在の状態が表示されます。

- Gitブランチ
- エラー・警告件数
- 行番号・列番号
- インデント
- 文字コード
- 改行コード
- 言語モード

文字化け、改行差分、フォーマット不一致を調べるときはStatus Barを確認します。

## Breadcrumbs

エディタ上部に、現在のファイル位置やシンボル階層を表示します。

```text
src > controllers > UserController.php > update
```

長いファイルで現在位置を把握する際に有効です。

## デバッグ時の標準導線

```text
Explorerで構造を確認
  ↓
Searchで候補を抽出
  ↓
Editorで実装を読む
  ↓
Problemsで静的エラーを確認
  ↓
Terminalでログやテストを実行
  ↓
Source Controlで差分を確認
```

## Zen Modeと集中表示

Zen Modeは余計なUIを隠して編集に集中する機能です。ただしデバッグではSide Bar、Panel、Status Barが重要なため、常時利用より用途を限定する方が安全です。

Command Palette:

```text
View: Toggle Zen Mode
```

## ハンズオン

1. Explorer、Search、Source Controlを順に開く
2. PanelでProblems、Output、Terminalを切り替える
3. 2つのファイルを左右へ分割表示する
4. Status Barで改行コードと文字コードを確認する
5. Previewタブと固定タブの違いを試す

## 確認問題

1. ProblemsとOutputの違いは何ですか。
2. Side BarとPanelはそれぞれどこに表示されますか。
3. 改行コードを確認する場所はどこですか。

## まとめ

- Activity Barから機能を選び、Side Barで詳細を操作する
- Editor Groupはコード・差分・設定を表示する中心領域
- Problems、Output、Debug Console、Terminalは用途が異なる
- Status Barは文字コードやGitブランチなどの重要情報を持つ
