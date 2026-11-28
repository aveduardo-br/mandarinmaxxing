"""The course's bookkeeping, so the tutor doesn't do it by hand.

Usage:
    python3 course.py overview LEVEL PACE
        The lessons of a level with their parts at that pace (3, 5 or 7) and the totals.
        Jump-start lessons come with their words, for asking a learner which they know.

    python3 course.py part COURSE.md [PLAN.txt] [--lesson N [--part K]]
        The brief for one part: by default the one in `Next`, or the lesson given (its first
        part not yet studied, or the part given, for practice). It prints the new words, what
        the review covers, older words to bring back, reminders for lessons marked (known),
        whether the part is an early one, how many exercises each step has, and what `Next`
        becomes. With PLAN.txt, it also writes that file's header, ready for check_plan.py.

    python3 course.py progress COURSE.md
        Parts done and parts in the level, for the course screen: lessons marked (known)
        are left out of both numbers.

COURSE.md is the learner's course file. If the chat holds it as a project document and
not as a file where code runs, save a copy first and pass that copy. The script only
reads it: saving the course is the tutor's step.

It stops with a message, and exit code 1, when the file contradicts itself: a lesson
twice on the route, the same part twice in Done, a Done line with no words, a `Next`
it can't read or that points to a lesson marked (known).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACES = (3, 5, 7)
BACK = (3, 7, 14, 30, 60)  # lines back in the Done log that give a word to reuse
NEXT = re.compile(r'^lesson\s+(\d+)\s*,?\s*part\s+(\d+)(?:\s+of\s+(\d+))?$', re.I)


def bare(word):
    return re.sub(r'\d+$', '', word)


def nearest_pace(pace):
    return 3 if pace <= 4 else 5 if pace <= 6 else 7


def read_map(level):
    path = os.path.join(HERE, 'maps', f'hsk-{level}.md')
    if not os.path.exists(path):
        sys.exit(f'HSK {level} has no map yet: levels 1 to 4 are mapped.')
    lessons = []
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('## '):
            num, kind, name = [x.strip() for x in line[3:].split('|')]
            lessons.append({'num': num, 'jump': kind == 'jump-start', 'name': name, 'blocks': [], 'split': None})
        elif line.startswith('Split:') and lessons:
            lessons[-1]['split'] = [[int(n) for n in seg.strip().split('-')] for seg in line[6:].split('/')]
        elif line.startswith('- ') and lessons:
            lessons[-1]['blocks'].append(line[2:].split())
    return lessons


def split_parts(lesson, split_index):
    """The lesson's parts, each a list of blocks, for one of the three paces."""
    out, i = [], 0
    for count in lesson['split'][split_index]:
        out.append(lesson['blocks'][i:i + count])
        i += count
    return out


def level_words(level):
    path = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    out = set()
    if os.path.exists(path):
        for line in list(open(path, encoding='utf-8-sig'))[1:]:
            cols = line.split(',')
            if len(cols) > 1:
                out.add(bare(cols[1]))
    return out


def overview(level, pace):
    lessons, idx = read_map(level), PACES.index(nearest_pace(pace))
    total = 0
    for group, label in ((True, 'JUMP START'), (False, 'SITUATIONS')):
        rows = [l for l in lessons if l['jump'] == group]
        if rows:
            print(label)
        for l in rows:
            n = len(l['split'][idx])
            total += n
            words = ': ' + ' '.join(w for b in l['blocks'] for w in b) if group else ''
            print(f"  {l['num']} {l['name']} ({n} part{'s' if n != 1 else ''}){words}")
    print(f'TOTAL: {len(lessons)} lessons, {total} parts at pace {PACES[idx]}: about {round(total / 7)} weeks at one part a day')


