# Notes · sim3 · HSK 3 · Lesson 18, part 1 of 2

Scenario: T1 `próxima aula`; course.md from an older skill version; HTML table available; ElevenLabs (clip stood in by an `audio-script` block); student declines the extra round and takes the listening step. 40 turns. Part taught: 3 new words (丢 卡 以为).

Files written: `transcript.md`, `course/course.md`, `course/plan.txt` (the skill requires it), `notes.md`. Housekeeping outside the skill's flow: three scratch copies in `/tmp` (original course.md, plan header, plan after run 1), and one scratch plan file created in the output folder by the after-session script run and deleted straight away.

## 1. Scripts

### Run A · brief
```
python3 -I /home/claude/review/sim3/hsk3/skill/course.py part /home/claude/review/sim3/hsk3/course/course.md /home/claude/review/sim3/hsk3/course/plan.txt
```
```
PART: HSK 3 · Lesson 18 · Perder o celular ou o cartão · part 1 of 2
NEW WORDS, in blocks that work together: 丢 卡 以为
REVIEW: one prompt per word of 3-17.2: 出院 健康 病人 脚 锻炼 坚持
  and one for each item to reinforce: 一定 打算
OLDER WORDS: use one from each line, the one that fits a sentence best:
  3 back (3-16.2): 起 or 刷
  7 back (3-14.4): 种 or 怎样
  14 back (3-12.1): 斤 or 羊
  30 back (3-06.3): 男人 or 一样
EARLY PART: no (747 words met before this part)
ROUNDS: three rounds of 3 prompts; every new word in at least three of them
LISTENING: dictation only with audio; one reading without
AT THE CLOSE: add `3-18.1 | 丢 卡 以为` to Done; Next becomes Lesson 18, part 2 of 2
PLAN HEADER written to /home/claude/review/sim3/hsk3/course/plan.txt: add SUPPORT or NAMES lines above DONE if the part needs them, and the plan lines at the end.
```
Exit 0. course.md was not touched by the script (diff against a copy: identical). plan.txt got `LEVEL 3`, `NEW 丢 卡 以为`, `DONE` + the 47 Done lines, `PLAN`.

Checked by hand after the session (map `skill/maps/hsk-3.md`, lesson 18: `Split: 1-1-1 / 1-2 / 3`, rows 丢 卡 以为 / 发现 关机 银行卡 / 开机 信用卡):
- Part and new words: correct for pace 5 (2 parts; part 1 = first row).
- Review words = last Done line (3-17.2), reinforce = file's list: correct.
- Older-word lines: 3, 7, 14 and 30 back counted by hand: 3-16.2, 3-14.4, 3-12.1, 3-06.3, all correct.
- 747 words met: 300 (HSK 1) + 200 (HSK 2) + 247 in Done: correct.
- Close line: correct.

What the brief got wrong or left unclear:
- **Said nothing about the old course file.** The file has no `Rounds` line and its Labels are `…Bateria, Exercício, Escuta, Leitura…` where the current skill expects `…round, dictation, audio…`. The script ran silently; the tutor has to notice both alone.
- **"dictation only" contradicts audio.md.** audio.md: narration "only once the met words can fill about 20 seconds; before that the dictation is the whole step". With 747 words met a narration is easy. The script decides by the number of new words (`'dictation and narration' if n >= 5 else 'dictation only'`), so a 3-word part at HSK 3 gets the listening step of a beginner. I followed the brief.
- **Rounds of 3 prompts** (`per_round = min(5, n)`): also tied to the 3 new words. The whole part has 9 new-material prompts against 8 review prompts.
- **Pace** says "about 5 words per part", the part has 3 and the next has 5. Not wrong, but nothing tells the tutor it is expected.
- The older-word candidate 起 is, for the learner, mostly inside 起床 (an HSK 1 word); 刷 mostly inside 刷牙. The brief does not say whether the compound counts.

### Run B · check_plan, first draft (Mandarin only, 24 lines)
```
python3 -I /home/claude/review/sim3/hsk3/skill/check_plan.py /home/claude/review/sim3/hsk3/course/plan.txt
```
```
NOT MET (rewrite the sentence, or list the word as a support word):
  公园  in review: 我每天早上六点起床，先刷牙，然后去公园锻炼。
  北京  in review: 放假的时候，我打算跟朋友一起去北京旅游。
  银  in round1: 我的银行卡丢了。
  银张  in round2: 这种卡丢了以后，得去银行换一张新的。
  银  in round3: 我今天去银行了，因为我的卡丢了。他们说下星期才能给我新卡，这几天我只能用手机。
  张  in listening: 请问，这张卡是谁的？
CHECK (met words cover it, but it is also a word not met yet; keep it only if you mean the parts):
  才能  in: 我今天去银行了，因为我的卡丢了。他们说下星期才能给我新卡，这几天我只能用手机。
```
Exit 1.

