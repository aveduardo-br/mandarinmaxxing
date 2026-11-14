"""Write the per-situation lesson splits into a level map.
usage: split_map.py <map.md>   (rewrites the file in place)"""
import sys, re
path = sys.argv[1]
PACES = [(3, 4), (5, 7), (7, 10)]  # pace, max new words per lesson
def split(n, hi, max_blocks=None):
    total = sum(n); k = -(-total // hi)
    while True:
        target = total / k; best = {(0, 0): (0, None)}
        for j in range(1, k + 1):
            for i in range(1, len(n) + 1):
                for p in range(i):
                    if (p, j - 1) in best and sum(n[p:i]) <= hi and (not max_blocks or i - p <= max_blocks):
                        c = best[(p, j - 1)][0] + (sum(n[p:i]) - target) ** 2
                        if c < best.get((i, j), (1e9,))[0]: best[(i, j)] = (c, p)
        if (len(n), k) in best: break
        k += 1
    out, i = [], len(n)
    for j in range(k, 0, -1): p = best[(i, j)][1]; out.append(i - p); i = p
    return out[::-1]
lines = [l for l in open(path, encoding='utf-8').read().split('\n') if not l.startswith('Split:')]
sits, cur = [], None
for idx, l in enumerate(lines):
    if l.startswith('## '): cur = {'head': idx, 'blocks': []}; sits.append(cur)
    elif l.startswith('- ') and cur: cur['blocks'].append(len(l[2:].split()))
totals = [0, 0, 0]; inserts = {}
for s_i, s in enumerate(sits):
    parts = []
    for p_i, (pace, hi) in enumerate(PACES):
        sp = split(s['blocks'], hi, 2 if s_i < 2 else None)
        totals[p_i] += len(sp); parts.append('-'.join(map(str, sp)))
    inserts[s['head']] = 'Split: ' + ' / '.join(parts)
out = []
for idx, l in enumerate(lines):
    if l.startswith('Source:'):
        l = re.sub(r'below: \d+ lessons\.', f'below: {len(sits)} lessons.', l)
        l = re.sub(r'Parts at paces 3 / 5 / 7: [\d /]+\.', f'Parts at paces 3 / 5 / 7: {totals[0]} / {totals[1]} / {totals[2]}.', l)
    out.append(l)
    if idx in inserts: out.append(inserts[idx])
open(path, 'w', encoding='utf-8').write('\n'.join(out))
print('parts at paces 3 / 5 / 7:', totals)
