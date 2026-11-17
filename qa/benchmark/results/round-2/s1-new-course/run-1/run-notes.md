# Run notes

- Scenario: s1-new-course (round 2, run 1)
- Turns: 72 (36 student, 36 tutor)
- Final state: course/course.md (Next: Lesson 02, part 1 of 2; To reinforce: 不客气, 谢谢您; Done: 1-01.1, 1-01.2)

## Unclear or uncertain points

1. Language of the setup. SKILL.md: "If there is too little text, use the language the interface or what you already know about the learner points to, or ask in one short line before the setup." The first message ("start mandarinmaxxing") is English and tiny. I opened the setup in Portuguese based on what is known about the learner (Brazilian) instead of asking a language line, so the scripted setup answer still fit. Unsure whether the skill wants the one-line question here.

2. Voice saved at setup or at first clip. SKILL.md says Audio holds "the provider the learner chose, with the one voice picked for the course", while lesson-format.md says "On the first clip of a course, choose the voice and save it in `course.md`". I saved `ElevenLabs` at setup and added `, voice Sarah` right before the first clip.

3. Round 3 skipped, so the offer after it. SKILL.md: "After round 3, offer one more round in the style of round 3, or the listening step." With fewer than ten words met (also after part 2, which brought the total to 9), round 3 is skipped; I went straight to the dictation without the offer, since no round 3 style exists to repeat.

4. Chunks versus words with very few words. SKILL.md: "Round 1 ... Each prompt uses one of the part's chunks, swapping its open slot". Part 1 has three words and no open slot, and part 2's chunk list (two to four) cannot cover all six words, so prompts for 不客气 and 没事 used table words rather than listed chunks.

5. "Every new word appears in at least three prompts" with six new words and only ten prompts (no round 3) forced four-line exchanges in two prompts, and 没关系/没事 count as appearing in the prompts that accept both ("accept both" was chosen from lesson-format.md: "give each prompt a context that fits only one, or accept both"). 好 appears only inside 您好/你好 prompts, never alone.

6. Review with fewer than five words. SKILL.md: "When that part had fewer than five words, fill the review with the items to reinforce and the older words (below), each in a prompt of its own". The log had one line, so no older words (lines 3, 7, ... back) existed, and the only item to reinforce was 再见. To reach five I used the three words plus 再见 twice (one alone, one in 谢谢，再见) and 你好 twice.

7. Dictation numbering. "Dictation 1" is numbered per part (restarts in part 2); the skill says only "its number".

8. Role-play replies counted toward the student's "every fourth answer in pinyin" rule (answers 26-29, with 28 in pinyin). The role-play stage directions in italics (scene cues) are not covered by the "never a stage direction in parentheses" rule, which is written for review and round prompts.

9. Hanzi size in the Markdown fallback: used bold Hanzi, per "Use bold Hanzi when the interface supports standard text formatting only."

10. The closing of part 1 says "Quer começar a próxima parte agora?" with no wrap-up offer (part 1 is not the last part of a lesson), and the part 2 closing carried both the wrap-up offer and the next-part offer; the role-play end repeated the next-part offer. The skill does not say whether to repeat the offer after the role-play.
