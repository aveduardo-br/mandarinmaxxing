"""The course's bookkeeping: it reads the learner's course file, says what to teach, and
writes every change to the file, so the tutor never edits it by hand.

Reading:
    python3 course.py overview LEVEL PACE
        The lessons of a level with their parts at that pace (3, 5 or 7) and the totals.
        Jump-start lessons come with their words, for asking a learner which they know.
    python3 course.py part COURSE.md [PLAN.txt] [--lesson N [--part K]]
        The brief for one part: by default the one in `Next`, or the lesson given (its first
        part not yet studied, or the part given, as practice). With PLAN.txt, it also writes
        that file's header, ready for check_plan.py.
    python3 course.py progress COURSE.md
        Parts done and parts in the level, for the course screen.
    python3 course.py check COURSE.md
        Everything wrong with the file, or OK.

Writing (each rewrites COURSE.md and prints what changed; save the file after it):
    python3 course.py new COURSE.md LEVEL PACE LANGUAGE
        A new course. Lesson names and labels come in English: translate them in the file.
    python3 course.py close COURSE.md [--missed "A, B"] [--recovered "C"]
        Close the part in `Next`: its Done line, the new `Next`, and To reinforce (items
        the learner missed in this part and didn't get right later join; items they got
        right unaided in the review leave; five at most).
    python3 course.py jump COURSE.md N        put lesson N first on the route
    python3 course.py known COURSE.md N [N…]  mark lessons as known: off the route
    python3 course.py study COURSE.md N       undo that: lesson N goes back on the route, first
    python3 course.py pace COURSE.md PACE     3, 5 or 7, from the next lesson on
    python3 course.py level COURSE.md LEVEL   move the course to another level
    python3 course.py audio COURSE.md TEXT    `none`, or the provider and voice
    python3 course.py migrate COURSE.md       bring an older file to the current format

COURSE.md is the learner's course file. If the chat holds it as a project document and
not as a file where code runs, save a copy first, pass the copy, and put the result back.
A file from an older version is read as it is and written in the current format.

It stops with a message, and exit code 1, when the file contradicts itself: a lesson
twice on the route, the same part twice in Done, a Done line with no words, a `Next`
it can't read or that points to a lesson marked (known).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FORMAT = 2
PACES = (3, 5, 7)
BACK = (3, 7, 14, 30, 60)  # lines back in the Done log that give a word to reuse
NEXT = re.compile(r'^lesson\s+(\d+)\s*,?\s*part\s+(\d+)(?:\s+of\s+(\d+))?$', re.I)
LABELS = ('lesson', 'part', 'review', 'round', 'dictation', 'audio', 'reading', 'phrases', 'jump start')
ENGLISH = {'lesson': 'Lesson', 'part': 'part', 'review': 'Review', 'round': 'Round', 'dictation': 'Dictation',
           'audio': 'Audio', 'reading': 'Reading', 'phrases': 'Useful phrases', 'jump start': 'Jump start'}
# labels by position in files written before format 2 (eleven, or nine before dictation and audio existed)
OLD_11 = ('lesson', 'part', 'review', 'round', None, None, 'dictation', 'audio', 'reading', 'phrases', 'jump start')
OLD_9 = ('lesson', 'part', 'review', 'round', None, None, 'reading', 'phrases', 'jump start')


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


# ---------------------------------------------------------------- the course file

def read_labels(text, notes):
    """Named labels (`lesson=Aula, part=parte`), or the positional list of older files."""
    if '=' in text:
        out = {}
        for piece in re.split(r'[,;]', text):
            if '=' in piece:
                key, value = piece.split('=', 1)
                out[key.strip().lower()] = value.strip()
        return out
    values = [v.strip() for v in text.split(',') if v.strip()]
    order = OLD_11 if len(values) >= 11 else OLD_9 if len(values) == 9 else None
    if order is None:
        notes.append('The Labels line is in an older shape this script can\'t place: check each label in the file.')
        order = OLD_11
    return {key: value for key, value in zip(order, values) if key}


def read_course(path):
    c = {'format': 1, 'level': 1, 'pace': 5, 'language': '', 'labels': {}, 'rounds': '', 'audio': 'none',
         'next': None, 'route': '', 'reinforce': [], 'lessons': {}, 'order': [], 'done': [], 'extra': [],
         'old_known': False, 'notes': []}
    section = None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if line.startswith('## '):
            section = line[3:].strip().lower()
            continue
        if not line or line.startswith('# '):
            continue
        if section not in ('lessons', 'done'):
            key, _, value = line.lstrip('- ').partition(':')
            key, value = key.strip().lower(), value.strip()
            if key == 'format':
                c['format'] = int(re.search(r'\d+', value).group()) if re.search(r'\d+', value) else 1
            elif key == 'syllabus':
                found = re.search(r'level\s*(\d)', value.lower())
                c['level'] = int(found.group(1)) if found else 1
            elif key == 'pace':
                found = re.search(r'\d+', value)
                pace = int(found.group()) if found else 0
                if pace not in PACES:
                    c['notes'].append(f'Pace is {pace or "missing"}: using {nearest_pace(pace or 5)}, the nearest of 3, 5 and 7.')
                c['pace'] = nearest_pace(pace or 5)
            elif key == 'language':
                c['language'] = value
            elif key == 'labels':
                c['labels'] = read_labels(value, c['notes'])
            elif key == 'rounds':
                c['rounds'] = value
            elif key == 'audio':
                c['audio'] = value or 'none'
            elif key == 'route':
                c['route'] = value
            elif key == 'next':
                c['next'] = value
            elif key == 'to reinforce':
                c['reinforce'] = [] if value.lower() in ('', 'none') else items(value)
                if len(c['reinforce']) == 1 and ' ' in value and re.fullmatch(r'[一-鿿\s]+', value):
                    c['reinforce'] = value.split()  # older files separated items with spaces
            elif key == 'known' and 'jump' in value.lower():
                c['old_known'] = True
            else:
                c['extra'].append(line)
        elif section == 'lessons':
            found = re.match(r'(\d\d)\s+(.*)', line)
            if found:
                text = found.group(2)
                known = bool(re.search(r'\(known\)\s*$', text))
                name = re.sub(r'\s*\((?:known|\d+\s+[^()]*)\)\s*$', '', text)
                c['lessons'][found.group(1)] = {'name': name, 'known': known}
                c['order'].append(found.group(1))
        elif section == 'done':
            found = re.match(r'(?:(\d)-)?(\d\d)\.(\d+)\s*\|(.*)', line)
            if not found:
                sys.exit(f"Can't read this Done line: {line}\nA Done line looks like `1-02.1 | 我 要 水 茶`.")
            words = found.group(4).split()
            if not words:
                sys.exit(f'This Done line has no words: {line}')
            level = int(found.group(1) or c['level'])
            c['done'].append({'level': level, 'lesson': found.group(2), 'part': int(found.group(3)), 'words': words,
                              'raw': f"{level}-{found.group(2)}.{found.group(3)} | {' '.join(words)}"})
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


def route_text(nums):
    """01 02 03 08 → `01–03, 08`."""
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and int(nums[j + 1]) == int(nums[j]) + 1:
            j += 1
        out.append(nums[i] if j == i else f'{nums[i]}–{nums[j]}' if j > i + 1 else f'{nums[i]}, {nums[j]}')
        i = j + 1
    return ', '.join(out)


def lesson_state(lesson, done_lines, pace, total=None):
    """Where a lesson stands, from the words Done actually holds for it.

    Returns (parts, studied): `parts` is the whole lesson as a list of parts (each a list of
    blocks) and `studied` how many of them are done. A lesson begun at another pace keeps
    that pace's split: the split is the one whose first parts match the Done lines. If no
    split matches (a file edited by hand), the blocks already in Done count as one studied
    part and the rest is divided at the current pace. `total` is the "of N" that `Next`
    gives for this lesson, when it names it."""
    lines = sorted(done_lines, key=lambda d: d['part'])
    current = PACES.index(pace)
    if not lines:
        return split_parts(lesson, current), 0
    had = [set(d['words']) for d in lines]
    fits = []
    for idx in [current] + [i for i in range(3) if i != current]:
        parts = split_parts(lesson, idx)
        if len(parts) >= len(had) and all({w for b in parts[i] for w in b} == had[i] for i in range(len(had))):
            fits.append(parts)
    # two paces can share a lesson's first parts: `Next` then says which one the lesson was begun at
    for parts in fits:
        if total and len(parts) == total:
            return parts, len(had)
    if fits:
        return fits[0], len(had)
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


class Course:
    """A course file, read once: its settings, where each lesson stands, and how to write it back."""

    def __init__(self, path):
        self.path = path
        self.c = c = read_course(path)
        self.level = c['level']
        self.lessons = read_map(self.level)
        self.by_num = {l['num']: l for l in self.lessons}
        self.known = sorted(n for n, l in c['lessons'].items() if l['known'] and n in self.by_num)
        self.route = [n for n in route_lessons(c['route']) if n in self.by_num]
        if c['old_known']:
            studied = {d['lesson'] for d in c['done'] if d['level'] == self.level}
            self.known = sorted(set(self.known) | {l['num'] for l in self.lessons if l['jump'] and l['num'] not in studied})
            c['notes'].append('The file had the old `Known: jump start` line: these lessons are now marked (known) and off the route: ' + ' '.join(self.known))
        self.route = [n for n in self.route if n not in self.known]
        self.refresh()

    def refresh(self):
        here = [d for d in self.c['done'] if d['level'] == self.level]
        found = NEXT.match((self.c['next'] or '').strip().strip('`'))
        named = {found.group(1).zfill(2): int(found.group(3))} if found and found.group(3) else {}
        self.state = {n: lesson_state(self.by_num[n], [d for d in here if d['lesson'] == n], self.c['pace'], named.get(n)) for n in self.by_num}

    def name(self, num):
        return self.c['lessons'].get(num, {}).get('name') or self.by_num[num]['name']

    def pending(self, num):
        parts, studied = self.state[num]
        return f'Lesson {num}, part {studied + 1} of {len(parts)}' if studied < len(parts) else None

    def first_open(self, after=None):
        """The first part still to study: on the route from lesson `after` on, then before it."""
        order = self.route
        if after in order:
            i = order.index(after)
            order = order[i:] + order[:i]
        for n in order:
            if self.pending(n):
                return self.pending(n)
        return 'level complete'

    def current(self):
        """The lesson and part `Next` names, checked against Done. Returns (num, part, notes)."""
        c, notes = self.c, []
        if c['next'] is None or not c['next'].strip():
            sys.exit('The file has no `Next` line, or it is empty. From the route and Done it should be: ' + self.first_open())
        if 'complete' in c['next'].lower():
            still = self.first_open()
            if still != 'level complete':
                sys.exit(f'Next says the level is complete, but the route still has {still}. Run `course.py check` on the file.')
            sys.exit('Next says the level is complete: read levels.md.')
        found = NEXT.match(c['next'].strip().strip('`'))
        if not found:
            sys.exit(f"Can't read the Next line: `{c['next']}`. It should read like `Lesson 02, part 1 of 2`.")
        num, k = found.group(1).zfill(2), int(found.group(2))
        if num not in self.by_num:
            sys.exit(f'HSK {self.level} has no lesson {num}.')
        if num in self.known:
            sys.exit(f'Next points to Lesson {num}, which is marked (known). Run `course.py study` to study it, or set Next to: ' + self.first_open())
        parts, studied = self.state[num]
        if studied >= len(parts):
            sys.exit(f'Next points to Lesson {num}, part {k}, but Done holds the whole lesson. Next should be: ' + self.first_open(num))
        if k != studied + 1:
            notes.append(f'Next said part {k}, but Done holds {studied} part(s) of Lesson {num}: this is part {studied + 1} of {len(parts)}.')
        elif found.group(3) and int(found.group(3)) != len(parts):
            notes.append(f'Next said "of {found.group(3)}", but Lesson {num} has {len(parts)} part(s) here.')
        return num, studied + 1, notes

    def met(self):
        below = set().union(*[level_words(n) for n in range(1, self.level)]) if self.level > 1 else set()
        known_words = [w for n in self.known for b in self.by_num[n]['blocks'] for w in b]
        return below | {bare(w) for d in self.c['done'] for w in d['words']} | {bare(w) for w in known_words}, known_words

    def write(self, next_line):
        c = self.c
        labels = dict(ENGLISH)
        labels.update({k: v for k, v in c['labels'].items() if k in LABELS and v})
        added = [k for k in LABELS if not c['labels'].get(k)]
        if added and c['labels']:
            c['notes'].append('Labels had no word for: ' + ', '.join(added) + '. They are in English now: translate them in the file.')
        if not c['rounds'] and c['labels']:
            c['notes'].append('The file had no Rounds line. It is in English now: translate the three names in the file.')
        lines = ['# mandarinmaxxing course',
                 f'- Format: {FORMAT}',
                 f'- Syllabus: HSK 3.0 (2025-11), level {self.level}',
                 f"- Pace: about {c['pace']} words per part",
                 f"- Language: {c['language'] or 'English'}",
                 '- Labels: ' + ', '.join(f'{k}={labels[k]}' for k in LABELS),
                 f"- Rounds: {c['rounds'] or 'Chunks, Full actions, Sequences'}",
                 f"- Audio: {c['audio']}",
                 f'- Route: {route_text(self.route)}',
                 f'- Next: {next_line}',
                 '- To reinforce: ' + (', '.join(c['reinforce']) if c['reinforce'] else 'none')]
        lines += c['extra'] + ['', '## Lessons']
        for l in self.lessons:
            lines.append(f"{l['num']} {self.name(l['num'])}" + (' (known)' if l['num'] in self.known else ''))
        lines += ['', '## Done'] + [d['raw'] for d in c['done']]
        open(self.path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        for note in c['notes']:
            print('NOTE: ' + note)
        print(f'SAVED to {self.path}: Next is `{next_line}`. Put this file back where the course is kept.')

    def keep_next(self):
        """`Next` for a write that doesn't finish a part: the lesson in progress if it is still
        open and on the route, otherwise the first open part."""
        found = NEXT.match((self.c['next'] or '').strip().strip('`'))
        num = found.group(1).zfill(2) if found else None
        if num in self.route and self.pending(num):
            return self.pending(num)
        return self.first_open()


# ---------------------------------------------------------------- reading commands

def part(course_path, plan_path=None, want_lesson=None, want_part=None):
    course = Course(course_path)
    c, level, done = course.c, course.level, course.c['done']
    practice, notes = False, []
    if want_lesson:
        num = str(want_lesson).zfill(2)
        if num not in course.by_num:
            sys.exit(f'HSK {level} has no lesson {num}.')
        parts, studied = course.state[num]
        k = want_part or min(studied + 1, len(parts))
        practice = k <= studied
    else:
        num, k, notes = course.current()
        parts, studied = course.state[num]
    if not 1 <= k <= len(parts):
        sys.exit(f'Lesson {num} has {len(parts)} part(s) here, not a part {k}.')
    blocks = parts[k - 1]
    new = [w for b in blocks for w in b]
    met, known_words = course.met()
    early = len(met) < 20

    for note in c['notes'] + notes:
        print('NOTE: ' + note)
    if c['format'] < FORMAT:
        print('NOTE: this file is in an older format. Before teaching, run `course.py migrate <course.md>`, translate what it asks, and put the file back.')
    print(f"PART: HSK {level} · Lesson {int(num)} · {course.name(num)}" + (f' · part {k} of {len(parts)}' if len(parts) > 1 else ''))
    if practice:
        print('PRACTICE: this part is already in Done. Teach it as practice; there is nothing to close.')
    print('NEW WORDS, in blocks that work together: ' + ' | '.join(' '.join(b) for b in blocks))
    last = done[-1] if done else None
    if last:
        how = 'the lines of' if early else 'one prompt per word of'
        print(f"REVIEW: {how} {last['raw'].split('|')[0].strip()}: " + ' '.join(last['words']))
        if c['reinforce']:
            print('  and the items to reinforce, once each: ' + ', '.join(c['reinforce']))
    else:
        print('REVIEW: none, nothing studied yet. Start at the vocabulary.')
    older = older_candidates(done)
    if older:
        print('OLDER WORDS: use one from each line, the one that fits a sentence best:')
        for back, line, pick in older:
            key = line['raw'].split('|')[0].strip()
            print(f'  {back} back ({key}): ' + (' or '.join(pick) if len(pick) <= 2 else 'any of ' + ' '.join(pick)))
    if course.known:
        print('KNOWN LESSONS (never shown by the course): ' + ' '.join(course.known))
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
        print('AT THE CLOSE: run `course.py close <course.md>`, with --missed and --recovered for the items to reinforce')

    if plan_path:
        head = [f'LEVEL {level}']
        if course.known:
            head.append('KNOWN ' + ' '.join(course.known))
        if early:
            head.append('EARLY')
        head.append('NEW ' + ' '.join(new))
        head.append('DONE')
        head += [d['raw'] for d in done]
        head.append('PLAN')
        open(plan_path, 'w', encoding='utf-8').write('\n'.join(head) + '\n')
        print(f'PLAN HEADER written to {plan_path}: add a SUPPORT or NAMES line above DONE if the part needs one, and the plan lines at the end.')


def progress(course_path):
    course = Course(course_path)
    active = [n for n in course.by_num if n not in course.known]
    done = sum(course.state[n][1] for n in active)
    total = sum(len(course.state[n][0]) for n in active)
    print(f'{done}/{total}')
    print(f'HSK {course.level}: {done} of {total} parts done' + (f' ({len(course.known)} lesson(s) marked known are left out)' if course.known else ''))
    print('NEXT: ' + course.keep_next())


def check(course_path):
    course = Course(course_path)
    c, problems = course.c, []
    if c['format'] < FORMAT:
        problems.append('Older format: run `course.py migrate` on the file.')
    if not c['language']:
        problems.append('No Language line.')
    english = c['language'].strip().lower() in ('', 'english', 'en')
    for key in LABELS:
        if not c['labels'].get(key):
            problems.append(f'Labels has no word for "{key}".')
        elif not english and c['labels'][key] == ENGLISH[key] and key != 'audio':
            problems.append(f'The label for "{key}" is still in English ({ENGLISH[key]}): translate it into {c["language"]}.')
    if not c['rounds']:
        problems.append('No Rounds line.')
    elif not english and c['rounds'].strip() == 'Chunks, Full actions, Sequences':
        problems.append(f'The Rounds line is still in English: translate the three names into {c["language"]}.')
    for n in course.by_num:
        if n not in c['lessons']:
            problems.append(f'The Lessons list has no line for lesson {n}.')
        elif n not in course.route and n not in course.known and course.pending(n):
            problems.append(f'Lesson {n} is neither on the route nor marked (known), and it isn\'t finished.')
    should = course.first_open()
    if c['next'] is None or not c['next'].strip():
        problems.append(f'No Next line: it should be `{should}`.')
    elif 'complete' in c['next'].lower():
        if should != 'level complete':
            problems.append(f'Next says the level is complete, but the route still has {should}.')
    else:
        found = NEXT.match(c['next'].strip().strip('`'))
        if not found:
            problems.append(f"Next can't be read: `{c['next']}`. It should be `{should}`.")
        else:
            num = found.group(1).zfill(2)
            if num not in course.by_num or num in course.known or not course.pending(num):
                problems.append(f"Next is `{c['next']}`, which is not a part still to study. It should be `{should}`.")
            elif course.pending(num) != f"Lesson {num}, part {found.group(2)} of {found.group(3) or len(course.state[num][0])}":
                problems.append(f"Next is `{c['next']}`, but Done says `{course.pending(num)}`.")
    if len(c['reinforce']) > 5:
        problems.append('To reinforce holds more than five items.')
    for note in c['notes']:
        problems.append(note)
    if problems:
        print('CHECK (the writing commands fix most of these: `course.py migrate` rewrites the file as it should be):')
        for p in problems:
            print('  ' + p)
        return 1
    print('OK: the course file is consistent.')
    return 0


# ---------------------------------------------------------------- writing commands

def new(path, level, pace, language):
    lessons = read_map(level)
    pace = nearest_pace(pace)
    first = len(lessons[0]['split'][PACES.index(pace)])
    lines = ['# mandarinmaxxing course', f'- Format: {FORMAT}', f'- Syllabus: HSK 3.0 (2025-11), level {level}',
             f'- Pace: about {pace} words per part', f'- Language: {language}',
             '- Labels: ' + ', '.join(f'{k}={ENGLISH[k]}' for k in LABELS),
             '- Rounds: Chunks, Full actions, Sequences', '- Audio: none',
             f"- Route: {route_text([l['num'] for l in lessons])}", f'- Next: Lesson 01, part 1 of {first}',
             '- To reinforce: none', '', '## Lessons']
    lines += [f"{l['num']} {l['name']}" for l in lessons] + ['', '## Done']
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f'SAVED to {path}: a new HSK {level} course at pace {pace}.')
    print(f'Now translate into {language}, in the file: the word after each `=` on the Labels line, the three names on the Rounds line, and every lesson name. Keep the numbers and everything else as they are. Then save the file where the course is kept.')


def items(text):
    """Items of a list written with commas or semicolons. A full-width comma stays inside
    its item: a chunk such as 不要，谢谢 is one item."""
    return [x.strip() for x in re.split(r'[,;]', text or '') if x.strip()]


def close(path, missed='', recovered=''):
    course = Course(path)
    c = course.c
    num, k, notes = course.current()
    parts, _ = course.state[num]
    new_words = [w for b in parts[k - 1] for w in b]
    line = f"{course.level}-{num}.{k} | {' '.join(new_words)}"
    c['done'].append({'level': course.level, 'lesson': num, 'part': k, 'words': new_words, 'raw': line})
    course.refresh()
    gone = set(items(recovered))
    queue = [x for x in c['reinforce'] if x not in gone]
    for x in items(missed):
        if x in queue:
            queue.remove(x)
        queue.append(x)
    c['reinforce'] = queue[-5:]
    c['notes'] += notes
    nxt = course.pending(num) or course.first_open(num)
    print(f'CLOSED: {line}')
    course.write(nxt)
    print('TO REINFORCE: ' + (', '.join(c['reinforce']) if c['reinforce'] else 'none'))
    if nxt == 'level complete':
        print('The level is complete: read levels.md.')
    elif not nxt.startswith(f'Lesson {num},'):
        print(f'Lesson {num} is complete.')


def jump(path, lesson):
    course = Course(path)
    num = str(lesson).zfill(2)
    if num not in course.by_num:
        sys.exit(f'HSK {course.level} has no lesson {num}.')
    if num in course.known:
        sys.exit(f'Lesson {num} is marked (known): use `course.py study` to study it.')
    if not course.pending(num):
        sys.exit(f'Lesson {num} is already finished: to go through it again, use `course.py part <course.md> --lesson {int(num)} --part 1`, as practice.')
    course.route = [num] + [n for n in course.route if n != num]
    skipped = [l['num'] for l in course.lessons if l['jump'] and l['num'] not in course.known and course.state[l['num']][1] == 0 and l['num'] != num]
    course.write(course.pending(num))
    print('ROUTE: ' + route_text(course.route))
    if skipped and not course.by_num[num]['jump']:
        print('JUMP-START LESSONS NOT STUDIED: ' + ' '.join(skipped) + '. Ask which of them the learner already knows (requests.md), then run `course.py known` for those.')


def known(path, lessons_):
    course = Course(path)
    nums = [str(n).zfill(2) for n in lessons_]
    for num in nums:
        if num not in course.by_num:
            sys.exit(f'HSK {course.level} has no lesson {num}.')
    course.known = sorted(set(course.known) | set(nums))
    course.route = [n for n in course.route if n not in course.known]
    course.write(course.keep_next())
    print('KNOWN: ' + ' '.join(course.known))
    waiting = [l['num'] for l in course.lessons if l['jump'] and l['num'] not in course.known and course.state[l['num']][1] == 0]
    first = course.route[0] if course.route else None
    if waiting and first and not course.by_num[first]['jump']:
        print(f'JUMP-START LESSONS STILL TO STUDY: {" ".join(waiting)}. They come before Lesson {first}: run `course.py jump <course.md> {int(waiting[0])}`.')


def study(path, lesson):
    course = Course(path)
    num = str(lesson).zfill(2)
    if num not in course.known:
        sys.exit(f'Lesson {num} is not marked (known).')
    course.known = [n for n in course.known if n != num]
    course.route = [num] + [n for n in course.route if n != num]
    nxt = course.pending(num) or course.keep_next()
    course.write(nxt)
    print('ROUTE: ' + route_text(course.route))


def set_pace(path, pace):
    if pace not in PACES:
        sys.exit('Pace is 3, 5 or 7.')
    course = Course(path)
    begun = course.keep_next()  # worked out at the old pace: a lesson already begun keeps its parts
    course.c['next'] = begun
    course.c['pace'] = pace
    course.c['notes'] = [n for n in course.c['notes'] if not n.startswith('Pace is')]
    course.refresh()
    course.write(begun)
    active = [n for n in course.by_num if n not in course.known]
    print(f'PACE {pace}: {sum(len(course.state[n][0]) for n in active)} parts in the level now. A lesson already begun finishes at its old pace: tell the learner the new pace starts with the next lesson.')


def set_level(path, level):
    course = Course(path)
    c = course.c
    if level == course.level:
        sys.exit(f'The course is already at HSK {level}.')
    lessons = read_map(level)
    course.level, course.lessons = level, lessons
    course.by_num = {l['num']: l for l in lessons}
    course.known, course.route = [], [l['num'] for l in lessons]
    c['lessons'] = {}
    c['notes'] = [n for n in c['notes'] if 'Known' not in n]
    course.refresh()
    course.write(course.first_open())
    print(f'LEVEL: the course is now at HSK {level}. Translate the lesson names in the file into {c["language"] or "the course language"}, then save it. Lessons marked (known) in the old level are not carried over.')


def set_audio(path, text):
    course = Course(path)
    course.c['audio'] = text.strip() or 'none'
    course.write(course.keep_next())


def migrate(path):
    course = Course(path)
    course.write(course.keep_next())


def option(rest, name):
    if name in rest:
        i = rest.index(name)
        value = rest[i + 1] if i + 1 < len(rest) else ''
        del rest[i:i + 2]
        return value
    return None


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd, rest = argv[0], argv[1:]
    try:
        if cmd == 'overview' and len(rest) == 2:
            return overview(int(rest[0]), int(rest[1]))
        if cmd == 'part' and rest:
            lesson, k = option(rest, '--lesson'), option(rest, '--part')
            return part(rest[0], rest[1] if len(rest) > 1 else None, int(lesson) if lesson else None, int(k) if k else None)
        if cmd == 'progress' and len(rest) == 1:
            return progress(rest[0])
        if cmd == 'check' and len(rest) == 1:
            return check(rest[0])
        if cmd == 'new' and len(rest) >= 4:
            return new(rest[0], int(rest[1]), int(rest[2]), ' '.join(rest[3:]))
        if cmd == 'close' and rest:
            missed, recovered = option(rest, '--missed'), option(rest, '--recovered')
            return close(rest[0], missed or '', recovered or '')
        if cmd == 'jump' and len(rest) == 2:
            return jump(rest[0], int(rest[1]))
        if cmd == 'known' and len(rest) >= 2:
            return known(rest[0], [int(n) for n in rest[1:]])
        if cmd == 'study' and len(rest) == 2:
            return study(rest[0], int(rest[1]))
        if cmd == 'pace' and len(rest) == 2:
            return set_pace(rest[0], int(rest[1]))
        if cmd == 'level' and len(rest) == 2:
            return set_level(rest[0], int(rest[1]))
        if cmd == 'audio' and len(rest) >= 2:
            return set_audio(rest[0], ' '.join(rest[1:]))
        if cmd == 'migrate' and len(rest) == 1:
            return migrate(rest[0])
    except ValueError:
        sys.exit('A number was expected where something else was given.\n\n' + __doc__)
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
