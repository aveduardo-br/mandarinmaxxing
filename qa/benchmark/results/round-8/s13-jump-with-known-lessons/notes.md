# Notes · sim3/known

Scenario: learner finished HSK 1 at pace 5, has just moved to HSK 2 (Next: Lesson 01, part 1 of 2). Chat 1: jumps to Lesson 12, says all four jump-start lessons are known, studies Lesson 12 part 1. Chat 2: `setup`, then un-skips Lesson 3. Chat 3: `próxima aula`, first message only. 62 turns (chat 1: T1–T56, chat 2: T57–T60, chat 3: T61–T62). Audio none; inline HTML available.

All commands were run from `/home/claude/review/sim3/known` (or its `course/`), never from inside the skill folder, with `python3 -I` and absolute paths. `S` below stands for `/home/claude/review/sim3/known/skill`, `C` for `/home/claude/review/sim3/known/course`.

## 1. Scripts

### Chat 1, before T2: finding the jump-start lessons

`python3 -I S/course.py` (no arguments, to see the usage) → exit 1, prints the docstring (usage of `overview` and `part`).

`python3 -I S/course.py overview 2 5` → exit 0

```
JUMP START
  01 Ask for help and say why (2 parts): 不好意思 帮 事情 为什么 因为 所以 帮忙 让 记得 别1 忘 告诉
  02 Make plans together (2 parts): 跟 一起 啊 还是 可能 就 但是 准备 等1 虽然 但
  03 Say what you've done and how well (2 parts): 过 次 已经 开始 完 时 每 周 有时 经常 得 比 最
  04 Say what's happening (1 part): 正 着 从 快 慢 地
SITUATIONS
  05 Introducing people (2 parts)
  06 Describing someone (2 parts)
  07 At the café and the restaurant (2 parts)
  08 Shopping for clothes (3 parts)
  09 Asking the way (3 parts)
  10 Getting around town (2 parts)
  11 Taking a trip (2 parts)
  12 Having someone over (2 parts)
  13 Looking for your things (2 parts)
  14 Going out and coming back (2 parts)
  15 Classes and exams (2 parts)
  16 Playing sports (2 parts)
  17 Hobbies and weekends (2 parts)
  18 Looking after your health (2 parts)
  19 Birthdays and holidays (1 part)
TOTAL: 19 lessons, 38 parts at pace 5: about 5 weeks at one part a day
```

Checked against `maps/hsk-2.md`: words and part counts match. This output is what made T2 possible, but `requests.md` → "Skip lessons the learner already knows" never names the command (see section 2, item 1).

### Chat 1, after T3: save of the jump (course-1-after-jump.md), then the brief

Saved by hand: lessons 01–04 → `(known)`, `Route: 12, 05–11, 13–19`, `Next: Lesson 12, part 1 of 2`. No script does this.

`python3 -I S/course.py part C/course.md C/plan.txt` → exit 0

```
PART: HSK 2 · Lesson 12 · Receber alguém em casa · part 1 of 2
NEW WORDS, in blocks that work together: 门 打开 进 | 门口 进来 过来
REVIEW: one prompt per word of 1-22.1: 病 看病 医生 生病 觉得 医院
  and one for each item to reinforce: 有点儿 一点儿
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (1-21.1): 工作 or 公司
  7 back (1-19.3): 对 or 再
  14 back (1-17.1): 大家 or 听
  30 back (1-12.1): 鸡蛋 or 早饭
KNOWN LESSONS (never shown by the course): 01 02 03 04
  their words: 不好意思 帮 事情 为什么 因为 所以 帮忙 让 记得 别1 忘 告诉 跟 一起 啊 还是 可能 就 但是 准备 等1 虽然 但 过 次 已经 开始 完 时 每 周 有时 经常 得 比 最 正 着 从 快 慢 地
  use four of them at most in this part, and list the ones used under the table with pinyin and meaning
EARLY PART: no (642 words met before this part)
ROUNDS: three rounds of 5 prompts; every new word in at least three of them
LISTENING: dictation and narration with audio; one reading without
AT THE CLOSE: add `2-12.1 | 门 打开 进 门口 进来 过来` to Done; Next becomes Lesson 12, part 2 of 2
PLAN HEADER written to /home/claude/review/sim3/known/course/plan.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```

