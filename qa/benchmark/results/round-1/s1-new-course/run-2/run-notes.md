# Run notes

- Scenario: s1-new-course (round-1, run-2)
- Turns: 100 (T1 to T100; student on odd turns, tutor on even turns)
- Result: setup, route, part 1 (HSK 1 Lesson 1), part 2, dictation in both parts, wrap-up role-play (6 turns). Final course.md: Done has 1-01.1 and 1-01.2, Next is Lesson 02 part 1 of 2, To reinforce: 没关系.

## Unclear or uncertain points

1. Language of the setup. The first message "start mandarinmaxxing" is English and has too little text. SKILL.md: "If there is too little text, use the language the interface or what you already know about the learner points to, or ask in one short line before the setup." I chose Portuguese from what is known about the learner rather than asking, so the setup answer in Portuguese in T3 fits. Asking first would have added a turn.

2. Voice saved at setup vs first clip. SKILL.md says the voice is chosen "On the first clip of a course" (lesson-format.md), but the Audio field is described as the provider "with the one voice picked for the course". I saved `Audio: ElevenLabs` at setup and updated to `ElevenLabs, voice Sarah` after the first dictation.

3. Chunks with only three words. In part 1 (你好 再见 谢谢) no chunk has an open slot, so "swapping its open slot" in round 1 is not possible: "Each prompt uses one of the part's chunks, swapping its open slot". Round 1 prompts are just the three words and short combinations. Rounds 2 and 3 cannot hold "who, when or where" either: "Each prompt is a complete sentence with who, when or where". I used chains of greetings. Prompts repeat heavily.

4. Review with three words. "One prompt per new word of the previous part ... at least five and at most ten." Part 1 had three words, so five prompts reuse them; each is longer than the chunk only by being a chain of two or three greetings.

5. Ambiguous Portuguese prompts for 没关系 versus 没事. "Não tem problema" and "Tudo bem" both fit either word. I mapped "Não tem problema" to 没关系 and "Tudo bem" to 没事, but a learner could not know that. Nothing in SKILL.md says how to disambiguate two words with the same meaning, beyond the usage note under the table ("two words that translate the same way").

6. Round counter wording. "Round 2 · 3 of 5" with "the saved label for round"; the label is Bateria and the round names ("Frases úteis" for Chunks, "Ações completas", "Sequências") are my own localization. The skill does not give the learner-language names for the three rounds.

7. Last exercise and closing message. "Send one short closing message after the last exercise" and "Give brief feedback and the next question in the same message." After the last dictation I put feedback and closing in the same turn to keep strict alternation with no student turn between them.

8. Wrap-up offer and next-part offer in the same message. After part 2 I did not offer the next part ("When the session ran well under an hour") because the chat had already run both parts; I kept only the wrap-up offer. Unclear whether the session counts as "well under an hour" when the learner accepted part 2 on the spot.

9. Dictation of a part with six words uses 5 sentences, one per line, some with a comma. "Write them as separate sentences so the voice pauses between them" is satisfied only loosely by 对不起，没关系。 style items.

10. Hanzi in the Markdown table. lesson-format.md names the Codex inline-math trick for large Hanzi only "where rendering and selection are confirmed"; I used bold Hanzi.

11. Role-play replies are not translation prompts. The student policy (every fourth answer in pinyin, a slip about every third) is defined for translation prompts; I applied it loosely to the role-play replies (pinyin in two, one slip). The tutor lines carry no expected comment, since the benchmark rule covers review and rounds only.

12. Correction of a review error: "ask the learner to use the target again in a fresh prompt after another question." In Review 3 the miss was 谢谢; Review 5 reused it after Review 4. Because the review has only five prompts and three words, the "fresh prompt" repeats the same pair of words.
