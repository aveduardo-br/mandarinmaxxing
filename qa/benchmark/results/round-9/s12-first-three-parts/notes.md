# Notes · sim4/new · scenario s12

Skill: `/home/claude/review/sim4/new/skill/`. Course folder: `/home/claude/review/sim4/new/course/`. Audio: none. All scripts run with `python3 -I` and full paths. The three parts were taught in one chat.

Files written: `transcript.md`, `notes.md`, `course/course.md`, `course-1.md` … `course-4.md`, `plan-1-01.1.txt`, `plan-1-01.2.txt`, `plan-1-02.1.txt`.

## 1. Scripts run, with their output

### Setup

`python3 -I skill/course.py overview 1 5` → exit 0

```
JUMP START
  01 Say hello and thank you (2 parts): 你好 再见 谢谢 不客气 对不起 没关系 您 好 没事
  02 Say what you want (2 parts): 我 要 水 茶 你 吗 不 喝 吃 饭 请 想 喜欢 做
  03 Say who you are (2 parts): 叫 什么 名字 请问 是 他 她 谁 也
  04 Where you're from and where you are (3 parts): 中国 人 在 哪 国 去 哪儿 今天 说 明天 会1 中文 昨天 汉语
  05 Introduce someone (3 parts): 这 那 朋友 的 认识 很 高兴 先生 女士 呢 我们 你们 们 他们 她们 都
  06 Say your age (4 parts): 岁 几 一 十 二 三 四 五 六 七 八 九 今年 多 大 了
  07 Who lives at home (3 parts): 家 有 爸爸 妈妈 口 个 两1 没有 哥哥 妹妹 和1 姐姐 弟弟 爱 家人 多少 零
SITUATIONS
  08 Phone calls (1 part)
  … 09–22 …
TOTAL: 22 lessons, 58 parts at pace 5: about 8 weeks at one part a day
```

`python3 -I skill/course.py new course/course.md 1 5 Português` → exit 0

```
SAVED to /home/claude/review/sim4/new/course/course.md: a new HSK 1 course at pace 5.
Now translate into Português, in the file: the word after each `=` on the Labels line, the three names on the Rounds line, and every lesson name. Keep the numbers and everything else as they are. Then save the file where the course is kept.
```

Translated by hand, as the command asks (Labels, Rounds, 22 lesson names). Copy: `course-1.md`.
`course.py check course/course.md` → `OK: the course file is consistent.`

### Part 1 (HSK 1 · Lesson 1 · part 1 of 2)

`course.py part course/course.md plan-1-01.1.txt` → exit 0

```
PART: HSK 1 · Lesson 1 · Cumprimentar e agradecer · part 1 of 2
NEW WORDS, in blocks that work together: 你好 再见 谢谢 | 不客气 对不起 没关系
REVIEW: none, nothing studied yet. Start at the vocabulary.
EARLY PART: yes: read first-parts.md (0 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
AT THE CLOSE: run `course.py close <course.md>`, with --missed and --recovered for the items to reinforce
PLAN HEADER written to …/plan-1-01.1.txt: add a SUPPORT or NAMES line above DONE if the part needs one, and the plan lines at the end.
```

`check_plan.py plan-1-01.1.txt` → `OK: 13 lines, every character met.` (first draft and again after the last step was reworked).

`student.py` N=1…11: see section 5.

`course.py close course/course.md` (nothing missed) → exit 0

```
CLOSED: 1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系
SAVED to …/course/course.md: Next is `Lesson 01, part 2 of 2`. Put this file back where the course is kept.
```

Kept file read again (first close of the course): the Done line is there. Copy: `course-2.md`.

### Part 2 (HSK 1 · Lesson 1 · part 2 of 2)

`course.py part course/course.md plan-1-01.2.txt` → exit 0

```
PART: HSK 1 · Lesson 1 · Cumprimentar e agradecer · part 2 of 2
NEW WORDS, in blocks that work together: 您 好 没事
REVIEW: the lines of 1-01.1: 你好 再见 谢谢 不客气 对不起 没关系
EARLY PART: yes: read first-parts.md (6 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
…
```

`check_plan.py plan-1-01.2.txt` → `OK: 14 lines, every character met.`

