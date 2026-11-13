"""Check a level map against the official list and simulate lesson slicing.
usage: check_map.py <vocabulary.csv> <map.md> <level-prefix e.g. 一级>"""
import csv, sys, collections
src, mapfile, level = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(src, encoding='utf-8-sig')) if r['级别'].startswith(level)]
pos = {r['词语']: r['词性'] for r in rows}
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
for name, lo, hi in [('light 1-4', 1, 4), ('standard 5-7', 5, 7), ('intensive 8-10', 8, 10)]:
    lessons = []
    for t, bs in sits:
        n = [len(b) for b in bs]; total = sum(n); k = -(-total // hi)
        while True:  # balanced contiguous split into k lessons, each <= hi
            target = total / k; INF = 1e9
            best = {(0, 0): (0, None)}
            for j in range(1, k + 1):
                for i in range(1, len(bs) + 1):
                    for p0 in range(i):
                        if (p0, j - 1) in best and sum(n[p0:i]) <= hi:
                            c = best[(p0, j - 1)][0] + (sum(n[p0:i]) - target) ** 2
                            if c < best.get((i, j), (INF,))[0]: best[(i, j)] = (c, p0)
            if (len(bs), k) in best: break
            k += 1
        cuts, i = [], len(bs)
        for j in range(k, 0, -1): p0 = best[(i, j)][1]; cuts.append((p0, i)); i = p0
        for a, b in reversed(cuts): lessons.append((t, [w for blk in bs[a:b] for w in blk]))
    sizes = collections.Counter(len(l) for _, l in lessons)
    under = sum(1 for _, l in lessons if len(l) < lo)
    print(f'{name}: {len(lessons)} lessons | sizes {dict(sorted(sizes.items()))} | below band: {under}')
    if '--show' in sys.argv:
        for i, (t, l) in enumerate(lessons, 1): print(f'  {i:02d} [{t.split("|")[0].strip()}] {" ".join(l)}')
sys.exit(0 if ok else 1)
