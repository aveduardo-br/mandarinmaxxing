# Notes · sim3/new

Scenario: Brazilian complete beginner, project "Mandarim", app in Portuguese, empty `course/`. Setup card (HSK 1, recommended, audio off), route accepted, then HSK 1 Lesson 1 part 1, Lesson 1 part 2, role-play declined, Lesson 2 part 1. 82 turns. All three parts were "early parts" (0, 6 and 9 words met), so `first-parts.md` governed all of them: the usual rounds of `SKILL.md` were never exercised.

Files: `transcript.md`, `course/course.md` (final), `course-after-setup.md`, `course-after-L1p1.md`, `course-after-L1p2.md`, `course-after-L2p1.md`, `plan-L1p1.txt`, `plan-L1p2.txt`, `plan-L2p1.txt`.

All commands were run from `/home/claude/review/sim3/new` (not from the skill folder), with `S=/home/claude/review/sim3/new/skill`.

## 1. Scripts

### Runs

**Run 1** · `python3 -I $S/course.py overview 1 5` · exit 0

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
  09 Kids, partners and pets (2 parts)
  10 Dates and weekdays (2 parts)
  11 Time and daily routine (4 parts)
  12 Eating and drinking (3 parts)
  13 Shopping and paying (4 parts)
  14 Choosing clothes and things (3 parts)
  15 Where things are (4 parts)
  16 Coming and going (2 parts)
  17 Free time (3 parts)
  18 Talking about the weather (2 parts)
  19 Studying Chinese (3 parts)
  20 At school (3 parts)
  21 Talking about work (2 parts)
  22 Getting sick (1 part)
