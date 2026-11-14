"""Extra checks on a level map, beyond check_map.py. Prints things to read, not errors.
usage: python3 tools/qa_map.py skills/mandarinmaxxing/maps/hsk-2.md
- words per lesson, and the size of every part at paces 3 / 5 / 7
- pairs of words in one block that share a character (possible look-alikes)
- compounds taught before the shorter word they contain, in the same lesson"""
import re, sys, collections
bare = lambda w: re.sub(r'\d', '', w)
lessons, cur = [], None
for l in open(sys.argv[1], encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cur = {'num': l[3:5], 'split': None, 'blocks': []}; lessons.append(cur)
    elif l.startswith('Split:'): cur['split'] = [[int(x) for x in s.strip().split('-')] for s in l[6:].split('/')]
    elif l.startswith('- '): cur['blocks'].append([bare(w) for w in l[2:].split()])
sizes = [(l['num'], sum(map(len, l['blocks']))) for l in lessons]
print('lessons:', len(lessons), '| words per lesson: min', min(s for _, s in sizes), 'max', max(s for _, s in sizes))
for i, (pace, hi) in enumerate([(3, 4), (5, 7), (7, 10)]):
    parts = []
    for l in lessons:
        if not l['split'] or sum(l['split'][i]) != len(l['blocks']): print('  Split line does not match the blocks: lesson', l['num']); continue
        j = 0
        for k in l['split'][i]: parts.append((l['num'], sum(map(len, l['blocks'][j:j + k])))); j += k
    count = collections.Counter(s for _, s in parts)
    print(f'pace {pace}: {len(parts)} parts, words per part {dict(sorted(count.items()))}, over {hi}: {[p for p in parts if p[1] > hi] or "none"}')
    print('  most parts in one lesson:', max(collections.Counter(n for n, _ in parts).values()))
shared = [f"{l['num']}:{a}/{b}" for l in lessons for bl in l['blocks'] for x, a in enumerate(bl) for b in bl[x + 1:] if set(a) & set(b)]
print('share a character inside a block:', ' '.join(shared) or 'none')
late = [f"{l['num']}:{w}<{base}" for l in lessons for i, bl in enumerate(l['blocks']) for w in bl if len(w) > 1
        for later in l['blocks'][i + 1:] for base in later if base != w and base in w]
print('compound before its base, same lesson:', ' '.join(late) or 'none')
