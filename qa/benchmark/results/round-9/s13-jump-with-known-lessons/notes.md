# Notes · scenario s13 · sim4/known

Files here: `transcript.md`, `notes.md`, `course-0.md` (the file as found) to `course-5.md`, `plan.txt` = `plan-1-final.txt` (part taught, with the three lines reworked during the part), `plan-1-as-planned.txt` (before teaching), `plan-header.txt`, `plan-2.txt` (next part, final), `plan-2-first-try.txt` (the version check_plan failed).

## Scripts run, with output (all with `python3 -I` and absolute paths)

1. `course.py check course.md` (file as found) → `CHECK … Older format: run course.py migrate on the file.` exit 1. Not required by the skill at this point; run to know the starting state. The tutor did not run `migrate`: the next writing command did it.
2. `course.py jump course.md 12` → `SAVED … Next is Lesson 12, part 1 of 2` / `ROUTE: 12, 01–11, 13–19` / `JUMP-START LESSONS NOT STUDIED: 01 02 03 04. Ask which of them the learner already knows (requests.md), then run course.py known for those.` → course-1.md. The file came out in Format 2.
3. `course.py overview 2 5` → the four jump-start lessons with words; `TOTAL: 19 lessons, 38 parts at pace 5: about 5 weeks at one part a day`.
4. `course.py known course.md 01 02 04` → `SAVED … Next is Lesson 12, part 1 of 2` / `KNOWN: 01 02 04` → course-2.md.
5. `course.py jump course.md 03` → `SAVED … Next is Lesson 03, part 1 of 2` / `ROUTE: 03, 12, 05–11, 13–19` → course-3.md.
6. `course.py part course.md plan.txt` → `PART: HSK 2 · Lesson 3 · … · part 1 of 2`; `NEW WORDS: 过 次 已经 | 开始 完 时`; `REVIEW: one prompt per word of 1-22.1: 病 看病 医生 生病 觉得 医院 and the items to reinforce, once each: 有点儿, 一点儿`; older words 工作/公司, 对/再, 大家/听, 鸡蛋/早饭; `KNOWN LESSONS … 01 02 04` with their 29 words; `EARLY PART: no (329 words met before this part)`; `ROUNDS: three rounds of 5 prompts`; `LAST STEP: … without, one reading`.
7. `check_plan.py plan.txt` → advice on 点 only; `OK: 29 lines, every character met, every new word in three round lines or more.` Run again after the three reworked lines: same result.
8. `student.py N "<expected>"` for N = 1…24 (replies are in the transcript, unchanged). N = 4, 22 and 23 were run on the reworked answers.
9. `course.py close course.md --missed "去医院了, 明天再来" --recovered "有点儿, 一点儿"` → `CLOSED: 2-03.1 | 过 次 已经 开始 完 时` / `SAVED … Next is Lesson 03, part 2 of 2` → course-4.md. To reinforce became `去医院了, 明天再来`.
10. Chat 2: `course.py progress course.md` → `1/33` / `HSK 2: 1 of 33 parts done (3 lesson(s) marked known are left out)` / `NEXT: Lesson 03, part 2 of 2`.
11. `course.py pace course.md 3` → `SAVED …` / `PACE 3: 54 parts in the level now. A lesson already begun finishes at its old pace.` → course-5.md (only the Pace line changed).
12. Chat 3: `course.py part course.md plan-2.txt` → `PART: HSK 2 · Lesson 3 · … · part 2 of 2`; `NEW WORDS: 每 周 有时 | 经常 得 | 比 最`; review of 2-03.1 plus `去医院了, 明天再来`; `ROUNDS: three rounds of 5 prompts`.
13. `check_plan.py plan-2.txt` → first run exit 1: `NOT MET … 打 in round1: 我每周给妈妈打两次电话。`; line rewritten (我每周看两次电影。); second run OK with advice on 点, 歌唱, 最好.
14. `course.py check` on every copy: course-0 → `Older format: run course.py migrate on the file.` (exit 1); course-1 to course-5 → `OK: the course file is consistent.`

