# Sabran から Bouthillier への書簡（1633年）の暗号部分の読み

[English README](README.en.md)

ジェノヴァに駐在したフランスの外交官 Melchior de Sabran が、Bouthillier 氏に送った1633年の書簡には、暗号で書いた短い部分があります。その書簡の写しを、Sabran の帳簿 BnF fr. 4134 で見て、George Lasry 氏が復元した鍵（"BNF Francais 4134"、2022年）で読んだ記録です。

- **状態：部分的な読み。** 帳簿の9葉（f. 46v・50v・54r・57r・57v・66r・66v・69v・73v）の暗号部分、897記号を書き起こしました。葉ごとの数字は下の表のとおりです。7葉（f. 46v・57r・57v・66r・66v・69v・73v）では、どの数字も高い値に届いています。ただ、AI 同士で一致して直した所に、かえって語が崩れた所が残っています（[docs/OPEN.md](docs/OPEN.md)）。f. 50v・54r・57r は、語にならない並びが長く続きます。
- **先行との関係：** 友清理士氏の Cryptiana は、この帳簿の f. 46・50・51・54・57・66・69・73 を「undeciphered」とし、Lasry 氏の鍵がこれらに当てはまることを Lasry 氏が確かめた、と書いています（[louisxiii.htm](https://cryptiana.web.fc2.com/code/louisxiii.htm)、[GL.htm](https://cryptiana.web.fc2.com/code/GL.htm)）。鍵は Lasry 氏の成果で、このリポジトリはそれを当てたものです。読みを公開した例は見つかりませんでした（[docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)、区分「見つからない」）。ただし、Lasry 氏が公開していない読みはありえます。また、Bouthillier が受け取った原本は外務省文書館にあるとみられますが、確かめていません。このため「初めて」とは書きません。
- **人は書き起こしを確かめていません。** 書き起こしは AI（Claude）が作りました。食い違いは、別の AI（OpenAI Codex と Claude Sonnet）に画像で判定させて直しています。AI どうしの一致は、人による確認の代わりにはなりません。
- **AI の使用：**
  - 書き起こし・判定の手順・スクリプト・文書：Anthropic の Claude（Claude Code、Claude Opus 5.5）。
  - 独立の2回目の書き起こし：OpenAI Codex（codex-cli 0.163.0-alpha.10.2、既定のモデル）。
  - 食い違いの判定：Codex と Claude Sonnet。
  - 対象の選定・作業の指示・公開の判断：人。

## 数字（葉ごと）
| 葉（Gallica のコマ） | 記号 | 値の付いた割合 | 対照（かき混ぜ鍵1000通りで本物以上） | 独立の2回目（Codex 3回の最低） | 読みの例 |
|---|---|---|---|---|---|
| f. 46v（f100） | 87 | 98.9% | 0 | 93.1% | les citadins la desirent … fier les armes … le senat … avec moy |
| f. 50v（f108） | 269 | 98.5% | 0 | 76.2% | … de raid(en) les places … il … estoit dispose … secret … faire … surprise（崩れが多い） |
| f. 54r（f115） | 44 | 90.9% | 0 | 84.1% | l'argent … Parme |
| f. 57r（f121） | 127 | 100% | 0 | 92.1% | du munitionnaire de Sa[vone] … en munitionnaire … le commis（崩れあり） |
| f. 57v（f122） | 64 | 100% | 0 | 90.6% | Savone … du chateau … assurer ses c[o]mpagnons |
| f. 66r（f139） | 149 | 96.6% | 0 | 91.3% | la ⟨3i⟩ de Savone … descouverte … l'on a mis prisonniers le munitionnaire … ceux qui sont pris … donner la place … le gouvernement |
| f. 66v（f140） | 59 | 98.3% | 0 | 96.6% | du soupçon … descouvert … de l'intelligence dans cet estat |
| f. 69v（f146） | 71 | 100% | 0 | 94.4% | le munitionnaire de Savone … amenes ici … le discours … n'est long |
| f. 73v（f154） | 27 | 100% | 0 | 100% | le general des postes … conseil |
| **計** | 897 | 98.3%（882） | — | 88.1〜92.6% | |

- 対照：表の記号だけで作った文字の連なりのフランス語らしさを、文字の値をかき混ぜた鍵と比べました（[controls/results.txt](controls/results.txt)、`src/control.py --strict`）。
- 独立の2回目：書き起こしを最後に直した後、Codex に、行画像と記号の見本と記号名の一覧だけを渡し、新しく3回読ませました。値・こちらの読み・鍵は渡していません。数字は、こちらの記号のうち同じ名前が対応した割合です（[second/](second/)）。
- 較正：当時の解読の書き込みは、この帳簿の見た葉にはありません。代わりに、同じ鍵で Lasry 氏が解読した BnF Baluze 155 f. 79（Louis XIII から Sabran へ、1631年3月28日）を使いました。答えを見ずに書き起こして鍵を当て、Lasry 氏の解読と文字で比べると **86.1%** でした（599文字中516）。この値を出した手順は、対象の葉の手順と同じではありません（[docs/METHOD.md](docs/METHOD.md)「較正」）。Codex だけの書き起こしでは 82.6〜88.3% です（[calib/](calib/)）。

## 内容（要約、推定を含む）
1633年の Savone（サヴォーナ）をめぐる企ての報告です。
- 市民（citadins）がそれを望んでいること、元老院（le senat）、武器（les armes）。
- この国の中での内通（de l'intelligence dans cet estat）と、疑い（du soupçon）が露見したこと（descouvert）。
- 糧秣係（munitionnaire）とほか2人が捕らえられ、ここへ連れてこられたこと。
- 捕らえられた者たちが、場所（la place）を明け渡すことに触れていること。

人名・地名とみられる鍵にない符号（35・3i・12・20・33）は、[docs/OPEN.md](docs/OPEN.md) に、推定とともに挙げました。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription.tsv                     # 読み（data/decoded.txt と同じ）
python3 src/control.py data/key.tsv data/transcription.tsv c139 1000 --strict  # 対照（wordfreq が必要）
python3 src/compare.py data/key.tsv data/transcription.tsv second/codex_pass*.txt   # 独立の2回目との一致
python3 src/calib.py data/key.tsv calib/lasry_plain.tsv calib/transcription_f79.tsv calib/codex_pass*.txt  # 較正
python3 -m unittest discover -s tests
```

## ファイル
| 場所 | 中身 |
|---|---|
| data/key.tsv | 鍵（Lasry 氏）を記号名で書いたもの |
| data/transcription.tsv | 9葉の書き起こし（最終） |
| data/transcription_first.tsv | 最初の書き起こし（照合の前） |
| data/decoded.txt | `src/decode.py` の出力 |
| corrections/ | 食い違いの判定と直した箇所（6周） |
| second/ | 独立の2回目（Codex 3回）と依頼文 |
| calib/ | 較正（Baluze 155 f. 79） |
| controls/results.txt | 対照の結果 |
| docs/ | METHOD・READING・OPEN・PRIOR_CHECK |

画像は含めていません。資料はコマ番号で示しています（[SOURCES.md](SOURCES.md)）。

## ライセンス
コードは MIT、自作の文書とデータは CC BY 4.0 です。鍵と較正の答えは Lasry 氏の成果です（[LICENSE](LICENSE)）。
