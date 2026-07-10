# Module21 FAQ

## VS CodeとVisual Studioは同じですか

別製品です。VS Codeは軽量なコードエディタを基盤とし、拡張機能で機能を追加します。Visual Studioは特に.NETなどで使われる統合開発環境です。

## ファイルを開いたのに全体検索できません

単一ファイルだけを開いている可能性があります。`File: Open Folder`またはTerminalから`code .`でプロジェクトルートを開いてください。

## User設定とWorkspace設定はどちらを使いますか

個人の全案件へ適用する見た目や操作はUser設定、フォーマッタや検索除外など案件固有のルールはWorkspace設定が基本です。

## 拡張機能は多いほど良いですか

いいえ。役割が重複すると補完、保存時処理、フォーマット、キーバインドが競合します。必要性を説明できるものだけ導入します。

## Searchと`Cmd + F`の違いは何ですか

`Cmd + F`は現在のファイル内、`Cmd + Shift + F`はワークスペース全体を検索します。

## Search結果に`vendor`や`node_modules`が出ません

`.gitignore`、`search.exclude`、検索設定で除外されている可能性があります。通常は依存物を検索しない方が効率的ですが、必要時のみ除外設定を見直します。

## Search結果が多すぎます

検索語を固有にする、Includeで対象ディレクトリや拡張子を限定する、Excludeで生成物やテストを外す、Whole WordやMatch Caseを使う、の順で絞ってください。

## 正規表現を最初から使うべきですか

固有文言や関数名が分かるなら通常検索を優先します。表記揺れ、番号違い、複数候補をまとめたい場合に正規表現を使います。

## 一括置換を元に戻せますか

直後ならUndoできますが、確実ではありません。置換前にGit状態を確認し、Preview後に実行し、`git diff`で確認してください。

## Explorerでクリックしたファイルが同じタブに上書きされます

Previewタブの動作です。ファイルまたはタブをダブルクリックすると固定できます。

## `code .`が使えません

macOSではCommand Paletteから`Shell Command: Install 'code' command in PATH`を実行し、Terminalを開き直します。詳細は[トラブルシューティング](troubleshooting.md)を参照してください。
