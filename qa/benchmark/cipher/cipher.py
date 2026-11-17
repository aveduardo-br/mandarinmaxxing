"""Cipher layer for the "ciphered student" benchmark.

The tutor teaches real Mandarin. Before a tutor message reaches the student, every Chinese word
is replaced by a nonsense token and all pinyin is removed, so the student can only know what the
tutor has actually taught. The student answers in tokens; decode turns them back into Hanzi for
the tutor.

Usage (paths relative to the repository root):
  python3 qa/benchmark/cipher/cipher.py encode <in.md> <out.md>
  python3 qa/benchmark/cipher/cipher.py decode <in.md> <out.md>

The token table is built from the syllabus (levels 1 to 6) and is deterministic. It is written
to qa/benchmark/cipher/.secret-map.json the first time; the student must never read that file.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
MAP_FILE = os.path.join(HERE, '.secret-map.json')
HAN = r'一-鿿'
TONED = 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ'
PLAIN = str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü', 'aaaaeeeeiiiioooouuuuvvvvv')
INITIALS = ['zh', 'ch', 'sh', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's', 'y', 'w', '']
FINALS = ['iang', 'iong', 'uang', 'ueng', 'ang', 'eng', 'ing', 'ong', 'ian', 'iao', 'uai', 'uan', 'van', 'ai', 'ei', 'ao', 'ou',
          'an', 'en', 'in', 'un', 'vn', 'ia', 'ie', 'iu', 'ua', 'uo', 'ui', 've', 'er', 'a', 'o', 'e', 'i', 'u', 'v']
SYLL = re.compile('^(?:(?:' + '|'.join(INITIALS[:-1]) + ')?(?:' + '|'.join(FINALS) + '))+$')


def is_pinyin(span):
    """True when every word of the span is made of pinyin syllables (tones optional) and at
    least one has a tone mark, so Portuguese italics like *Frases úteis* are left alone."""
    words = re.findall(r"[A-Za-z" + TONED + "ü']+", span)
    if not words or not any(c in TONED for c in span):
        return False
    if re.search(r'[ãõçâêôàÃÕÇ]', span):
        return False
    return all(SYLL.match(w.lower().replace("'", '').translate(PLAIN)) for w in words)
CONS = 'bdfgklmnprstvz'
VOWS = 'aeiou'


def _token(word, used):
    n_syll = 1 + len(word)  # 1 char -> 2 syllables, 2 chars -> 3, ...
    salt = 0
    while True:
        h = hashlib.sha1(f'{word}:{salt}'.encode()).digest()
        tok = ''.join(CONS[h[2 * i] % len(CONS)] + VOWS[h[2 * i + 1] % len(VOWS)] for i in range(n_syll)) + 'q'
        if tok not in used:
            used.add(tok)
            return tok
        salt += 1


def build_map():
    if os.path.exists(MAP_FILE):
        return json.load(open(MAP_FILE, encoding='utf-8'))
    words, chars = set(), set()
    for n in range(1, 7):
        path = os.path.join(ROOT, 'skills', 'mandarinmaxxing', 'syllabus', f'hsk-{n}.csv')
        for line in list(open(path, encoding='utf-8'))[1:]:
            w = re.sub(r'\d+$', '', line.split(',')[1].strip())
            if re.fullmatch(f'[{HAN}]+', w):
                words.add(w)
                chars.update(w)
    used, table = set(), {}
    for w in sorted(words | chars, key=lambda x: (len(x), x)):
        table[w] = _token(w, used)
    json.dump(table, open(MAP_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    return table


def _segment(run, table):
    out, i = [], 0
    while i < len(run):
        for L in range(min(4, len(run) - i), 0, -1):
            piece = run[i:i + L]
            if piece in table or L == 1:
                out.append(piece)
                i += L
                break
    return out


def _drop_pinyin_columns(text):
    """In Markdown tables whose header has a Pinyin column, remove that column."""
    out, drop = [], None
    for line in text.split('\n'):
        if line.lstrip().startswith('|'):
            cells = line.strip().strip('|').split('|')
            if drop is None and any(c.strip().lower() == 'pinyin' for c in cells):
                drop = [i for i, c in enumerate(cells) if c.strip().lower() == 'pinyin'][0]
            if drop is not None and drop < len(cells):
                cells = cells[:drop] + cells[drop + 1:]
                line = '| ' + ' | '.join(c.strip() for c in cells) + ' |'
        else:
            drop = None
        out.append(line)
    return '\n'.join(out)


def encode(text, table):
    # what the student must not see: the benchmark's expected answers and every piece of pinyin.
    # Pinyin is written in italics (lesson-format.md) and in the table's Pinyin column; Portuguese
    # shares the accented letters, so nothing outside those two places is touched.
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', lambda m: '' if is_pinyin(m.group(1)) else m.group(0), text)
    text = _drop_pinyin_columns(text)
    text = re.sub(r'\(\s*,\s*', '(', text)
    text = re.sub(r'\(\s*\)', '', text)

    def repl(m):
        toks = []
        for piece in _segment(m.group(0), table):
            if piece not in table:  # a character outside the syllabus gets a stable token too
                table[piece] = _token(piece, set(table.values()))
            toks.append(table[piece])
        return ' ' + ' '.join(toks) + ' '

    text = re.sub(f'[{HAN}]+', repl, text)
    return re.sub(r'[ \t]+', ' ', text).replace(' \n', '\n')


def decode(text, table):
    back = {v: k for k, v in table.items()}
    # every token ends in q, which no Portuguese word does, so Portuguese is never touched
    out = re.sub(r'\b[a-z]+q\b', lambda m: back.get(m.group(0), m.group(0)), text)
    out = re.sub(f'(?<=[{HAN}]) (?=[{HAN}])', '', out)
    return re.sub(f'(?<=[{HAN}]) (?=[，。！？、；：])', '', out)


if __name__ == '__main__':
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    table = build_map()
    text = open(src, encoding='utf-8').read()
    result = encode(text, table) if mode == 'encode' else decode(text, table)
    json.dump(table, open(MAP_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    open(dst, 'w', encoding='utf-8').write(result)
