"""Check a level map against the official word list in this repository.
usage: python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md"""
import csv, sys, collections, os, re
mapfile = sys.argv[1]
n = re.search(r'hsk-(\d)\.md$', mapfile).group(1)
src = os.path.join(os.path.dirname(os.path.abspath(mapfile)), '..', 'syllabus', f'hsk-{n}.csv')
rows = list(csv.DictReader(open(src, encoding='utf-8-sig')))
pos = {r['word']: r['part_of_speech'] for r in rows}
official = list(pos)
sits = []  # (title, [blocks])
for line in open(mapfile, encoding='utf-8'):
    line = line.strip()
    if line.startswith('## '): sits.append((line[3:], []))
    elif line.startswith('- '): sits[-1][1].append(line[2:].split())
seen = collections.Counter(w for _, bs in sits for b in bs for w in b)
ok = True
missing = [w for w in official if w not in seen]
extra = [w for w in seen if w not in pos]
dup = [w for w, c in seen.items() if c > 1]
badsize = [(t, b) for t, bs in sits for b in bs if not 2 <= len(b) <= 4]
print(f'official {len(official)} | mapped {sum(seen.values())} | situations {len(sits)} | blocks {sum(len(bs) for _, bs in sits)}')
for label, v in [('missing', missing), ('not in list', extra), ('duplicated', dup), ('block size not 2-4', badsize)]:
    print(f'{label}: {v if v else "none"}'); ok &= not v
def content(b):  # block has something besides nouns / numerals / measure words
    return any(not set(p for p in pos[w].replace('（', '、').replace('）', '').split('、') if p) <= {'名', '数', '量', '数量'} or not pos[w] for w in b)
weak = [(t.split('|')[0].strip(), ' '.join(b)) for t, bs in sits for b in bs if not content(b)]
print('blocks with only nouns/numerals/measure words:', weak if weak else 'none')
parts = [0, 0, 0]
for line in open(mapfile, encoding='utf-8'):
    if line.startswith('Split:'):
        for i, seg in enumerate(line[6:].split('/')): parts[i] += len(seg.strip().split('-'))
print('parts at paces 3 / 5 / 7:', ' / '.join(map(str, parts)))
sys.exit(0 if ok else 1)
