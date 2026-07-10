# Lesson01 VS Codeとは

## ゴール

VS Codeを「コードを書く場所」ではなく「調査の中心」と説明できるようになる。

## VS Codeが担う役割

- コード閲覧
- 全文検索
- Git差分確認
- ターミナル
- Docker操作
- Debugger
- AIアシスタント

## 実務例

### PHP

500エラーが発生した。

1. Searchで対象ルートを探す
2. ターミナルで `docker compose logs`
3. Debuggerで停止
4. Git diffで変更確認

## CLIとの使い分け

|作業|VS Code|CLI|
|---|---|---|
|コード検索|◎|○ (`rg`)|
|ログ加工|△|◎|
|デバッグ|◎|△|
|自動化|△|◎|

## ハンズオン

```bash
code .
rg -n "function" .
git status
```

比較して、どちらが速く原因へ近づけるか記録する。
