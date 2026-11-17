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