def read_course(path):
    c = {'level': 1, 'pace': 5, 'next': None, 'route': '', 'reinforce': '', 'lessons': {}, 'done': [],
         'old_known': False, 'notes': []}
    section = None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if line.startswith('## '):
            section = line[3:].strip().lower()
            continue
        if not line:
            continue
        if section not in ('lessons', 'done'):
            low = line.lower()
            if 'syllabus:' in low:
                found = re.search(r'level\s*(\d)', low)
                c['level'] = int(found.group(1)) if found else 1
            elif 'pace:' in low:
                found = re.search(r'\d+', low.split('pace:', 1)[1])
                pace = int(found.group()) if found else 0
                if pace not in PACES:
                    c['notes'].append(f'Pace is {pace or "missing"}: using {nearest_pace(pace or 5)}, the nearest of 3, 5 and 7. Save that in the file.')
                c['pace'] = nearest_pace(pace or 5)
            elif 'route:' in low:
                c['route'] = line.split(':', 1)[1].strip()
            elif 'next:' in low:
                c['next'] = line.split(':', 1)[1].strip()
            elif 'to reinforce:' in low:
                c['reinforce'] = line.split(':', 1)[1].strip()
            elif 'known:' in low and 'jump' in low:
                c['old_known'] = True
        elif section == 'lessons':
            found = re.match(r'(\d\d)\s+(.*)', line)
            if found:
                text = found.group(2)
                known = bool(re.search(r'\(known\)\s*$', text))
                name = re.sub(r'\s*\([^()]*\)\s*$', '', text)
                c['lessons'][found.group(1)] = {'name': name, 'known': known}
        elif section == 'done':
            found = re.match(r'(?:(\d)-)?(\d\d)\.(\d+)\s*\|(.*)', line)
            if not found:
                sys.exit(f"Can't read this Done line: {line}\nA Done line looks like `1-02.1 | 我 要 水 茶`.")
            words = found.group(4).split()
            if not words:
                sys.exit(f'This Done line has no words: {line}')
            c['done'].append({'level': int(found.group(1) or c['level']), 'lesson': found.group(2), 'part': int(found.group(3)),
                              'words': words, 'raw': line})
    seen = set()
    for d in c['done']:
        key = (d['level'], d['lesson'], d['part'])
        if key in seen:
            sys.exit(f"Done has the part {d['level']}-{d['lesson']}.{d['part']} twice: delete the extra line.")
        seen.add(key)
    return c


def route_lessons(text):
    out = []
    for piece in re.split(r'[,;]', text):
        nums = re.findall(r'\d+', piece)
        if len(nums) == 2 and re.search(r'[–—-]', piece):
            out += [str(n).zfill(2) for n in range(int(nums[0]), int(nums[1]) + 1)]
        else:
            out += [n.zfill(2) for n in nums]
    twice = sorted({n for n in out if out.count(n) > 1})
    if twice:
        sys.exit('Route lists a lesson more than once (' + ' '.join(twice) + '): each lesson goes on the route once.')
    return out


def lesson_state(lesson, done_lines, pace):
    """Where a lesson stands, from the words Done actually holds for it.

    Returns (parts, studied): `parts` is the whole lesson as a list of parts (each a list of
    blocks) and `studied` how many of them are done. A lesson begun at another pace keeps
    that pace's split: the split is the one whose first parts match the Done lines. If no
    split matches (a file edited by hand), the blocks already in Done count as one studied
    part and the rest is divided at the current pace."""
    lines = sorted(done_lines, key=lambda d: d['part'])
    current = PACES.index(pace)
    if not lines:
        return split_parts(lesson, current), 0
    had = [set(d['words']) for d in lines]
    for idx in [current] + [i for i in range(3) if i != current]:
        parts = split_parts(lesson, idx)
        if len(parts) >= len(had) and all({w for b in parts[i] for w in b} == had[i] for i in range(len(had))):
            return parts, len(had)
    known = set().union(*had)
    studied = [b for b in lesson['blocks'] if set(b) <= known]
    rest = [b for b in lesson['blocks'] if not set(b) <= known]
    parts, size, group = [studied], 0, []
    for b in rest:
        if group and size + len(b) > pace + 1:
            parts.append(group)
            group, size = [], 0
        group.append(b)
        size += len(b)
    if group:
        parts.append(group)
    return parts, 1


def older_candidates(done):
    """Older words to bring back: for each distance in BACK that the log reaches, the Done
    line that many parts back and two of its words, taken by turn (every word from the
    fifth on for the farthest line). tools/review_coverage.py measures this same choice."""
    out = []
    for turn, back in enumerate(BACK):
        if len(done) < back:
            continue
        line = done[-back]
        words = line['words']
        if turn == len(BACK) - 1 and len(words) > turn + 1:
            pick = words[turn:]
        else:
            pick = list(dict.fromkeys(words[(turn + j) % len(words)] for j in range(2)))
        out.append((back, line, pick))
    return out


