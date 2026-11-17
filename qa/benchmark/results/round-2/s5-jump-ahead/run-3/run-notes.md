# Run notes: s5-jump-ahead, run-3

- Scenario: s5-jump-ahead (starting course: Lesson 1 done, next Lesson 2 part 1; first message "quero ir para a aula 22").
- Turns: 52 (T1 to T52, last turn is the tutor's closing message).
- Final state: course/course.md has Known: jump start, Route 01, 22, 02–21, Done line 1-22.1, Next Lesson 02 part 1 of 2, To reinforce: 爸爸, 想在家喝茶.

## Unclear points in the skill files

1. Review after a jump. SKILL.md: "One prompt per new word of the previous part in the **Done** log, at least five and at most ten." After a jump the previous part in the log is 1-01.2, not a part of the neighbouring lesson. I reviewed its six words (not the jump start's other words). Unsure if a review is intended here.
2. Labels. The starting course.md Labels line lacks Ditado, Áudio and the Rounds line. SKILL.md: "If an older file lacks one, choose it once and save it right away." I added Ditado, Áudio and "Rounds: Chunks, Ações completas, Sequências".
3. Route format after a jump with Lesson 01 already done. SKILL.md only gives the example "01–07, 12, 13, 08, ...". I wrote "01, 22, 02–21" (kept 01 so the level-complete rule still counts it).
4. When to ask the two questions. SKILL.md: "confirm in one line what comes after it, and save the route. If that lesson comes before the jump start is finished, ask once whether to count the jump start's words as known." I asked both in one message and proposed "2 to 21" for what comes after, rather than only confirming.
5. 病 as a standalone word. "every new word appears in at least three prompts" does not say whether 看病/生病 count for 病. To be safe I used 病 alone (没有病) in three prompts (Round 1 #5, Round 2 #3, Round 3 #5). Chunk limit of four left no chunk for 病 alone, so I put 我没有病 in the meaning line of the 我生病了 chunk and in the usage note.
6. Chunks must "swap its open slot" in Round 1. For 我觉得我没有病 (rework of a prompt after a slip) I treated the nested sentence as the slot of 我觉得……
7. Reinforce list after listening. SKILL.md talks about misses in "that part" but is not explicit about slips in dictation and narration. I added 爸爸 (dictation slip) and 想在家喝茶 (wrong narration answer), as a word and a short chunk.
8. Wrap-up role-play. Lesson 22 has one part, so the "two or more parts" condition was not met and no role-play was offered.
9. Meaning-line spelling for the Markdown fallback: "Use bold Hanzi when the interface supports standard text formatting only." I used bold Hanzi in the table, no inline math.
10. Met-word check. 好了 (got better), 大病 and 位 are not clearly "met" even though 好 / 了 / 大 are, so I avoided them in prompts and scripts.
