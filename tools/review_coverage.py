"""Simulate how often older words come back under the rules in SKILL.md.

Usage: python3 tools/review_coverage.py skills/mandarinmaxxing/maps/hsk-1.md [pace]

Builds the parts from the map's Split lines (pace 3, 5 or 7, default 5), then
applies "Bring older words back": lines 3, 7, 14, 30 and 60 back in the Done
log, words chosen by turn (two per visit for lines over five words), at most
six per part, dropping the nearest lines first. The review of the previous
part is not counted. Reports the share of words that come back at least once
and at least twice, and the average number of older words per part.
"""
import sys

OFFSETS = [3, 7, 14, 30, 60]
CAP = 6


def parts(path, pace):
    idx = {3: 0, 5: 1, 7: 2}[pace]
    out, split, blocks = [], None, []

    def flush():
        if split is None:
            return
        i = 0
        for size in (int(x) for x in split[idx].split('-')):
            out.append(sum(blocks[i:i + size], []))
            i += size

    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            flush()
            split, blocks = None, []
        elif line.startswith('Split:'):
            split = [x.strip() for x in line[6:].split('/')]
        elif line.startswith('- ') and split is not None:
            blocks.append(line[2:].split())
    flush()
    return out


def simulate(ps):
    seen, loads = {}, []
    for i in range(len(ps)):
        picks = []  # (offset, line, word index)
        for k, off in enumerate(OFFSETS, 1):
            j = i - off
            if j < 0:
                continue
            n = len(ps[j])
            per = 1 if n <= 5 else 2
            for t in range(per):
                picks.append((off, j, ((k - 1) * per + t) % n))
        picks.sort(key=lambda p: -p[0])  # farthest first, so nearest are dropped
        picks = picks[:CAP]
        for _, j, w in picks:
            seen[(j, w)] = seen.get((j, w), 0) + 1
        loads.append(len(picks))
    words = [(j, w) for j in range(len(ps)) for w in range(len(ps[j]))]
    once = sum(seen.get(x, 0) >= 1 for x in words) / len(words)
    twice = sum(seen.get(x, 0) >= 2 for x in words) / len(words)
    return once, twice, sum(loads) / len(loads)


if __name__ == '__main__':
    path = sys.argv[1]
    pace = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    ps = parts(path, pace)
    once, twice, load = simulate(ps)
    print(f'{len(ps)} parts at pace {pace}: {once:.0%} of words come back at least once, '
          f'{twice:.0%} at least twice; {load:.1f} older words per part on average')
