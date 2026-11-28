"""Check a level map the tutor built against the official word list.

Usage: python3 check_map.py map-hsk-5.md 5 [pace]

Reports official words the map leaves out, words that aren't in the level's list,
words used more often than the list has them, and blocks that aren't two to four words.
Every word is listed, however many there are. With a pace, it also prints the parts of
each lesson at that pace (whole blocks, until the next would pass the pace by more than
one word) and their total: the numbers the course overview needs.
"""
import collections
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def parts_at(blocks, pace):
    """Sizes of a lesson's parts: whole blocks until the next would pass the pace by more than one word."""
    parts, size = [], 0
    for b in blocks:
        if size and size + len(b) > pace + 1:
            parts.append(size)
            size = 0
        size += len(b)
    return parts + [size] if size else parts


def main(mapfile, level, pace=None):
    src = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    official = collections.Counter(r['word'] for r in csv.DictReader(open(src, encoding='utf-8-sig')))
    blocks, lessons = [], []
    for line in open(mapfile, encoding='utf-8'):
        line = line.strip()
        if line.startswith('## '):
            lessons.append((line[3:], []))
        elif line.startswith('- '):
            blocks.append(line[2:].split())
            if lessons:
                lessons[-1][1].append(blocks[-1])
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
            print(f'{label} ({len(items)}): ' + ' '.join(items))
    if ok:
        print('OK: every official word appears exactly once, in blocks of two to four.')
    if pace:
        total = 0
        for title, bs in lessons:
            sizes = parts_at(bs, pace)
            total += len(sizes)
            print(f'{title.split("|")[0].strip()}: {len(sizes)} parts ({"-".join(map(str, sizes))} words)')
        print(f'PARTS AT PACE {pace}: {total} in {len(lessons)} lessons')
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    if not os.path.exists(os.path.join(HERE, 'syllabus', f'hsk-{sys.argv[2]}.csv')):
        sys.exit(f'No word list for level {sys.argv[2]}: levels are 1 to 6.')
    sys.exit(main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) == 4 else None))
