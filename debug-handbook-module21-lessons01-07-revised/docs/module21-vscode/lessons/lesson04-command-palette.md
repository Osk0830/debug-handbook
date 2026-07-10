# Lesson04 Command Palette

## ゴール

- Command Paletteから機能名で操作を呼び出せる
- ショートカットを知らない機能でも自力で探せる
- 設定・再読み込み・表示切り替えを安全に実行できる

## Command Paletteとは

VS Codeのほぼすべての操作を、コマンド名から検索して実行する入口です。

```text
macOS: Cmd + Shift + P
Windows/Linux: Ctrl + Shift + P
```

先頭に`>`が表示されます。続けてキーワードを入力します。

```text
> reload window
> open settings json
> format document
> toggle terminal
```

メニューの場所やショートカットを覚えていなくても、目的を表す語から機能へ到達できます。

## よく使うコマンド

### ウィンドウを再読み込み

```text
Developer: Reload Window
```

拡張機能の導入後や設定変更が反映されない場合に使用します。編集中ファイルは通常保持されますが、Terminal上で実行中の処理には注意してください。

### User設定をJSONで開く

```text
Preferences: Open User Settings (JSON)
```

### Workspace設定をJSONで開く

```text
Preferences: Open Workspace Settings (JSON)
```

### キーボードショートカットを開く

```text
Preferences: Open Keyboard Shortcuts
```

### ドキュメントをフォーマット

```text
Format Document
```

複数フォーマッタがある場合は次を使います。

```text
Format Document With...
```

### 言語モードを変更

```text
Change Language Mode
```

拡張子のないファイルや誤認識されたテンプレートを正しい言語として扱わせるときに使います。

### 新しいSearch Editorを開く

```text
Search: Open New Search Editor
```

大量の検索結果をエディタとして残したい場合に利用します。

## ファジー検索

コマンド名を完全一致で入力する必要はありません。

```text
open user json
```

のように主要語だけを入力して候補を絞れます。見つからない場合は、日本語UIでも英語の機能名を試してください。

## コマンド履歴

Command Paletteを開くと、直近で使ったコマンドが上位に表示されます。繰り返し使う操作は、履歴からすぐ呼び出せます。

## `Cmd + P`との違い

```text
Cmd + P
```

はQuick Openで、主にファイル名検索に使います。ただし先頭文字を追加すると機能が変わります。

| 入力 | 機能 |
|---|---|
| `>` | コマンド検索 |
| `@` | 現在ファイルのシンボル |
| `#` | ワークスペースのシンボル |
| `:` | 指定行へ移動 |

例:

```text
:120
```

現在ファイルの120行目へ移動します。

## キーバインドの確認

Command Paletteの候補右側にショートカットが表示されることがあります。よく使うコマンドだけ、使用しながら覚えます。

キーバインドが競合する場合:

1. `Preferences: Open Keyboard Shortcuts`を開く
2. コマンド名を検索する
3.割り当て元を確認する
4. 不要な割り当てを削除または変更する

## 実務例: 設定変更が反映されない

1. `Preferences: Open User Settings (JSON)`で値を確認
2. Workspace設定が上書きしていないか確認
3. `Developer: Reload Window`を実行
4. Outputで関係拡張のログを確認

Command Paletteは単なるランチャーではなく、原因調査の導線になります。

## ハンズオン

Command Paletteだけを使って次を実行してください。

1. User Settings(JSON)を開く
2. Keyboard Shortcutsを開く
3. Panelを表示する
4. Terminalを新規作成する
5. 現在のファイルをフォーマットする
6. ウィンドウを再読み込みする

## 確認問題

1. Command PaletteとQuick Openの主な違いは何ですか。
2. ファイルの150行目へ移動するには何を入力しますか。
3. フォーマッタが複数ある場合に使うコマンドは何ですか。

## まとめ

- Command Paletteは機能名から操作を探す入口
- ショートカットを暗記していなくても作業できる
- `Cmd + P`は先頭記号によってコマンド・シンボル・行移動にも使える
- 設定反映や拡張機能調査でもCommand Paletteを活用する