## Course screen arithmetic (step 3)

- Done in this level: Done lines starting with `2-`: one (`2-03.1`). → 1.
- Total: the course file no longer says how many parts a lesson has (the old file had "(2 partes)" on each line; the migration removed it), so the total can't be checked from course.md alone. From `overview 2 5`: 01:2 02:2 03:2 04:1 05:2 06:2 07:2 08:3 09:3 10:2 11:2 12:2 13:2 14:2 15:2 16:2 17:2 18:2 19:1 = 38. Known lessons out: 2 + 2 + 1 = 5. 38 − 5 = 33. Same by adding the 16 lessons on the route. → `1/33` is right.
- Percentage written by setup.js: `Math.round(100 × 1 / 33)` = round(3.03) = 3%.
- Next line: `Next: Lesson 03, part 2 of 2` + Lessons `03 Dizer o que você já fez e como se saiu` → "Aula 3 · … · parte 2 de 2". Right.
- After the pace change: `overview 2 3` total 66; known out 4 + 4 + 2 = 10 → 56; Lesson 03 keeps its 2 parts and not 4 → 54. `1/54` → round(1.85) = 2%. The script's 54 is right.

## Message of the card's button (step 4)

setup.js: a click on a fieldset button sets the group's index; a click on `[data-start]` in a `data-home` card keeps only the lines that differ from the initial ones and sends `data-lead + ' ' + lines.join('. ') + '.'`. The line is the legend's first text node + `: ` + the button's text + ` (` + its `<small>` + `)`. With the translated card: `Mudar meu curso. Ritmo: Leve (cerca de 3).`

## Where the skill's text was unclear, silent or contradictory

