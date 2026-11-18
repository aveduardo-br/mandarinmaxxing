# Run notes · s11-hsk2-mid · run-a

- Scenario: s11-hsk2-mid. HSK 2, Lessons 1–9 done, taught Lesson 10 part 1 (pace 5, split `1-2`, one block: 地铁 站1 离 远). First message `próxima aula`. Student declined the extra round (chose the listening step). Stopped at the tutor's closing message.
- Turns: 48.
- Skill used: `/home/claude/mm-056/skills/mandarinmaxxing/` (SKILL.md, lesson-format.md, maps/hsk-2.md, syllabus lookups).
- Saves: `course.md` was saved once at the start (missing labels `Ditado`, `Áudio` and the `Rounds` line added) and once at the close (Done line `2-10.1`, Next, To reinforce).
- Older words picked (lines 3, 7, 14 back): 走 (2-09.1, 1st), 手 (2-07.2, 2nd), 有时 (2-03.2, 3rd). All three are in the review.
- To reinforce at the close: 虽然 and 得 removed (used correctly unaided in the review); 离 added (dictation slip 里 for 离, after the last written use) and 后面 added (missed in the narration answers). 有时, 跟…一起, 离 order, 地铁站 and 吃完饭 were corrected and then answered right unaided in a later prompt, so they were not added.

## Places where the instructions were unclear or hard to apply

1. **Saved file older than the format.** The starting `course.md` had no `Rounds` line and its `Labels` lacked dictation and audio. "If an older file lacks one, choose it once and save it right away." covers Labels explicitly; I applied the same to `Rounds`, which the sentence does not name.
2. **Lesson names in English with Language: Português.** The `Lessons` list in the saved course is in English. "Write it once and use these names in every chat." I kept "Getting around town" in the title rather than translating it, which reads oddly in a Portuguese lesson.
3. **Reviewing a suffix.** "One prompt per new word of the previous part" with 面1 (suffix) in the line: there is no way to ask for a suffix alone, and 左边/右边 were in the same line. I reviewed it through 前面; a learner could not tell that prompt was "for 面".
4. **Two rules on the reinforce list.** "When an answer needs a correction, bring that word back in a later prompt of the same or the next round, and add it to the words to reinforce" against "add the items the learner missed and did not get right unaided later in the same part". I followed the second (an item answered right later is not saved).
5. **Listening slips and the reinforce list.** Nothing says whether a dictation slip or a wrong narration answer counts as "missed". I counted both (离, 后面), since nothing later in the part could show them right.
6. **Review total against extra items.** The previous part had exactly five words, so the review is five prompts, yet "Put the older words picked for this part in the review itself" plus two words to reinforce meant weaving five extra items into five prompts. It worked here, but "Weave items into a sentence only where they fit one natural situation" and the fixed count pull against each other.
7. **"never shorter than the review" for round 1.** With review prompts written at round-2 length, round 1 chunk prompts also have to be two-clause sentences; a plain chunk swap (请问，火车站在哪儿？) would break the rule. I lengthened every round 1 prompt.
8. **Narration question on a chunk against keeping the script hidden.** "what a chunk meant in context" needs the chunk quoted in the question, while "Keep the script out of the message" applies before the learner answers. I quoted only 就到了.
9. **站 as a counted unit.** 过两站 uses 站 without 个; the map gives 站1 as a noun only. I added a usage note under the table so the prompt was answerable.
10. **Bringing a corrected item back on the last review prompt.** Review 5 was reworked to carry 有时 while keeping 虽然; the result (虽然饭馆前面有时人很多…) is acceptable but denser than a prompt written fresh.
