"""Check a level map the tutor built against the official word list.

Usage: python3 check_map.py map-hsk-5.md 5

Reports official words the map leaves out, words that aren't in the level's list,
words used more often than the list has them, and blocks that aren't two to four words.
"""
import collections
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(mapfile, level):
    src = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    official = collections.Counter(r['word'] for r in csv.DictReader(open(src, encoding='utf-8-sig')))
    blocks = []
    for line in open(mapfile, encoding='utf-8'):
        line = line.strip()
        if line.startswith('- '):
            blocks.append(line[2:].split())
    seen = collections.Counter(w for b in blocks for w in b)
    missing = [w for w in official if seen[w] < official[w]]
    extra = [w for w in seen if w not in official]
    repeated = [w for w, c in seen.items() if w in official and c > official[w]]
    badsize = [' '.join(b) for b in blocks if not 2 <= len(b) <= 4]
    print(f'official {sum(official.values())} | mapped {sum(seen.values())} | blocks {len(blocks)}')
    ok = True
    for label, items in (('MISSING', missing), ('NOT IN THE LIST', extra), ('REPEATED', repeated), ('BLOCK NOT 2-4 WORDS', badsize)):
        if items:
            ok = False
            print(f'{label} ({len(items)}): ' + ' '.join(items[:200]))
    if ok:
        print('OK: every official word appears exactly once, in blocks of two to four.')
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