`course.py close course/course.md --missed "没关系"` → exit 0

```
CLOSED: 1-01.2 | 您 好 没事
SAVED to …/course/course.md: Next is `Lesson 02, part 1 of 2`. Put this file back where the course is kept.
Lesson 01 is complete.
```

`To reinforce: 没关系`. Copy: `course-3.md`.

### Part 3 (HSK 1 · Lesson 2 · part 1 of 2)

`course.py part course/course.md plan-1-02.1.txt` → exit 0

```
PART: HSK 1 · Lesson 2 · Dizer o que você quer · part 1 of 2
NEW WORDS, in blocks that work together: 我 要 水 茶 | 你 吗 不
REVIEW: the lines of 1-01.2: 您 好 没事
  and the items to reinforce, once each: 没关系
EARLY PART: yes: read first-parts.md (9 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
…
```

`check_plan.py plan-1-02.1.txt` → exit 0

```
CHECK (advice only, the plan does not fail on these):
  不要: met words cover it, but it is also a word not met yet. Keep it only if you mean the parts. In: 我不要水。 (and 7 more lines)
OK: 21 lines, every character met.
```

Kept: the plan means the parts (不 + 要, "not want").

`course.py close course/course.md --missed "没事, 不要，谢谢" --recovered "没关系"` → exit 0

```
CLOSED: 1-02.1 | 我 要 水 茶 你 吗 不
SAVED to …/course/course.md: Next is `Lesson 02, part 2 of 2`. Put this file back where the course is kept.
```

Result in the file: `To reinforce: 没事, 不要, 谢谢`. **Wrong**: see 2.1. Copy: `course-4.md`.

### Checks on every copy

```
== course-1.md   OK: the course file is consistent.   (exit 0)
== course-2.md   OK: the course file is consistent.   (exit 0)
== course-3.md   OK: the course file is consistent.   (exit 0)
== course-4.md   OK: the course file is consistent.   (exit 0)
```

`course.py progress course/course.md` → `3/58` / `HSK 1: 3 of 58 parts done` / `NEXT: Lesson 02, part 2 of 2`.

After the session I also ran `course.py part course/course.md` with no plan file, to see what the next chat would get: `REVIEW: the lines of 1-02.1 … and the items to reinforce, once each: 没事, 不要, 谢谢`. So the next review would ask 不要 and 谢谢 as two items, not the refusal 不要，谢谢.

## 2. Script failures

### 2.1 `course.py close --missed` splits a chunk at its own comma

SKILL.md, "Closing a part": "`--missed`: … For a slip of word order or grammar, give the short chunk as it should be said." and "each in quotes with commas between items". A Mandarin chunk naturally carries a full-width comma. I passed `--missed "没事, 不要，谢谢"` (two items) and the file got three: `To reinforce: 没事, 不要, 谢谢`. `course.py` line 548 splits on `[,;，；]`. The close prints nothing about To reinforce, so the tutor only sees it by reading the file; `check` says OK; and there is no command to take an item out except `--recovered` at a later close. The skill forbids hand edits, so the file stayed wrong. The same happens with any two-clause chunk (好，再见 / 谢谢，再见 / 我不要茶，我要水).

### 2.2 The close doesn't print the new To reinforce line

Example: the close of part 3 printed only `CLOSED:` and `SAVED … Next is …`. The tutor has no confirmation of what was added, removed or dropped (five at most) without opening the file. This is what hid 2.1.

### 2.3 `check_plan.py` with EARLY lets everything through

In an early part the same line in two rounds is expected (meaning, reply, translation), so the repeat check is off. But it also means nothing checks the rule of first-parts.md "a line is asked once at most in each kind": the plan labels have no way to say the kind (I wrote it in the `prompt:` line, in parentheses, which the checker ignores). Example: in `plan-1-01.1.txt`, `round1: 再见！` and `round2: 再见！` look identical to the checker whether they are a reply and a translation or the same translation twice.

### 2.4 The plan has no label for the last step of an early part

SKILL.md lists `review:`, `round1:`, `round2:`, `round3:`, `chunk:`, `listening:`. The early last step is "moments" under the reading title, with several answers. I put the four expected lines on one `listening:` line. It passed, but nothing says that is the right place.

