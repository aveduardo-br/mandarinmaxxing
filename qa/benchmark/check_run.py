"""Check one benchmark run against the rules a script can verify.

Usage: python3 qa/benchmark/check_run.py <run_dir> <start_course.md or ->

Reads <run_dir>/transcript.md and <run_dir>/course/course.md and prints a JSON report:
- vocabulary: Hanzi the tutor used outside the vocabulary table that aren't in any word the
  learner has met (start Done log, jump start if counted as known, words taught this session)
- review and round counters, and how many prompts of each round carry each new word
- [NÃO SEI] markers from the student (prompts that needed an unknown word)
- audio scripts: dictation and narration, and narration lines that address a listener
- course.md: new Done lines, Next, To reinforce, Known
"""
import json
import re
import sys

MAP = 'skills/mandarinmaxxing/maps/hsk-1.md'
HAN = re.compile(r'[一-鿿]')


def done_words(path):
    words, lines = set(), []
    if path == '-':
        return words, lines
    in_done = False
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            in_done = line.strip() == '## Done'
            continue
        if in_done and '|' in line:
            key, ws = line.split('|', 1)
            ws = [re.sub(r'\d+$', '', w) for w in ws.split()]
            lines.append((key.strip(), ws))
            words.update(ws)
    return words, lines


def jump_start_words():
    out, js = set(), False
    for line in open(MAP, encoding='utf-8'):
        if line.startswith('## '):
            js = '| jump-start |' in line
        elif line.startswith('- ') and js:
            out.update(re.sub(r'\d+$', '', w) for w in line[2:].split())
    return out


def turns(path):
    text = open(path, encoding='utf-8').read()
    parts = re.split(r'^## T(\d+) · (STUDENT|TUTOR)\s*$', text, flags=re.M)
    out = []
    for i in range(1, len(parts) - 2, 3):
        out.append((parts[i + 1], parts[i + 2]))
    return out


def main(run, start):
    start_words, start_lines = done_words(start)
    end_words, end_lines = done_words(f'{run}/course/course.md')
    course = open(f'{run}/course/course.md', encoding='utf-8').read()
    known_js = 'Known: jump start' in course
    new_lines = end_lines[len(start_lines):]
    taught = set(w for _, ws in new_lines for w in ws)
    known = start_words | taught | (jump_start_words() if known_js else set())
    known_chars = set(''.join(known))

    ts = turns(f'{run}/transcript.md')
    tutor = [t for r, t in ts if r == 'TUTOR']
    student = [t for r, t in ts if r == 'STUDENT']

    # vocabulary: Hanzi outside table rows
    leaks = {}
    for msg in tutor:
        for line in msg.splitlines():
            if line.lstrip().startswith('|'):
                continue
            for ch in HAN.findall(line):
                if ch not in known_chars:
                    leaks.setdefault(ch, line.strip()[:90])
    # leaks inside expected answers only (what the learner was asked to produce)
    expected = []
    for i, msg in enumerate(tutor):
        for m in re.finditer(r'<!--\s*expected:\s*(.*?)-->', msg, flags=re.S):
            expected.append((i, m.group(1).strip()))
    exp_leaks = sorted({ch for _, e in expected for ch in HAN.findall(e) if ch not in known_chars})

    # counters
    review = [(int(a), int(b)) for a, b in re.findall(r'\*\*(?:Revisão|Review)\s+(\d+)\s+(?:de|of)\s+(\d+)\*\*', '\n'.join(tutor))]
    rounds = {}
    for r, k, n in re.findall(r'\*\*(?:Bateria|Round)\s+(\d)\s*·\s*(\d+)\s+(?:de|of)\s+(\d+)\*\*', '\n'.join(tutor)):
        rounds.setdefault(int(r), set()).add((int(k), int(n)))
    round_summary = {r: {'max_index': max(k for k, _ in v), 'denominators': sorted({n for _, n in v})} for r, v in sorted(rounds.items())}

    # coverage of new words in expected answers after round 1 starts
    first_round_turn = next((i for i, m in enumerate(tutor) if re.search(r'\*\*(?:Bateria|Round)\s+1', m)), None)
    round_expected = [e for i, e in expected if first_round_turn is not None and i >= first_round_turn]
    coverage = {w: sum(w in e for e in round_expected) for w in sorted(taught)}

    # audio
    audio = []
    for msg in tutor:
        for m in re.finditer(r'```audio-script\n(.*?)```', msg, flags=re.S):
            before = msg[:m.start()][-300:]
            kind = 'dictation' if re.search(r'Ditado|Dictation', before) else 'narration'
            script = m.group(1).strip()
            addresses = bool(re.search(r'[你您]|吗|[“”"「」]', script)) if kind == 'narration' else None
            audio.append({'kind': kind, 'chars': len(HAN.findall(script)), 'addresses_listener': addresses})

    flags = {
        'wrapup_offered': any(re.search(r'role-?play|encena|dramatiz|simula(r|ção) (a|da) situação', m, re.I) for m in tutor),
        'jump_start_question': any(re.search(r'[Ll]argada|jump start', m) and re.search(r'conhecid', m) for m in tutor),
        'next_part_offered': any(re.search(r'próxima parte|começar a parte|seguir (para|com) a (próxima|parte)', m, re.I) for m in tutor),
    }
    next_line = re.search(r'^- Next: (.*)$', course, flags=re.M)
    reinforce = re.search(r'^- To reinforce: ?(.*)$', course, flags=re.M)
    report = {
        'run': run,
        'turns': len(ts),
        'tutor_turns': len(tutor),
        'new_done_lines': [k for k, _ in new_lines],
        'taught_words': len(taught),
        'next': next_line.group(1) if next_line else None,
        'to_reinforce': reinforce.group(1) if reinforce else None,
        'known_jump_start': known_js,
        'review_counter': sorted({b for _, b in review}),
        'rounds': round_summary,
        'expected_answers': len(expected),
        'unknown_hanzi_outside_table': leaks,
        'unknown_hanzi_in_expected_answers': exp_leaks,
        'student_nao_sei': sum(s.count('NÃO SEI') for s in student),
        'new_word_coverage_min': min(coverage.values()) if coverage else None,
        'new_words_under_3': [w for w, c in coverage.items() if c < 3],
        'audio': audio,
        'flags': flags,
    }
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
