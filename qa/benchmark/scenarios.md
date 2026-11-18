# Benchmark scenarios

Each scenario gives the starting `course.md` (or none), the student's first message, and when to stop. The runner instructions are in `runner.md`.

## s1-new-course

- Starting `course.md`: none (empty `course/` folder).
- First message: `start mandarinmaxxing`
- Setup answer: `Começo do zero. HSK 1, ritmo 5. Quero áudio, já conectei o ElevenLabs.`
- Accept the route as shown. Teach part 1. When the tutor offers the next part, accept. Teach part 2. When the tutor offers the wrap-up role-play, accept and do it.
- Stop after the wrap-up ends.
- What it tests: setup, the shortest parts (jump start), the offer of the next part, review after part 1, dictation with very few words, the wrap-up offer at the end of Lesson 1.

## s2-rotation

- Starting `course.md`: `scenarios/s2-course.md` (25 parts done, up to Lesson 11 part 1; next is Lesson 11 part 2).
- First message: `próxima aula`
- Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: a full one-hour part with a real vocabulary, the three rounds with longer sentences, older words coming back by turn (lines 3, 7 and 14 back), the items to reinforce, dictation plus narration.

## s5-jump-ahead

- Starting `course.md`: `scenarios/s5-course.md` (Lesson 1 done; next is Lesson 2 part 1).
- First message: `quero ir para a aula 22`
- If the tutor asks whether to count the jump start's words as known, answer `pode contar como conhecidas`. If it asks what comes after Lesson 22, answer `depois volta para a aula 2`.
- Teach Lesson 22. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: the jump start question, route confirmation, and that prompts use only met words (jump start plus Lesson 22) and not words from Lessons 8 to 21.

## s6-hsk3-mid

- Starting `course.md`: `scenarios/s6-course.md` (HSK 3, Lessons 1 to 17 done, 47 parts; next is Lesson 18 part 1). The learner started at HSK 3, so HSK 1 and 2 count as met.
- First message: `próxima aula`
- Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: whether the review and the rounds rise to an intermediate level (longer sentences, HSK 1 to 3 words), older words from up to 30 parts back, natural Mandarin at HSK 3.

## s7-jump-hsk3

- Starting `course.md`: `scenarios/s7-course.md` (HSK 3, Lessons 1 to 6 done, jump start finished; next is Lesson 7 part 1).
- First message: `quero ir para a aula 30`
- If the tutor asks what comes after Lesson 30, answer `depois volta para a aula 7`.
- Teach the first part of Lesson 30. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: a jump inside a level whose jump start is done (no jump start question), a review at the course's level although the last part reviewed is from Lesson 6, and prompts with no words from Lessons 7 to 29.

## s8-hsk2-after-jump-start

- Starting `course.md`: `scenarios/s8-course.md` (HSK 2, jump start done: Lessons 1 to 4; next is Lesson 5 part 1). HSK 1 counts as met.
- First message: `próxima aula`
- Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: the first situation after a jump start that carries grammar (比, 得, 从, 着, 正, 地), HSK 1 and 2 words together, the level of the review.

## s9-hsk4-mid

- Starting `course.md`: `scenarios/s9-course.md` (HSK 4, Lessons 1 to 27 done; next is Lesson 28 part 1). HSK 1 to 3 count as met.
- First message: `próxima aula`
- Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: an upper-intermediate part with a large vocabulary, older words from 30 and 60 parts back, natural Mandarin in long sentences.

## s10-synonyms

- Starting `course.md`: `scenarios/s10-course.md` (HSK 1, up to Lesson 4 part 2; next is Lesson 4 part 3, which teaches 明天 会 中文 昨天 汉语).
- First message: `próxima aula`
- The student always prefers 中文 over 汉语 when both fit. Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests (from the ciphered-student run): prompts that hold words the answer leaves out, hints and scripts with unmet words, a neglected synonym (汉语), answers accepted without the new word.

## s11-hsk2-mid

- Starting `course.md`: `scenarios/s11-course.md` (HSK 2, Lessons 1 to 9 done, 19 parts; next is Lesson 10 part 1). HSK 1 counts as met.
- First message: `próxima aula`
- Teach the whole part. Decline anything optional.
- Stop after the tutor's closing message.
- What it tests: a full part with a real vocabulary (HSK 1 plus half of HSK 2), where natural Mandarin can be judged fairly: the level of the review, three full rounds, older words from 3, 7 and 14 parts back, items to reinforce, dictation plus narration.
