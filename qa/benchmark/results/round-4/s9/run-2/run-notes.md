# Run notes: s9-hsk4-mid, run-2

Scenario: s9-hsk4-mid (HSK 4, Lesson 28 "At the gym", part 1 of 3, pace 5, blocks 1-2: 健身 教练 力气 健身房 汗 流 身).
Turns: 52 (T1 student to T52 tutor closing).
Older words used (by Done-log distance 3/7/14/30/60): 使用, 重 (zhòng), 寄, 皮鞋, 懒.

Unclear points or judgment calls:

1. Lessons list language. course.md says `Language: Português` but its Lessons list has English names ("28 At the gym (3 partes)"). SKILL.md: "Write it once and use these names in every chat." I kept the saved English name in the title line.
2. Missing labels. The starting course.md had no `Rounds:` line and no labels for dictation and audio. SKILL.md: "If an older file lacks one, choose it once and save it right away." I added `Ditado`, `Áudio` and `Rounds: Chunks, Ações completas, Sequências`.
3. One prompt per new word in the review. SKILL.md: "One prompt per new word of the previous part ... at least five and at most ten." The previous part had 7 words plus 5 older words to weave in. I merged 吸 and 烟 into one natural prompt (吸烟), and 7 prompts in total covered everything. Unsure whether each word should have its own prompt.
4. Few usable words. Many natural gym words (计划, 公里, 机器, 台) are HSK 4/5 but not yet in the Done log, so I had to avoid them. That limits what "natural Mandarin in long sentences" can be at this point of Lesson 28. Quote: "Design every prompt so it can be answered with words the learner has met."
5. Reworking prompts after a correction. "rework a prompt still to come so it uses the item that went wrong, and add a prompt only if none is left." Done in review (停止, 发出) and rounds. The last slip (搬完家) came in round 3 prompt 4, with only one prompt left, so it stayed in To reinforce.
6. Round 3 length. "Make them as long as the met words allow." I used two to three sentences per prompt. Not sure how long is long enough.
7. Narration and quotes. "The speaker never ... quotes anyone." I used indirect speech (教练很耐心，让我慢慢来) and wasn't sure whether reported speech counts as quoting.
8. Audio script visibility. The runner shows the script in an `audio-script` block as the clip, while SKILL.md says "Keep the script out of the message" until the learner answers. I followed the runner format and showed pinyin and translation only after the answers.
9. Pinyin cadence. I counted only translation prompts (22) for "every fourth answer in pinyin" (answers 4, 8, 12, 16, 20); dictation and narration were not counted.
10. No role-play offer, since part 1 of 3 is not the last part of the lesson.
11. 健身 and 锻炼 translate the same way; I gave a usage note and accepted both in prompts.
