# Lesson27 VS Codeのパフォーマンスを改善する

## このLessonのゴール

- 重さの原因を計測できる
- 検索・監視・拡張・Gitの負荷を切り分けられる
- 設定変更の効果を比較できる

## はじめに

VS Codeが重いとき、メモリ不足と決めつけず、起動、入力、検索、Git、Terminal、拡張ホストのどこが遅いかを分けます。最適化は、変更前後を同じ操作で比較して初めて効果を判断できます。

## 症状を分ける

起動が遅い、キー入力が遅延する、検索が終わらない、CPUが高い、拡張ホストが停止する、Terminalだけ遅い、を区別します。発生するWorkspaceとEmpty Windowも比較します。

## 計測機能

Developer: Startup Performance、Developer: Show Running Extensions、Process Explorer、Extension Bisectを使います。OSのActivity MonitorやTask Managerも併用します。

## 除外設定

`files.watcherExclude`、`search.exclude`、Git設定で生成物や巨大ディレクトリを対象外にします。ただし必要なファイルまで除外すると変更検知や検索を見逃します。目的ごとに設定を分けます。

## 典型的な対象

`node_modules`、`vendor`、`dist`、`build`、ログ、キャッシュ、大量画像、巨大なGit履歴などです。モノレポではルート全体ではなく必要なサブフォルダーだけを開く方法もあります。

## 拡張と設定

使わない言語拡張をWorkspaceで無効化し、重複フォーマッターやAI補完を整理します。Empty Profileで改善するなら、拡張またはUser設定が原因候補です。

## 改善の記録

変更項目、計測方法、変更前、変更後、副作用を記録します。「軽くなった気がする」だけでは共有できません。

## ハンズオン

1. 重いWorkspaceで症状と再現操作を記録します。
2. Running ExtensionsとProcess Explorerを確認します。
3. Empty Profileと比較します。
4. 1つだけ除外または無効化し、同じ操作を再計測します。
5. 効果と副作用を表へまとめます。

## 確認問題

1. パフォーマンス問題を最初に症状別へ分ける理由は何ですか。
2. watcherExcludeとsearch.excludeの違いは何ですか。
3. 改善効果を判断するために何を記録しますか。

## まとめ

このLessonでは、**27 VS Codeのパフォーマンスを改善する**を、単なる機能紹介ではなくデバッグの流れに組み込む方法を学びました。

次は [Lesson28 チーム開発](lesson28-team-development.md) へ進みます。
