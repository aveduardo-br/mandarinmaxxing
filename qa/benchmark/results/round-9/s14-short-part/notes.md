# Notes · sim4 · hsk3 · scenario s14

Files in this folder: `transcript.md`, `notes.md`, `plan.txt` (the plan of the new chat, Lesson 18 part 2), `plan-part1.txt` (the plan of Lesson 18 part 1, copied before the second `course.py part` overwrote `plan.txt`), `course-0.md` (the older-format file as found, kept for the comparison), `course-1.md` (after `close`), `course-2.md` (after the tutor translated the labels the close asked for), `course-3.md` (after `pace 7`; identical to `course/course.md`).

All scripts were run with `python3 -I` and absolute paths. `S` = `/home/claude/review/sim4/hsk3/skill`, `O` = `/home/claude/review/sim4/hsk3`.

## Scripts run, with output

1. `course.py part O/course/course.md O/plan.txt` (file not changed by it)

```
NOTE: this file is in an older format. It is read as it is; the next `course.py close` writes it in the current one.
PART: HSK 3 · Lesson 18 · Perder o celular ou o cartão · part 1 of 2
NEW WORDS, in blocks that work together: 丢 卡 以为
REVIEW: one prompt per word of 3-17.2: 出院 健康 病人 脚 锻炼 坚持
  and the items to reinforce, once each: 一定, 打算
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (3-16.2): 起 or 刷
  7 back (3-14.4): 种 or 怎样
  14 back (3-12.1): 斤 or 羊
  30 back (3-06.3): 男人 or 一样
EARLY PART: no (739 words met before this part)
ROUNDS: three rounds of 3 prompts (up to 5 when the words have that many different contexts); every new word in at least three prompts
LAST STEP: with audio, the dictation, and the narration when the met words carry it (audio.md); without, one reading
AT THE CLOSE: run `course.py close <course.md>`, with --missed and --recovered for the items to reinforce
PLAN HEADER written to /home/claude/review/sim4/hsk3/plan.txt: add a SUPPORT or NAMES line above DONE if the part needs one, and the plan lines at the end.
```

2. `check_plan.py O/plan.txt`, first run (exit 1)

```
NOT MET (rewrite the sentence, or list the word as a support word):
  公园  in review: 我平时下了班就去公园锻炼。
  司机  in round3: 上个星期我把手机丢在出租车上了。我以为找不到了，可是第二天司机给我打了电话。
  银  in round3: 对不起，我把你的卡丢了。我以为放在包里了，可是找了半天也没找到。我明天一定去银行问一下。
  银  in round3: 别着急，这种卡丢了没关系。你先给银行打个电话，他们会给你换新的。
CHECK (advice only, the plan does not fail on these):
  会 (this level teaches another reading or sense of it later). In: 只要你坚持学习，你的中文就会越来越好。 (and 1 more lines)
```

3. `check_plan.py O/plan.txt`, second run after rewriting four lines (exit 0)

```
CHECK (advice only, the plan does not fail on these):
  会 (this level teaches another reading or sense of it later). In: 只要你坚持学习，你的中文就会越来越好。 (and 1 more lines)
OK: 25 lines, every character met, every new word in three round lines or more.
```

4. `check_plan.py O/plan.txt`, third run, on the plan as actually taught (four prompts reworked during the part to bring corrected items back; exit 0): same CHECK line for 会, `OK: 25 lines, every character met, every new word in three round lines or more.`

