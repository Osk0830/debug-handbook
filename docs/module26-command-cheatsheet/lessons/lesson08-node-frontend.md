# Lesson08 Node.js・フロントエンド

## このLessonの使い方

コマンドを暗記するのではなく、**何を確認したいか**から逆引きします。破壊的操作や本番操作では、対象・影響範囲・復旧方法を確認してください。

## バージョン

```bash
node -v
npm -v
pnpm -v
corepack --version
which node
```

**判断ポイント:** プロジェクト指定バージョンと実際の実行バージョンを確認する。

## 依存関係

```bash
pnpm install --frozen-lockfile
pnpm list
pnpm why PACKAGE
pnpm outdated
pnpm audit
```

**判断ポイント:** CIではlockファイル固定を使い、再現性を保つ。

## 開発・ビルド

```bash
pnpm dev
pnpm build
pnpm lint
pnpm test
pnpm typecheck
```

**判断ポイント:** ビルド・lint・型チェック・テストを分けて失敗地点を特定する。

## キャッシュ調査

```bash
rm -rf node_modules
pnpm store path
pnpm store prune
rm -rf .next dist build
```

**判断ポイント:** 削除前に再インストール可能か、lockファイルがあるか確認する。

## ブラウザ補助

```bash
npx serve dist
npx http-server .
open http://localhost:3000
```

**判断ポイント:** 静的成果物を単体で配信すると、開発サーバー依存を切り分けられる。

## 実務チェック

- [ ] 実行場所と対象環境を確認した
- [ ] 読み取りコマンドで現状を確認した
- [ ] 破壊的操作の影響範囲を確認した
- [ ] 実行結果を記録した
- [ ] 正常状態へ戻ったことを確認した
