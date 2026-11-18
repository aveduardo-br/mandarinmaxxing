"""Check a planned part before teaching it.

Usage: python3 check_plan.py plan.txt

plan.txt, written by the tutor and never shown to the learner:

    LEVEL 2
    KNOWN jump start        (only if course.md has that line)
    NEW 地铁 站 离 远
    SUPPORT 杯              (only if the part has support words)
    DONE
    ...the Done lines of course.md, pasted as they are...
    PLAN
    review: 我明天去医院看病。
    round1: ...
    round2: ...
    round3: ...
    listening: ...
    chunk: ...

One Mandarin sentence or text per PLAN line. The script reports:
- characters that no met word covers (met: the levels below LEVEL, DONE, NEW, SUPPORT,
  and the level's jump start when KNOWN is given)
- new words that appear in fewer than three round lines

It checks vocabulary only. Whether a sentence is natural is still the tutor's call.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[一-鿿]+')


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


def jump_start(level):
    out, inside = set(), False
    path = os.path.join(HERE, 'maps', f'hsk-{level}.md')
    if not os.path.exists(path):
        return out
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            inside = '| jump-start |' in line
        elif line.startswith('- ') and inside:
            out |= words_in(line[2:])
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
    level, known, new, support, done, plan = 1, False, set(), set(), set(), []
    section = None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if not line:
            continue
        head = line.split()[0].upper().rstrip(':')
        if head == 'LEVEL':
            level = int(re.search(r'\d', line).group())
        elif head == 'KNOWN':
            known = True
        elif head == 'NEW':
            new |= words_in(line[3:].lstrip(': '))
        elif head == 'SUPPORT':
            support |= words_in(line[7:].lstrip(': '))
        elif head in ('DONE', 'PLAN'):
            section = head
        elif section == 'DONE':
            done |= words_in(line.split('|', 1)[-1])
        elif section == 'PLAN':
            label, _, text = line.partition(':')
            if not HAN.search(text) or HAN.search(label):
                label, text = '', line
            plan.append((label.strip().lower(), text.strip()))

    vocab = lower_levels(level) | done | new | support
    if known:
        vocab |= jump_start(level)
    longest = max((len(w) for w in vocab), default=1)

    unmet, counts = [], {w: 0 for w in new}
    for label, text in plan:
        seen, missing = set(), []
        for run in HAN.findall(text):
            tokens, miss = segment(run, vocab, longest)
            seen.update(tokens)
            missing += miss
        if missing:
            unmet.append((''.join(dict.fromkeys(missing)), label, text))
        if label.startswith('round'):
            for w in new & seen:
                counts[w] += 1

    if not plan:
        print('No PLAN lines found.')
        return
    if unmet:
        print('NOT MET (rewrite the sentence, or list the word as a support word):')
        for chars, label, text in unmet:
            print(f'  {chars}  in {label or "line"}: {text}')
    under = sorted((c, w) for w, c in counts.items() if c < 3)
    if under:
        print('NEW WORDS IN FEWER THAN THREE ROUND LINES:')
        for c, w in under:
            print(f'  {w}: {c}')
    if not unmet and not under:
        print(f'OK: {len(plan)} lines, every character met, every new word in three round lines or more.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
