# 先行の確かめ（2026-10-20）

[English](PRIOR_CHECK.en.md)

解読の作業に加わっていない、1回目の読みも答えも見ていない別の読み手が、「すでに読まれている」と示すつもりで探した記録です。対象は fr. 4134 の暗号部分の葉（f. 46v・50v・54r・57r・57v・66r・66v・69v・73v）です。解読した側も、着手前に同じ先を調べています（下の表の「着手前の確認」）。

## 結論
- 区分：**見つからない**。下の調べた先（2026-10-20）では、fr.4134 の暗号部分の解読（当時の解読の写し、刊本、他のプロジェクトの読み）は見当たらない。
- ただし、「初めて」とは書かない。理由は次の2つ。
  1. 友清氏は「George Lasry confirmed this cipher is also used for many letters of Sabran in BnF fr.4134 and fr.4135」と書いている（GL.htm）。Lasry 氏は、鍵が合うことを確かめる程度には読んでいる可能性がある。その読みは公開されていない。
  2. fr.4134 は、Sabran が手元に残した写しの帳簿（BnF の目録：「Recueil de copies … Troisième livre des negotiations du Sr de Sabran à Gennes … Année 1633」）である。Bouthillier が受け取った原本（当時の解読が添えられている可能性がある）は、外務省文書館（Correspondance politique, Gênes など）にあるとみられる。ウェブ検索（「Archives diplomatiques Correspondance politique Gênes 1633 volume numérisé Sabran」）では、デジタル化された巻は出なかった。外務省文書館の目録は直接引いていないので、確かめていない。

## 調べた先（2026-10-20）
| 先 | 版・日付 | 方法 | 結果 |
|---|---|---|---|
| Cryptiana GL.htm | Last-Modified 2026-10-15 | 取得して「4134」「Sabran」「4135」「Bouthillier」を検索。Sabran の節の画像3枚を開いた | 図の BnF_fr4134.jpg（鍵）・BnF_fr4134_decipher.png・_decipher2.png は、図中の表示が「BnF Baluze 155, f.79」と「BnF Baluze 155, f.79 b」で、Baluze 155 f.79 の解読（Lasry 氏）。fr.4134 の読みは載っていない。上の一文だけ |
| Cryptiana louisxiii.htm | Last-Modified 2025-02-01 | ヘッダで確認 | 着手前の確認のとおり、fr.4134 の f.46・50・51・54・57・66・69・73 を undeciphered としている |
| Cyphersolver（D. Bourdeau 氏）の台帳 | origin/main 0258b8ab（2026-10-18、変わっていない） | `git grep`（着手前の確認）。issue #51 まで・PR の題で「Sabran」「4134」「4135」「Bouthillier」 | CATALOGUE.md の catalogue 310 の1行（keys in hand）と、targets/sabran1631（Baluze 155 f.79）だけ。issue・PR に当たりなし |
| GeorgeLasry/cyphersolver（Lasry 氏のフォーク） | pushed 2026-10-19 22:18 UTC、13ブランチ | 全ブランチのファイル一覧で「sabran」「4134」「4135」 | writeup-nino1522 に本家と同じ targets/sabran1631（Baluze 155）があるだけ。fr.4134 の読みはない |
| NoAutopilot/cipher-lab | 2026-10-20 | ciphers/ の名前、fr4137-sabran/NOTES.md（2026-09-23） | Sabran 関係は fr4137-sabran と decode-2754-bnf-baluze156-1636 だけ。fr4137 は写しの帳簿の平文の覚え書（1637）で、暗号文はないと結論。fr.4134 は扱っていない |
| GitHub のコード検索 | 2026-10-20 | 「Sabran 4134」「Sabran Bouthillier」「Sabran Savone」 | cyphersolver の sabran1631（Baluze 155）、cipher-lab の Baluze 156 の鍵、無関係のファイルだけ |
| BnF Archives et manuscrits | cc505343（Français 4133–4138） | 目録を取得 | fr.4134 は Sabran の1633年の写しの帳簿。暗号部分の解読の記載はない |
| ウェブ検索 | 2026-10-20 | 「Lasry Sabran cipher Genoa 1633 BnF fr. 4134 decipherment」「Melchior de Sabran Gênes 1633 Savone munitionnaire dépêches Bouthillier」 | fr.4134 の解読や、Savone の件の刊本は出ない。Cryptiana の索引（satoru.net）で Melchior de Sabran (1631-1635) は「part」、Lasry 2022 |

## 確かめられなかった先
- Google Books の全文検索：API が 429（回数の上限）。
- dblp の Lasry 氏の論文一覧：API が 202 で、中身が空だった。
- 外務省文書館（La Courneuve）の Correspondance politique, Gênes：ウェブ検索ではデジタル化された巻が出なかった。目録は直接引いていない。
- DECODE：ログインが要る（Cryptoole の DECODE の項目に fr.4134 はない。着手前の確認）。
- Lasry 氏の未公開の作業。
