# Lesson02 TerminalとShell

## ゴール

TerminalとShellの違いを説明できるようになる。

## 実務ではいつ使う？

シェルの違いによって、設定ファイルや補完、PATHの挙動が変わることがあります。

## 基本

|用語|役割|
|---|---|
|Terminal|文字を入力・表示するアプリ|
|Shell|入力されたコマンドを解釈するプログラム|

代表的なShell:

- bash
- zsh
- fish

確認:

```bash
echo $SHELL
```

## ハンズオン

```bash
echo $SHELL
which bash
which zsh
```

## よくある失敗

`.bashrc` を編集したのに反映されない場合、実際には zsh を使っていることがあります。

## 演習

1. 自分のShellを確認してください。
2. TerminalとShellの違いを説明してください。

## 模範解答

Terminalは画面、Shellはコマンドを解釈するプログラムです。

## FAQ

### Q. macOSではどのShellが標準ですか？

現在のmacOSでは zsh が標準です。

## 関連リンク

- https://www.gnu.org/software/bash/manual/
- https://zsh.sourceforge.io/Doc/

## 次へ進む条件

- [ ] `echo $SHELL` の結果を説明できる
