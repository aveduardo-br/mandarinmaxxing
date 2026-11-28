"""Check a planned part before teaching it.

Usage: python3 check_plan.py plan.txt

plan.txt, written by the tutor and never shown to the learner:

    LEVEL 2
    KNOWN 01 02 03          (only if course.md marks lessons as known: their numbers)
    MAP map-hsk-5.md        (only for a level whose map you built: its path)
    EARLY                   (only while the learner has met fewer than twenty words)
    NEW 地铁 站 离 远
    SUPPORT 杯              (only if the part has support words)
    NAMES 北京 小王         (only if the plan uses names of people or places)
    DONE
    ...the Done lines of course.md, pasted as they are...
    PLAN
    review: 我明天去医院看病。
    round1: ...
    round2: ...
    round3: ...
    listening: ...
    chunk: ...

One Mandarin sentence or text per PLAN line. A line that has no Hanzi, such as the
prompt in the learner's language written under its answer, is skipped; so is a line
with Japanese kana or Korean letters. The script reports:
- NOT MET: characters that no met word covers (met: the levels below LEVEL, DONE, NEW,
  SUPPORT, and the lessons KNOWN lists; NAMES are allowed). A review line is checked
  without NEW and SUPPORT: the review comes before the table.
- CHECK: stretches that met words cover but that are also an official word the learner
  hasn't met, such as 要是 from 要 and 是. Keep one only if you mean its parts.
  A word of this level that a lower level also has with another reading or sense (还 huán
  when 还 hái is met) is listed too, until its own part is in DONE.
- new words that appear in fewer than three round lines, alone or inside a longer word
  (not reported with EARLY)

It exits with 1 when it reports NOT MET or a count, and 0 otherwise. It checks vocabulary only. Whether a sentence is natural is still the tutor's call.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[一-鿿]+')
OTHER_SCRIPT = re.compile(r'[぀-ヿ가-힯]')  # kana, hangul: a prompt, not Mandarin
ALWAYS = {'没'}  # in every list only inside 没有, 没事, 没关系, and said alone all the time


def with_plain_er(words):
    """面条儿 is also met as 面条: the final 儿 is optional in writing."""
    return words | {w[:-1] for w in words if len(w) > 1 and w.endswith('儿')}


def clean(word):
    return re.sub(r'\d+$', '', word.strip())


def words_in(text):
    return {clean(w) for w in text.split() if HAN.search(w)}


def lower_levels(level):
    out = set()
    for n in range(1, level):
        path = os.path.join(HERE, 'syllabus', f'hsk-{n}.csv')
        for line in list(open(path, encoding='utf-8'))[1:]:
            parts = line.split(',')
            if len(parts) > 1:
                out.add(clean(parts[1]))
    return out


def known_lessons(level, numbers, mapfile):
    """Words of the lessons the course counts as known. `numbers` holds two-digit lesson
    numbers; empty means every jump-start lesson (the older `KNOWN jump start`)."""
    out, inside = set(), False
    path = mapfile or os.path.join(HERE, 'maps', f'hsk-{level}.md')
    if not os.path.exists(path):
        print(f'KNOWN: no map at {path}; give its path on a MAP line.')
        return out
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            inside = line[3:5] in numbers if numbers else '| jump-start |' in line
        elif line.startswith('- ') and inside:
            out |= words_in(line[2:])
    return out


def all_levels():
    out = set()
    for n in range(1, 7):
        path = os.path.join(HERE, 'syllabus', f'hsk-{n}.csv')
        if os.path.exists(path):
            for line in list(open(path, encoding='utf-8'))[1:]:
                parts = line.split(',')
                if len(parts) > 1:
                    out.add(clean(parts[1]))
    return out


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
    level, known, new, support, names, done, plan = 1, None, set(), set(), set(), set(), []
    section, mapfile, early, done_here = None, None, False, set()
    for raw in open(path, encoding='utf-8'):
        line = raw.strip().replace('：', ':')
        if not line:
            continue
        head = line.split()[0].upper().rstrip(':')
        if section == 'PLAN':
            head = ''  # nothing in the plan is a command: a prompt may start with any word
        elif section == 'DONE' and head != 'PLAN':
            head = ''
        if head == 'LEVEL':
            found = re.search(r'\d+', line)
            if not found:
                sys.exit('LEVEL needs a number, such as: LEVEL 2')
            level = int(found.group())
        elif head == 'KNOWN':
            known = set(n.zfill(2) for n in re.findall(r'\d+', line))
        elif head == 'MAP':
            mapfile = line[3:].lstrip(': ').strip()
        elif head == 'EARLY':
            early = True
        elif head == 'NEW':
            new |= words_in(line[3:].lstrip(': '))
        elif head == 'SUPPORT':
            support |= words_in(line[7:].lstrip(': '))
        elif head == 'NAMES':
            names |= words_in(line[5:].lstrip(': '))
        elif head in ('DONE', 'PLAN'):
            section = head
        elif section == 'DONE':
            done |= words_in(line.split('|', 1)[-1])
            prefix = re.match(r'\s*(\d)-', line)
            if not prefix or int(prefix.group(1)) >= level:
                done_here |= words_in(line.split('|', 1)[-1])
        elif section == 'PLAN':
            if OTHER_SCRIPT.search(line):
                continue
            label, _, text = line.partition(':')
            if not HAN.search(text) or HAN.search(label):
                label, text = '', line
            if HAN.search(text):
                plan.append((label.strip().lower().replace(' ', ''), text.strip()))

    before = lower_levels(level) | done | ALWAYS
    if known is not None:
        before |= known_lessons(level, known, mapfile)
    before = with_plain_er(before) | names
    vocab = before | with_plain_er(new | support)
    longest = max((len(w) for w in vocab), default=1)
    later = {w for w in all_levels() - vocab if len(w) > 1}

    # words this level teaches that a lower level already has: another reading or sense
    lower = lower_levels(level)
    again = set()
    here = os.path.join(HERE, 'syllabus', f'hsk-{level}.csv')
    if os.path.exists(here):
        for row in list(open(here, encoding='utf-8'))[1:]:
            cols = row.split(',')
            if len(cols) > 1 and clean(cols[1]) in lower:
                again.add(clean(cols[1]))
    again -= done_here | new

    unmet, check, counts = [], {}, {w: 0 for w in new}
    for label, text in plan:
        seen, missing = set(), []
        allowed = before if label.startswith('review') else vocab
        for run in HAN.findall(text):
            tokens, miss = segment(run, allowed, longest)
            seen.update(tokens)
            # a separable word said apart (打了电话 for 打电话) is met
            miss = [ch for ch in miss if not any(w[0] == ch and len(w) > 1 and w[1:] in text for w in allowed)]
            missing += miss
            for w in again & set(tokens):
                check.setdefault(w + ' (this level teaches another reading or sense of it later)', []).append(text)
            if not miss:
                # an unmet word spelled by two or more whole met words in a row
                for a in range(len(tokens)):
                    for b in range(a + 2, len(tokens) + 1):
                        w = ''.join(tokens[a:b])
                        if w in later:
                            check.setdefault(w, []).append(text)
        if missing:
            unmet.append((''.join(dict.fromkeys(missing)), label, text))
        if label.startswith('round'):
            for w in new:
                if w in seen or w in text or (w.endswith('儿') and len(w) > 1 and w[:-1] in text):
                    counts[w] += 1

    if not plan:
        print('No PLAN lines found.')
        return 1
    if unmet:
        print('NOT MET (rewrite the sentence, or list the word as a support word):')
        for chars, label, text in unmet:
            print(f'  {chars}  in {label or "line"}: {text}')
    if check:
        print('CHECK (met words cover it, but it is also a word not met yet; keep it only if you mean the parts):')
        for w, texts in check.items():
            more = f' (and {len(texts) - 1} more lines)' if len(texts) > 1 else ''
            print(f'  {w}  in: {texts[0]}{more}')
    under = [] if early else sorted((c, w) for w, c in counts.items() if c < 3)
    if under:
        print('NEW WORDS IN FEWER THAN THREE ROUND LINES:')
        for c, w in under:
            print(f'  {w}: {c}')
    if not unmet and not under and not check:
        print(f'OK: {len(plan)} lines, every character met' + ('.' if early else ', every new word in three round lines or more.'))
    return 1 if unmet or under else 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