Hand check against course-1-after-jump.md and the map:

- PART / NEW WORDS: Lesson 12, pace 5 split `2-2`, first two blocks = 门 打开 进 | 门口 进来 过来. Correct.
- REVIEW: last Done line is 1-22.1 (6 words) + To reinforce (2 items) = 8 prompts. Correct.
- OLDER WORDS: Done has 58 lines. 3 back = 1-21.1, 7 back = 1-19.3, 14 back = 1-17.1, 30 back = 1-12.1, no 60 back. Words picked as the code rotates them. Correct.
- KNOWN LESSONS: 12 + 11 + 13 + 6 = 42 words. Correct.
- **Wrong: "642 words met before this part".** The true number is 342: 300 (HSK 1) + 42 (known lessons). `course.py` line 174 adds `level_size(1)` = 300 for the level below **and** the 300 unique words of the Done log, which in this file *are* HSK 1. Any learner who studied a lower level with the skill is counted twice. Harmless for the EARLY test here (threshold 20), but the printed number is false.
- The brief never mentions the Route, and `course.py` never reads the `Route` line at all. That is invisible here and bites after the un-skip (below).
- The plan header: `LEVEL 2 / KNOWN 01 02 03 04 / NEW … / DONE … / PLAN`. Correct.

### Chat 1: check_plan.py

Run 1: `python3 -I S/check_plan.py C/plan.txt` → exit 1

```
NOT MET (rewrite the sentence, or list the word as a support word):
  打  in listening: 今天是星期天，我的朋友小王过来玩。下午三点，他到了我家门口，给我打了电话。我打开门，请他进来。他进了我的房间，我们喝茶、看电影。晚上我妈妈做了饺子，非常好吃。
```

A false alarm: 打电话 is an HSK 1 word (1-08.1), and 打了电话 is the same word with 了 inside it. The checker has no notion of a separable verb, and 打 alone is 打1 of HSK 2 Lesson 16. I rewrote to 给我打电话 (no 了), which is fine in a narration, but the tool pushed me off a normal sentence. The same will happen with 睡了觉, 上了课, 下了班, 见了面, 起了床.

Run 2 (after the rewrite) → exit 0

```
OK: 28 lines, every character met, every new word in three round lines or more.
```

What the checker got wrong or could not see in this plan:

- It let through `我来开门` (来 + verb, "let me"), a pattern the learner has not met. I caught it by eye before teaching and changed it to `我去开门`. Expected: it checks vocabulary only.
- It counts 门 inside 门口 and 进 inside 进来 ("alone or inside a longer word"). So the "three round lines" for 门 and 进 would pass with zero standalone uses, while `SKILL.md` asks "A word that is natural on its own is used on its own at least once". In my plan both are alone three times, but nothing would have told me otherwise.
- It does not know the brief's "use four of them at most": with `KNOWN 01 02 03 04` all 42 words are simply met, in review lines too. The brief and the checker disagree on what a known lesson allows (section 2, item 4).
- Three prompts were reworked during the part (after corrections). The skill does not ask for a second check; I ran one anyway on a copy (`/tmp/plan-reworked.txt`) → exit 0, same OK line.

### Chat 1, close: save of the part (course-2-after-part.md)

By hand, as the brief's AT THE CLOSE line says: Done + `2-12.1 | 门 打开 进 门口 进来 过来`, `Next: Lesson 12, part 2 of 2`, `To reinforce: 在门口说话 我家门口`.

Reviewer's extra run (no chat needed it): `python3 -I S/course.py part C/course.md` → exit 0