def load(course_path):
    c = read_course(course_path)
    level = c['level']
    lessons = read_map(level)
    by_num = {l['num']: l for l in lessons}
    known = sorted(n for n, l in c['lessons'].items() if l['known'] and n in by_num)
    if c['old_known']:
        studied = {d['lesson'] for d in c['done'] if d['level'] == level}
        known = sorted(set(known) | {l['num'] for l in lessons if l['jump'] and l['num'] not in studied})
        c['notes'].append('The file has the old `Known: jump start` line. Mark these lessons (known), take them off the route, delete the line: ' + ' '.join(known))
    route_lessons(c['route'])  # stops here if the route repeats a lesson
    here = [d for d in c['done'] if d['level'] == level]
    state = {n: lesson_state(by_num[n], [d for d in here if d['lesson'] == n], c['pace']) for n in by_num}
    return c, lessons, by_num, known, state


def next_on_route(c, by_num, known, state, after=None):
    """The first part still to study: on the route from lesson `after` on, then before it."""
    route = [n for n in route_lessons(c['route']) if n in by_num and n not in known]
    order = route
    if after in route:
        i = route.index(after)
        order = route[i:] + route[:i]
    for n in order:
        parts, studied = state[n]
        if studied < len(parts):
            return f'Lesson {n}, part {studied + 1} of {len(parts)}'
    return 'level complete'


