"""Measure how often older words come back, with the same choice the lessons use.

Usage: python3 tools/review_coverage.py LEVEL [PACE]

Walks a level part by part at a pace (3, 5 or 7, default 5), in map order, and asks
skills/mandarinmaxxing/course.py for the older words each part would be offered
(`older_candidates`: two candidates from the lines 3, 7, 14, 30 and 60 back). It reports
the share of words that are offered at least once, and the share that come back when the
tutor always takes the first candidate or always the second. The review of the previous
part is not counted. The tutor may skip a line when neither word fits, so these are upper
bounds, and distances are counted in parts, not in days.
"""
import importlib.util
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
spec = importlib.util.spec_from_file_location('course', os.path.join(ROOT, 'skills', 'mandarinmaxxing', 'course.py'))
course = importlib.util.module_from_spec(spec)
spec.loader.exec_module(course)


def main(level, pace=5):
    idx = course.PACES.index(pace)
    done, offered, first, second, loads = [], set(), set(), set(), []
    for lesson in course.read_map(level):
        for k, blocks in enumerate(course.split_parts(lesson, idx), 1):
            picks = course.older_candidates(done)
            loads.append(len(picks))
            for back, line, pick in picks:
                key = line['raw']
                offered.update((key, w) for w in pick)
                first.add((key, pick[0]))
                second.add((key, pick[-1] if len(pick) <= 2 else pick[1]))
            words = [w for b in blocks for w in b]
            done.append({'words': words, 'raw': f"{level}-{lesson['num']}.{k}"})
    total = sum(len(d['words']) for d in done)
    print(f'HSK {level}, pace {pace}: {len(done)} parts, {total} words')
    print(f'  offered at least once: {len(offered) / total:.0%}')
    print(f'  come back if the tutor always takes the first candidate: {len(first) / total:.0%}; always the second: {len(second) / total:.0%}')
    print(f'  older-word lines per part: {sum(loads) / len(loads):.1f} on average, {max(loads)} at most')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 5)