```
PART: HSK 2 · Lesson 12 · Receber alguém em casa · part 2 of 2
NEW WORDS, in blocks that work together: 楼 上来 下来 | 进去 上去 下去
REVIEW: one prompt per word of 2-12.1: 门 打开 进 门口 进来 过来
  and one for each item to reinforce: 在门口说话 我家门口
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (1-21.2): 上班 or 事
  7 back (1-20.1): 老师 or 学生
  14 back (1-17.2): 见 or 正在
  30 back (1-12.2): 好吃 or 晚饭
KNOWN LESSONS (never shown by the course): 01 02 03 04
  their words: (the same 42)
  use four of them at most in this part, and list the ones used under the table with pinyin and meaning
EARLY PART: no (648 words met before this part)
ROUNDS: three rounds of 5 prompts; every new word in at least three of them
LISTENING: dictation and narration with audio; one reading without
AT THE CLOSE: add `2-12.2 | 楼 上来 下来 进去 上去 下去` to Done; Next becomes the first part of the next lesson on the route (or `level complete`)
```

Hand check: all correct except the count (648; true 348 = 300 + 6 + 42). "one for each item to reinforce: 在门口说话 我家门口" prints the raw line: nothing tells the next chat whether that is two items or more (section 2, item 8).

### Chat 2: course screen (T58), arithmetic by hand from course-2-after-part.md

No script computes these; `setup.md` has the tutor count.

- Parts done = Done lines of the current level (level 2): only `2-12.1` → **1**.
- Parts in the level = sum of the Lessons list, known lessons excluded: 05:2 + 06:2 + 07:2 + 08:3 + 09:3 + 10:2 + 11:2 + 12:2 + 13:2 + 14:2 + 15:2 + 16:2 + 17:2 + 18:2 + 19:1 = **31**. Cross-check: the overview's 38 minus the known lessons' 2 + 2 + 2 + 1 = 7 → 31.
- `data-progress="1/31"`; the script writes round(100 × 1 / 31) = round(3.23) = **3%**.
- Next lesson line: `Next: Lesson 12, part 2 of 2` + Lessons list → "Aula 12 · Receber alguém em casa · parte 2 de 2".
- `data-on`: level 2, pace Recomendado (5), audio Desligado (`Audio: none`).
- Buttons (from `web/setup.js` lines 260–275): each `nav` button sends its `data-send` text; "Salvar alterações" is hidden until a setting changes and then sends `Alterar meu curso. <Group>: <value>.` for the changed groups only. No button was clicked in this scenario.

One number the screen will show oddly later: after the un-skip the total becomes 33 (31 + 2), so a learner who saw "1 de 31" will see "1 de 33" next time. Correct by the rule, just not explained anywhere.

### Chat 2, T59: un-skip of Lesson 3 (course-3-after-unskip.md)

`python3 -I S/course.py overview 2 5` → exit 0 (same output as above; line used: `03 Say what you've done and how well (2 parts)`).

Saved by hand: `03 … (known)` → `03 Dizer o que você já fez e como se saiu (2 partes)`; `Route: 03, 12, 05–11, 13–19`; `Next: Lesson 03, part 1 of 2` (my decision, see section 2, item 2). Done and To reinforce untouched.

### Chat 3: `próxima aula`

`python3 -I S/course.py part C/course.md C/plan.txt` → exit 0

```
PART: HSK 2 · Lesson 3 · Dizer o que você já fez e como se saiu · part 1 of 2
NEW WORDS, in blocks that work together: 过 次 已经 | 开始 完 时
REVIEW: one prompt per word of 2-12.1: 门 打开 进 门口 进来 过来
  and one for each item to reinforce: 在门口说话 我家门口
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (1-21.2): 上班 or 事
  7 back (1-20.1): 老师 or 学生
  14 back (1-17.2): 见 or 正在
  30 back (1-12.2): 好吃 or 晚饭
KNOWN LESSONS (never shown by the course): 01 02 04
  their words: 不好意思 帮 事情 为什么 因为 所以 帮忙 让 记得 别1 忘 告诉 跟 一起 啊 还是 可能 就 但是 准备 等1 虽然 但 正 着 从 快 慢 地
  use four of them at most in this part, and list the ones used under the table with pinyin and meaning
EARLY PART: no (635 words met before this part)
ROUNDS: three rounds of 5 prompts; every new word in at least three of them
LISTENING: dictation and narration with audio; one reading without
AT THE CLOSE: add `2-03.1 | 过 次 已经 开始 完 时` to Done; Next becomes Lesson 03, part 2 of 2
PLAN HEADER written to /home/claude/review/sim3/known/course/plan.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```

