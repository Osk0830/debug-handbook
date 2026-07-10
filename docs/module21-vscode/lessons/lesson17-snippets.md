# Lesson17 Snippetsで安全に定型入力する

## このLessonのゴール

- Snippetの構造を理解できる
- プレースホルダーと選択肢を使える
- 乱用せず保守可能なSnippetを作れる

## はじめに

Snippetsは定型コードを素早く入力する機能です。速度だけでなく、ログ形式、ガード節、コメント形式などを統一できます。ただし古い実装を大量複製する危険もあるため、対象を選びます。

## 基本構造

Snippetは名前、prefix、body、descriptionで構成します。言語別SnippetとグローバルSnippetがあります。チームで共有したい場合は、プロジェクトの `.vscode` 配下へ置く方法を検討します。

## 例: PHPのデバッグログ

```json
{
  "Structured debug log": {
    "prefix": "dlog",
    "body": [
      "error_log(json_encode([",
      "  "event" => "${1:event_name}",",
      "  "value" => ${2:\$value},",
      "], JSON_UNESCAPED_UNICODE));"
    ],
    "description": "一時調査用の構造化ログ"
  }
}
```

## Tab stopと変数

`${1}`、`${2}` で移動順を指定し、`${1:default}` で初期値を設定します。`${TM_FILENAME}` などの変数も利用できます。変換記法は複雑になりやすいため、読みやすさを優先します。

## 共有に向くSnippet

エラーハンドリング、テスト雛形、構造化ログ、アクセシビリティ属性など、プロジェクトで繰り返し、かつレビュー基準が明確なものが向きます。巨大なコンポーネント全体の複製は避けます。

## Snippetの検証

展開後のコードがlint、型チェック、フォーマッターを通るか確認します。依存APIが変わったらSnippetも更新します。Snippet内へ秘密情報や実URLを含めません。

## ハンズオン

1. 自分が週に複数回入力する定型コードを1つ選びます。
2. 言語別Snippetを作成します。
3. 2つ以上のTab stopを設定します。
4. 展開したコードへlintとフォーマットを実行します。
5. 共有価値と陳腐化リスクをREADMEへ1行で記録します。

## 確認問題

1. Snippetに向く処理と向かない処理の違いは何ですか。
2. Tab stopの番号は何を表しますか。
3. Snippet更新が必要になる契機を挙げてください。

## まとめ

このLessonでは、**17 Snippetsで安全に定型入力する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson18 Extensions](lesson18-extensions.md) へ進みます。
