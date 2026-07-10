# Lesson12 launch.jsonを理解する

## このLessonのゴール

- launch.jsonの役割と主要項目を説明できる
- launchとattachを使い分けられる
- 環境差分を安全に設定できる

## はじめに

`.vscode/launch.json` は、VS CodeがどのDebuggerを使い、何をどの条件で起動または接続するかを定義します。設定をコピーして終わりにせず、各項目が「実行対象」「接続先」「パス対応」のどれを決めるか理解します。

## 最小構成

基本は `version` と `configurations` です。各構成には `name`、`type`、`request` があり、言語やDebuggerに応じて `program`、`cwd`、`port`、`url` などを追加します。

## launchとattach

`launch` はVS Codeがプロセスを起動します。`attach` はすでに動いているプロセスへ接続します。Docker、PHP-FPM、ブラウザ、リモート環境ではattachが必要になることがあります。

## Node.jsの例

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug current file",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "cwd": "${workspaceFolder}",
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

## 変数置換

`${workspaceFolder}`、`${file}`、`${env:NAME}` などを使えます。絶対パスを直接書くと他メンバーや別PCで壊れるため、ワークスペース基準の値を優先します。

## 秘密情報を入れない

APIキーやパスワードをlaunch.jsonへ直接コミットしません。環境変数ファイルの扱い、`.gitignore`、チームの秘密管理方針を確認します。サンプル値と実値を分離します。

## 複数構成とcompound

フロントエンドとAPIを同時にデバッグする場合はcompound構成を使えます。まず各構成を単独で動作確認してから組み合わせると、失敗箇所を切り分けやすくなります。

## ハンズオン

1. Run and Debugから現在の環境向けlaunch.jsonを生成します。
2. `name`、`type`、`request`、`cwd` の意味をコメントなしで説明できるようにします。
3. 絶対パスがあれば変数置換へ変更します。
4. 通常実行とDebugger実行で、環境変数・カレントディレクトリ・ポートを比較します。
5. 設定をGit差分で確認し、共有してよい値だけか点検します。

## 確認問題

1. launchとattachの違いは何ですか。
2. 絶対パスを避ける理由は何ですか。
3. launch.jsonに秘密情報を書かないため、どのような方法を取りますか。

## まとめ

このLessonでは、**12 launch.jsonを理解する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson13 tasks.json](lesson13-tasks-json.md) へ進みます。
