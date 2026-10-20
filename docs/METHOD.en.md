# Method

[日本語](METHOD.md)

## Sources and key
- Ciphertext: BnF fr. 4134 (copies, Sabran's letter-book for 1633), Gallica ark:/12148/btv1b9060193z, images f100, f108, f115, f121, f122, f139, f140, f146, f154, fetched at full size from the openapi.bnf.fr IIIF service.
- Key: George Lasry's reconstruction "BNF Francais 4134" (25/05/2022), published as an image on S. Tomokiyo's Cryptiana GL.htm, rewritten with sign names (shape-like labels) in `data/key.tsv`: 52 letter signs, 19 word numbers, 1 doubling sign. 0, 34 and 29 stand together in Lasry's table as "o- 34 29. ET"; we read all three as et (our interpretation).

## Transcription
1. Each page was deskewed (the angle that makes the horizontal ink profile sharpest) and cut into lines. Only f. 54r was tilted (about 2°); its first cut mixed lines and it was recut after deskewing.
2. Claude transcribed the enlarged line images with sign names (`data/transcription_first.tsv`).

## Correcting disagreements from the images (corrections/)
OpenAI Codex transcribed the same line images without seeing our reading. Signs where it disagreed one-to-one with us were judged from the images, separately and blind, by two other AI models (Codex and Claude Sonnet). We changed a sign **only where both chose the same other name**.

| Round | How the sign was judged | Changed |
|---|---|---|
| r1 | line image, with the sign hidden as [?n] in the sign sequence; reference sheet of signs cut from the key image (names only, no values) | 26 |
| r2 | as r1; Codex's transcriptions made with the reference sheet attached | 17 |
| r3, r4 | each sign cut out on its own, without context; positions given by Codex on line images with a pixel ruler | 16, 4 |
| r5, r6 | as r3; the reference sheet extended with up to four examples per name from this scribe, taken from signs that we and Codex named alike | 5, 2 |

Some corrections improved the reading (intelligence, commis, l'argent); some made it worse (f. 46v ie les excite → ieleseecite, f. 57v compagnons → cimpagnons, etc., see [OPEN.en.md](OPEN.en.md)). Agreement between two models does not remove all errors.

## Independent second reading (second/)
After the last correction, Codex transcribed the lines three times in fresh contexts, given only the 116 line images, the two reference sheets (key signs and this scribe's examples) and the sign-name list (`second/PROMPT.md`); no values, no reading, no key, no judgements. Each run's log contains a single reply and no command execution or file reading.

Agreement = share of our signs inside matching blocks of the per-line sign sequences (`src/compare.py`): 92.6%, 92.1%, 88.1% overall. The README gives, per leaf, the lowest of the three runs. In run 3 Codex wrote r for most pl on f. 50v, bringing that leaf to 76.2%.

The comparisons used to make corrections (the rounds above) are not called independent.

## Control (controls/)
1000 keys with the letter values shuffled among the letter signs; French-likeness = mean log-likelihood of letter trigrams built from wordfreq's top 50,000 French words. Runs are broken at word numbers, the doubling sign, unreadable and uncertain signs. On all nine leaves, 0 of 1000 shuffled keys scored as high as the real key.

## Calibration (calib/)
No contemporary decipherment was found on the leaves examined in this volume. We used BnF Baluze 155 f. 79 (Gallica btv1b9001401d f163), 17 cipher lines deciphered by Lasry with the same key. His decipherment (red overlay in the GL.htm images) was transcribed into `calib/lasry_plain.tsv` (599 letters; signs he left without a value are omitted).

| Procedure | Agreement |
|---|---|
| Claude Sonnet transcription (blind, with the reference sheet) | 78.6% |
| + judging in context (Codex and Sonnet, as r1; 36 changed) | 82.5% |
| + single-sign judging (as r3; 37 changed) | 86.1% |
| + single-sign judging with scribe examples (as r5; 2 changed) | **86.1%** (`calib/transcription_f79.tsv`) |
| For reference: Codex only (sheet with examples), 3 runs | 87.0%, 82.6%, 88.3% |

**Differences from the procedure on the target leaves** (their effect on the figure was not measured):
- First transcriber: Claude Opus (the author of this repository) for the target, Claude Sonnet for the calibration leaf. Opus had seen the answer (Lasry's decipherment) and so could not transcribe the calibration leaf blind.
- Number of rounds: target 2 context rounds + 4 single-sign rounds; calibration 1 + 2. On the target the number of changes fell round by round (26, 17, 16, 4, 5, 2).
- Scribe examples: taken from the fr. 4134 hand. Baluze 155 f. 79 is in another hand, so they were presented as "another scribe's examples".
- The calibration leaf was not deskewed.

86.1% is therefore given as an approximation of the accuracy of the target procedure. The table shows that judging raises Sonnet's 78.6%, and that Codex alone varies between 82.6% and 88.3%.

## Valued share
`src/decode.py` counts the signs whose name is in the key (882 of 897, 98.3%). Stretches that have values but form no words are marked in READING and OPEN.

## Limits
- No human has checked the transcription.
- Sign names, shape descriptions and the reference crops were made by us. Errors shared by us and the other AI are not caught by comparison.
- fr. 4134 is a copy book; copying errors cannot be told apart.
- fr. 4135 (1635) has cipher in the same key, but the scribe's sign shapes differ and it is not read here ([OPEN.en.md](OPEN.en.md)).
