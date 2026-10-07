# 株式会社Yodasou コーポレートサイト

Claude の Design キャンバスで作成したコーポレートサイトとイベントキービジュアルです。

公開URL: https://nazo-yodasou.github.io/yodasou-corporate-site/

ルートの `index.html` などは `python3 build.py` で `project/` から生成した静的HTMLです。デザインを変更したら `project/` を更新して再生成してください。

## ページ

| ファイル | 内容 |
| --- | --- |
| `project/Main.dc.html` | トップ（index） |
| `project/About.dc.html` | 会社概要 |
| `project/Faq.dc.html` | よくある質問 |
| `project/Contact.dc.html` | お問い合わせ |

## イベントキービジュアル（1200×900）

- `project/KV-Kudan-A.dc.html` — 案A：古地図
- `project/KV-Kudan-B.dc.html` — 案B：夜の九段坂
- `project/KV-Clock.dc.html` — 時計塔に残された七つの手紙
- `project/KV-Radio.dc.html` — 深夜二時の暗号放送
- `project/KV-RouteEnigma.dc.html` — ROUTE ENIGMA〜夜明けの鍵を奪い合え〜

`project/canvas.json` はキャンバス上の配置情報です。

※ `.dc.html` は Design キャンバス用の形式で、専用ランタイム（`support.js`）上で表示されます。
