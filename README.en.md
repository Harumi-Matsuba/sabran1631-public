# A reading of the cipher passages in Sabran's letters to Bouthillier (1633)

[日本語 README](README.md)

Melchior de Sabran, French diplomat resident in Genoa, wrote short passages in cipher in his 1633 letters to Bouthillier. This repository reads those passages as copied in Sabran's letter-book BnF fr. 4134, using the key reconstructed by George Lasry ("BNF Francais 4134", 2022).

- **Status: partial reading.** The cipher passages of nine leaves (ff. 46v, 50v, 54r, 57r, 57v, 66r, 66v, 69v, 73v), 897 signs, were transcribed. Figures per leaf are in the table below. Seven leaves (ff. 46v, 57r, 57v, 66r, 66v, 69v, 73v) reach high values on every measure. Some corrections that two AI checkers agreed on made words worse, and those remain ([docs/OPEN.en.md](docs/OPEN.en.md)). On ff. 50v, 54r and 57r, long stretches do not form words.
- **Prior work:** S. Tomokiyo's Cryptiana lists ff. 46, 50, 51, 54, 57, 66, 69, 73 of this volume as "undeciphered" and reports that George Lasry found his key applies to them ([louisxiii.htm](https://cryptiana.web.fc2.com/code/louisxiii.htm), [GL.htm](https://cryptiana.web.fc2.com/code/GL.htm)). The key is Lasry's work; this repository applies it. No published reading was found ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md), category "not found"). Lasry may have unpublished readings, and the originals received by Bouthillier (probably in the French diplomatic archives) were not checked, so we do not claim a first reading.
- **No human has checked the transcription.** It was made by an AI (Claude). Disagreements were judged from the images by two other AI models (OpenAI Codex and Claude Sonnet). Agreement between AIs is no substitute for a human check.
- **AI use:**
  - Transcription, checking procedure, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5).
  - Independent second transcription: OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model).
  - Judging disagreements: Codex and Claude Sonnet.
  - Choice of target, instructions and the decision to publish: a human.

## Figures (per leaf)
| Leaf (Gallica image) | Signs | Valued | Control (shuffled keys ≥ real, of 1000) | Independent second reading (lowest of 3 Codex runs) | Sample |
|---|---|---|---|---|---|
| f. 46v (f100) | 87 | 98.9% | 0 | 93.1% | les citadins la desirent … fier les armes … le senat … avec moy |
| f. 50v (f108) | 269 | 98.5% | 0 | 76.2% | … de raid(en) les places … il … estoit dispose … secret … faire … surprise (many broken stretches) |
| f. 54r (f115) | 44 | 90.9% | 0 | 84.1% | l'argent … Parme |
| f. 57r (f121) | 127 | 100% | 0 | 92.1% | du munitionnaire de Sa[vone] … en munitionnaire … le commis (some broken) |
| f. 57v (f122) | 64 | 100% | 0 | 90.6% | Savone … du chateau … assurer ses c[o]mpagnons |
| f. 66r (f139) | 149 | 96.6% | 0 | 91.3% | la ⟨3i⟩ de Savone … descouverte … l'on a mis prisonniers le munitionnaire … ceux qui sont pris … donner la place … le gouvernement |
| f. 66v (f140) | 59 | 98.3% | 0 | 96.6% | du soupçon … descouvert … de l'intelligence dans cet estat |
| f. 69v (f146) | 71 | 100% | 0 | 94.4% | le munitionnaire de Savone … amenes ici … le discours … n'est long |
| f. 73v (f154) | 27 | 100% | 0 | 100% | le general des postes … conseil |
| **Total** | 897 | 98.3% (882) | — | 88.1–92.6% | |

- Control: French-likeness of the letter runs (table signs only) compared with keys whose letter values are shuffled ([controls/results.txt](controls/results.txt), `src/control.py --strict`).
- Independent second reading: after the last correction, Codex was given only the line images, two reference sheets of sign shapes and the list of sign names, and transcribed three times in fresh contexts; no values, no reading, no key. The figure is the share of our signs matched by the same name ([second/](second/)).
- Calibration: no contemporary decipherment was found on the leaves examined in this volume. Instead we used BnF Baluze 155 f. 79 (Louis XIII to Sabran, 28 March 1631), deciphered by Lasry with the same key. Transcribed without seeing the answer and deciphered with the key, it agrees with Lasry's decipherment at **86.1%** of letters (516 of 599). The procedure that produced this figure is not identical to the one used on the target leaves ([docs/METHOD.en.md](docs/METHOD.en.md), "Calibration"). Codex-only transcriptions give 82.6–88.3% ([calib/](calib/)).

## Content (summary, partly conjectural)
A report of 1633 on an affair at Savona:
- the citizens (citadins) want it; the senate (le senat); arms (les armes);
- a plot within this state (de l'intelligence dans cet estat) and suspicion (du soupçon) have been discovered (descouvert);
- the munitions officer (munitionnaire) and two others were arrested and brought here;
- those taken refer to handing over the place (donner la place).

Codes not in the key (35, 3i, 12, 20, 33), probably names, are listed with conjectures in [docs/OPEN.en.md](docs/OPEN.en.md).

## Usage
```
python3 src/decode.py data/key.tsv data/transcription.tsv                     # reading (= data/decoded.txt)
python3 src/control.py data/key.tsv data/transcription.tsv c139 1000 --strict  # control (needs wordfreq)
python3 src/compare.py data/key.tsv data/transcription.tsv second/codex_pass*.txt   # independent second reading
python3 src/calib.py data/key.tsv calib/lasry_plain.tsv calib/transcription_f79.tsv calib/codex_pass*.txt  # calibration
python3 -m unittest discover -s tests
```

## Files
| Path | Content |
|---|---|
| data/key.tsv | Lasry's key with sign names |
| data/transcription.tsv | transcription of the nine leaves (final) |
| data/transcription_first.tsv | first transcription (before any comparison) |
| data/decoded.txt | output of `src/decode.py` |
| corrections/ | judgements of disagreements and the corrections made (six rounds) |
| second/ | independent second reading (3 Codex runs) and the prompt |
| calib/ | calibration (Baluze 155 f. 79) |
| controls/results.txt | control results |
| docs/ | METHOD, READING, OPEN, PRIOR_CHECK |

Images are not included; sources are cited by image number ([SOURCES.en.md](SOURCES.en.md)).

## Licence
Code MIT; own documents and data CC BY 4.0. The key and the calibration answer are Lasry's work ([LICENSE](LICENSE)).