Changed before the next run (I looked up 银行, 张, 公园, 办 one by one in `syllabus/hsk-3.csv`: all HSK 3, none in Done):
- review: 去公园锻炼 → 出去锻炼; 去北京旅游 → 去旅游.
- round1: 我的银行卡丢了 → 我的学生卡丢了.
- round2: 这种卡丢了以后，得去银行换一张新的 → 这种卡不能丢，丢了就不能进小区了.
- round3: the bank message → 我的饭卡又丢了，这是第二次了。今天中午我不能在学校吃饭，只能叫外卖。
- listening: 这张卡是谁的 → 这是谁的卡.
- No SUPPORT line: I chose to drop 张 and 银行 instead of spending the two support words (see section 3).

### Run C · check_plan, second draft
Same command.
```
OK: 24 lines, every character met, every new word in three round lines or more.
```
Exit 0.

### Run D · check_plan after adding the Portuguese prompts (diagnostic; the skill does not ask for it)
Between C and D: one Portuguese line under each Mandarin line; 叫外卖 → 点外卖 (syllabus look-up: 叫 "to order" is not the HSK 1 sense, 点2 is HSK 2); and round3 line 2 rewritten to 我的学生卡又丢了，到现在还没找到。今天中午我不能在学校吃饭，只能点外卖。 In the session's story that rewrite happens after T25/T27 (the 钱包 gap and the 没找到 correction); I wrote the session after planning it whole, so the file already held it at this run.
```
OK: 24 lines, every character met, every new word in three round lines or more.
```
Exit 0. Unlabelled prompt lines are ignored without complaint (good, but undocumented: SKILL.md says to write prompts "under the answer" and never says how).

### Run E · after the session, `course.py part` on the saved course.md with a scratch plan path (deleted afterwards)
Exit 0. It accepted the saved file and printed the part 2 brief: `NEW WORDS: 发现 关机 银行卡 | 开机 信用卡`, `REVIEW: … 丢 卡 以为 and … 瘦了很多 又`, `ROUNDS: three rounds of 5 prompts`, `LISTENING: dictation and narration`. So the hand-made save parses.

### What check_plan got wrong
It checks characters, not words or senses, so it passed three things the learner had not met:
- **还 (huán, devolver)** in review 7, 把书还给你. HSK 3 word (map line 243, a later lesson), not in Done. Covered by 还 hái of HSK 1. The student could not answer (T15); the tutor fell back to 把书给你, which changes the meaning.
- **钱包** in round 2. Not in the syllabus at any level; 钱 and 包 are met, so no NOT MET and no CHECK. The student did not know it (T25).
- **饭卡** (first draft of round 3) and **学生卡**, **羊肉**, **刷卡**: same mechanism. 学生卡 and 羊肉 are guessable from their parts, 饭卡 and 钱包 are not.
- It reported 银张 as one item for a line where 银 and 张 are far apart (cosmetic).
- It does not look at the prompts, the frames or the chunk coverage of round 1; "OK" only means characters and the three-lines count.
- The CHECK list flagged 才能 (correct: I meant 才 + 能), but not the 以为/认为 type of risk, nor any compound that is absent from the syllabus.

## 2. Had to guess

