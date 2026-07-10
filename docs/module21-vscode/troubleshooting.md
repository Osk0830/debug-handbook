# Module21 Troubleshooting

## Terminalが起動しない

1. 外部Terminalでシェルが起動するか確認
2. Terminal Profileと既定シェルを確認
3. User / Workspace設定の上書きを確認
4. Empty Profileで再現するか確認
5. TerminalログとDeveloper Toolsを確認

## 検索結果が少なすぎる

- Include / Excludeを解除する
- `search.exclude` と `files.exclude` を確認する
- `.gitignore` の利用設定を確認する
- Multi-rootの対象フォルダーを確認する
- `rg --hidden --no-ignore` と比較する

## Problemsへ結果が出ない

- 言語モードを確認する
- 対応拡張が有効か確認する
- Outputで言語サーバーのエラーを見る
- CLIのlint・型チェックと比較する
- TaskではproblemMatcherを確認する

## Debuggerが停止しない

- 該当処理が本当に実行されているか
- 実行中プロセスと接続先が一致しているか
- source mapが生成されているか
- Docker / Remoteのpath mappingが正しいか
- 最適化・キャッシュ・古いビルドを使っていないか

## VS Codeだけ重い

- Empty Windowと対象Workspaceを比較
- Show Running Extensionsを確認
- Process Explorerを確認
- Extension Bisectを実行
- watcher/search/Gitの対象を見直す
- 巨大ファイルや生成物を閉じる・除外する

## フォーマッターが競合する

- Format Document Withで使用中のFormatterを確認
- 言語別`editor.defaultFormatter`を設定
- 重複拡張を無効化
- `formatOnSave`と`codeActionsOnSave`を分けて確認

## 設定を変えても反映されない

- User / Workspace / Remote / Language-specificのスコープを確認
- Modified設定を確認
- Reload Windowを実行
- 設定キーが非推奨になっていないか現行ドキュメントを確認
