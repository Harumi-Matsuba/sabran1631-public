# 未解決の点・確かめていないこと

[English](OPEN.en.md)

## 鍵にない符号（値は推定）
| 符号 | 出る所 | 推定（根拠） |
|---|---|---|
| 3i | f. 66r「la ⟨3i⟩ de Savone」「a ⟨35⟩ la ⟨3i⟩」 | 場所を表す語。citadelle かもしれない（f. 46v の「les citadins」、f. 66r の「donner la place」）。推定 |
| 35 | f. 66r「a ⟨35⟩ la ⟨3i⟩」「…de ⟨35⟩」 | 人名か称号。推定 |
| 12 | f. 50v・f. 54r（「J'ay respondu a ⟨12⟩」は平文中の数字） | 人名の符号。f. 54r では平文の中にも数字の符号（12・33・27 34 26 33）が書かれている |
| 33 | f. 54r「le passage ⟨27 34 26 33⟩」「sans ⟨33⟩」 | 人名か地名。推定 |
| 20 | f. 46v「(en)(de)fiance ⟨20⟩ e」 | 不明 |

## 直したことで崩れた所（AI 2つの判定が一致して直した箇所）
- f. 46v c100_32：ie les excite → ieleseecite（x→pl、r1）
- f. 57v c122_6：compagnons → cimpagnons（r2）
- f. 66r c139_23：deux avec luy → eue avec luiu（r2）。c139_23c：secre[t] → secee（r3）
- f. 57r c121_21・c121_24：r3・r4 で崩れた（saeamilie、capitanuelutp）

画像で確かめたうえでの修正という決まりで直したため、戻していません。どれを戻すべきかは、人の確認か、別の方法での判定が要ります（`corrections/`）。

## 語にならない並び
- f. 50v：17〜23・25・26・29・30・32行の多く（例 aeed eteeitcete、giuuerietmiielicuiemait）。独立の2回目とは記号の 76.2〜90.0% が一致します。書き起こしの誤りのほかに、鍵にない値、写しの誤り、この葉での別の値が考えられます（推定）。
- f. 57r：21・24・27・36・38行。
- f. 54r：9行（agareanic）。

## 確かめていないこと
- 人による書き起こしの確認。
- Bouthillier が受け取った原本（外務省文書館 Correspondance politique, Gênes とみられる）と、当時の解読の有無（[PRIOR_CHECK.md](PRIOR_CHECK.md)）。
- 友清氏が挙げた f. 51 の画像は開いていません。f. 54r の5行目の上の書き込み（12 26 …、消されている）は読み切れていません。
- fr. 4135（1635年）の f. 132・215v・217・224v・226v・227v・231v・239v・243・251：同じ鍵とされていますが、写字生が違い、記号の形がこの帳簿と合いません。Codex に2回書き起こさせて鍵を当てると、le Milanois・a Milan・de la ligue avec・passages などの語と、Alexandrie らしい aletandrie が出ますが、語にならない所が大半です。このリポジトリには含めていません。
- 較正の手順と対象の手順の違いが、較正の値にどう効くか（[METHOD.md](METHOD.md)）。
