# 未解決の点・確かめていないこと

[English](OPEN.en.md)

## 鍵にない符号（値は推定）
| 符号 | 出る所 | 推定（根拠） |
|---|---|---|
| 3i | f. 66r「la ⟨3i⟩ de Savone」「a ⟨35⟩ la ⟨3i⟩」 | 場所を表す語。citadelle かもしれない（f. 46v の「les citadins」、f. 66r の「donner la place」）。推定 |
| 35 | f. 66r「a ⟨35⟩ la ⟨3i⟩」「…de ⟨35⟩」 | 人名か称号。推定 |
| 12 | f. 50v（暗号の連なりの中）、f. 54r の平文（「J'ay respondu a .12.」。書き起こしには含めていない） | 人名の符号。推定 |
| 33 | f. 54r「le passage ⟨27 34 26 33⟩」（平文の「sans .33.」は書き起こしに含めていない） | 人名か地名。推定 |
| 20 | f. 46v「(en)(de)fiance ⟨20⟩ e」 | 不明 |

## 直したことで崩れた所（AI 2つの判定が一致して直した箇所）
r7（直した所の2択での再判定）で、compagnons・deux・dedit などは直す前に戻った。2択でも2つのモデルが直した後を選び、崩れたまま残っている所：
- f. 46v c100_32：ie les excite → ieleseecite（x→pl）
- f. 66r c139_23c：secre[t] → secee（z→lh）
- f. 57r c121_24：capitan del… → capitanuel…（nj→n ほか）

どれを戻すべきかは、人の確認か、別の方法での判定が要ります（`corrections/`）。

## 語にならない並び
- f. 50v：17〜23・25・26・29・30・32行の多く（例 aeed eteeittete、giuuerietmiielicuiemait）。独立の2回目とは記号の 91.8〜92.2% が一致します。書き起こしの誤りのほかに、鍵にない値、写しの誤り、この葉での別の値が考えられます（推定）。
- f. 57r：21・24・27・36・38行。
- f. 54r：9行（agareanic）。

## 確かめていないこと
- 人による書き起こしの確認。
- Bouthillier が受け取った原本（外務省文書館 Correspondance politique, Gênes とみられる）と、当時の解読の有無（[PRIOR_CHECK.md](PRIOR_CHECK.md)）。
- 友清氏が挙げた f. 51 の画像は開いていません。f. 54r の5行目の上の消された書き込み（12 26 …）は、書き起こしに含めていません。
- fr. 4135（1635年）の f. 132・215v・217・224v・226v・227v・231v・239v・243・251：同じ鍵とされていますが、写字生が違い、記号の形がこの帳簿と合いません。Codex に2回書き起こさせて鍵を当てると、le Milanois・a Milan・de la ligue avec・passages などの語と、Alexandrie らしい aletandrie が出ますが、語にならない所が大半です。このリポジトリには含めていません。
- 較正の葉は別の写字生の手で、見本の実例はこの帳簿の手から取った。この違いが較正の値にどう効くか（[METHOD.md](METHOD.md)）。
