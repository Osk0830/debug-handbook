
# 第13章 React・APIデバッグ実践

> **目的**: ReactアプリとAPI通信で発生する問題を、ブラウザ・Network・状態管理・CLIを使って切り分けられるようになる。

---

# この章で身につくこと

- Reactの描画フロー
- API通信の調査
- Networkタブの見方
- CORSの理解
- 状態(state)の追跡
- 非同期処理のデバッグ
- よくあるエラーの切り分け

---

# Reactの流れ

```text
Browser
 ↓
React
 ↓
fetch / axios
 ↓
API
 ↓
JSON
 ↓
State更新
 ↓
再描画
```

---

# まず見る場所

1. Console
2. Network
3. Response
4. Request Payload
5. React Component
6. APIログ

---

# Console

見るもの

- JavaScript Error
- Warning
- Promise Error
- Stack Trace

---

# Network

確認項目

- URL
- Method
- Status
- Request Headers
- Response Headers
- Payload
- Response
- Timing

---

# fetch

```js
const res = await fetch("/api/users");
const json = await res.json();
```

確認すること

- Status
- JSON形式
- エラー時の処理

---

# axios

```js
const res = await axios.get("/api/users");
```

エラー

```js
try {
} catch(e) {
    console.error(e);
}
```

---

# State

よくある原因

- 更新されていない
- 非同期を誤解
- Props渡し忘れ

確認

- useState
- useEffect
- props

---

# useEffect

```js
useEffect(()=>{
},[])
```

依存配列を確認します。

---

# APIデバッグ

curlで再現

```bash
curl -i http://localhost:8080/api/users
```

レスポンス確認

- Status
- JSON
- Header

---

# CORS

症状

```
Access-Control-Allow-Origin
```

確認

- Origin
- Response Header
- サーバー設定

---

# JSON

確認

```json
{
  "success":true
}
```

キー名や型を確認します。

---

# 404

確認

- URL
- Route
- Method
- Proxy設定

---

# 500

確認

- APIログ
- Dockerログ
- PHPログ
- SQL

---

# 実務シナリオ

## 一覧が表示されない

確認

1. Network
2. API
3. JSON
4. State
5. render

---

## ボタン押しても更新されない

確認

- onClick
- state
- setState
- API

---

## APIだけ失敗

確認

- URL
- Method
- Authorization
- Token
- Cookie

---

# ハンズオン

1. DevToolsを開く
2. Networkを見る
3. Consoleを見る
4. APIレスポンス確認
5. curlで再現
6. Stateを確認
7. useEffect確認
8. JSONを比較
9. 404を再現
10. 500を調査

---

# タイムアタック

30分以内で

- API URL特定
- Response確認
- JSON確認
- curl再現
- State確認

---

# 練習問題

1. fetchとaxiosの違いは？
2. useEffectの依存配列の役割は？
3. CORSとは？
4. API404の原因を3つ挙げる
5. Networkタブで最初に見る項目は？
6. Reactで画面更新されない原因を3つ挙げる

---

# チェックリスト

- [ ] Networkを読める
- [ ] APIをcurlで再現できる
- [ ] JSONを確認できる
- [ ] Stateを追える
- [ ] useEffectを理解した
- [ ] CORSを説明できる

---

# コラム

Reactの不具合は「Reactが悪い」のではなく、

- API
- JSON
- State
- 非同期

のどこで止まっているかを切り分けることが重要です。

---

# 次章予告

第14章では Nginx・Apache・リバースプロキシ・リダイレクト・HTTPS・アクセスログ・エラーログを使ったWebサーバーデバッグを学びます。
