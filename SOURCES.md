# 出典

[English](SOURCES.en.md)

## 一次資料（画像はリポジトリに含めていない）
- **BnF, Français 4134**（Recueil de copies … ambassades du Sr de Sabran … Année 1633）、Gallica ark:/12148/btv1b9060193z。
  - 暗号部分を読んだコマ：f100（f. 46v）、f108（f. 50v）、f115（f. 54r）、f121（f. 57r）、f122（f. 57v）、f139（f. 66r）、f140（f. 66v）、f146（f. 69v）、f154（f. 73v）。
  - 画像は https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060193z/f{コマ}/full/max/0/default.jpg（2026-10-20 取得）。
- **BnF, Baluze 155** f. 79（Louis XIII から Sabran へ、Dijon、1631年3月28日）、Gallica ark:/12148/btv1b9001401d f163。較正に使った。
- **BnF, Français 4135**（1635年）、Gallica ark:/12148/btv1b9060194c。同じ鍵とされる暗号があるが、このリポジトリでは読んでいない。

Source gallica.bnf.fr / BnF.

## 鍵と答え
- George Lasry, "BNF Francais 4134"（2022-05-25）。友清理士（Satoshi Tomokiyo）, Cryptiana, code/GL.htm「Melchior de Sabran (1631)」（Last-Modified 2026-10-15）に画像で掲載。`data/key.tsv` はこれを記号名で書き写したもの。
- 同じページの Lasry 氏の解読の画像（Baluze 155 f. 79）。`calib/lasry_plain.tsv` に書き写した。
- 友清理士, Cryptiana, code/louisxiii.htm（Last-Modified 2025-02-01）：fr. 4134・4135 の暗号部分を undeciphered とし、Lasry 氏の鍵が当てはまると書く。

## 照らしたもの
- D. Bourdeau, cyphersolver（origin/main 0258b8ab、2026-10-18）：CATALOGUE.md の catalogue 310「Sabran to Bouthillier … Lasry 1631 Sabran key」、targets/sabran1631（Baluze 155 f. 79）。
- NoAutopilot/cipher-lab：ciphers/decode-2754-bnf-baluze156-1636/key_sabran_1631_letters.tsv（同じ鍵の別の書き写し。記号の読みを照らした）。

先行の確かめは [docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)。見つからないことは、手を付けた人がいないことの証明にはなりません。