1. **Labels of the old file.** Nine labels, same positions as the current list, but slot 5 is `Exercício` (current: dictation) and slot 6 is `Escuta` (current: audio/narration). No label is "lacking", so the rule "if a file lacks one, choose it once and save it" does not apply. I read them by position: the dictation is titled **Exercício 1**. That title tells the learner nothing about listening. `Escuta` went unused. I did not rewrite the Labels line.
2. **Rounds missing.** Chose `Chunks, Ações completas, Sequências` (the SKILL.md example is already in Portuguese) and saved it. The skill does not say when; I saved at the close, with the rest, because "nothing is saved before a part closes".
3. **Name of the listening step in the offer** after round 3. No label exists for "the listening step" as a whole; I wrote "a parte de ouvir".
4. **Narration or not**: followed the brief against audio.md (section 1).
5. **Voice.** audio.md says to choose Yun on the first clip of a course; the file already says Sarah, so Sarah.
6. **The student answered 一公斤 where I expected 两斤.** Accepted without comment (both natural, and older words have "nothing to track"). The exposure to 斤 was lost.
7. **A gap that is my fault (还, 钱包).** The skill has no rule for a `[não sei]` caused by an unmet word in the tutor's own prompt. For 还 I accepted the answer with 给 and did not teach 还 ("never teach a near-miss" is about prompts, but teaching a later lesson's word seemed wrong). For 钱包 I gave the word inline with a breakdown, as an unlisted extra word, because its parts are met. Two different treatments for the same failure.
8. **Does the dictation count as "got right later"?** I decided no. 又 went to To reinforce (and the student missed it again in the dictation anyway).
9. **Grammar in To reinforce.** The 了 slip is not a word; I stored the chunk 瘦了很多. 又 is stored bare, which gives the next review little to go on (the slip was 再 for 又).
10. **Where prompts go in plan.txt**: plain lines under each answer, no label.
11. **Whether 起床 / 刷牙 satisfy the older-word line "起 or 刷".** I counted them.
12. **Chunk 3 (我想刷卡)** uses 刷 in a sense the learner has not met (刷牙 only). I added a breakdown line; the rule allows one when the parts are "words met before", and says nothing about a new sense.

## 3. Rules I could not satisfy

- **"Met words only"**: broken twice in what reached the learner (还 huán in Revisão 7, 钱包 in Bateria 2 · 1), both invisible to check_plan.
- **A card lesson without 张 and 银行.** Both are HSK 3 words of later lessons (map lines 175 and 182), yet part 2 of this lesson teaches 银行卡. In part 1 the natural sentences (我的银行卡丢了, 这张卡是谁的, 去银行换一张新的) are all out of reach. Support words would cover two, but they may be "used only in that chunk's prompts", so 张 could not also appear in the dictation. I avoided both, which pushed every card sentence to 学生卡.
- **"Two to four chunks … every chunk listed is practised in round 1"** with a round 1 of 3 prompts: four chunks are impossible, and "when a chunk comes up twice, change a different slot each time" never applies.
- **"Older words: use one from each line"** against **"Same content"**: 两斤 has no Portuguese prompt that is not "um quilo", and "um quilo" got 一公斤.
- **"After a correction, bring the item back once"**: worked for 等了半天 (找了半天, Bateria 2 · 2), 以为 (same prompt) and 没找到 (Bateria 3 · 2, reworked for it). Failed for 瘦了很多 (no later sentence took a change-of-state 了 naturally) and for 又 (wrong in the second-to-last prompt; the one prompt left had no place for it).
- **Dictation: "No sentence repeats a chunk or a prompt of the part".** With three new words, 我弟弟又把学生卡丢了 is close to Bateria 3 · 2 (我的学生卡又丢了), and 我以为你已经出院了 is the chunk 我以为你回家了 with the clause swapped. Any dictation line with 以为 is that chunk's frame.
- **"A new frame" in rounds 2 and 3**: 以为 only works as 我以为 + clause, so four round prompts and one dictation line open or turn on the same frame.
- **Labels "never a synonym"**: kept, at the cost of the **Exercício 1** heading (section 2).

## 4. Counts

| Step | Exercises |
|---|---|
| Revisão | 8 (6 words of 3-17.2 + 一定 + 打算) |
| Bateria 1 · Chunks | 3 |
| Bateria 2 · Ações completas | 3 |
| Bateria 3 · Sequências | 3 |
| Listening | 1 dictation clip, 4 sentences |
| Total | 17 translation prompts + 1 dictation |

New words in round prompts (9 prompts):
- 丢: 5 (B1·1, B2·1, B2·3, B3·1, B3·2); on its own in all five. Dictation: 2 more.
- 卡: 5 (B1·1 学生卡, B1·3 刷卡, B2·2, B2·3, B3·2 学生卡); on its own in two. Dictation: 2 more.
- 以为: 4 (B1·2, B2·2, B3·1, B3·3). Dictation: 1 more.

Student: 17 answers, 4 in pinyin, 5 slips (T7 order, T13 missing 了, T21 认为 for 以为, T27 不 for 没, T33 再 for 又), 2 `[NÃO SEI]` caused by the tutor (T15, T25), 1 dictation slip (有 for 又).

## 5. Older words

