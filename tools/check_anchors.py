"""Check the anchor sentences of a level against its map.
usage: python3 tools/check_anchors.py 2        (level number)

qa/anchors/hsk-N.md holds one line per block of maps/hsk-N.md, under the same `## NN` lesson
numbers: `words of the block | one or two sentences`. A line passes when
- the sentences contain every word of the block, and
- every other word in them was already taught: all lower levels, this level's jump start
  (for a jump-start lesson, only the lessons before it), and this lesson up to this block.
That is the worst case: a learner who goes straight from the jump start to this lesson.
Whether a sentence sounds natural is for a person to judge."""
import csv, os, re, sys
n = int(sys.argv[1]); root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
skill = os.path.join(root, 'skills', 'mandarinmaxxing')
bare = lambda w: re.sub(r'\d', '', w)
EXTRA = {'没'}  # in every list only inside 没有, 没事, 没关系
def words(level):
    return {bare(r['word']) for r in csv.DictReader(open(os.path.join(skill, 'syllabus', f'hsk-{level}.csv'), encoding='utf-8-sig'))}
lessons, cur = [], None
for l in open(os.path.join(skill, 'maps', f'hsk-{n}.md'), encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cur = {'num': l[3:5], 'jump': 'jump-start' in l, 'blocks': []}; lessons.append(cur)
    elif l.startswith('- '): cur['blocks'].append(l[2:].split())
anchors, num = {}, None
path = os.path.join(root, 'qa', 'anchors', f'hsk-{n}.md')
for l in open(path, encoding='utf-8'):
    l = l.strip()
    if l.startswith('## '): num = l[3:5]
    elif '|' in l: w, s = l.split('|', 1); anchors[(num, w.strip())] = s.strip()
lower = set(EXTRA)
for m in range(1, n): lower |= words(m)
jump = {l['num']: {bare(w) for b in l['blocks'] for w in b} for l in lessons if l['jump']}
def uncovered(text, known):
    bad = []
    for seg in re.split(r'[，。？！、：；“”‘’《》（）\s0-9A-Za-z…—·]+', text):
        ok = [True] + [False] * len(seg)
        for i in range(1, len(seg) + 1):
            ok[i] = any(ok[j] and seg[j:i] in known for j in range(max(0, i - 6), i))
        if seg and not ok[-1]:
            i = 0
            while i < len(seg):
                for size in range(6, 0, -1):
                    if seg[i:i + size] in known: i += size; break
                else: bad.append(seg[i]); i += 1
    return bad
problems = total = 0
for l in lessons:
    known = set(lower)
    for num, ws in jump.items():
        if not l['jump'] or num < l['num']: known |= ws
    for b in l['blocks']:
        total += 1; known |= {bare(w) for w in b}; key = (l['num'], ' '.join(b)); s = anchors.pop(key, None)
        if s is None: print(f"{l['num']} no anchor: {' '.join(b)}"); problems += 1; continue
        missing = [w for w in b if bare(w) not in s]; bad = uncovered(s, known)
        if missing or bad:
            problems += 1
            print(f"{l['num']} {' '.join(b)} | {s}" + (f"  << block word not used: {' '.join(missing)}" if missing else '') + (f"  << not taught yet: {' '.join(bad)}" if bad else ''))
for (num, w) in anchors: print(f'{num} anchor for a block that is not in the map: {w}'); problems += 1
print(f'HSK {n}: {total} blocks, {problems} problems')
sys.exit(1 if problems else 0)