### 2.5 No script failure otherwise

`overview`, `new`, `part`, `close`, `check`, `progress` all ran with exit 0 and the Done lines, Next and Route were right after every write.

## 3. Where the skill's text was unclear, silent or contradictory

1. **first-parts.md, "Each round has one exercise per new word, five at most" against SKILL.md, "A part of two or three words can have more prompts a round, up to five".** Part 2 has three words (您 好 没事). I took first-parts.md as the page that overrides, so three exercises a round. Result: a part of 11 exercises and about 8 minutes, and no room in round 1 for a fourth line.
2. **SKILL.md, "two to four useful chunks, no more than round 1 has prompts" + "every chunk listed is practised in round 1".** With three round-1 exercises in part 2, only three chunks could be listed. The words give four lines (您好 / 谢谢您 / 好，再见 / 对不起 — 没事). 谢谢您 was left out of the list, so the learner first met it as a translation in round 2 ("Obrigado, senhor!") with nothing but the table to go on.
3. **first-parts.md, "Round 3 is given only when the words make two connected sentences" and "What matters is whether the words allow a question, a negation and two connected sentences: once they do, use the usual rounds".** In Lesson 2 part 1 the brief says `EARLY PART: yes` (9 words met before), but the part's own words (我 要 不 吗) allow a question, a negation and two connected sentences. The text doesn't say whether "the words" counts this part's table. I kept the early format and gave a round 3 of three exercises.
4. **first-parts.md, "Each round has one exercise per new word, five at most"** doesn't say whether round 3 follows it. I gave three in round 3 because the fourth and fifth would have repeated the frame 不要 X，要 Y.
5. **first-parts.md, Review: "Ask the last part's lines in a new situation"** against SKILL.md, "A line, not a description. Never a fragment, a scene description, a stage direction in parentheses". With nine formula words the only way to give "a new situation" is to describe one. I did not describe scenes in the review; I varied the combination (谢谢，再见！).
6. **Asking for one of two synonyms.** lesson-format.md: "give each prompt a context that fits only one, or accept both. When the learner keeps choosing one, ask for the other by name". 没关系 and 没事 have no context that fits only one, and "by name" gives the answer away. I used "a expressão da tabela de hoje", "a palavra nova de hoje", "a expressão mais longa das duas". All three are stage directions in parentheses or instructions, which "Every prompt" forbids. The brief's "items to reinforce, once each: 没关系" has the same problem in the review.
7. **Whether a hinted answer counts for `--recovered`.** SKILL.md: "the items of To reinforce they got right unaided in this part's review". 没关系 was right at review 2 of part 3, after the hint "the longer of the two". I counted it as recovered. "Unaided" is not defined for this case.
8. **"I don't know."** No file says what to do. I treated it as a missed item: the answer on three lines, one line of help, no blockquote, and the item brought back as "After a correction" says.
9. **A natural answer with a word not taught yet.** N=9: the learner wrote 没事 for 没关系 in part 1, one part before 没事 is taught. lesson-format.md says accept any natural version and name the chunk; SKILL.md says "Every piece of Mandarin you show … uses only met words". I accepted without showing 没事 back in bold with pinyin, and said it is a word of the next part.
10. **The exercise count of the last step.** In an early part the last step is one message with two to four moments. The runner counts exercises; I counted the step as one (one student.py call with all the lines). The skill doesn't say whether the moments are sent one at a time, which "Give one exercise at a time" would suggest.
11. **Reading number.** lesson-format.md: "A bold title with the label for reading and its number: **Reading 1**." It doesn't say whether the number restarts in each part. I restarted it (Leitura 1 in all three parts).
12. **Pinyin tones.** SKILL.md: "Accept them and correct them the same way" and "pronunciation and tones are the learner's own practice". The student's pinyin has citation tones (xiè xiè, méi guān xì) where the table has xièxie, méi guānxi. I accepted them without comment. The text doesn't say whether a wrong tone mark in a pinyin answer is an error.
13. **Keyboard reminder.** "The first time in a chat, remind the learner once". Given once, at N=4. The three later pinyin answers got none. In a course where each part is a new chat the reminder would come back every day for a learner who has chosen pinyin.
14. **setup.md, order of the route steps.** "Show a compact overview before the first part … Then: 1. Run `course.py new` … 3. Ask where they want to start". It doesn't say whether `new` runs before or after the learner answers. I ran it in the same turn as the overview (T4), before the answer.
15. **setup.md, "Name the learner's own language where the card says 'your language'."** The card's English text says "from your language into Mandarin"; I wrote "do português".
16. **The 您 rule against "Same content".** "Olá, senhor!" → 您好！ follows the rule for 您 ("put the form of address inside the line") but the answer leaves out the form of address, which "Same content" forbids by name. The text gives the exception only by example.
17. **`--missed` after a "don't know" on an exchange.** N=20 (— 对不起！ — 没事。): the learner didn't know. 没事 came back right at N=22; 对不起 did not come back in the part. I did not list 对不起 (written right at N=15). The rule "got wrong in this part and didn't get right later in it" would list it.