def part(course_path, plan_path=None, want_lesson=None, want_part=None):
    c, lessons, by_num, known, state = load(course_path)
    level, done = c['level'], c['done']
    practice = False
    if want_lesson:
        num = str(want_lesson).zfill(2)
        if num not in by_num:
            sys.exit(f'HSK {level} has no lesson {num}.')
        parts, studied = state[num]
        k = want_part or min(studied + 1, len(parts))
        practice = k <= studied
    else:
        if c['next'] is None or not c['next'].strip():
            sys.exit('The file has no `Next` line, or it is empty. From the route and Done it should be: ' + next_on_route(c, by_num, known, state))
        if 'complete' in c['next'].lower():
            still = next_on_route(c, by_num, known, state)
            if still != 'level complete':
                sys.exit(f'Next says the level is complete, but the route still has {still}. Set Next to that.')
            sys.exit('Next says the level is complete: read levels.md.')
        found = NEXT.match(c['next'].strip().strip('`'))
        if not found:
            sys.exit(f"Can't read the Next line: `{c['next']}`. It should read like `Lesson 02, part 1 of 2`.")
        num, k = found.group(1).zfill(2), int(found.group(2))
        if num not in by_num:
            sys.exit(f'HSK {level} has no lesson {num}.')
        if num in known:
            sys.exit(f'Next points to Lesson {num}, which is marked (known). Remove the mark to study it, or set Next to: ' + next_on_route(c, by_num, known, state))
        parts, studied = state[num]
        if studied >= len(parts):
            sys.exit(f'Next points to Lesson {num}, part {k}, but Done holds the whole lesson. Set Next to: ' + next_on_route(c, by_num, known, state, num))
        if k != studied + 1:
            c['notes'].append(f'Next says part {k}, but Done holds {studied} part(s) of Lesson {num}: this is part {studied + 1} of {len(parts)}. Correct Next when you save.')
            k = studied + 1
        elif found.group(3) and int(found.group(3)) != len(parts):
            c['notes'].append(f'Next says "of {found.group(3)}", but Lesson {num} has {len(parts)} part(s) here. Correct it when you save.')
    if not 1 <= k <= len(parts):
        sys.exit(f'Lesson {num} has {len(parts)} part(s) here, not a part {k}.')
    blocks = parts[k - 1]
    new = [w for b in blocks for w in b]
    name = c['lessons'].get(num, {}).get('name') or by_num[num]['name']

    known_words = [w for n in known for b in by_num[n]['blocks'] for w in b]
    below = set().union(*[level_words(n) for n in range(1, level)]) if level > 1 else set()
    met = below | {bare(w) for d in done for w in d['words']} | {bare(w) for w in known_words}
    early = len(met) < 20

    for note in c['notes']:
        print('NOTE: ' + note)
    print(f"PART: HSK {level} · Lesson {int(num)} · {name}" + (f' · part {k} of {len(parts)}' if len(parts) > 1 else ''))
    if practice:
        print('PRACTICE: this part is already in Done. Teach it as practice and leave Next and Done as they are.')
    print('NEW WORDS, in blocks that work together: ' + ' | '.join(' '.join(b) for b in blocks))
    last = done[-1] if done else None
    reinforce = '' if c['reinforce'].lower() in ('', 'none') else c['reinforce']
    if last:
        how = 'the lines of' if early else 'one prompt per word of'
        print(f"REVIEW: {how} {last['raw'].split('|')[0].strip()}: " + ' '.join(last['words']))
        if reinforce:
            print('  and the items to reinforce, once each: ' + reinforce)
    else:
        print('REVIEW: none, nothing studied yet. Start at the vocabulary.')
    older = older_candidates(done)
    if older:
        print('OLDER WORDS: use one from each line, the one that fits a sentence best:')
        for back, line, pick in older:
            key = line['raw'].split('|')[0].strip()
            print(f'  {back} back ({key}): ' + (' or '.join(pick) if len(pick) <= 2 else 'any of ' + ' '.join(pick)))
    if known:
        print('KNOWN LESSONS (never shown by the course): ' + ' '.join(known))
        print('  their words: ' + ' '.join(known_words))
        print('  they count as met; list the ones this part uses under the table, with pinyin and meaning')
    n = len(new)
    print(f'EARLY PART: {"yes: read first-parts.md" if early else "no"} ({len(met)} words met before this part)')
    if early:
        print('ROUNDS AND LAST STEP: as first-parts.md says')
    else:
        per = min(5, n)
        more = '' if per == 5 else ' (up to 5 when the words have that many different contexts)'
        print(f'ROUNDS: three rounds of {per} prompt{"s" if per != 1 else ""}{more}; every new word in at least three prompts')
        print('LAST STEP: with audio, the dictation, and the narration when the met words carry it (audio.md); without, one reading')
    if practice:
        print('AT THE CLOSE: nothing to save')
    else:
        state[num] = (parts, k)
        if k < len(parts):
            nxt = f'Lesson {num}, part {k + 1} of {len(parts)}'
        elif num not in route_lessons(c['route']):
            nxt = None
        else:
            nxt = next_on_route(c, by_num, known, state, num)
        print(f"AT THE CLOSE: add `{level}-{num}.{k} | {' '.join(new)}` to Done; " + (f'Next becomes `{nxt}`' if nxt else 'Next stays as it is: this lesson is not on the route'))

    if plan_path:
        head = [f'LEVEL {level}']
        if known:
            head.append('KNOWN ' + ' '.join(known))
        if early:
            head.append('EARLY')
        head.append('NEW ' + ' '.join(new))
        head.append('DONE')
        head += [d['raw'] for d in done]
        head.append('PLAN')
        open(plan_path, 'w', encoding='utf-8').write('\n'.join(head) + '\n')
        print(f'PLAN HEADER written to {plan_path}: add a SUPPORT or NAMES line above DONE if the part needs one, and the plan lines at the end.')


def progress(course_path):
    c, lessons, by_num, known, state = load(course_path)
    active = [n for n in by_num if n not in known]
    done = sum(state[n][1] for n in active)
    total = sum(len(state[n][0]) for n in active)
    print(f'{done}/{total}')
    print(f'HSK {c["level"]}: {done} of {total} parts done' + (f' ({len(known)} lesson(s) marked known are left out)' if known else ''))
    print('NEXT: ' + next_on_route(c, by_num, known, state))


def main(argv):
    if len(argv) >= 3 and argv[0] == 'overview':
        return overview(int(argv[1]), int(argv[2]))
    if len(argv) >= 2 and argv[0] == 'progress':
        return progress(argv[1])
    if len(argv) >= 2 and argv[0] == 'part':
        rest, lesson, k = argv[1:], None, None
        if '--lesson' in rest:
            i = rest.index('--lesson')
            lesson = int(rest[i + 1])
            del rest[i:i + 2]
        if '--part' in rest:
            i = rest.index('--part')
            k = int(rest[i + 1])
            del rest[i:i + 2]
        return part(rest[0], rest[1] if len(rest) > 1 else None, lesson, k)
    sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