| Brief line | Used | Where | Odd? |
|---|---|---|---|
| 3-16.2: 起 or 刷 | both, inside compounds | Revisão 5 (起床, 刷牙); 刷 again in the chunk 刷卡 | No. But 起床 is HSK 1 and 刷卡 is a new sense |
| 3-14.4: 种 or 怎样 | 种 | Bateria 2 · 3 (这种卡) | No, it fits well |
| 3-12.1: 斤 or 羊 | both planned | Revisão 1 (羊肉, 两斤) | Slightly: a father leaving hospital who wants mutton is a sentence built around the word. 斤 did not survive: the student wrote 一公斤 |
| 3-06.3: 男人 or 一样 | 一样 | Bateria 3 · 3 (跟我的一样) | No, it is the best sentence of the part |

Not on the brief but reused: 半天 (twice), 把, 小区, 沙发, 着急, 放心, 刚才, 后来, 才, 其实, 别人, 外卖, 特别, 双, 鞋, 瘦.

## 6. Repetition

- **我以为 + clause**: chunk, B1·2, B2·2, B3·1, B3·3, dictation 2 = 6 times.
- **X 丢了 as the whole clause**: chunk (手机), B1·1 (学生卡), B3·1 (手机), B3·2 (学生卡又), dictation 4 (把学生卡) = 5 times. 学生卡 is the lost thing 3 times, 手机 4 times (chunk, B3·1, B3·3, dictation 1).
- **找 … 找到 / 没找到**: B2·2, B3·1, B3·2 = 3 times (one of them added on purpose after the correction).
- **在包里**: B2·2 and B3·3.
- **半天**: Revisão 3 and B2·2 (the second on purpose).
- Review: the first three prompts are all hospital scenes (the reviewed words force it), and Revisão 5 and 6 are both "every day + exercise" (每天…锻炼, 每天坚持跑步).
- The session reads as one story told nine times: I thought X, I lost Y, I looked and found or did not find it. Three words, two of which only combine one way, cannot fill 9 prompts plus a dictation with different situations.

## 7. Unnatural Mandarin

- **学生卡 as the card that pays for lunch** (B3·2). On a mainland campus this is 饭卡, 校园卡 or 一卡通. Cause: 饭卡 dropped after the 钱包 gap showed that compounds of met characters are not met words; 银行卡 unavailable.
- **今天中午我不能在学校吃饭** (B3·2): stiff; a speaker says 没法在食堂吃 or 吃不了食堂. Cause: no 食堂, potential complements not surely met.
- **丢了就不能进小区了** (B2·3): 进不了小区 is what is said. Same cause. "这种卡" for a gate card is also vague (门禁卡).
- **把钱包丢在出租车上了** (B2·1): fine, though 落在 is more usual for "left behind". 钱包 itself was not met.
- **你放心，我明天一定把书给你** (T16): natural, but it is not the prompt's sentence; it is the fallback for the unmet 还.
- **我想刷卡** (chunk): acceptable; at a till people say 刷卡 or 我刷卡. The 想 is there to make a "chunk longer than a single word".
- **看见一个手机** (B3·3): colloquial; 一部手机 is the careful form. Fine.
- Portuguese side: "Os pacientes deste hospital são muitos mesmo" (Revisão 3) is bent to mirror 特别多 under "same content"; "não pode ser perdido" (B2·3) likewise.

## 8. Time

About 25 to 30 minutes for this learner: review 9–10 min (8 full sentences, 2 corrections), table and chunks 2 min, Bateria 1 3 min, Bateria 2 4–5 min, Bateria 3 6–7 min, dictation 3–4 min. A third of the sitting is review; the three new words get roughly 15 minutes. SKILL.md says a late part runs "up to about an hour".

## 9. Reading load

Read before or during the lesson: `SKILL.md` (2,343 words), `lesson-format.md` (1,177), `audio.md` (472) = about 3,990 words, plus the brief (about 150) and course.md (about 600). Not read: `setup.md`, `first-parts.md`, `levels.md`, `requests.md`. Single-word greps in `syllabus/hsk-*.csv`. After the session only, for the checks above: lesson 18 of `maps/hsk-3.md` and lines 176–212 of `course.py`.

About a third of lesson-format.md did not apply to this part (meaning and reply exercises, the Reading section, the Markdown fallback), and the narration half of audio.md was read and then overruled by the brief.

## What I did with the old course file

- Added `- Rounds: Chunks, Ações completas, Sequências` under Labels.
- Left Labels as it was (section 2, item 1).
- Added `3-18.1 | 丢 卡 以为` to Done, set `Next: Lesson 18, part 2 of 2`, replaced To reinforce with `瘦了很多 又`.
- Left the missing blank line before `## Lessons` alone.