## 4. Rules I could not satisfy

- **"After a correction, bring the item back once."** 没事 (N=26, wrong order) had no natural later prompt in a part about ordering tea; it went to `--missed`. 没关系 (N=12) came back only inside an exchange that accepts both words (N=20), where the learner didn't know; `--missed`.
- **"Across this step, use every new word that fits."** In part 3 the moments use 我 要 茶 不 and not 你 吗 水: the learner speaks only their own side, so a question to "you" has no moment.
- **"A line, not a description … no stage direction in parentheses."** Broken three times to ask for one synonym (see 3.6), and the reply exercises all carry an instruction ("accept", "refuse", "start with 好").
- **A review "at the level of the course".** With 6 to 9 formula words the review can only be single lines; 谢谢，再见！ and 好，谢谢！ were the only combinations.
- **`--missed` with a chunk that has a comma** (2.1).

## 5. The student, exercise by exercise

| N | Part · step | Expected | Student | Kind |
|---|---|---|---|---|
| 1 | P1 · round 1 meaning | Olá! | Olá! | right |
| 2 | P1 · round 1 meaning | Desculpa. | Desculpa. | "missing word" rule, no Hanzi: right |
| 3 | P1 · round 1 reply | 不客气。 | 不客气。 + grammar question | right + question |
| 4 | P1 · round 1 reply | 没关系。 | méi guān xì 。 | pinyin |
| 5 | P1 · round 1 reply | 再见！ | 见再 | wrong order |
| 6 | P1 · round 2 | — 谢谢！ — 不客气。 | não sei essa | doesn't know |
| 7 | P1 · round 2 | 对不起！ | 对不起！ | right |
| 8 | P1 · round 2 | 你好！ | 你好！ | right |
| 9 | P1 · round 2 | 没关系。 | 没事。 | natural alternative |
| 10 | P1 · round 2 | 再见！ | 再见！ | right |
| 11 | P1 · last step | 谢谢！ 不客气。 没关系。 再见！ | xiè xiè ！ bú kè qì 。 méi guān xì 。 zài jiàn ！ | pinyin |
| 12 | P2 · review reply | 没关系。 | 关系没 | wrong order |
| 13 | P2 · review | 谢谢，再见！ | não sei essa | doesn't know |
| 14 | P2 · review reply | 不客气。 | 不客气。 | right |
| 15 | P2 · review | 对不起！ | 对不起！ | right |
| 16 | P2 · round 1 meaning | Olá! (dito a um senhor ou a uma senhora) | same | "missing word" rule, no Hanzi: right |
| 17 | P2 · round 1 reply | 没事。 | 没事。 | right |
| 18 | P2 · round 1 reply | 好，再见！ | hǎo ， zài jiàn ！ | pinyin |
| 19 | P2 · round 2 | 谢谢您！ | 谢您谢 | wrong order |
| 20 | P2 · round 2 | — 对不起！ — 没事。 | não sei essa | doesn't know |
| 21 | P2 · round 2 | 好，谢谢！ | 好，谢谢！ | right |
| 22 | P2 · last step | 您好！ 谢谢您！ 没事。 谢谢，再见！ | same | right |
| 23 | P3 · review | 您好！ | 您！ | last character missing |
| 24 | P3 · review reply | 没关系。 | 没关系。 | right |
| 25 | P3 · review | 好，谢谢！ | hǎo ， xiè xiè ！ | pinyin |
| 26 | P3 · review | 没事。 | 事没 | wrong order |
| 27 | P3 · round 1 meaning | Quero água. | não sei essa | doesn't know |
| 28 | P3 · round 1 reply | 要，谢谢。 | 要，谢谢。 | right |
| 29 | P3 · round 1 meaning | Não quero chá. | Não quero chá. | right |
| 30 | P3 · round 1 reply | 不要，谢谢。 | 不要，谢。 | last character missing |
| 31 | P3 · round 1 meaning | O senhor quer chá? | O senhor quer chá? | right |
| 32 | P3 · round 2 | 我要茶，谢谢。 | wǒ yào chá ， xiè xiè 。 | pinyin |
| 33 | P3 · round 2 | 您要水吗？ | 水吗您要 | wrong order |
| 34 | P3 · round 2 | — 你要茶吗？ — 不要，谢谢。 | não sei essa | doesn't know |
| 35 | P3 · round 2 | 您好！我要水。 | 您好！我要水。 | right |
| 36 | P3 · round 2 | 我不要水，谢谢。 | 我不要水，谢谢。 | right |
| 37 | P3 · round 3 | 我不要茶，我要水。 | 我不要茶，我要。 | last character missing |
| 38 | P3 · round 3 | — 您要水吗？ — 不要，谢谢。我要茶。 | same | right |
| 39 | P3 · round 3 | 好，我要茶。谢谢！ | hǎo ， wǒ yào chá 。 xiè xiè ！ | pinyin |
| 40 | P3 · last step | 您好！ 我要茶。 不要，谢谢。 再见！ | 谢谢。 再见，您好！ 我要茶。 不要。 | wrong order |