**Which lesson and part came out, and why:** HSK 2, Lesson 3, part 1 of 2 (过 次 已经 | 开始 完 时), because the tutor in chat 2 wrote `Next: Lesson 03, part 1 of 2`. `course.py` reads only `Next`; the Route line plays no part. Had chat 2 followed `requests.md` to the letter and left `Next` alone, this chat would have taught Lesson 12 part 2. Verified on a copy of the file with `Next: Lesson 12, part 2 of 2` and the new route: the brief opens `PART: HSK 2 · Lesson 12 · Receber alguém em casa · part 2 of 2`.

Hand check against course-3-after-unskip.md:

- Lesson 03, pace 5 split `2-3`: part 1 = 过 次 已经 | 开始 完 时. Correct.
- REVIEW: 2-12.1 (6) + 2 items = 8. Correct.
- OLDER WORDS: Done has 59 lines; 3 back = 1-21.2, 7 back = 1-20.1, 14 back = 1-17.2, 30 back = 1-12.2. Correct.
- KNOWN: 01 02 04 only, 12 + 11 + 6 = 29 words; Lesson 3's words are gone from the list. Correct.
- Count: 635 printed; true 335 (300 + 6 + 29). Wrong, same double count.

`python3 -I S/check_plan.py C/plan.txt` (the whole part planned before the first message) → exit 0

```
OK: 28 lines, every character met, every new word in three round lines or more.
```

Probe (reviewer, `/tmp/probe.txt`: same header, three lines using Lesson 3 words) → exit 1: `已经` NOT MET in a review line, `每` and `经常` NOT MET in round lines. So after the un-skip the checker treats Lesson 3 as unmet, part 2's words included. Correct.

What goes wrong after the un-skip, seen from the scripts:

- **The close of Lesson 3 will point at the wrong part.** Preview with `Next: Lesson 03, part 2 of 2`: `AT THE CLOSE: add 2-03.2 | 每 周 有时 经常 得 比 最 to Done; Next becomes the first part of the next lesson on the route (or level complete)`. The next lesson on the route is Lesson 12, whose part 1 is done. The brief says "the first part"; `requests.md` says "its Done lines show which part comes next". A tutor who follows the brief writes `Next: Lesson 12, part 1 of 2` and teaches 门 打开 进 again. The script holds the Done log and could say "Lesson 12, part 2 of 2", but it never reads the Route.
- Nothing records which known-lesson words a part actually used. Lesson 12 part 1 used 等 (02), 快 (04), 让 (01), so no harm here. Had it used 已经 as one of its four, the learner would have met it in 2-12.1, and after the un-skip the checker would call it NOT MET in every review until 2-03.1 is done.
- Each `part` run overwrites `plan.txt`: the plan of Lesson 12 part 1 was gone as soon as chat 3 ran. Fine for a plan; worth knowing if a practice run (`--lesson`) happens mid-part.
- `read_course` parses each lesson's part count (`parts`) and never uses it: if the Lessons list said "(3 partes)" for Lesson 3 and the map gives 2, nothing warns.

### The plan of Lesson 12 part 1 as taught (plan.txt was later overwritten by chat 3)

