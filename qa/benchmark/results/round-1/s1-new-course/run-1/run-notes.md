# Run notes

Scenario: s1-new-course (round 1, run 1)
Turns: 100 (T1 to T100)
Final state: course/course.md has Done lines 1-01.1 and 1-01.2, Next: Lesson 02, part 1 of 2, To reinforce: 没事, Audio: ElevenLabs, voice Sarah.

## Unclear or ambiguous instructions

1. Language choice with a bare first message.
   SKILL.md: "If there is too little text, use the language the interface or what you already know about the learner points to, or ask in one short line before the setup."
   The first message was only "start mandarinmaxxing". The tutor knows nothing about the learner (the student policy is hidden), so it asked one short line (T2) and the student answered "Português." (T3). This adds a turn before the setup that scenarios.md does not list. If the benchmark expects the setup message on T2, the tutor would need some other signal.

2. Audio script block versus "keep the script out of the message".
   runner.md: "write a line [AUDIO CLIP] followed by the exact script in a fenced block ... Follow the rules on when the script may be shown." lesson-format.md: "Keep the script out of the message. Share it with pinyin and a translation only after the learner answers".
   Treated the audio-script block as the stand-in for the clip itself (a tool call), and showed pinyin and translation only after the learner's answer.

3. Review counter when a correction needs a fresh prompt.
   SKILL.md: "If an answer needs a hint or correction, ask the learner to use the target again in a fresh prompt after another question." and lesson-format.md: "the counter counts the whole review".
   The review had 5 planned prompts for 3 words. After the miss at review 3, the fresh re-ask took the place of the planned 5th prompt (the total stayed 5). It is unclear whether the total may grow instead.

4. "To reinforce" bookkeeping.
   SKILL.md: "remove the items the learner used correctly without help during that part, then add the new ones at the end. An item stays until it is answered right".
   Unclear whether an item missed and then answered correctly later in the same part is saved at all. Decision: an item missed in a part is saved only if it was not answered right again afterwards in that part; items on the list are removed when used correctly in the next part. For a word-order slip the stretch was saved ("你好，你好！谢谢！").

5. "When the session ran well under an hour" at the end of part 2.
   lesson-format.md: "When the session ran well under an hour, an offer to start the next part now."
   After part 1 (3 words, no review) the tutor offered the next part. After part 2, two short jump-start parts back to back made roughly an hour, so only the wrap-up offer was made. No rule says whether to count the session or the part.

6. Round prompts with only 3 to 9 known words.
   SKILL.md: round 2 "complete sentence with who, when or where, and what happens" and round 3 "two or three connected sentences". With only greetings known, prompts are strings of exchange lines (for example "Oi! Obrigado! Tchau, tchau!"). Followed "a short line of an exchange is a whole sentence", but repeated words (tchau, tchau) were needed to reach three prompts per word.

7. Formal "您" prompt in Portuguese.
   A Portuguese prompt cannot force 您好 over 你好. Added a parenthetical hint ("a uma pessoa mais velha, com respeito") and accepted 你好 as a valid alternative, naming 您好 as the chunk wanted. Unclear whether parenthetical hints are allowed in prompts ("Every prompt is a whole sentence someone would actually say").

8. Chunk list with single-word chunks.
   Part 1 has three words and no slot to swap, so the chunks are the words themselves plus one combination. "Round 1 ... swapping its open slot" could not be applied.

9. Role-play format.
   SKILL.md says to play the other person "with the meaning under each line" and "Correct each reply with the written-translation format". Used the three-line Mandarin pattern (Hanzi, pinyin, meaning) for each tutor line and added one scene sentence before each line so the student knows what is happening, since no instruction says whether scene cues are allowed.

10. Closing message ordering with the wrap-up.
   lesson-format.md lists "what comes next" first, then the wrap-up offer. Did that, and the closing was merged into the feedback message of the last exercise (no further learner input to wait for).