The script's answers were used unchanged. The last-step expected answers of parts 1 and 2 were written after the corrections earlier in the part (the plan is a draft), before the student was run for them.

## 6. How the tutor handled each kind of reply

- **The grammar question (N=3, "why is the sentence in this order?" about 不客气).** Confirmed the answer, then two sentences: it is a fixed expression said as one block, and in the exchange the thanks comes first. No breakdown into 不 + 客气, because neither piece was a met word. The skill has no instruction for a question asked inside an answer; the rule "Keep messages on the exercise" was the only guide.
- **The natural alternative (N=9, 没事 for 没关系).** Accepted, named 没关系 in one line as lesson-format.md says, and brought it back in the last step with "the expression of today's table". The learner then wrote it right (N=11), so nothing went to `--missed`. Problems: 3.6 and 3.9.
- **The missing word.** With no small particle in these sentences the student dropped the last character each time: 您！ (N=23), 不要，谢。 (N=30), 我不要茶，我要。 (N=37). All three corrected with the "Incorrect" format: "Você escreveu:", blockquote, one fix line, the sentence on three lines. Brought back: 您好 at N=35 (right), 不要，谢谢 at N=34 (didn't know), N=36 and N=38 (right), 水 after 要 at N=38 (right, but in the other person's question, not after 我要).
- **Pinyin (N=4, 11, 18, 25, 32, 39).** Accepted, sentence shown in Hanzi on one line, keyboard reminder once at N=4. Tones not commented (3.12).
- **The wrong order (N=5 见再, N=12 关系没, N=19 谢您谢, N=26 事没, N=33 水吗您要, N=40).** "Incorrect" format with the stretch in the right order. For the two-character and three-character words the "order" error is really a scrambled word, and the fix line can only say "this character first". N=33 was the one real word-order error, and the fix line gave the pattern (who, 要, what, 吗 at the end). N=40 scrambled the four moments and split 不要，谢谢: corrected as order of the encounter plus the broken refusal; it was the last exercise, so nothing could come back and the chunk went to `--missed`.
- **"I don't know" (N=6, 13, 20, 27, 34).** Answer on three lines, one line of help, next exercise; no blockquote. Brought back: 谢谢 and 不客气 at N=11 (right), 谢谢，再见 at N=22 (right), 没事 at N=22 (right), 我要水 at N=35 (right), the question and the refusal at N=38 (right).

