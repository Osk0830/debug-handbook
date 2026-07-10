# Module21 Cheatsheet

## 開く・探す

|目的|macOS|Windows / Linux|
|---|---|---|
|Command Palette|`Shift + Cmd + P`|`Ctrl + Shift + P`|
|ファイル検索|`Cmd + P`|`Ctrl + P`|
|全体検索|`Shift + Cmd + F`|`Ctrl + Shift + F`|
|Problems|`Shift + Cmd + M`|`Ctrl + Shift + M`|
|Terminal|``Ctrl + ` ``|``Ctrl + ` ``|
|ファイル内シンボル|`Shift + Cmd + O`|`Ctrl + Shift + O`|
|Workspaceシンボル|`Cmd + T`|`Ctrl + T`|

## コード移動

- `F12`: 定義
- `Option / Alt + F12`: Peek Definition
- `Shift + F12`: 参照
- Call Hierarchy: 呼び出し元・呼び出し先
- Outline: 現在のファイル構造

## Debugger

- `F5`: 開始・継続
- `F9`: ブレークポイント
- `F10`: Step Over
- `F11`: Step Into
- `Shift + F11`: Step Out
- Variables: 現在の値
- Watch: 継続観察する式
- Call Stack: 現在位置までの経路

## 設定ファイル

|ファイル|役割|
|---|---|
|`.vscode/settings.json`|Workspace設定|
|`.vscode/launch.json`|Debugger起動・接続|
|`.vscode/tasks.json`|定型コマンド|
|`.vscode/extensions.json`|推奨・非推奨拡張|
|`*.code-workspace`|Multi-root Workspace|

## 調査の型

1. 現象と期待結果
2. 再現条件
3. ログ・Problems・Network
4. Search・Symbols
5. Terminal・Debugger
6. Git履歴
7. 最小修正
8. テスト
9. 差分確認
10. 再発防止
