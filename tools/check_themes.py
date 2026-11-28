"""Editorial warnings about the maps: words a situation leans on that come later, and
pairs of words that are taught in different parts.

Usage: python3 tools/check_themes.py

The rules below are written by hand: the script can't know by itself that a lesson about
a lost card wants 张 and 银行. It walks each level at paces 3, 5 and 7, in map order, and
prints one line per warning. A warning asks for a person's judgement; it is not an error,
and the script always exits 0. Add a rule when a lesson is found to miss a word.
"""
import importlib.util
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
spec = importlib.util.spec_from_file_location('course', os.path.join(ROOT, 'skills', 'mandarinmaxxing', 'course.py'))
course = importlib.util.module_from_spec(spec)
spec.loader.exec_module(course)

# level -> lesson -> words of the same level the situation leans on
WANTS = {3: {'18': ['张', '银行']}}
# level -> pairs that are easier to teach side by side
PAIRS = {2: [('进来', '进去'), ('上来', '上去'), ('下来', '下去')]}


def main():
    count = 0
    for level in range(1, 5):
        lessons = course.read_map(level)
        for pace in course.PACES:
            units = []
            for lesson in lessons:
                for k, blocks in enumerate(course.split_parts(lesson, course.PACES.index(pace)), 1):
                    units.append((lesson['num'], k, {course.bare(w) for b in blocks for w in b}))
            where = lambda word: [(i, n, k) for i, (n, k, ws) in enumerate(units) if word in ws]
            for num, words in WANTS.get(level, {}).items():
                end = max(i for i, (n, k, ws) in enumerate(units) if n == num)
                for word in words:
                    found = where(word)
                    if not found or found[0][0] > end:
                        at = f'{found[0][1]}.{found[0][2]}' if found else 'nowhere in this level'
                        print(f'HSK {level} pace {pace}: lesson {num} leans on {word}, taught later ({at})')
                        count += 1
            for a, b in PAIRS.get(level, []):
                fa, fb = where(a), where(b)
                if fa and fb and fa[0][0] != fb[0][0]:
                    print(f'HSK {level} pace {pace}: {a} ({fa[0][1]}.{fa[0][2]}) and {b} ({fb[0][1]}.{fb[0][2]}) are in different parts')
                    count += 1
    print(f'{count} warning(s) for a person to judge')


if __name__ == '__main__':
    main()