`--missed` and `--recovered` at each close:

- Part 1: none. Everything missed was right later in the part.
- Part 2: `--missed "没关系"`.
- Part 3: `--missed "没事, 不要，谢谢" --recovered "没关系"` → written as 没事, 不要, 谢谢 (2.1).

## 7. Mandarin a mainland speaker would not say

- **我要茶。 / 您好！我要水。 / 好，我要茶。** Grammatical, and said, but bare. At a counter a speaker says 我要一杯茶 or 来杯茶. Cause: no measure word and no 一 before Lesson 6; the SUPPORT allowance (two extra words) would cover 一杯 but then every ordering prompt needs it, in the second lesson of the course. I did not add it.
- **不要，谢谢。 as the answer to 您要水吗？** Natural. **我不要水，谢谢。** as a full sentence is stiffer than 不用了，谢谢, which needs 用 and 了. Cause: met words.
- **您要水吗？** Said by staff as 您要喝水吗 or 您喝水吗 (喝 comes in the next part). Acceptable.
- **谢谢您！ to a cashier, 您好！ to the woman at the counter.** Fine for an older person; to staff of one's own age 你好 is more usual. Cause: the part has to practise 您 with nine words.
- **The reply exercises "start with 好" → 好，再见！** Natural as a line, artificial as an exercise.
- Nothing ungrammatical was shown or expected.

## 8. Exercises per step and estimated minutes

| Part | Review | Round 1 | Round 2 | Round 3 | Last step | Total | Estimate |
|---|---|---|---|---|---|---|---|
| HSK 1 · Lesson 1 · part 1 (6 words) | none | 5 (2 meaning, 3 reply) | 5 translations | none | 1 message, 4 moments | 11 | about 8 to 10 min |
| HSK 1 · Lesson 1 · part 2 (3 words) | 4 (2 reply, 2 translation) | 3 (1 meaning, 2 reply) | 3 translations | none | 1 message, 4 moments | 11 | about 8 min |
| HSK 1 · Lesson 2 · part 1 (7 words) | 4 (1 reply, 3 translation) | 5 (3 meaning, 2 reply) | 5 translations | 3 translations | 1 message, 4 moments | 18 | about 15 to 18 min |

Student numbers: N=1–11, N=12–22, N=23–40.

## 9. Decisions the skill left to me

- The learner's language: Portuguese, from the interface and the project name (setup.md covers this).
- The button message, worked out from `web/setup.js`: legend text + `: ` + `data-value` or label with the `<small>` text in parentheses, joined with `. ` → `Nível: HSK 1. Ritmo: Recomendado (cerca de 5). Áudio: desligado, com leitura no lugar.`
- Part 1: no round 3 (six formula words), and the echo reply used once, for 再见.
- Part 1, last step: the four moments were changed after N=5, N=6 and N=9 to bring back 谢谢, 不客气 and 没关系; 你好 and 对不起 left it.
- Part 2: three exercises a round (3.1); 谢谢您 not listed as a chunk (3.2).
- Part 3: round 3 given, three exercises (3.3, 3.4); 您好 brought back at N=35 and the refusal at N=34, N=36, N=38.
- The role-play offer was made once at the close of part 2 and not mentioned again after the learner declined.
- The learner's lines outside the exercises that the scenario doesn't word (T5, T29, T53) are mine, kept minimal.

## 10. Observations on the lesson itself

- The three parts work as a first sitting: short, every line written by the learner in Mandarin at least once, nothing shown that wasn't met.
- Part 2 is thin. Three words at "one exercise per new word" give six round exercises, and the review (four) is longer than either round.
- The same exchange (对不起 — 没关系/没事) came up in nine of the 40 exercises (N=4, 9, 11, 12, 17, 20, 22, 24, 26). With two synonyms and nine words there is little else to ask, and the learner sees it.
- The "wrong order" correction format ("the stretch in the right order") says nothing useful for a two-character word.
- A learner who answers "I don't know" to a meaning exercise (N=27) gets the meaning and moves on; the line can't be asked again as meaning in the part ("once at most in each kind"), so only the translation later tests it.