TOTAL: 22 lessons, 58 parts at pace 5: about 8 weeks at one part a day
```

**Run 2** · `python3 -I $S/course.py` (no arguments, to see the usage) · exit 1. Printed the usage text (`overview LEVEL PACE`, `part COURSE.md [PLAN.txt] [--lesson N [--part K]]`).

**Run 3** · `python3 -I $S/course.py part /home/claude/review/sim3/new/course/course.md /home/claude/review/sim3/new/plan-L1p1.txt` · exit 0

```
PART: HSK 1 · Lesson 1 · Cumprimentar e agradecer · part 1 of 2
NEW WORDS, in blocks that work together: 你好 再见 谢谢 | 不客气 对不起 没关系
REVIEW: none, nothing studied yet. Start at the vocabulary.
EARLY PART: yes: read first-parts.md (0 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
AT THE CLOSE: add `1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系` to Done; Next becomes Lesson 01, part 2 of 2
PLAN HEADER written to /home/claude/review/sim3/new/plan-L1p1.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```

Header written: `LEVEL 1 / EARLY / NEW 你好 再见 谢谢 不客气 对不起 没关系 / DONE / PLAN`.

**Run 4** · `python3 -I $S/check_plan.py` (no arguments, to see the plan format, which `SKILL.md` does not give in full) · exit 1. Printed the usage text (plan layout, what NOT MET / CHECK / counts mean).

**Run 5** · `python3 -I $S/check_plan.py /home/claude/review/sim3/new/plan-L1p1.txt` · exit 0

```
OK: 17 lines, every character met.
```

**Run 6** · `python3 -I $S/course.py part .../course/course.md .../plan-L1p2.txt` (after the part 1 save) · exit 0

```
PART: HSK 1 · Lesson 1 · Cumprimentar e agradecer · part 2 of 2
NEW WORDS, in blocks that work together: 您 好 没事
REVIEW: one prompt per word of 1-01.1: 你好 再见 谢谢 不客气 对不起 没关系
EARLY PART: yes: read first-parts.md (6 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
AT THE CLOSE: add `1-01.2 | 您 好 没事` to Done; Next becomes the first part of the next lesson on the route (or `level complete`)
PLAN HEADER written to /home/claude/review/sim3/new/plan-L1p2.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```

**Run 7** · `python3 -I $S/check_plan.py .../plan-L1p2.txt` · exit 0

```
OK: 18 lines, every character met.
```

**Run 8** · `python3 -I $S/course.py part .../course/course.md .../plan-L2p1.txt` (after the part 2 save) · exit 0

```
PART: HSK 1 · Lesson 2 · Dizer o que você quer · part 1 of 2
NEW WORDS, in blocks that work together: 我 要 水 茶 | 你 吗 不
REVIEW: one prompt per word of 1-01.2: 您 好 没事
  and one for each item to reinforce: 您好
EARLY PART: yes: read first-parts.md (9 words met before this part)
ROUNDS AND LAST STEP: as first-parts.md says
AT THE CLOSE: add `1-02.1 | 我 要 水 茶 你 吗 不` to Done; Next becomes Lesson 02, part 2 of 2
PLAN HEADER written to /home/claude/review/sim3/new/plan-L2p1.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```

**Run 9** · `python3 -I $S/check_plan.py .../plan-L2p1.txt` · exit 0

```
CHECK (met words cover it, but it is also a word not met yet; keep it only if you mean the parts):
  不要  in: 我不要茶。 (and 8 more lines)
```

Kept: 不 + 要 is meant.

**Runs 10–11** · `check_plan.py` again on `plan-L1p1.txt` and `plan-L1p2.txt` after one last-step line in each was reworked during the part (after a correction) · both exit 0, `OK: 17 lines` and `OK: 18 lines`.

**Run 12** (simulator probe, not something the skill asks for) · a copy of `plan-L2p1.txt` with two lines appended, `(dica) 喝水` and `review: 我要水。` · exit 1

```
NOT MET (rewrite the sentence, or list the word as a support word):
  喝  in line: (dica) 喝水
  我要水  in review: 我要水。
CHECK ...
  不要  in: 我不要茶。 (and 8 more lines)
```

**Saves.** There is no script for saving. `course.md` was written by hand four times (setup, and the close of each part): append the Done line, edit `Next`, edit `To reinforce`.

### What the scripts got wrong or left unclear

1. **The brief does not name `Next` at the end of a lesson.** Run 6: "Next becomes the first part of the next lesson on the route (or `level complete`)". The tutor has to work out `Lesson 02, part 1 of 2` from Route and Lessons by hand, in the one case where it is easiest to get wrong. Runs 3 and 8 give the exact line.
2. **The brief's review line double-counts.** Run 8 asks for "one prompt per word of 1-01.2: 您 好 没事" and "one for each item to reinforce: 您好". 您 and 您好 are the same prompt, so the stated total of four is really three.
3. **The brief's review count contradicts `first-parts.md`.** Runs 6 and 8 say "one prompt per word" while the same brief says the part is early, and `first-parts.md` says the review "can have fewer prompts than that part had words" and must use a kind not asked before. The brief gives no number for the rounds or the last step in early parts ("as first-parts.md says"), so "how many exercises each step has" (`SKILL.md`) is not delivered for the parts where the count is hardest to work out.
4. **`course.py` "does the course's bookkeeping" (`SKILL.md`) but writes nothing to `course.md`.** The save is three hand edits per part. A `close` command would remove the risk.
5. **`check_plan.py` checks unlabelled lines that contain Hanzi.** The usage says a line with no Hanzi is skipped; a prompt line that quotes the other speaker, such as `(resposta a 谢谢！) De nada.`, is counted as a plan line (17 and 18 lines reported, against 15 and 17 labelled ones) and checked (run 12). Harmless here, but a prompt quoting a word outside the met set would be reported as a NOT MET answer.
6. **The plan format is only in the script's usage text.** `SKILL.md` names the labels but not the header, `SUPPORT`, `NAMES`, or how a two-speaker exchange or the early last step should be written. I ran the script with no arguments to find out, and used `listening:` for the "moments" lines.
7. **The CHECK for 不要** fires on 9 of the lines of a part whose whole point is 不 + 要. Exit 0, so no harm, but it is noise the tutor cannot act on.
8. **The checker sees none of what actually went wrong in these parts**: the same line planned twice (我不要茶，我要水 as meaning and as translation), every sentence on one frame, a chunk never asked. With `EARLY` it reports no counts at all, so in the first parts it only confirms the characters.
9. **Paths.** `SKILL.md` writes `python3 course.py part <course.md> plan.txt` with relative paths. Run from the course folder the script path is wrong; run from the skill folder the plan lands in the skill folder. Absolute paths were needed for all three arguments.
10. **Overview** prints lesson names in English and the brief prints the translated name from `course.md`: fine. "about 8 weeks" for 58 parts is 8.3 weeks: fine.

## 2. Had to guess

1. **Route format.** `setup.md`: "the route in map order". `SKILL.md` shows `Route: 01–07, 12, 13, 08, 09, …`. I wrote `Route: 01–22`.
2. **Labels and Rounds at setup.** `setup.md` step 1 says to save "the settings"; only `SKILL.md` says "If a file lacks one, choose it once and save it". I chose them at setup: `Aula, parte, Revisão, Rodada, Ditado, Áudio, Leitura, Frases úteis, Largada` and `Frases prontas, Ações completas, Sequências`. The three round names were never shown (early rounds open "with their number alone").
3. **The card's `data-value` texts are translated** (`setup.md`: "translate … the `data-value` and `data-note` texts with it"), so the button sent `Áudio: desligado, leitura no lugar.` and the tutor has to read back its own translation. The level value `HSK 1` needs no translation. Worked, but the message is only as stable as the tutor's wording.
4. **How many exercises a round has.** `first-parts.md`: "Each round has one exercise per new word, five at most, and fewer when the lines run out." With 6 words I read 5 for round 1 and gave 4 in round 2 (lines ran out); with 3 words, 3 and 3; with 7 words, 5, 4 and 2. Whether the same cap applies to round 3 is not said.
5. **"A line is asked once at most in each kind"** (`first-parts.md`). Not said: whether a line inside a two-line exchange counts as that line asked; whether the limit is per part or carries into the next part's review; whether the last step's "moments" are a fourth kind. I treated an exchange as its own line, the limit as per part plus the review rule, and the moments as outside the count.
6. **The early review.** "Ask the last part's lines in a kind they weren't asked in, or inside a new exchange with words met since." In part 2 nothing has been met since, and 你好, 再见 and 没关系 had no unused kind (see section 3). I gave 4 prompts for 6 words and left 你好 and 没关系 out.
7. **How to write an exchange as a chunk.** `lesson-format.md`: a chunk "takes three lines"; `first-parts.md`: "An exchange of two lines can be listed as a chunk". I put both speakers on each of the three lines with dashes.
8. **The early last step without audio.** `first-parts.md`: "skip the reading text: under the reading title, name two to four moments". Not said: whether the **Your turn** line stays, whether the moments are a numbered list, how the answer is corrected, and whether "Reading 1" restarts in each part. I used the title, one framing line, a numbered list, and "Leitura 1" in every part.
9. **Feedback on a wrong meaning answer** (T34). The "Incorrect" format in `lesson-format.md` is written for a Mandarin answer ("the full corrected sentence once, on three lines"). I quoted the Portuguese answer and gave the Mandarin line on three lines.
10. **Feedback on a wrong reply** (T12): the corrected "sentence" could be the reply alone or the whole exchange. I gave the reply alone.
11. **Whether a wrong meaning answer is "corrected" in the sense of "After a correction"** and can go to To reinforce. I treated it so: reworked the last step of part 2 to call for 不客气.
12. **The role-play offer.** `lesson-format.md`: "the wrap-up role-play (it is described in `requests.md`)". `SKILL.md` says to read `requests.md` only when the learner asks for something. I offered it in one sentence without reading the file ("uma conversa simulada, usando o que você viu nela"); there is no label for it in **Labels**. The learner declined, so the file was never read.
13. **"When the learner keeps choosing one, ask for the other by name … and again in the next part's review."** One choice of 没关系 over 没事 (T39): is that "keeps choosing"? I treated it so. Nothing in `course.md` records it, so "again in the next part's review" only happened because part 3 ran in the same chat; in a new chat it would be lost.
14. **Pinyin reminder.** "The first time in a chat": the three parts were one chat, so it was given once (T20).
15. **Does a chunk's "slot" hint and "never the chunk as listed" apply when round 1 is meaning and reply exercises?** I changed a slot in each round 1 line of Lesson 2 part 1. The result: 我要水 and 你要茶吗 as listed were never asked in a round.
16. **Reading `web/setup.js`.** `SKILL.md` says `web/` is never read during a lesson. I read it only as the simulator, to compute the button's message; the tutor did not need it.

## 3. Rules I could not satisfy

1. **"Every chunk listed is practised in round 1" against "one exercise per new word"** (Lesson 1 part 2, three words). The natural lines are four: 您好, 谢谢您, 好，再见, 对不起 — 没事. Round 1 has three exercises. I left 谢谢您 off the chunk list, so the learner was asked to translate "Obrigada, senhora!" (T44) without ever having seen 谢谢您.
2. **No reply exercise exists for a greeting.** `first-parts.md` forbids an echo ("Hi! — Hi!"), and the natural reply to 你好, 您好 and 再见 is the echo. So in a lesson about greeting, the greetings can only be asked as "what does it mean?" (directly under a table that says what they mean) and as a translation. The reply kind is left to 谢谢 → 不客气 and 对不起 → 没关系.
3. **The polite-form rule cannot produce a prompt for 您好.** `SKILL.md`: "put the form of address inside the line where 您 goes … never as a call at the start", and "Same content … Nothing in it that the answer leaves out". 您 is the first word of 您好, and Portuguese has no polite "olá". "Olá, senhor!" (T42) adds a word the answer does not have, and the student did what the rule predicts, translating every word: **你好，您！** (T43).
4. **To reinforce against "never repeat a prompt" and "a kind they weren't asked in".** 您好 went to To reinforce. It had already been asked as meaning and as translation, a reply is an echo, and the review cannot use the new words. The only possible prompt was the same one with senhor swapped for senhora (T54): the third time in two parts.
5. **没事 against 没关系.** `lesson-format.md`: "give each prompt a context that fits only one, or accept both". No context separates them with twelve words. Accepting both meant the new word 没事 was never produced until I asked for it by name (T48, T56), and asking by name hands over the answer and is the kind of instruction in brackets that "A line, not a description" forbids.
6. **"A new frame"** (rounds 2 and 3) in Lesson 2 part 1. With 我 要 水 茶 你 吗 不, every sentence is (不)要 + 水/茶. Of the 15 exercises, all 12 outside the review are that frame. I stopped round 2 at 4 and round 3 at 2, and it was still the same sentence all the way.
7. **好 "used on its own at least once".** Its only line is 好，再见！, and the only way to set it up was a moment where the teacher says 再见 and the learner "agrees" (T48), which is not what 好 answers.
8. **"A line is asked once at most in each kind" still leaves the same line twice close together.** 我不要茶，我要水 was a meaning exercise (T66) and a translation (T74) four exercises apart; the rule allows it and it read as a repeat.
9. **The setup card's promises do not match the first parts.** The card (copied from `setup.md`) says "três rodadas de tradução" and "sem áudio, você lê um texto no lugar". The first parts have meaning and reply exercises, two rounds, and no text to read under the title "Leitura 1". The pace legend says "palavras novas por dia" while the file says "per part", and part 1 brought 6 and part 3 brought 7 at a pace of "cerca de 5".

## 4. Repetition

Kinds: M = meaning, R = reply (learner produces it), cue = shown as the other speaker's line in a reply exercise, T = translation, S = a moment in the last step.

### HSK 1 · Lesson 1 · part 1

| Line | Times produced or asked | Where |
|---|---|---|
| 你好 | 3 | M, T, S |
| 再见 | 3 | M, T (inside 谢谢，再见), S |
| 谢谢 | 3 (+1 cue) | T (in exchange), T (谢谢，再见), S |
| 不客气 | 2 | R, T (in exchange) |
| 对不起 | 1 (+1 cue) | T (in exchange) |
| 没关系 | 4 | M, R, T (in exchange), S |

没关系 was asked in every kind, the meaning one right after a correction that had just explained it (T12). 对不起 was produced once.

### HSK 1 · Lesson 1 · part 2

| Line | Times | Where |
|---|---|---|
| 谢谢 / 对不起 / 不客气 | 1 each | review, all three M |
| 再见 | 1 | review, T |
| 您好 | 3 | M, T, S |
| 好，再见 | 3 | M, T, S |
| 没事 | 2 | R (learner gave 没关系), S (asked by name) |
| 谢谢您 | 1 | T, never shown before |
| 不客气 | 1 more | S (brought back after the review slip) |

The review was three "what does it mean?" in a row on words the learner had typed ten minutes before. The last step was the same four-moment drill as part 1 with the place changed.

### HSK 1 · Lesson 2 · part 1

| Line | Times | Where |
|---|---|---|
| 谢谢您 | 1 | review, M |
| 您好 | 1 (4th time in two parts) | review, T |
| 对不起 — 没事 | 1 | review, T (没事 by name) |
| 我要茶 | 4 | M, T (我要茶，谢谢), T in both round 3 prompts |
| 我不要水 | 2 | M, T (round 3) |
| 你要水吗 | 1 (+1 cue) | T (in exchange) |
| 您要茶吗 | cue only | R cue |
| 要，谢谢 | 1 | R |
| 不要，谢谢 | 3 | R, T (in exchange), S |
| 我不要茶，我要水 | 2 | M, T |
| 你不要茶吗 | 1 | T |
| 你要茶吗 (chunk as listed) | 2 | T (round 3), S |
| 我要水 (chunk as listed) | 1 | S only (你好，我要水) |
| 谢谢，再见 | 1 (also part 1) | S |

All 12 exercises outside the review are 要 with 水 or 茶.

## 5. Unnatural Mandarin

- **好，再见！** as the answer to someone saying 再见 (part 2, T48). 好 answers a proposal, not a goodbye. With these words there is no natural setting for 好 alone, and `first-parts.md` itself gives 好，再见！ as a model line.
- **我要水。** bare, as an order at a counter: blunt. A speaker says 我要一杯水 or 来杯水. Fixing it needs 一 and 杯, two support words for one chunk.
- **你要茶吗？ / 您要茶吗？** as an offer: understood, but an offer is usually 你喝茶吗？ or 要不要喝点茶？ (喝 comes in part 2).
- **要，谢谢。** as acceptance: correct, but 好的，谢谢 is what people say. **不要，谢谢。** as refusal: 不用，谢谢 is the polite one; 不要 can sound sharp. I corrected the student's 不，谢谢 to 不要，谢谢 (T66), teaching the less polite form as the natural one because 用 is not met.
- **你好！我要茶。你要茶吗？** (round 3): the third sentence repeats 茶; a speaker says 你呢？ or 你也要吗？ (呢 and 也 not met).
- **对不起，我不要水。我要茶，谢谢。** (round 3): for this small a thing 不好意思 is the natural opener; 对不起 is heavy.
- **你不要茶吗？**: natural only as surprise or insistence; the prompt had no context to carry that.
- **没事 and 没关系** shown as interchangeable: fine, but the note "没事 é a mais leve" was my addition; the skill gives no line for it.
- Portuguese side: "Olá, senhor!" for 您好 is not something a Brazilian says to mean a polite hello; "Não quero, obrigada." (T70) is stiffer than "Não, obrigada", and the natural Portuguese is exactly what produces 不，谢谢.

## 6. Time

Estimates for a real beginner typing Hanzi with an IME or pinyin with tone marks.

| Stage | Exercises per step | Total | Minutes |
|---|---|---|---|
| Setup (card, route, agreement) | none | 0 | 3–4 |
| Lesson 1 · part 1 | review 0 · round 1: 5 (3 meaning, 2 reply) · round 2: 4 · round 3: 0 · last step: 1 (4 lines) | 10 | 6–8 |
| Lesson 1 · part 2 | review 4 (3 meaning, 1 translation) · round 1: 3 (2 meaning, 1 reply) · round 2: 3 · round 3: 0 · last step: 1 (4 lines) | 11 | 6–8 |
| Lesson 2 · part 1 | review 3 (1 meaning, 2 translation) · round 1: 5 (3 meaning, 2 reply) · round 2: 4 · round 3: 2 · last step: 1 (4 lines) | 15 | 10–13 |

Whole session: 36 exercises, about 25–33 minutes. Of the 36, 12 were "what does it mean?" answered in Portuguese, 5 were replies, 16 translations, 3 last steps. The learner produced Mandarin in 24 of 36. Part 2 is the thinnest: three new words, and only 2 of its 11 exercises asked for a new word in Mandarin before the last step (您好 once, 好，再见 once; 没事 not at all, since 没关系 was accepted).

## 7. Reading load

Read by the tutor before the first lesson message (T6):

| File | Words | When |
|---|---|---|
| `SKILL.md` | 2,343 | at the start |
| `setup.md` | 1,561 | no `course.md` found |
| `lesson-format.md` | 1,177 | before the first lesson message |
| `first-parts.md` | 487 | the brief said the part is early |
| Total | about 5,570 | |

Plus script output: the overview (about 230 words), the first brief (about 90), and the `check_plan.py` usage (about 250), which I needed for the plan format. About 6,100 words in all. Of `setup.md`, about a third (the course screen) is not needed at a first start; of `SKILL.md`, the sections on the usual three rounds, older words and round names describe a lesson the learner will not see for several parts.

Not read by the tutor: `audio.md` (Audio is none), `levels.md`, `requests.md` (the learner only asked for the next part; the role-play was offered without it), `maps/`, `syllabus/` (single-word lookups of pinyin only, by grep), `LICENSE`, `fonts/`, the source of `course.py` and `check_plan.py`. `web/setup.js` (about 2,000 words) was read by the simulator only, for the button message.

Nothing new was read for parts 2 and 3.