```
review: 我爸爸的病好了，明天他能去上班了。
review: 我明天上午不上课，要去看病。
review: 这个医生太忙了，我们明天再来吧。
review: 我妹妹生病了，今天没去学校。
review: 我觉得这本书很好看，你也读一下吧。
review: 我姐姐在医院工作，她星期天也要上班。
review: 我今天有点儿忙，没时间吃早饭。
review: 这个手机太贵了，有便宜一点儿的吗？
chunk: 打开门 / 进房间 / 在门口等我 / 你过来一下
round1: 请大家打开书。
round1: 他们进了电影院。
round1: 我在门口等你。
round1: 请你们过来一下。
round1: 他在医院门口等我。
round2: 老师进来的时候，我们正在说话。
round2: 我今天早上打开门，看见外边下雪了。
round2: 今天太晚了，你们明天再过来吃饺子吧。      (reworked; was 明天晚上你们都过来吃饺子吧。)
round2: 她进了房间，打开电视看电影。
round2: 我们公司门口有一个小商店。
round3: 你到门口了吗？我去开门，你快进来吧，外边下雨了。   (reworked; was 我来开门 … 外边太冷了。)
round3: 今天晚上我在家做饺子。你下班了过来吃吧！我爸爸妈妈也想见你。
round3: 昨天晚上我在家看电视，听见有人在门口说话。我打开门，看见我哥哥和他的两个朋友在外边。   (reworked; was 看见我哥哥在外边。)
round3: 这是我的房间，请进！你坐这儿吧。你想喝茶吗？
round3: 你过来一下。你朋友在门口，你去让她进来吧。
listening: 今天是星期天，我的朋友小王过来玩。下午三点，他到了我家门口，给我打电话。我打开门，请他进来。他进了我的房间，我们喝茶、看电影。晚上我妈妈做了饺子，非常好吃。
```

## 2. Had to guess

1. **Where the jump-start words come from.** `requests.md`, "Skip lessons…": "name those lessons, with a few of the words each one teaches". It names no source. `SKILL.md` says "You don't need to read `maps/`", and `course.py overview` is mentioned in `requests.md` only under the un-skip and "Change the pace". I found it by running `course.py` with no arguments and reading its usage ("Jump-start lessons come with their words, for asking a learner which they know"). A tutor that does not think to do that reads the map, or invents the words.
2. **Un-skip: what happens to `Next`.** `requests.md` opens with "Unless a request says otherwise, it leaves **Next** and **Done** as they are", and the un-skip sentence says only "remove the mark, write its parts again (from `course.py overview`), and put it on the route, first if the learner wants it now and otherwise after the lesson in progress". It never says to set `Next`. Read literally, `Next` stays `Lesson 12, part 2 of 2`, the route says 03 first, and the next chat teaches 12.2 (verified, section 1). I set `Next: Lesson 03, part 1 of 2`, because `SKILL.md` defines Next as "the lesson and part to teach next" and the learner said "agora". The opposite case is as open: "otherwise after the lesson in progress" with Next left alone is right, but only by accident.
3. **"Confirm that in one line, save the route"** (`requests.md`, "Changing the route"). A statement, or a question to wait on? "Change the level" in the same file says "confirm it first in one line … When the learner confirms", which is clearly a wait; here "save" follows at once. I stated the order in one line at the top of T4 and went on. The scenario's "if asked about the order" never triggered.
4. **How many known-lesson words a part may use.** Three texts, three answers. `SKILL.md`, "Met words": the learner has met "the words of the lessons marked `(known)`", and every piece of Mandarin "uses only met words", so all 42 are free. `requests.md`: "Their words count as met, and the brief of each part lists them so you can remind the learner". The brief: "use four of them at most in this part, and list the ones used under the table with pinyin and meaning". `check_plan.py` sides with `SKILL.md` (all 42 met, no limit). I obeyed the brief (used 等 快 让). Open inside the brief's rule: does the limit cover the review, which comes before the table where the reminders are listed? I kept known words out of the review. Does it cover what the learner writes? I assumed not. Is it four per part forever? The brief says so in every part: 一起, 已经, 就, 得, 比 never become freely usable, since known lessons never get a Done line.
5. **The label of the known-word reminders.** `SKILL.md` step 2: "The table, any extra words and known-word reminders". `lesson-format.md` gives no format or label for them. I wrote one line, "Palavras que você já conhece e que aparecem hoje:", with inline **Hanzi** (*pinyin*, meaning).
6. **Labels in the file don't match the skill.** `course.md` has eleven: "Aula, parte, Revisão, Bateria, Exercício, Escuta, Ditado, Áudio, Leitura, Frases úteis, Largada". `SKILL.md` defines nine: "lesson, part, review, round, dictation, audio (the narration clip), reading, useful phrases (the chunk list), and jump start". Nothing says what "Exercício" and "Escuta" stand for (an older version of the skill, presumably). I used neither. "Escuta" may be the name of the listening step, which matters in the offer after round 3 ("one more round like it or the listening step"): with Audio none I called it "a Leitura".
7. **"Your turn"** (`lesson-format.md`, Reading: "A bold line such as **Your turn**") is not one of the Labels, so each chat words it afresh. I used "Sua vez".
8. **Shape of `To reinforce`.** `SKILL.md`: "five words or short chunks at most". No separator is given; the examples have single words. I saved `在门口说话 我家门口`, space-separated like the starting file. A chunk can't contain a space, and a pattern (place before the verb) has to be stored as one sample chunk; the next chat must guess from 在门口说话 that the point was word order.
9. **Correcting the rewrite.** `lesson-format.md`: "Correct the rewrite as a written translation", and the incorrect-answer format wants "the learner's whole answer in a blockquote … Then the full corrected sentence once". For a five-sentence text with one slip, the whole text again or the one sentence? I quoted the whole rewrite and gave only the corrected sentence.
10. **After the learner declines the offer at the close.** Nothing is said. I sent one line ("Combinado, até a próxima!").
11. **Un-skip in a chat that then teaches.** "quero estudar ela agora": the skill implies starting the part in the same chat. The scenario stopped at the save, so T60 is only the one-line confirmation (which the un-skip paragraph does not ask for either; I borrowed it from "Changing the route").
12. **Which file to read for `setup`.** `SKILL.md` says read `setup.md` when the learner writes "setup"; it also says read `requests.md` for "anything other than the next part", and `requests.md` → "The course screen" only says to read `setup.md`. I read both in chat 2 (and needed `requests.md` anyway one turn later).
13. **`data-value` on the level buttons.** `setup.md`: translate "the `data-value` and `data-note` texts". "HSK 1" has nothing to translate; I left the four as they are and translated the audio values.
14. **Student policy, not the skill:** the 24th answer (the rewrite) should have been in pinyin by "every fourth answer"; I kept the rewrite in Hanzi because the policy names translation prompts, and it carries the mistake due on every third answer.

