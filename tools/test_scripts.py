"""Regression tests for course.py and check_plan.py.

Usage: python3 tools/test_scripts.py

Each case is a small course file or plan with the result it must give: the exit code and
a piece of the output. Most come from defects found in the reviews of November 2026.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKILL = os.path.join(ROOT, 'skills', 'mandarinmaxxing')
HEAD = '# mandarinmaxxing course\n- Syllabus: HSK 3.0 (2025-11), level {level}\n- Pace: about {pace} words per part\n- Route: {route}\n{next}- To reinforce: none\n\n## Lessons\n{lessons}\n## Done\n{done}\n'
L1P1 = '1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系'


def course(next='Lesson 01, part 1 of 2', done='', route='01–22', lessons='', pace=5, level=1):
    return HEAD.format(level=level, pace=pace, route=route, next=f'- Next: {next}\n' if next is not None else '', lessons=lessons, done=done)


def plan(body, head='LEVEL 1\nNEW 你好\nDONE\nPLAN\n'):
    return head + body + '\n'


COURSE = [
    # name, file, command and arguments (the file's path is added after the command), exit code, text the output must hold
    ('first part', course(), ['part'], 0, 'NEW WORDS, in blocks that work together: 你好 再见 谢谢 | 不客气 对不起 没关系'),
    ('closing the first part', course(), ['close'], 0, 'Next is `Lesson 01, part 2 of 2`'),
    ('a lesson begun at pace 3 keeps its split after the pace changes',
     course('Lesson 02, part 2 of 2', '1-02.1 | 我 要 水 茶\n' + L1P1 + '\n1-01.2 | 您 好 没事', route='01,02'), ['part'], 0, 'NEW WORDS, in blocks that work together: 你 吗 不'),
    ('the close points at the next part of a lesson begun at another pace',
     course('Lesson 01, part 2 of 2', '1-02.1 | 我 要 水 茶\n' + L1P1, route='01,02'), ['close'], 0, 'Next is `Lesson 02, part 2 of 4`'),
    ('a lesson twice on the route', course('Lesson 01, part 2 of 2', L1P1, route='01,01,02'), ['part'], 1, 'more than once'),
    ('the level is not complete while an earlier lesson of the route is open',
     course('Lesson 02, part 2 of 2', '1-02.1 | 我 要 水 茶 你 吗 不', route='01,02'), ['close'], 0, 'Next is `Lesson 01, part 1 of 2`'),
    ('the last part of the route completes the level',
     course('Lesson 01, part 2 of 2', L1P1, route='01'), ['close'], 0, 'Next is `level complete`'),
    ('the same part twice in Done', course('Lesson 01, part 2 of 2', L1P1 + '\n' + L1P1), ['part'], 1, 'twice'),
    ('a Done line with no words', course('Lesson 02, part 1 of 2', '1-01.1 |'), ['part'], 1, 'no words'),
    ('no Next line', course(None), ['part'], 1, 'no `Next` line'),
    ('an empty Next is not a finished level', course(''), ['part'], 1, 'Lesson 01, part 1 of 2'),
    ('a Next it cannot read', course('HSK 1 Lesson 02 part 1 of 2'), ['part'], 1, "Can't read the Next line"),
    ('a wrong total in Next is noted', course('Lesson 01, part 1 of 99'), ['part'], 0, 'NOTE: Next said "of 99"'),
    ('Next on a lesson marked known', course(lessons='01 Say hello (known)\n'), ['part'], 1, 'marked (known)'),
    ('Done and known words are counted once', course('Lesson 02, part 1 of 2', L1P1, lessons='01 Say hello (known)\n'), ['part'], 0, '(9 words met before this part)'),
    ('Next says complete with lessons left', course('level complete', L1P1), ['part'], 1, 'still has Lesson 01, part 2 of 2'),
    ('a pace that is none of the three', course(pace=4), ['part'], 0, 'NOTE: Pace is 4: using 3'),
    ('practice of a part already studied changes nothing', course('Lesson 01, part 2 of 2', L1P1), ['part', '--lesson', '1', '--part', '1'], 0, 'AT THE CLOSE: nothing to save'),
    ('--lesson alone gives the first part not yet studied', course('Lesson 02, part 1 of 2', L1P1), ['part', '--lesson', '1'], 0, 'part 2 of 2'),
    ('the old Known line still works', course('Lesson 08, part 1 of 1', lessons='').replace('- To reinforce', '- Known: jump start\n- To reinforce'), ['part'], 0, 'KNOWN LESSONS (never shown by the course): 01 02 03 04 05 06 07'),
    ('To reinforce: missed items join, recovered ones leave, five at most',
     course('Lesson 01, part 2 of 2', L1P1).replace('To reinforce: none', 'To reinforce: 一, 二, 三, 四, 五'), ['close', '--recovered', '二', '--missed', '六, 七'], 0, None),
    ('a jump puts the lesson first and lists the jump start not studied', course(), ['jump', '12'], 0, 'JUMP-START LESSONS NOT STUDIED: 01 02 03 04 05 06 07'),
    ('a jump to a finished lesson is practice', course('Lesson 02, part 1 of 2', L1P1 + '\n1-01.2 | 您 好 没事'), ['jump', '1'], 1, 'as practice'),
    ('marking the lesson in Next as known moves Next', course(), ['known', '1'], 0, 'Next is `Lesson 02, part 1 of 2`'),
    ('studying a known lesson half done goes to its open part',
     course('Lesson 02, part 1 of 2', L1P1, lessons='01 Say hello (known)\n', route='02–22'), ['study', '1'], 0, 'Next is `Lesson 01, part 2 of 2`'),
    ('a pace change keeps a lesson begun at its old pace',
     course('Lesson 02, part 2 of 2', L1P1 + '\n1-01.2 | 您 好 没事\n1-02.1 | 我 要 水 茶 你 吗 不'), ['pace', '3'], 0, 'Next is `Lesson 02, part 2 of 2`'),
    ('a level change starts the new level and keeps Done', course('level complete', L1P1), ['level', '2'], 0, 'Next is `Lesson 01, part 1 of 2`'),
    ('an old file is written in the current format', course(), ['migrate'], 0, 'SAVED'),
    ('check finds a Next that disagrees with Done', course('Lesson 01, part 1 of 2', L1P1), ['check'], 1, 'Done says `Lesson 01, part 2 of 2`'),
]

PLAN = [
    ('a good early plan', plan('chunk: 你好！\nround1: 你好！\nprompt: Olá!\nround2: 你好！', 'LEVEL 1\nEARLY\nNEW 你好\nDONE\nPLAN\n'), 0, 'OK'),
    ('a character nobody taught', plan('round1: 龘\nround2: 你好\nround3: 你好！你好'), 1, 'NOT MET'),
    ('the review cannot use the new words', plan('review: 你好\nround1: 你好\nround2: 你好。\nround3: 你好！你好'), 1, 'in review: 你好'),
    ('a label it does not know', plan('revisao: 你好\nround1: 你好\nround2: 你好。\nround3: 你好！'), 1, 'no label this script knows'),
    ('a prompt in Chinese needs its label', plan('round1: 你好\n请翻译下面的句子'), 1, 'no label this script knows'),
    ('a labelled prompt is skipped', plan('round1: 你好\nprompt: 请翻译\nround2: 你好。你好\nround3: 你好！你好。你好'), 0, 'OK'),
    ('an answer written only in pinyin', plan('round1: ni hao\nround2: 你好\nround3: 你好。'), 1, 'has no Hanzi'),
    ('a round with no line', plan('round1: 你好\nround1: 你好。你好\nround1: 你好！你好！你好'), 1, 'No round2 line'),
    ('the same sentence twice', plan('round1: 你好\nround2: 你好\nround3: 你好。你好'), 1, 'comes twice'),
    ('a word only inside a longer word is counted, with advice', plan('round1: 你好\nround2: 你好，你好\nround3: 你好。你好。你好', 'LEVEL 1\nNEW 好 你好\nDONE\nPLAN\n'), 0, '好 never stands on its own'),
    ('a separable word said apart', plan('round1: 我洗了澡\nround2: 我洗过澡\nround3: 我想洗个澡', 'LEVEL 3\nNEW 洗澡\nDONE\nPLAN\n'), 0, 'OK'),
    ('two words are not joined into a separable one', plan('round1: 超市场\nround2: 你好\nround3: 你好。你好', 'LEVEL 1\nNEW 你好\nDONE\n1-01.1 | 超市 市场\nPLAN\n'), 1, 'NOT MET'),
    ('more than two support words', plan('round1: 你好\nround2: 你好。你好\nround3: 你好！你好。', 'LEVEL 1\nNEW 你好\nSUPPORT 一 二 三\nDONE\nPLAN\n'), 1, 'two extra words at most'),
    ('KNOWN with no numbers', plan('round1: 你好\nround2: 你好。你好\nround3: 你好！你好。', 'LEVEL 1\nKNOWN\nNEW 你好\nDONE\nPLAN\n'), 1, 'KNOWN has no lesson numbers'),
    ('CHECK is advice and does not fail', plan('round1: 要是\nround2: 是，要\nround3: 是，要。要是', 'LEVEL 1\nNEW 要 是\nDONE\nPLAN\n'), 0, 'advice only'),
    ('没 alone and a missing final 儿 are met', plan('round1: 我没吃面条\nround2: 面条儿，我没吃\nround3: 我吃面条儿。我没吃', 'LEVEL 1\nNEW 面条儿\nDONE\n1-02.1 | 我 吃\nPLAN\n'), 0, 'OK'),
    ('a prompt that starts with a keyword is not a command', plan('round1: 你好\nprompt: Level 3 is hard.\nround2: 因为\nround3: 你好。你好'), 1, 'NOT MET'),
    ('a met word this level teaches again later', plan('round1: 丢了，我还书\nround2: 丢了吗\nround3: 我丢了。你丢了', 'LEVEL 3\nNEW 丢\nDONE\nPLAN\n'), 0, 'another reading or sense'),
]


def run(script, text, args=()):
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(text)
    args = list(args)
    cmd = [sys.executable, os.path.join(SKILL, script)] + (args[:1] + [f.name] + args[1:] if script == 'course.py' else [f.name])
    out = subprocess.run(cmd, capture_output=True, text=True)
    after = open(f.name, encoding='utf-8').read()
    os.unlink(f.name)
    return out.returncode, out.stdout + out.stderr, after


def main():
    failed = 0
    for name, text, args, code, want in COURSE:
        got, out, after = run('course.py', text, args)
        ok = got == code and (want in out if want else '- To reinforce: 三, 四, 五, 六, 七' in after)
        if ok and got == 0 and args[0] not in ('part', 'check'):
            again, report, _ = run('course.py', after, ['check'])
            # the test files carry no labels and some have a short route: only a wrong Next or Done fails here
            ok = again == 0 or not any(w in report for w in ('Next', 'Done says', 'twice'))
        if not ok:
            failed += 1
            print(f'FAIL course.py: {name}\n  wanted exit {code} and "{want}"\n  got exit {got}:\n    ' + out.strip().replace('\n', '\n    '))
    for name, text, code, want in PLAN:
        got, out, _ = run('check_plan.py', text)
        if got != code or want not in out:
            failed += 1
            print(f'FAIL check_plan.py: {name}\n  wanted exit {code} and "{want}"\n  got exit {got}:\n    ' + out.strip().replace('\n', '\n    '))
    print(f'{len(COURSE) + len(PLAN) - failed} of {len(COURSE) + len(PLAN)} tests passed')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
