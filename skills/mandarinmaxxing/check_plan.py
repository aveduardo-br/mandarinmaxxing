"""Check a planned part before teaching it.

Usage: python3 check_plan.py plan.txt

plan.txt is written by the tutor and never shown to the learner. `course.py part` writes
its header; the tutor adds the lines under PLAN:

    LEVEL 2
    KNOWN 01 02 03          (only if course.md marks lessons as known: their numbers)
    EARLY                   (only while the learner has met fewer than twenty words)
    NEW 地铁 站 离 远
    SUPPORT 杯              (only if the part has extra words: two at most)
    NAMES 北京 小王         (only if the plan uses names of people or places)
    DONE
    ...the Done lines of course.md, as they are...
    PLAN
    review: 我明天去医院看病。
    prompt: Amanhã vou ao hospital.
    chunk: ...
    round1: ...
    round2: ...
    round3: ...
    listening: ...

Every line under PLAN is one Mandarin sentence or text with its label (review, chunk,
round1, round2, round3, listening or reading), or the prompt in the learner's language
on a line that starts with `prompt:`. A line with no Hanzi needs no label and is skipped.

It fails, with exit code 1, on:
- NOT MET: characters that no met word covers. Met: the levels below LEVEL, DONE, NEW,
  SUPPORT, and the lessons KNOWN lists; NAMES are allowed. A review line is checked
  without NEW and SUPPORT: the review comes before the table. A word said apart after
  its first character (洗了澡 for 洗澡, 打两次电话 for 打电话) is met.
- new words in fewer than three round lines, alone or inside a longer word (not with EARLY)
- a round with no line (round 3 may be missing with EARLY), the same sentence twice in
  the review and rounds (not with EARLY), a line with Hanzi and no label or an unknown one, more than two
  SUPPORT words, a KNOWN line with no numbers

It advises, under CHECK, without failing:
- a stretch that met words cover but that is also a word the learner hasn't met (要是 from
  要 and 是): keep it only if you mean the parts
- a met word that this level teaches again later with another reading or sense (还 huán
  when 还 hái is met): use only the sense met
- a new word that never stands on its own in the rounds, only inside longer words

It checks vocabulary and the shape of the plan. Whether a sentence is natural, and which
sense of a word it uses, is still the tutor's call.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[一-鿿]+')
ALWAYS = {'没'}  # in every list only inside 没有, 没事, 没关系, and said alone all the time
BETWEEN = '了过着完个一下点儿的不得两三几次会'  # what can stand inside a separable word: 洗了澡, 洗个澡, 见过面
LABELS = ('review', 'chunk', 'round1', 'round2', 'round3', 'listening', 'reading', 'prompt')


def clean(word):
    return re.sub(r'\d+$', '', word.strip())


def words_in(text):
    return {clean(w) for w in text.split() if HAN.search(w)}


def with_plain_er(words):
    """面条儿 is also met as 面条: the final 儿 is optional in writing."""
    return words | {w[:-1] for w in words if len(w) > 1 and w.endswith('儿')}


def level_list(level):
    path = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    out = set()
    if os.path.exists(path):
        for line in list(open(path, encoding='utf-8-sig'))[1:]:
            cols = line.split(',')
            if len(cols) > 1:
                out.add(clean(cols[1]))
    return out


def known_lessons(level, numbers, jump_start):
    """Words of the lessons the course counts as known: the numbered ones, or every
    jump-start lesson for the older `KNOWN jump start`."""
    out, inside = set(), False
    path = os.path.join(HERE, 'maps', f'hsk-{level}.md')
    if not os.path.exists(path):
        return out
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            inside = line[3:5] in numbers or (jump_start and '| jump-start |' in line)
        elif line.startswith('- ') and inside:
            out |= words_in(line[2:])
    return out


def join_separated(run, vocab):
    """洗了澡 → 洗澡 plus what stood between: a met word of two or three characters said
    apart after its first character (打了电话, 打两次电话 for 打电话)."""
    found = []
    for word in vocab:
        if len(word) not in (2, 3) or word in run:
            continue
        pattern = re.escape(word[0]) + '([' + BETWEEN + ']{1,3})' + re.escape(word[1:])
        if re.search(pattern, run):
            run = re.sub(pattern, lambda m: word + m.group(1), run, count=1)
            found.append(word)
    return run, found


def segment(run, vocab, longest):
    """Split a run of Hanzi into met words, covering as many characters as possible
    and, among equal covers, using the fewest (so the longest) words."""
    n = len(run)
    best = [(0, 0, None)] * (n + 1)  # (uncovered, tokens, back-pointer)
    for i in range(1, n + 1):
        u, t, _ = best[i - 1]
        cand = (u + 1, t, (i - 1, None))
        for k in range(1, min(longest, i) + 1):
            w = run[i - k:i]
            if w in vocab:
                u2, t2, _ = best[i - k]
                c = (u2, t2 + 1, (i - k, w))
                if c[:2] < cand[:2]:
                    cand = c
        best[i] = cand
    tokens, missing, i = [], [], n
    while i > 0:
        j, w = best[i][2]
        if w is None:
            missing.append(run[j])
        else:
            tokens.append(w)
        i = j
    return tokens[::-1], missing[::-1]


def main(path):
    level, known, jump, new, support, names = None, None, False, set(), [], set()
    done, done_here, plan, problems = set(), set(), [], []
    section, early = None, False
    for raw in open(path, encoding='utf-8'):
        line = raw.strip().replace('：', ':')
        if not line:
            continue
        head = line.split()[0].upper().rstrip(':')
        if section == 'PLAN' or (section == 'DONE' and head != 'PLAN'):
            head = ''  # nothing below DONE is a command, except PLAN itself
        if head == 'LEVEL':
            found = re.search(r'\d+', line)
            if not found or not 1 <= int(found.group()) <= 6:
                sys.exit('LEVEL needs a number from 1 to 6, such as: LEVEL 2')
            level = int(found.group())
        elif head == 'KNOWN':
            known = set(n.zfill(2) for n in re.findall(r'\d+', line))
            jump = 'jump' in line.lower()
            if not known and not jump:
                problems.append('KNOWN has no lesson numbers: write them (KNOWN 01 02), or delete the line.')
        elif head == 'EARLY':
            early = True
        elif head == 'NEW':
            new |= words_in(line[3:].lstrip(': '))
        elif head == 'SUPPORT':
            support += sorted(words_in(line[7:].lstrip(': ')))
        elif head == 'NAMES':
            names |= words_in(line[5:].lstrip(': '))
        elif head in ('DONE', 'PLAN'):
            section = head
        elif section == 'DONE':
            words = words_in(line.split('|', 1)[-1])
            done |= words
            prefix = re.match(r'\s*(\d)-', line)
            if level is None or not prefix or int(prefix.group(1)) >= level:
                done_here |= words
        elif section == 'PLAN':
            label, colon, text = line.partition(':')
            label = label.strip().lower().replace(' ', '')
            if colon and label in LABELS:
                if label != 'prompt' and HAN.search(text):
                    plan.append((label, text.strip()))
                elif label != 'prompt':
                    problems.append(f'`{line}` has no Hanzi: the plan is written in Hanzi, also when the learner will answer in pinyin.')
            elif HAN.search(line):
                problems.append(f'`{line}` has Hanzi and no label this script knows. Label answers ({", ".join(LABELS[:-1])}) and start a prompt line with `prompt:`.')
    if level is None:
        sys.exit('The plan has no LEVEL line, such as: LEVEL 2')
    if len(support) > 2:
        problems.append('SUPPORT has ' + str(len(support)) + ' words: a part takes two extra words at most.')

    lower = set().union(*[level_list(n) for n in range(1, level)]) if level > 1 else set()
    before = lower | done | ALWAYS
    if known is not None:
        before |= known_lessons(level, known, jump)
    before = with_plain_er(before) | names
    vocab = before | with_plain_er(new | set(support))
    longest = max((len(w) for w in vocab), default=1)
    every = set().union(*[level_list(n) for n in range(1, 7)])
    later = {w for w in every - vocab if len(w) > 1}
    again = (level_list(level) & lower) - done_here - new  # this level re-teaches them with another reading or sense

    unmet, check, counts, alone = [], {}, {w: 0 for w in new}, set()
    for label, text in plan:
        allowed = before if label == 'review' else vocab
        seen, missing = set(), []
        for run in HAN.findall(text):
            run, _ = join_separated(run, allowed)
            tokens, miss = segment(run, allowed, longest)
            seen.update(tokens)
            missing += miss
            for w in again & set(tokens):
                check.setdefault(w + ' (this level teaches another reading or sense of it later)', []).append(text)
            if not miss:
                for a in range(len(tokens)):
                    for b in range(a + 2, len(tokens) + 1):
                        w = ''.join(tokens[a:b])
                        if w in later:
                            check.setdefault(w, []).append(text)
        if missing:
            unmet.append((''.join(dict.fromkeys(missing)), label, text))
        if label.startswith('round'):
            joined = ''.join(HAN.findall(text))
            for w in new:
                plain = w[:-1] if w.endswith('儿') and len(w) > 1 else w
                if w in seen or plain in seen:
                    counts[w] += 1
                    alone.add(w)
                elif w in joined or plain in joined:
                    counts[w] += 1

    if not plan:
        problems.append('No plan lines found: write the answers under PLAN, each with its label.')
    else:
        need = ('round1', 'round2') if early else ('round1', 'round2', 'round3')
        for r in need:
            if not any(label == r for label, _ in plan):
                problems.append(f'No {r} line: every round needs its answers in the plan.')
        seen_text = set()
        for label, text in plan:
            if not early and (label == 'review' or label.startswith('round')):
                key = re.sub(r'[^一-鿿]', '', text)
                if key in seen_text:
                    problems.append(f'The same sentence comes twice in the review and rounds: {text}')
                seen_text.add(key)

    under = [] if early else sorted((c, w) for w, c in counts.items() if c < 3)
    never_alone = sorted(w for w in new if counts[w] and w not in alone)
    if problems:
        print('PLAN (fix these):')
        for p in dict.fromkeys(problems):
            print('  ' + p)
    if unmet:
        print('NOT MET (rewrite the sentence, or list the word as a support word):')
        for chars, label, text in unmet:
            print(f'  {chars}  in {label}: {text}')
    if under:
        print('NEW WORDS IN FEWER THAN THREE ROUND LINES:')
        for c, w in under:
            print(f'  {w}: {c}')
    if check or never_alone:
        print('CHECK (advice only, the plan does not fail on these):')
        for w, texts in check.items():
            more = f' (and {len(texts) - 1} more lines)' if len(texts) > 1 else ''
            print(f'  {w}: met words cover it, but it is also a word not met yet. Keep it only if you mean the parts. In: {texts[0]}{more}' if '(' not in w else f'  {w}. In: {texts[0]}{more}')
        for w in never_alone:
            print(f'  {w} never stands on its own in the rounds, only inside longer words: use it alone once if it is natural alone.')
    failed = bool(problems or unmet or under)
    if not failed:
        print(f'OK: {len(plan)} lines, every character met' + ('.' if early else ', every new word in three round lines or more.'))
    return 1 if failed else 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
