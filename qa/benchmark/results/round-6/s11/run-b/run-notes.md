# Run notes

- Scenario: s11-hsk2-mid (HSK 2, Lessons 1–9 done; taught Lesson 10, part 1: 地铁 站1 离 远). First student message `próxima aula`; student chose the listening step and the session stops at the tutor's closing message.
- Turns: 48.
- Saves: `course.md` was written twice: once before the first message (missing labels and round names chosen), once at the close (Done line, Next, To reinforce).

## What happened in the part

- Older words due back: 走 (3 back, 1st word), 手 (7 back, 2nd word), 有时 (14 back, 3rd word); lines 30 and 60 are beyond the log. All three were placed in the review. Items to reinforce 虽然 and 得 were placed in Review 3.
- Prompts reworked after corrections (the plan had different sentences): Review 5 (to bring 得 back), Bateria 2 · 4 (to bring 从…到 back), Bateria 3 · 5 (to bring the final 吗 back). The other corrected items came back in prompts already planned (每天 before the verb in Bateria 2 · 2, 已经…了 in Bateria 3 · 2, the 离 order in Bateria 3 · 3).
- No support words.

## Places where the instructions were unclear

1. **Labels and Rounds missing from the file.** The saved course had no `Rounds` line and its `Labels` had no words for dictation and audio. I applied "If a file lacks one, choose it once and save it" and added `Ditado`, `Áudio` and `Rounds: Chunks, Ações completas, Sequências`. The skill doesn't say when to save them; I saved before the first message.
2. **Lesson names in English in a Portuguese course.** The `Lessons` list holds English names ("Getting around town") with "(2 partes)". "**Lessons** is the level as the learner saw it at setup: map number, name in their language ... Use these names in every chat." I kept the English name in the title rather than translating it, since the instruction to use the saved names is explicit; the result is a mixed-language title.
3. **To reinforce after a part in which every miss was later answered right.** `SKILL.md` says in one place "After a correction, bring the item back in a later prompt ... and add it to the words to reinforce", and in another "After each part, remove the items the learner got right unaided during the part, then add the ones they missed and didn't get right later." I followed the second at the save: 虽然 was right unaided twice; 得 was missed once and then right twice; the five new slips (每天 order, 从…到, 已经…了, 离 order, final 吗) were each answered right when they came back. So the list ended empty. Whether 得, missed and then right in the same part, should stay is not clear to me. The file format for an empty list is also not given; I left `- To reinforce:` with nothing after it.
4. **"The same or the next round" for a correction in the review.** "bring the item back in a later prompt of the same or the next round": the review isn't called a round. I treated it as one and reworked Review 5.
5. **Review prompt for 面1.** The last Done line includes the suffix 面, which the learner can only show inside 前面/后面/左面/右面, and 左面 and 左边 translate the same way. I wrote a prompt whose answer has 前面 and 左面, accepted 左边, and named 左面 in one line. "One prompt per new word of the last Done line" is hard to apply to a suffix.
6. **"Rounds 1 and 2 are never shorter than the review."** I read this as the number of prompts (five each), not sentence length, since round 1 prompts built on a chunk are naturally shorter than review sentences "as long as round 2's".
7. **Chunk question in the narration vs. keeping the script hidden.** The narration needs a question on "what a chunk meant in context", while "Keep the script out of the message." I quoted only the four-character chunk 走路过去 in the question.
8. **Frame rule vs. round 1.** "no two prompts share a frame" against round 1's "uses one of the part's chunks with a slot changed": with a pattern word such as 离 (A 离 B + distance), several prompts necessarily keep the A 离 B 远 skeleton. I varied the sentence type (statement, question, 太…了 plus a suggestion, inside a sequence) rather than avoid the pattern.
9. **Composed words.** 火车站, 每天, 下周, 上个月, 星期六 and 回/吃 compounds are not syllabus entries but are built from met words; I counted them as met. I avoided 下车 and 没 alone to stay on the safe side.
10. **Narration length.** "20 to 40 seconds" can't be measured without generating; the script has about 95 characters in seven sentences.
