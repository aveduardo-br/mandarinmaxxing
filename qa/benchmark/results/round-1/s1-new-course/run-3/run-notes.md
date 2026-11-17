# Run notes

- Scenario: s1-new-course (round 1, run 3)
- Turns: 98 (T1 to T98)
- Result: setup, route, Lesson 1 part 1, Lesson 1 part 2, wrap-up role-play. Final course.md: Next Lesson 02 part 1 of 2; To reinforce 再见, 对不起, 没关系, 没事; Done has 1-01.1 and 1-01.2.

## Unclear instructions and doubts

1. Setup language. "If there is too little text, use the language the interface or what you already know about the learner points to, or ask in one short line". The first message was English ("start mandarinmaxxing") and the setup message went out in Portuguese, based on the known learner (Brazilian). No language question was asked.
2. Parts with very few words. "Round 2 · Full actions. Each prompt is a complete sentence with who, when or where, and what happens" and "every new word appears in at least three prompts". Lesson 1 part 1 has only 3 words (你好 再见 谢谢), so rounds 1 to 3 are heavily repetitive two- and three-line exchanges. The skill allows "a short line of an exchange" but does not say how to vary rounds 2 and 3 with so few words.
3. Review size. "One prompt per new word of the previous part in the Done log, at least five and at most ten." Part 1 had 3 words, so the review used 5 prompts that repeat words; unclear whether "at least five" overrides "one per word".
4. Chunks for a 3-word part. "two to four useful chunks": 你好, 谢谢, 谢谢，再见 are barely chunks, and no breakdown applies (你 not yet known).
5. Vocabulary title in Markdown fallback. "With the Markdown fallback, the title goes in a bold line above the table." Used a bold line above the table; in part 2 the title also opened the review, so it appears twice, as the skill says ("the table's heading repeats it later").
6. To reinforce update. "remove the items the learner used correctly without help during that part, then add the new ones at the end." Unclear whether a word corrected and then answered right later in the same part (e.g. 再见 in part 1, 谢谢 omitted in part 1) counts as "new" or as resolved. Chose: any word that needed correction in the part is added; words used right in the next part's review without help (谢谢) are removed; 再见 stays because it was missed again.
7. Prompts that accept two answers. 没关系 and 没事 are both valid for "tudo bem / não foi nada". Prompts say which alternative is also valid in the expected comment; no instruction on how to design prompts so only one target fits (the skill's "valid alternative" rule only covers the feedback).
8. Closing message after part 2. "When the part was the last part of a lesson with two or more parts, ... offering the wrap-up" and "When the session ran well under an hour, an offer to start the next part now." Two short parts were done back to back, so only the wrap-up offer was sent, not the offer to start Lesson 2 part 1. Not sure whether the second offer should also apply.
9. Narration. "Use the narration only once the learner has met enough words to fill about 20 seconds." After part 2 only 9 words were met, so both listening steps were dictation only.
10. Script block in the transcript. The runner says to write the exact script in an `audio-script` block as a stand-in for the clip, and the skill says to keep the script out of the message until the learner answers. The block is included in the tutor's message in the transcript (as the runner requires), but it stands for the audio and was not meant to be read by the learner. The script was shown again with pinyin and meaning after the student answered.
11. Wrap-up role-play, learner cues. The skill does not say whether the tutor may give the learner a cue in Portuguese for what to say ("Sua vez: ..."). Cues were added because the learner knows only 9 words.
12. Student policy note. The student's mistakes were placed on answers 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 37, 40, the dictation slip was one wrong sentence each time, and every fourth answer was in pinyin.
