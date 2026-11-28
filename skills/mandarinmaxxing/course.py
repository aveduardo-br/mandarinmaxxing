"""The course's bookkeeping, so the tutor doesn't do it by hand.

Usage:
    python3 course.py overview LEVEL PACE
        The lessons of a level with their parts at that pace (3, 5 or 7) and the totals.
        Jump-start lessons come with their words, for asking a learner which they know.

    python3 course.py part COURSE.md [PLAN.txt] [--lesson N [--part K]]
        The brief for one part: by default the one in `Next`, or the lesson and part given.
        It prints the new words, what the review covers, older words to bring back,
        reminders for lessons marked (known), whether the part is an early one, and how
        many exercises each step has. With PLAN.txt, it also writes that file's header
        (everything above the PLAN line), ready for check_plan.py.

COURSE.md is the learner's course file. If the chat holds it as a project document and
not as a file where code runs, save a copy first and pass that copy.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACES = (3, 5, 7)
BACK = (3, 7, 14, 30, 60)  # lines back in the Done log that give a word to reuse


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


def parts_of(lesson, split_index):
    """The lesson's parts as lists of words, for one of the three paces."""
    out, i = [], 0
    for count in lesson['split'][split_index]:
        out.append(lesson['blocks'][i:i + count])
        i += count
    return out


def level_size(level):
    path = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    return max(0, sum(1 for _ in open(path, encoding='utf-8')) - 1) if os.path.exists(path) else 0


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
    weeks = round(total / 7)
    print(f'TOTAL: {len(lessons)} lessons, {total} parts at pace {PACES[idx]}: about {weeks} weeks at one part a day')


def read_course(path):
    c = {'level': 1, 'pace': 5, 'next': '', 'route': '', 'reinforce': '', 'lessons': {}, 'done': [], 'old_known': False}
    section = None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if line.startswith('## '):
            section = line[3:].strip().lower()
            continue
        if not line:
            continue
        if section is None or section not in ('lessons', 'done'):
            low = line.lower()
            if 'syllabus:' in low:
                found = re.search(r'level\s*(\d)', low)
                c['level'] = int(found.group(1)) if found else 1
            elif 'pace:' in low:
                found = re.search(r'\d+', low.split('pace:', 1)[1])
                c['pace'] = int(found.group()) if found else 5
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
                parts = re.search(r'\((\d+)\s+\S+\)\s*$', text)
                name = re.sub(r'\s*\([^()]*\)\s*$', '', text)
                c['lessons'][found.group(1)] = {'name': name, 'known': known, 'parts': int(parts.group(1)) if parts else None}
        elif section == 'done' and '|' in line:
            key, words = line.split('|', 1)
            key = key.strip()
            found = re.match(r'(?:(\d)-)?(\d\d)\.(\d+)', key)
            if found:
                c['done'].append({'level': int(found.group(1) or 0), 'lesson': found.group(2), 'part': int(found.group(3)),
                                  'words': words.split(), 'raw': line})
    for d in c['done']:
        d['level'] = d['level'] or c['level']
    return c


def split_index_for(lesson, pace, of=None, begun=0):
    """Which of the three splits a lesson uses: the pace's, unless the lesson was begun at
    another pace (its `of N` or its Done lines then tell which)."""
    idx = PACES.index(nearest_pace(pace))
    counts = [len(s) for s in lesson['split']]
    if of and counts[idx] != of and of in counts:
        return counts.index(of)
    if begun and begun > counts[idx]:
        fits = [i for i, n in enumerate(counts) if n >= begun]
        return fits[0] if fits else idx
    return idx


def route_lessons(text):
    out = []
    for piece in re.split(r'[,;]', text):
        nums = re.findall(r'\d+', piece)
        if len(nums) == 2 and re.search(r'[–—-]', piece):
            out += [str(n).zfill(2) for n in range(int(nums[0]), int(nums[1]) + 1)]
        else:
            out += [n.zfill(2) for n in nums]
    return out


