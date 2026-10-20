# EN: Tests: decoded file up to date, known words present, independent-reading and calibration figures reproduce.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable


def run(*args):
    return subprocess.run([PY] + [os.path.join(ROOT, a) if not a.startswith('-') and '/' in a else a for a in args],
                          capture_output=True, text=True, check=True, cwd=ROOT).stdout


class TestReading(unittest.TestCase):
    def test_decoded_file_is_current(self):
        out = run('src/decode.py', 'data/key.tsv', 'data/transcription.tsv')
        with open(os.path.join(ROOT, 'data', 'decoded.txt'), encoding='utf-8') as f:
            self.assertEqual(out, f.read())

    def test_known_words(self):
        out = run('src/decode.py', 'data/key.tsv', 'data/transcription.tsv')
        for w in ['lescitadinsladesirent', 'donerlaplace', 'delintelligencedanscetetat', 'legeneraldespostes', 'largent']:
            self.assertIn(w, out)

    def test_valued_share(self):
        out = run('src/decode.py', 'data/key.tsv', 'data/transcription.tsv')
        self.assertIn('symbols 897 valued 882 98.3%', out)

    def test_second_reading(self):
        out = run('src/compare.py', 'data/key.tsv', 'data/transcription.tsv',
                  'second/codex_pass1.txt', 'second/codex_pass2.txt', 'second/codex_pass3.txt')
        self.assertIn('same name 831 (92.6%)', out)
        self.assertIn('same name 826 (92.1%)', out)
        self.assertIn('same name 790 (88.1%)', out)

    def test_calibration(self):
        out = run('src/calib.py', 'data/key.tsv', 'calib/lasry_plain.tsv', 'calib/transcription_f79.tsv')
        self.assertIn('516/599 = 86.1%', out)


if __name__ == '__main__':
    unittest.main()