## 3. Rules I could not satisfy

1. **"Met words only … Never teach a near-miss" against the part's own split.** Lesson 12 part 1 has 进来 but 进去 is in part 2. Any sentence told from outside the room ("my friend's mother opened the door and asked me in") needs 进去, so every 进来 sentence had to put the speaker inside, and 进 alone had to be 进 + place or 请进. I dropped two planned sequences for this (a visit to a friend's home; "the shop isn't open yet, we can't go in").
2. **"Natural … everyday verbs" against the new word 打开.** For a door, people say 开门; 打开门 is correct but heavier. The chunk 打开门 and the review line for 打开 teach the heavier form because 打开 is the table word. In round 3 I planned 我去开门 and accepted the learner's 我去打开门.
3. **"use four of them at most"** was satisfied (3 used), at a price: 一起 (我们一起喝茶), 已经 (他已经到门口了), 就 (下班了就过来), 着 (门开着) were all natural here and all left out to stay under four.
4. **"Same content"**, one bent prompt: to bring 再 back after the correction I wrote "venham de novo amanhã para comer jiaozi" for 你们明天再过来吃饺子吧. The Mandarin is natural (再 = "then, another time"); the Portuguese "de novo" overstates it. The rule "bring the item back once … never force the item into a sentence" and "Same content" pull against each other here.
5. **"Every chunk … longer than a single table word wherever the met words allow."** Satisfied, but 进来 is in no chunk: with four chunks and five round-1 prompts there was no room, and the natural chunk (快进来, 请进来坐) needs a known word or is nearly unswappable. It got its three lines in rounds 2 and 3.
6. **A planned answer with an unmet pattern** (我来开门) passed the checker; caught by eye. Not a rule I failed in the end, but the plan-then-check routine did not protect against it.