5. `student.py N "<expected>"` for N = 1 to 19: outputs are the STUDENT turns of the transcript, unchanged. (N = 11, 15, 16, 17 were run on the reworked answers. N = 20 was also run once, by mistake, for the first prompt of the new chat; its output, `não sei essa`, is not used: the scenario stops at the tutor's first message.)

6. `course.py close O/course/course.md --recovered "一定, 打算"`

```
CLOSED: 3-18.1 | 丢 卡 以为
NOTE: Labels had no word for: dictation, audio. They are in English now: translate them in the file.
NOTE: The file had no Rounds line. It is in English now: translate the three names in the file.
SAVED to /home/claude/review/sim4/hsk3/course/course.md: Next is `Lesson 18, part 2 of 2`. Put this file back where the course is kept.
```

7. Hand edit of `course.md` that the close asked for (the one edit SKILL.md allows): `dictation=Dictation, audio=Audio` → `dictation=Ditado, audio=Escuta`; `Rounds: Chunks, Full actions, Sequences` → `Rounds: Chunks, Ações completas, Sequências`.

8. `course.py check O/course/course.md` after 6 and again after 7: `OK: the course file is consistent.` both times.

9. `course.py pace O/course/course.md 7`

```
SAVED to /home/claude/review/sim4/hsk3/course/course.md: Next is `Lesson 18, part 2 of 3`. Put this file back where the course is kept.
PACE 7: 83 parts in the level now. A lesson already begun finishes at its old pace.
```

10. `course.py progress O/course/course.md`: `48/83`, `HSK 3: 48 of 83 parts done`, `NEXT: Lesson 18, part 2 of 3`.

11. New chat: `course.py part O/course/course.md O/plan.txt`

```
PART: HSK 3 · Lesson 18 · Perder o celular ou o cartão · part 2 of 3
NEW WORDS, in blocks that work together: 发现 关机 银行卡
REVIEW: one prompt per word of 3-18.1: 丢 卡 以为
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (3-17.1): 感冒 or 发烧
  7 back (3-15.1): 沙发 or 屋子
  14 back (3-12.2): 差 or 鸡
  30 back (3-07.1): 身高 or 米
EARLY PART: no (742 words met before this part)
ROUNDS: three rounds of 3 prompts (up to 5 when the words have that many different contexts); every new word in at least three prompts
LAST STEP: with audio, the dictation, and the narration when the met words carry it (audio.md); without, one reading
AT THE CLOSE: run `course.py close <course.md>`, with --missed and --recovered for the items to reinforce
PLAN HEADER written to /home/claude/review/sim4/hsk3/plan.txt: add a SUPPORT or NAMES line above DONE if the part needs one, and the plan lines at the end.
```

12. `check_plan.py O/plan.txt` (part 2 plan, first run, exit 0)

```
CHECK (advice only, the plan does not fail on these):
  还 (this level teaches another reading or sense of it later). In: 我弟弟上个月丢了手机，他到现在还很难过。
OK: 20 lines, every character met, every new word in three round lines or more.
```

13. `course.py check` on each copy

```
course-0.md  (exit 1)
CHECK (the writing commands fix most of these: `course.py migrate` rewrites the file as it should be):
  Older format: run `course.py migrate` on the file.
  Labels has no word for "dictation".
  Labels has no word for "audio".
  No Rounds line.
course-1.md  OK: the course file is consistent.
course-2.md  OK: the course file is consistent.
course-3.md  OK: the course file is consistent.
```

Also run as reviewer, not as tutor: `course.py overview 3 5` and `overview 3 7` (Lesson 18 is 2 parts at pace 5, 1 part at pace 7), and a reading of `course.py` and `maps/hsk-3.md` to find the cause of the pace problem below.

## The older-format file: before and after the first write

`diff course-0.md course-1.md`:

- Added `- Format: 2`.
- Labels went from positional to named. Seven of the nine words were kept (Aula, parte, Revisão, Bateria, Leitura, Frases úteis, Largada). **Two were dropped without a word: `Exercício` and `Escuta`** (positions 5 and 6, which the script's `OLD_9` table maps to nothing). In their place the file got `dictation=Dictation, audio=Audio`, **in English**.
- Added `- Rounds: Chunks, Full actions, Sequences`, **in English**.
- `To reinforce: 一定 打算` → `none` (both recovered in the review; correct).
- `Next: Lesson 18, part 1 of 2` → `part 2 of 2`; Done got `3-18.1 | 丢 卡 以为`.
- Every lesson name lost its ` (3 partes)` suffix. The names themselves are intact and in Portuguese. The part counts are derivable (`overview`), so nothing the script needs was lost, but it is a visible change the close does not mention.
- Route, Pace, Language, Audio (`ElevenLabs, voice Sarah`) and the 47 old Done lines are unchanged.

The close did say what was left in English (two NOTE lines), and the tutor translated them by hand. Nothing else was lost.

## Where the skill's text or scripts failed or were unclear

1. **`pace` re-splits the lesson already begun, against its own message and `requests.md`.** `requests.md`, "Change the pace": "It takes effect at the next lesson: a lesson already begun finishes at the old pace." The command printed the same promise and, on the line above it, `Next is Lesson 18, part 2 of 3`. Before the command the file said `part 2 of 2`. At the old pace (5) the rest of Lesson 18 is one part of five words (发现 关机 银行卡 开机 信用卡); after asking for the intense pace the learner gets two parts of 3 and 2 words: the split of pace 3. Cause, `course.py` `lesson_state`: it tries the current pace's split, then the others in the order 3, 5, 7, and keeps the first whose first parts match Done. The first part of Lesson 18 is the same block (丢 卡 以为) at pace 3 and pace 5 (`Split: 1-1-1 / 1-2 / 3`), so pace 3 wins. Any lesson whose first part is the same at two paces will do this. The tutor in T44 told the learner what the file says (3 parts), not what `requests.md` says.

2. **An older positional Labels line during the part: SKILL.md is silent.** `part` says "It is read as it is; the next `course.py close` writes it in the current one", and prints nothing about labels. SKILL.md says "Use exactly these in every chat, never a synonym" and describes only the named form. With `Labels: Aula, parte, Revisão, Bateria, Exercício, Escuta, Leitura, Frases úteis, Largada` the tutor has to guess which is which, and has no Rounds line at all, until the close (the last step) reports it. Decision: read the nine words by position against SKILL.md's nine labels, which gives dictation=Exercício and audio=Escuta; `Exercício 1` is no title for a dictation, so the tutor wrote **Ditado 1** and **Escuta 1 · No shopping**, and took the round names from SKILL.md's own Portuguese example (Chunks, Ações completas, Sequências). The script reads the same line differently (positions 5 and 6 are older labels it discards), so the tutor's reading and the script's disagree and nothing tells the tutor. The brief should print the labels and round names it resolved, or say at the start that dictation, audio and Rounds are missing.

3. **`check` says OK on a file with English labels in a Portuguese course.** After the close, `course-1.md` has `dictation=Dictation, audio=Audio` and `Rounds: Chunks, Full actions, Sequences` under `Language: Português`, and `course.py check` prints `OK: the course file is consistent.` The two NOTE lines of the close are the only signal; a tutor that misses them, or a later chat, will never be told.

4. **`migrate` is not in SKILL.md.** SKILL.md says to run `check` only "when a command stops with a message about the file". `part` did not stop, so the tutor never learns that `course.py migrate` exists (it is named only in `check`'s output and the script's docstring). Had the skill said to run `migrate` when `part` prints the older-format NOTE, the labels would have been settled before the lesson, not after it.

5. **`part` overwrites `plan.txt`.** SKILL.md fixes the name `plan.txt`; the second `part` (new chat) replaced part 1's plan. Harmless for the learner, but the previous plan is gone unless copied (here: `plan-part1.txt`).

6. **"Intenso" is not mapped in `requests.md`.** "Change the pace" says "(3, 5 or 7)". The names light, recommended and intense are only in `setup.md`, which SKILL.md says to read only when there is no course or the learner writes "setup". The tutor took intenso = 7 (confirmed afterwards in `setup.md` line 62, as reviewer).

7. **"I don't know" has no instruction.** `lesson-format.md`, "Feedback on a translation", covers correct, unnatural and incorrect. For `não sei essa` (T13, T27) the tutor decided: no "You wrote" blockquote, name the missing word or pattern in one line, give the sentence on three lines, treat it as a correction (bring the item back once), and go on.

8. **Is "right meaning, unnatural phrasing" a miss?** SKILL.md, `--missed`: "what the learner got wrong in this part". At T5 the learner wrote 为身体健康 for 为了身体健康: understandable, bookish. The tutor used the "unnatural phrasing" format, found no later prompt where 为了 fits naturally, and did not put it in `--missed`. The skill doesn't say which way this goes.

9. **Counter for the narration questions.** `audio.md` gives titles for the clips but no counter, and SKILL.md's "Fix the total in the first counter" covers the review only. Not a problem, but the dictation and the narration are the only exercises with no "n of m".

10. **The old labels `Exercício` and `Escuta` and the suffix `(3 partes)` vanish silently** (see the comparison above). The close reports what it added in English, not what it removed.

## Rules that could not be satisfied, with the case

- **Older words, line "30 back (3-06.3): 男人 or 一样".** Neither went into the review or the rounds without bending a sentence; 一样 was used in the dictation (这种卡我也有，跟你的一样), which the rule doesn't count. Lines 3, 7 and 14 back were used (刷牙 in review 7, 这种卡 in round 2, 羊肉 in review 8).
- **Dictation "No sentence repeats a chunk or a prompt of the part".** Kept, but with three new words and two of them tied to one scene, the dictation lines are close relatives of the round lines (丢 + 卡 again).
- **"After a correction, bring the item back once"**: done for 坚持 (T22), 下了班就 (T30), 以为……其实…… (T32), 这种卡 and 把卡丢了 (T34). Not done for 为了 (no natural place; see 8 above). Four of the nine round prompts were reworked for this, so the rounds drifted from the plan `check_plan.py` first approved; the plan as taught was checked again (run 4).

## Mandarin a mainland speaker would not say, and what caused it

- **银行 is not met.** The lesson is "Perder o celular ou o cartão", and part 2 teaches 银行卡, but 银行 itself is an HSK 3 word of a later lesson. `check_plan.py` rejected 去银行问一下 and 给银行打个电话, the two most natural follow-ups to losing a card. They became 再去商场问一下 and 学校给我换了新的: natural sentences, but the scene had to turn into a shop and a school card. In part 2 the learner will say 银行卡 without being able to say 银行.
- **No measure word for a card.** 张 is HSK 3 and not yet met, so 一张卡, 这张卡, 办一张新的 are out. The tutor did not use the SUPPORT allowance, because a support word may be "used only in that chunk's prompts" and the three chunks were needed for the three new words. Result: 我的卡, 这种卡, 换了新的 (where 换了一张新的 is what one would say). 办 (办卡, 补办) is also unmet, so "getting a new card" is always 换.
- **司机** is unmet: 第二天司机给我打了电话 became 第二天有人给我打了电话 (fine, less specific).
- **为了身体健康，你应该少喝啤酒** (review 2) is correct but stiff: a speaker would more likely say 为了健康. 身体健康 as a set phrase is said, so it stays within natural.
- 丢在车上 (round 3) uses 丢 as "leave behind", a normal extension of the table's "lose"; the prompt says "deixei o celular no carro".

## How the tutor handled each kind of student reply

- **Grammar question (N = 3, T7):** confirmed the answer, answered in four sentences (topic first, 需要 before the verbs, actions in the order they happen), went on. No instruction in the skill for questions; handled as part of the feedback.
- **Natural alternative (N = 9, T19):** did not come up. The expected answer, 我的包丢了。, holds none of the student's five pairs, so the student answered as expected. The handling of synonyms was not exercised in this session.
- **Missing word (N = 2, T5; N = 16, T33):** T5 dropped 了 from 为了 → "right meaning, unnatural phrasing", three-line corrected sentence, not counted as missed. T33 dropped 了 after 把…丢 → "Incorrect" format (blockquote, one fix line, full sentence), brought back in the next prompt (我去年也把卡丢了), answered right.
- **Pinyin (N = 4, 11, 18):** accepted, Hanzi shown on one line, keyboard reminder once (T10). In the dictation the student's raw `bù yòng`, `yī yàng`, `nǎ ér` (no tone sandhi, 儿 apart) were accepted as right: the skill leaves tones to the learner.
- **Wrong order (N = 5, T11; N = 12, T25):** "Incorrect" format with the stretch in the right order; both items came back in round 3 and were answered right. T25's swapped clauses (其实…，我以为…) are a believable error and got a real explanation; T11's scramble (就在小区里锻炼我平时下了班) is not something a learner writes, and the fix line could only say "subject and time first".
- **"I don't know" (N = 6, T13; N = 13, T27):** see point 7 above. Both items came back later and were answered right, so nothing went into `--missed`.

Close: `--recovered "一定, 打算"` (both right unaided in the review), no `--missed`. **To reinforce** is now `none`, although the learner failed 5 of 19 exercises at first try: every item was "got right later in the part", in a prompt reworked to contain it, right after seeing the answer. The rule as written makes it easy to end a weak session with an empty list.

## Exercises per step and estimated minutes

Part 1 (Lesson 18, part 1), as taught:

| Step | Exercises | Minutes (est.) |
|---|---|---|
| Review | 8 (six words of 3-17.2 + 一定, 打算) | 9 |
| Vocabulary (table, one usage note, 3 chunks) | 0 | 2 |
| Bateria 1 · Chunks | 3 | 3 |
| Bateria 2 · Ações completas | 3 | 4 |
| Bateria 3 · Sequências | 3 | 7 |
| Extra round | declined | 0 |
| Ditado 1 (4 sentences) | 1 | 4 |
| Escuta 1 · No shopping (7 sentences, 5 questions) | 1 | 4 |
| Close | 0 | 1 |
| **Total** | **19** | **about 34** |

For three new words the review (8 prompts) is almost as long as the three rounds (9 prompts).

New chat (Lesson 18, part 2 of 3), planned and checked, only the first message written: review 3, rounds 3 + 3 + 3, dictation of 4 sentences, one narration; about 25 minutes.
