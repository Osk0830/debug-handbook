# Module21 FAQ

## Problemsが0件ならコードに問題はありませんか

いいえ。Problemsは主に言語機能やリンターが検出した診断です。実行時例外、HTTPエラー、DB障害、環境差は別途ログやDebuggerで確認します。

## ブレークポイントが灰色で止まりません

対象コードが読み込まれているか、launch構成、source map、path mapping、接続先、ビルド済みファイルとの対応を確認します。

## settings.jsonは全部コミットしてよいですか

成果物や検証の再現性に必要なWorkspace設定だけを共有します。テーマ、フォント、個人AI設定などはUser設定向きです。

## VS Code Searchとrgはどちらを使うべきですか

検索結果を開きながら調査するならVS Code Search、件数集計・パイプ・スクリプト化なら`rg`が便利です。同じ条件で結果が違う場合はexcludeやignore設定を確認します。

## 拡張機能が原因か確認するには

Empty Profile、Extension Bisect、Disable All Installed Extensionsを使い、無効化前後を比較します。

## AIにリポジトリ全体を渡してよいですか

組織の情報分類と利用規約に従います。必要最小限のファイルだけを選び、秘密情報や個人情報を送信しません。

## launch.jsonとtasks.jsonの違いは

launch.jsonはDebuggerの起動・接続、tasks.jsonはlint、テスト、ビルドなどの定型コマンドを定義します。`preLaunchTask`で連携できます。

## GitLensがないと履歴調査できませんか

標準Git機能や `git log`、`git blame`、`git show` でも調査できます。GitLensは履歴をエディタ内で見やすくする選択肢です。