Everything else I could satisfy: review total fixed at 8, "Traduza para o mandarim" twice only, title above the review and repeated in the table heading, each corrected item brought back once in a reworked prompt (再 → Bateria 2·3; lugar antes do verbo → Bateria 1·3; 打开 → Bateria 2·2; 过来 → Bateria 2·3; 了 → Bateria 3·1; 个 → Bateria 3·3), one older word from each of the four lines (公司, 再, 大家, 早饭).

## 4. Unnatural Mandarin

- `打开门` (chunk; Bateria 2·2, 3·3; reading): correct, but 开门 is the everyday form. See above.
- `他们进了电影院。` / `她进了房间` / review `我们进那个超市买水吧`: bare 进 + place is grammatical and a little stiff; speech prefers 进去 / 进…去. Forced by the split (进去 comes in part 2).
- `你下班了过来吃吧！`: fine in speech; 下了班 or 下班以后 would be more usual, but 以后 is not met and 下了班 would trip the checker like 打了电话.
- `他到了我家门口，给我打电话。` (reading): natural, but I wanted 打了电话 and the checker refused it.
- `我爸爸的病好了` and `你看，那个商店的门开了` (chat 3 review 1): acceptable; the second would more often be 那个商店开门了.
- `我家门口有一个小饭店` (chat 3 plan): 饭店 for a small eatery is dated on the mainland (小饭馆; 饭馆 is HSK 2 Lesson 07, not met).
- Learner's accepted `我去打开门`: a native speaker would say 我去开门. Accepted without comment under "Accept any natural version"; arguably it deserved the "right meaning, more natural version" treatment.

## 5. Counts and time (HSK 2, Lesson 12, part 1)

- Review: 8 prompts (6 words of 1-22.1 + 2 to reinforce). 2 corrections (再来; 在医院工作).
- Vocabulary: 6 words, 1 usage note, 3 known-word reminders (等 快 让; limit 4), 0 extra words, 1 name (小王), 4 chunks.
- Rounds: 5 + 5 + 5 = 15 prompts, as the brief says. 5 corrections (打开; 过来; 下雪了; 一个; 在门口说话). 3 prompts reworked to bring items back.
- New words in round lines (alone / counting longer words): 门 3 / 9, 打开 4, 进 3 / 6, 门口 6, 进来 3, 过来 4.
- Reading: 1 text, 5 sentences, all 6 new words; rewrite with 4 changes; 1 correction (门口).
- Learner answers: 24 (5 in pinyin), 8 with a mistake. Extra round declined.
- To reinforce at the close: 在门口说话, 我家门口.
- Turns in the chat: 56 (4 before the part, 52 in it).
- Time for a real learner, estimated: review 8 min, vocabulary and chunks 4 min, round 1 5 min, round 2 8 min, round 3 13 min, reading and rewrite 7 min: about 45 minutes. Inside "up to about an hour".

## 6. Reading load

| Chat | Skill files the tutor read | Scripts run |
|---|---|---|
| 1 (jump + Lesson 12 part 1) | `SKILL.md` (13.4 kB), `requests.md` (4.4 kB), `lesson-format.md` (7.0 kB); single-word lookups in `syllabus/hsk-1..3.csv` with grep (欢迎, 客人, 关, 走, 带: not met) | `course.py` (usage), `course.py overview 2 5`, `course.py part`, `check_plan.py` ×2 |
| 2 (setup + un-skip) | `SKILL.md`, `requests.md`, `setup.md` (10.5 kB, of which only the last 35 lines apply to a saved course) | `course.py overview 2 5` |
| 3 (próxima aula) | `SKILL.md`, `lesson-format.md` | `course.py part`, `check_plan.py` |

Not read by the tutor in any chat: `first-parts.md` (brief said EARLY PART: no), `audio.md` (Audio: none), `levels.md`, `maps/`, `fonts/`, `LICENSE`. `course/course.md` was read at the start of every chat and reread before each save.

Read by me as reviewer only, never as the tutor: `course.py`, `check_plan.py`, `maps/hsk-2.md` (to check the briefs by hand), `web/setup.js` (to work out what the card's buttons send).
