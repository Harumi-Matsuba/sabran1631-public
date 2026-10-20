# 食い違いの判定と修正 / Judgements and corrections

| ファイル / file | 周 / round | 方法 / method |
|---|---|---|
| r1_context.tsv | 1 | 行画像の中で位置を伏せて判定 / sign hidden in the line image |
| r2_context.tsv | 2 | 同上 / same |
| r3_single_sign.tsv, r4_single_sign.tsv | 3, 4 | 記号を1つずつ切り出して判定 / single sign cut out |
| r5_single_sign_examples.tsv, r6_single_sign_examples.tsv | 5, 6 | 同上、見本にこの写字生の実例 / same, reference sheet with this scribe's examples |

列：id、行、位置（行の中の記号の番号）、直す前の名前（「1回目」「before」）、Codex の答え、Sonnet の答え、結果。結果が fix の所だけ、Codex と Sonnet が同じ別の名前を選んだので直した。
Columns: id, line, position of the sign in the line, name before correction, Codex's answer, Sonnet's answer, outcome. Only rows marked fix were changed (both chose the same other name).

r1・r2 の行番号は最初の切り出し（傾きを直す前）の番号。f. 54r（c115）は後で切り直したため、r1〜r4 の c115 の行番号は data/transcription.tsv と合わない。
Line numbers in r1–r2 follow the first cut; f. 54r (c115) was recut later, so its line numbers in r1–r4 differ from data/transcription.tsv.
