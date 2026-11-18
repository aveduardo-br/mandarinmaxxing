# Run notes · s11-hsk2-mid · round 6 · run c

## Scenario

- Learner in the middle of HSK 2: Lessons 1 to 9 done, HSK 1 counted as met. First message: `próxima aula`.
- Part taught: HSK 2, Lesson 10, part 1 of 2 (pace 5, `Split: 1-1-1 / 1-2 / 3`, so one block: 地铁 站1 离 远).
- The student chose the listening step over an extra round. The run stops at the tutor's closing message (T48), which offers the next part.
- Turns: 48.

## State changes in `course/course.md`

- At the start: added the missing labels `Ditado` and `Áudio` to **Labels** and the missing line `Rounds: Chunks, Ações completas, Sequências`.
- At the close: `Next: Lesson 10, part 2 of 2`; Done line `2-10.1 | 地铁 站1 离 远`; `To reinforce: 远` (was `虽然 得`).

## Planning step

- Older words due back, from the 20-line Done log: line 3 back (2-09.1) 1st word 走; line 7 back (2-07.2) 2nd word 手; line 14 back (2-03.2) 3rd word 有时. Lines 30 and 60 back are not reached. Items to reinforce: 虽然, 得.
- Drafted in one pass, Mandarin first: 5 review sentences, 3 chunks, 15 round sentences (5 + 5 + 5), 4 dictation sentences and a 7-sentence narration; 28 plan lines in `scratch/plan.txt`. Before that I looked up 面1, 站1, 过去1 and 离 in `syllabus/hsk-2.csv` and listed the HSK 1 words once, to keep out words such as 以后, 先, 下车, 近, 一会儿 and measure-word uses of 家 and 杯.
- Checker runs: 2.
  - Run 1 reported everything met and every new word in three round lines or more. On my own recount of frames I then saw that review sentences 3 and 5 shared a frame (place + 后面/前面 + 有一个 …), so I replaced review 5 (医院前面有一个很大的书店，我们在那儿等你。) with 我已经到了，正在学校前面等你。
  - Run 2, on the changed plan, reported the same OK.
- Prompts reworked during the session (checked word by word by hand, not with the checker, since the skill caps it at two runs):
  - Review 5 became 我跟弟弟一起在学校前面等你，你快来吧。 (brings back 跟…一起 after the slip in Revisão 3).
  - Bateria 1 · 5 became a question, 你丈夫坐地铁去公司吗？ (brings back 吗 after Bateria 1 · 4).
  - Bateria 2 · 3 became 我们公司离地铁站不远，可以走路过去。 (brings back 走路过去 after Bateria 2 · 2).
  - Bateria 3 · 3 became 我有时坐地铁去学校，有时走路去。我走得很快，二十分钟就到了。 (brings back 得 after Bateria 2 · 5).
  - Bateria 3 · 5 became 我已经在地铁上了。医院不远，坐两站就到了，你别开车了。 (brings back 已经…了 after Bateria 3 · 4).
  - 离 after the slip in Bateria 1 · 1 came back in Bateria 1 · 4 as planned, so no rework there.
  - `scratch/plan.txt` holds the plan as checked, not these later reworks.

## Tool output

### check_plan.py, run 1

```
OK: 28 lines, every character met, every new word in three round lines or more.
```

### check_plan.py, run 2

```
OK: 28 lines, every character met, every new word in three round lines or more.
```

## Places where an instruction was unclear or hard to apply

1. **Lesson names saved in English.** `SKILL.md`: "**Lessons** is the level as the learner saw it at setup: map number, name in their language, number of parts. Use these names in every chat." The saved `course.md` has `Language: Português` but English lesson names ("10 Getting around town (2 partes)"). I used the saved name as it stands in the title (`HSK 2 · Aula 10 · Getting around town · parte 1 de 2`) rather than translating it, because the instruction says to use these names; the result is an English name inside a Portuguese title.
2. **Missing labels and Rounds.** `SKILL.md`: "If a file lacks one, choose it once and save it." It does not say when to save. I saved the added `Ditado`, `Áudio` and the `Rounds` line right away, before the first message, instead of waiting for the close.
3. **To reinforce after an item is corrected and then answered right.** Two sentences pull in different directions. "After each part, remove the items the learner got right unaided during the part, then add the ones they missed anywhere in it (review, rounds, dictation, rewrite) and didn't get right later." versus "**After a correction**, bring the item back in a later prompt of the same or the next round, in a new frame, and add it to the words to reinforce." I read the first as the rule for the saved list: 跟…一起, 离, 吗, 走路过去 and 已经…了 were each missed once and answered right in the later prompt, so none was saved. 得 was already on the list, was missed in Bateria 2 · 5 and answered right in Bateria 3 · 3; I removed it on the literal reading ("got right unaided", "didn't get right later"), though a tutor could fairly keep it. 虽然 was right at the first try and was removed. 远 (heard as 晚 in the dictation) had no later prompt and was saved.
4. **Whether a dictation or narration miss counts for the list.** The same sentence names "dictation" but not the narration. I saved the dictation slip (远) and not the wrong narration answer (十二 heard as 二十).
5. **面1 in the review.** "One prompt per new word of the last **Done** line". 面1 is a suffix in the syllabus (后缀), so it has no use on its own, and its met compounds are other table words (前面, 后面). I gave it a prompt with 前面, on the ground of "a word that lives mostly in compounds can stay in them", which is written for the rounds and not for the review.
6. **The script and the "what a chunk meant in context" question.** `lesson-format.md`: "Keep the script out of the message. Show it, with pinyin and meaning, only after the learner answers or if they ask." and, for the narration, questions on "what a chunk meant in context". Asking about a chunk means showing a few words of the script before the answer. I showed only that one phrase (走了五分钟就到了) in question 4.
7. **Older word 手.** "use each in at least one prompt of the review or the rounds". 手 only fitted naturally as the object in 洗手 (Bateria 3 · 4), next to 洗手间. I counted that as using the word, since 洗手 is verb plus object and not a table word.
8. **Round 1 with three chunks and five prompts.** "when a chunk comes up twice, change a different slot each time". After the rework for 吗, Bateria 1 · 5 changes the person and also turns the chunk into a question; I took that as still one chunk with a slot changed.
