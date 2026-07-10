# Module21 VS Code チートシート

## 基本操作

| 操作 | macOS | Windows/Linux |
|---|---|---|
| Command Palette | `Cmd + Shift + P` | `Ctrl + Shift + P` |
| Quick Open | `Cmd + P` | `Ctrl + P` |
| Side Bar切替 | `Cmd + B` | `Ctrl + B` |
| Panel切替 | `Cmd + J` | `Ctrl + J` |
| 全体検索 | `Cmd + Shift + F` | `Ctrl + Shift + F` |
| ファイル内検索 | `Cmd + F` | `Ctrl + F` |
| ファイル内シンボル | `Cmd + Shift + O` | `Ctrl + Shift + O` |

## Quick Open記法

```text
> command          コマンド検索
@ symbol           現在ファイルのシンボル
# symbol           ワークスペースシンボル
:120               120行目へ移動
```

## Search

```text
src/**                         src配下
**/*.php                       PHPファイル
**/*Controller.php             Controller
**/*.{js,jsx,ts,tsx}           JS/TS系
**/node_modules/**             node_modules除外
**/vendor/**                   vendor除外
```

## 正規表現

```regex
\d+                            1文字以上の数字
\s+                            1文字以上の空白
[A-Z][A-Za-z0-9_]*             大文字始まりの識別子
\b(TODO|FIXME)\b              TODOまたはFIXME
console\.(log|warn|error)\(    console出力
https?://[^\s"'<>]+            URL候補
[ \t]+$                        行末空白
```

## CLI連携

```bash
code .
code -g src/app.ts:120:5
code --version
code --list-extensions
rg -n "keyword" .
rg -l "TODO" src
rg -c "console\.log" src
```

## 安全な置換手順

```text
1. git status
2. Search
3. Include / Exclude
4. 件数確認
5. Replace Preview
6. Replace
7. Test / Lint / Format
8. git diff
```