def part(course_path, plan_path=None, want_lesson=None, want_part=None):
    c = read_course(course_path)
    level = c['level']
    lessons = read_map(level)
    by_num = {l['num']: l for l in lessons}
    known = sorted(n for n, l in c['lessons'].items() if l['known'])
    if c['old_known']:
        studied = {d['lesson'] for d in c['done'] if d['level'] == level}
        known = sorted(set(known) | {l['num'] for l in lessons if l['jump'] and l['num'] not in studied})
        print('NOTE: the file has the old `Known: jump start` line. Mark these lessons (known), take them off the route, delete the line: ' + ' '.join(known))

    of = None
    if want_lesson:
        num, k = str(want_lesson).zfill(2), want_part or 1
    else:
        if 'complete' in c['next'].lower() or not c['next']:
            sys.exit('Next says the level is complete (or is empty): read levels.md.')
        found = re.search(r'(\d+)\D+?(\d+)(?:\D+(\d+))?', c['next'])
        if not found:
            sys.exit(f"Can't read the Next line: {c['next']}")
        num, k = found.group(1).zfill(2), int(found.group(2))
        of = int(found.group(3)) if found.group(3) else None
    if num not in by_num:
        sys.exit(f'HSK {level} has no lesson {num}.')
    lesson = by_num[num]
    begun = max([d['part'] for d in c['done'] if d['level'] == level and d['lesson'] == num] or [0])
    parts = parts_of(lesson, split_index_for(lesson, c['pace'], of, begun))
    if not 1 <= k <= len(parts):
        sys.exit(f'Lesson {num} has {len(parts)} part(s) here, not a part {k}.')
    blocks = parts[k - 1]
    new = [w for b in blocks for w in b]
    name = c['lessons'].get(num, {}).get('name') or lesson['name']

    done = c['done']
    known_words = [w for n in known if n in by_num for b in by_num[n]['blocks'] for w in b]
    met_before = sum(level_size(n) for n in range(1, level)) + len({bare(w) for d in done if d['level'] >= level for w in d['words']}) + len(known_words)
    early = met_before < 20

    print(f"PART: HSK {level} · Lesson {int(num)} · {name}" + (f' · part {k} of {len(parts)}' if len(parts) > 1 else ''))
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
    older = []
    for turn, back in enumerate(BACK):
        if len(done) >= back:
            words = done[-back]['words']
            pick = [words[(turn + j) % len(words)] for j in range(min(2, len(words)))]
            if turn == len(BACK) - 1 and len(words) > turn + 1:
                pick = words[turn:]
            older.append(f"{back} back ({done[-back]['raw'].split('|')[0].strip()}): " + ' or '.join(pick) if turn < len(BACK) - 1 or len(pick) <= 2 else f"{back} back: any of " + ' '.join(pick))
    if older:
        print('OLDER WORDS: use one from each line, the one that fits a sentence best:')
        for row in older:
            print('  ' + row)
    if known:
        print('KNOWN LESSONS (never shown by the course): ' + ' '.join(known))
        print('  their words: ' + ' '.join(known_words))
        print('  they count as met; list the ones this part uses under the table, with pinyin and meaning')
    n = len(new)
    per_round = min(5, n)
    print(f'EARLY PART: {"yes: read first-parts.md" if early else "no"} ({met_before} words met before this part)')
    if not early:
        print(f'ROUNDS: three rounds of {per_round} prompt{"s" if per_round != 1 else ""}; every new word in at least three of them')
    if early:
        print('ROUNDS AND LAST STEP: as first-parts.md says')
    else:
        print('LISTENING: ' + ('dictation and narration' if n >= 5 else 'dictation only') + ' with audio; one reading without')
    if k < len(parts):
        nxt = f'`Lesson {num}, part {k + 1} of {len(parts)}`'
    else:
        route = route_lessons(c['route'])
        if num not in route:
            nxt = 'what it was: this lesson is not on the route'
        else:
            nxt = '`level complete`'
            for cand in route[route.index(num) + 1:]:
                if cand not in by_num or cand in known:
                    continue
                had = max([d['part'] for d in done if d['level'] == level and d['lesson'] == cand] or [0])
                total = len(by_num[cand]['split'][split_index_for(by_num[cand], c['pace'], None, had)])
                if had < total:
                    nxt = f'`Lesson {cand}, part {had + 1} of {total}`'
                    break
    print(f"AT THE CLOSE: add `{level}-{num}.{k} | {' '.join(new)}` to Done; Next becomes {nxt}")

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
        print(f'PLAN HEADER written to {plan_path}: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.')


def main(argv):
    if len(argv) >= 3 and argv[0] == 'overview':
        return overview(int(argv[1]), int(argv[2]))
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
