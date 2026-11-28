"""A fixed student for simulated lessons: its answers are decided by rule, not by the tutor.

Usage: python3 qa/benchmark/student.py N "EXPECTED ANSWER"

N is the number of the exercise in the session, counted from 1 across every step. The
tutor passes the answer it expects and sends the learner whatever this prints, unchanged.
The same N and answer always give the same reply, so two versions of the skill can be
compared on the same student.

What it does, by N:
  N = 3            answers right and asks a grammar question
  N = 9            answers with a natural alternative when it knows one (没事 for 没关系, …)
  N % 7 = 2        leaves out a small word (了, 的, 吗, …), or the last character
  N % 7 = 4        answers right, in pinyin (needs the pypinyin package; else in Hanzi)
  N % 7 = 5        gets the order wrong: swaps the two halves of the sentence
  N % 7 = 6        says it doesn't know
  anything else    answers right

An expected answer with no Hanzi (a meaning exercise) is given back as it is, except
when the rule says the student doesn't know.
"""
import re
import sys

SMALL = '了的吗吧呢很也都就'
ALTERNATIVES = [('没关系', '没事'), ('中文', '汉语'), ('星期天', '星期日'), ('一点儿', '有点儿'), ('但是', '可是')]


def reply(n, expected):
    han = re.search(r'[一-鿿]', expected)
    if n % 7 == 6:
        return 'não sei essa'
    if not han:
        return expected
    if n == 3:
        return expected + '\n\n(uma dúvida: por que a frase fica nessa ordem?)'
    if n == 9:
        for a, b in ALTERNATIVES:
            if a in expected:
                return expected.replace(a, b)
        return expected
    if n % 7 == 2:
        for ch in SMALL:
            if ch in expected:
                return expected.replace(ch, '', 1)
        return re.sub(r'([一-鿿])([^一-鿿]*)$', r'\2', expected)
    if n % 7 == 4:
        try:
            from pypinyin import pinyin, Style
            return ' '.join(s[0] for s in pinyin(re.sub(r'[^一-鿿，。？！]', '', expected), style=Style.TONE))
        except ImportError:
            return expected
    if n % 7 == 5:
        parts = re.split(r'([，,])', expected.rstrip('。！？'), maxsplit=1)
        if len(parts) == 3:
            return parts[2].strip() + '，' + parts[0] + '。'
        text = re.sub(r'[^一-鿿]', '', expected)
        half = max(1, len(text) // 2)
        return text[half:] + text[:half]
    return expected


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    print(reply(int(sys.argv[1]), sys.argv[2]))
