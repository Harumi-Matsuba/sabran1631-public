# Task: transcribe cipher signs by sign name

The images in img/ are crops of the cipher lines of one 17th-century French letter (17 lines, each cut into three overlapping thirds: b79_L09a/b/c … b79_L27a/b/c). The cipher uses separated signs: letters, digits and odd signs, plus two-digit numbers that stand for words.

The key is given as an image (key_image.jpg: George Lasry's reconstruction, columns headed by plaintext letters, word numbers below) and as key.tsv (one line per sign: NAME, value, kind, shape description in Japanese). Use ONLY the names in key.tsv's first column.

For each image, write one line: `<image name><TAB><sign names left to right, separated by spaces>`. Two-digit numbers written as one unit: write the number (e.g. 26). A sign you cannot match: `?`. Unsure between two names: write the more likely one. Ignore plain handwriting (if a plain word separates two cipher runs you may write `[word]`). Transcribe each image on its own (the thirds overlap a little).

Write the result to opus_transcription.tsv in this folder (51 lines).
