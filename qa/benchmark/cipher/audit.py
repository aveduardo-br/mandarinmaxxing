"""Assemble and audit a ciphered-student run.

Usage (from the repository root):
  python3 qa/benchmark/cipher/audit.py assemble <run>/part-NN
      Builds part-NN/transcript.md (the tutor's real messages and the decoded answers) and
      part-NN/transcript.student.md (what the student saw and wrote) from the numbered files.
  python3 qa/benchmark/cipher/audit.py report <run>
      Runs qa/benchmark/check_run.py on every part and writes <run>/report.md: words that never
      came back, how often each word was practised, every [NÃO SEI], review length against round 2,
      and whether course.md stayed consistent.

A run folder holds part-01, part-02, ...; each part holds the message files, course-start.md
(course.md before the part) and course/course.md (after it).
"""
import glob
import json
import os
import re
import subprocess
import sys

HAN = re.compile(r'[一-鿿]')


def numbered(part, prefix, suffix):
    files = glob.glob(os.path.join(part, f'{prefix}-[0-9][0-9][0-9]{suffix}'))
    return sorted(files, key=lambda f: int(re.search(r'-(\d{3})', os.path.basename(f)).group(1)))


def assemble(part):
    real, seen = [], []
    a_real = {int(re.search(r'-(\d{3})', f).group(1)): f for f in numbered(part, 'a', '.md')}
    a_enc = {int(re.search(r'-(\d{3})', f).group(1)): f for f in numbered(part, 'a', '.enc.md')}
    t_real = {int(re.search(r'-(\d{3})', f).group(1)): f for f in numbered(part, 't', '.md')}
    s_enc = {int(re.search(r'-(\d{3})', f).group(1)): f for f in numbered(part, 's', '.enc.md')}
    n, turn = 0, 0
    while n in a_real or n in t_real:
        if n in a_real:
            turn += 1
            real.append(f'## T{turn} · STUDENT\n{open(a_real[n], encoding="utf-8").read().strip()}\n')
            seen.append(f'## T{turn} · STUDENT\n{open(a_enc.get(n, a_real[n]), encoding="utf-8").read().strip()}\n')
        if n + 1 in t_real:
            turn += 1
            real.append(f'## T{turn} · TUTOR\n{open(t_real[n + 1], encoding="utf-8").read().strip()}\n')
            seen.append(f'## T{turn} · TUTOR\n{open(s_enc.get(n + 1, t_real[n + 1]), encoding="utf-8").read().strip()}\n')
        n += 1
    open(os.path.join(part, 'transcript.md'), 'w', encoding='utf-8').write('\n'.join(real))
    open(os.path.join(part, 'transcript.student.md'), 'w', encoding='utf-8').write('\n'.join(seen))
    print(f'{part}: {turn} turns')


def done_lines(path):
    lines, on = [], False
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            on = line.strip() == '## Done'
        elif on and '|' in line:
            k, ws = line.split('|', 1)
            lines.append((k.strip(), [re.sub(r'\d+$', '', w) for w in ws.split()]))
    return lines


def report(run):
    parts = sorted(glob.glob(os.path.join(run, 'part-[0-9][0-9]')))
    rows, expected_by_part, nao_sei = [], {}, []
    for i, part in enumerate(parts, 1):
        start = os.path.join(part, 'course-start.md')
        out = subprocess.run([sys.executable, 'qa/benchmark/check_run.py', part, start if os.path.exists(start) else '-'],
                             capture_output=True, text=True)
        if out.returncode:
            rows.append((i, None, out.stderr.strip()[-200:]))
            continue
        d = json.loads(out.stdout)
        json.dump(d, open(os.path.join(part, 'check.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        rows.append((i, d, None))
        t = open(os.path.join(part, 'transcript.md'), encoding='utf-8').read()
        expected_by_part[i] = [e.split('(')[0] for e in re.findall(r'<!--\s*expected:(.*?)-->', t, flags=re.S)]
        for f in numbered(part, 'a', '.enc.md'):
            for w in re.findall(r'\[NÃO SEI:\s*([^\]]+)\]', open(f, encoding='utf-8').read()):
                nao_sei.append((i, os.path.basename(f), w.strip()))

    final = os.path.join(parts[-1], 'course', 'course.md') if parts else None
    taught = []  # (part index, word)
    if final and os.path.exists(final):
        for idx, (key, ws) in enumerate(done_lines(final), 1):
            taught += [(idx, w) for w in ws]
    practice = {}
    for p_taught, w in taught:
        later = [p for p, exps in expected_by_part.items() if p > p_taught and any(w in e for e in exps)]
        total = sum(sum(w in e for e in exps) for p, exps in expected_by_part.items() if p > p_taught)
        practice[w] = (p_taught, later, total)
    eligible = {w: v for w, v in practice.items() if v[0] < len(parts)}
    never = sorted(w for w, v in eligible.items() if not v[1])

    md = [f'# Ciphered-student run: {os.path.basename(os.path.abspath(run))}', '',
          f'{len(parts)} parts, {len(taught)} words taught.', '',
          '## Words that never came back after the part that taught them', '',
          (', '.join(never) if never else 'None.') + f'  ({len(never)} of {len(eligible)} words taught before the last part)', '',
          '## How often each word came back (expected answers in later parts)', '',
          '| Word | Taught in part | Later parts with it | Times |', '|---|---|---|---|']
    md += [f'| {w} | {p} | {", ".join(map(str, later)) or "—"} | {tot} |' for w, (p, later, tot) in sorted(practice.items(), key=lambda x: x[1][0])]
    md += ['', '## [NÃO SEI] from the student', '']
    md += [f'- part {p}, {f}: {w}' for p, f, w in nao_sei] or ['None.']
    md += ['', '## Per part', '', '| Part | Done line | Next | Review prompts | Review / round 2 length | Older words used | Unknown Hanzi |', '|---|---|---|---|---|---|---|']
    for i, d, err in rows:
        if d is None:
            md.append(f'| {i} | error: {err} | | | | | |')
            continue
        L = d['avg_hanzi_per_expected_answer']
        md.append(f"| {i} | {', '.join(d['new_done_lines'])} | {d['next']} | {d['review_counter']} | {L.get('review')} / {L.get('2')} | "
                  f"{len(d['older_words']['used'])} of {len(d['older_words']['scheduled'])} | {''.join(d['unknown_hanzi_outside_table'].keys()) or '—'} |")
    open(os.path.join(run, 'report.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(f'wrote {os.path.join(run, "report.md")}')


if __name__ == '__main__':
    {'assemble': assemble, 'report': report}[sys.argv[1]](sys.argv[2])
