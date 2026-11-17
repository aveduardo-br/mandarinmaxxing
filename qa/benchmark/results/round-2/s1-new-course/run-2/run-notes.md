# Run notes

- Scenario: s1-new-course (round 2, run 2)
- Turns: 72 (T1 to T72)
- Final state: `course/course.md` saved after part 2 (Next: Lesson 02, part 1 of 2; To reinforce: 不客气). The wrap-up role-play left Next and Done unchanged.

## Unclear instructions or uncertain applications

1. Setup language. The first message is English ("start mandarinmaxxing"), which is too little text to infer a language. SKILL.md: "If there is too little text, use the language the interface or what you already know about the learner points to, or ask in one short line before the setup." I used Portuguese because the benchmark defines the learner as a Brazilian who writes in Portuguese, and I did not ask the one-line question, so the setup answer in the scenario applies directly.

2. Review size in part 2. The previous part had 3 words. SKILL.md: "One prompt per new word of the previous part in the Done log, at least five and at most ten. When that part had fewer than five words, fill the review with the items to reinforce and the older words (below), each in a prompt of its own, rather than stretching sentences." The log held only those 3 words, and the single reinforce item (再见) was one of them, so there was nothing distinct to reach five without repeating. I used a 3-prompt review and reworked prompt 3 so it brought back the missed 再见. The "at least five" minimum and the "each in a prompt of its own" rule conflict here.

3. Rounds with fewer than ten met words. SKILL.md: "give round 1, then a round 2 of short exchanges ... and skip round 3." I kept the saved round name "Ações completas" for round 2 even though its content is short exchanges. After round 2 I wasn't sure what to offer, because the rule says "After round 3, offer one more round in the style of round 3, or the listening step", and round 3 was skipped. I offered "another round of short exchanges, or the listening step".

4. Part 2 met 9 words, so round 3 was skipped in both parts, and the narration was skipped as well ("before that, the dictation alone"). The skill doesn't say whether to count the review words (the previous part's words) toward the ten.

5. Three prompts per new word with near-synonyms. "Every new word appears in at least three prompts" is tight when 没关系 and 没事 translate the same way and the lesson-format note says to "give each prompt a context that fits only one, or accept both." I accepted both and assigned an expected answer to each prompt to keep three appearances per word, which forced several four-line exchanges in round 2 of part 2 ("short exchanges" has no length limit).

6. 您 needed three prompts. Its only natural prompt shape is a greeting to a senhor or senhora, so I reused that scenario in R1.4, R2.2 and R2.4.

7. Audio setting at setup. The skill says to save the choice at setup but to choose and save the voice "on the first clip of a course". The final `course.md` shows `ElevenLabs, voice Sarah`. I did not model an intermediate `Audio: ElevenLabs` state.

8. Part 1 chunk breakdown. 你好 = 你 + 好 was left out because 你 isn't met. Part 2 included the 您好 breakdown because both of its parts are new words of that part.

9. Closing of part 2. The skill offers both the next part and the wrap-up role-play in the same closing. The scenario says to accept the role-play and stop after it, so the next-part offer was left unanswered.

10. Role-play format. SKILL.md says "writing in Mandarin with the meaning under each line", and I used the bold Hanzi, italic pinyin, plain meaning pattern for the tutor's lines. It is not specified whether the tutor's lines in a role-play need pinyin.

11. Corrections inside the role-play and the "natural but unnatural" case. 你好 to an elderly woman is correct but less natural than 您好, so I treated it as "correct meaning, noticeably unnatural phrasing" and showed 您好 without a "You wrote" blockquote.

12. To reinforce after part 1. I kept the rule literally: slips corrected and then answered right later in the same part were not saved; only the dictation slip at the end (再见) was. Part 2 then removed 再见 (answered right in review 3 and round 2) and added 不客气 from the last dictation sentence.