1. **Older file, silent migration.** SKILL.md has no word on an older-format file; `course.py --help` says "A file from an older version is read as it is and written in the current format", and `check` says to run `migrate`. `jump` migrated without saying so. In the migration the labels `Exercício` and `Escuta` (two of the old eleven) were dropped and each lesson line lost "(2 partes)". Nothing was printed about either. The result is consistent, but the tutor never learns the file changed format.
2. **requests.md, "Going to another lesson": "Say in one line what comes after it, without waiting for an answer."** against "Skip lessons the learner already knows": "ask once which of them the learner already knows". When the jump leaves jump-start lessons unstudied both apply; I asked the question and gave the order only after the answer. After the answer the text does not say whether to wait for the learner to agree to "Lesson 3 first" (a change to what they asked for) before teaching. Decided: state the order in one line and start the part in the same message.
3. **Two jumps.** The learner's request needed `jump 12`, then `known 01 02 04`, then `jump 03`. The text says so, in two different paragraphs. After `known` the output says `Next is Lesson 12` with no reminder that Lesson 03 is still an unstudied jump-start lesson; a tutor who stops there teaches Lesson 12 without 过, 已经, 得, 比.
4. **Words of (known) lessons in the review.** SKILL.md: the reminder line for those words goes in the vocabulary step; the review comes before it, and both SKILL.md and check_plan count those words as met in the review. A review sentence with 但是 or 一起 would show a word "the course never showed" before its reminder. Decided: no known-lesson word in the review.
5. **"I don't know".** lesson-format.md describes correct, unnatural and incorrect answers; nothing for a learner who gives no answer. Decided: the sentence on three lines, one line pointing at its key pieces, and the item brought back later.
6. **A learner's question.** "Keep messages on the exercise" is the only nearby rule; nothing says how to answer a grammar question. Decided: two sentences, then the next prompt.
7. **`--missed` after "I don't know" to a three-sentence prompt.** "what the learner got wrong … give the short chunk as it should be said": with no attempt there is no slip to name. Decided: the pieces that came out right later (开始, 已经…了) are out; the one never tried again (明天再来) goes in.
8. **Plan labels.** SKILL.md step 1 lists `review:`, `round1:`, `round2:`, `round3:`, `chunk:` or `listening:` and says the reading goes under them; check_plan also accepts `reading:`. I used `reading:`, with the expected rewrite as a second `reading:` line (nothing says where the rewrite's answer goes).
9. **Pace changed inside a lesson.** requests.md: "It takes effect at the next lesson: a lesson already begun finishes at the old pace." The learner who has just asked for about 3 words gets, as their very next part, the largest part of the lesson: 7 words (每 周 有时 经常 得 比 最), three of them new structures (得, 比, 最). The brief of that part says nothing about the pace in the file being 3, and "no remarks on how the lesson is divided" keeps the tutor from saying it in the lesson. I said it in the answer to the pace change.
10. **Course screen.** `progress` prints "(3 lesson(s) marked known are left out)", and the card has no place for it: the learner sees "1 de 33" with no hint why a level of 38 parts shows 33.
11. **Prompt for 过 in Portuguese.** "Same content … nothing in it that the answer leaves out ('already')": Portuguese says 过 with "já", the same word as 已经. Decided: keep "já" (the natural prompt) and add the usage note for two words that translate the same way.

## Rules I could not satisfy, or scripts that got it wrong

- **check_plan false failure:** `NOT MET 打 in round1: 我每周给妈妈打两次电话。` 打电话 is a met word (1-08.1) said apart; the script's rule for separated words only handles two-character words (`len(word) != 2`), so 打两次电话, 打了电话, 打个电话 all fail. In a part that teaches 次, 打两次电话 is one of the most natural sentences there is. I rewrote the line as the skill says; a tutor could also let it stand ("what still stands after that is your call").
- **"Every chunk listed is practised in round 1" + "two to four chunks"** with six new words: 时 has no chunk and appears only in rounds 2 and 3 and the reading (three round lines, as required).
- **Older words:** used 公司 and 工作, 再, 大家 and 听, 早饭: all four lines covered.
- **Natural alternative (N = 9):** the answer expected at N = 9 (你去过我们学校吗？) holds none of the student's pairs, so that kind of reply did not occur in this run.

## Mandarin a mainland speaker would not say, and the cause

- 这个歌 / 这个饭店: 这首歌 and 这家饭店 are what people say; 首 and 家 as measure words are not met. 这个 is common in speech, so I kept it rather than add support words.
- …时 (吃饭时, 开车时我也听): correct but bookish; in speech it is 的时候. The cause is the word list itself (时 is the new word).
- 我去过中国两次 / 去过两次中国: both said.
- 你什么时候开始上班？ (plan-2): fine.

## How the tutor handled each kind of reply

- **Grammar question (N = 3):** confirmed the answer, answered in two sentences (time before the verb, 也 before the verb), next prompt.
- **Natural alternative (N = 9):** did not occur (see above).
- **Missing word (N = 2, 16, 23):** N = 2 我要去看 for 看病: corrected, and 看病 brought back in Review 4 (reworked), where it came out right. N = 16 and 23, a missing 了: corrected with one line each; 已经…了 came back right at N = 23; 就去医院了 had no prompt left, so it went to `--missed`.
- **Pinyin (N = 4, 11, 18):** accepted, Hanzi shown, keyboard reminder once at the first.
- **Wrong order (N = 5, 12, 19):** N = 5 and 12 corrected with the stretch in the right order, both brought back (你觉得呢 in Round 3 · 4, reworked; 做完饭 already in two later prompts) and right the second time. N = 19 swapped whole sentences: each was right Mandarin, so the tutor said so and corrected only the sequence.
- **"I don't know" (N = 6, 13, 20):** answer on three lines with one pointer; 医院 brought back at N = 23 (reworked), 没…过 at N = 19, 开始/已经 at N = 23; 明天再来 went to `--missed`.

## Exercises and minutes

Part taught (HSK 2, Lesson 3, part 1): review 8, round 1 5, round 2 5, round 3 5, reading 1 = 24 exercises. About 40 minutes (review 8, table and chunks 4, rounds 22, reading 6). Step 1 itself: no exercises. Step 5: one message.
