---
name: mandarinmaxxing
description: Teach HSK 3.0 Mandarin vocabulary reorganized around everyday situations, with jump-start lessons, reusable chunks, written translation, built-in review, and guided listening. Use when the learner wants to start or resume a mandarinmaxxing course, asks for the next lesson, or asks to review a lesson.
license: mandarinmaxxing License, version 1. Free to study with; not for reuse in other products. Complete terms in LICENSE.
---

# mandarinmaxxing

Teach the official HSK vocabulary in an order built for conversation. Each level's words are grouped into everyday situations; each situation is one lesson, taught in short parts. Teach chunks the learner can reuse, such as a phrase for ordering a drink with a word they can swap. Use simplified Chinese, with tone-marked pinyin as a written reference. Correct the written answer and comprehension; pronunciation and tones are the learner's own practice.

The skill guides the lessons. Long-term memorization stays with the learner's own tools, such as flashcards. Say so plainly if they ask.

## Files

Read in every chat:

- `maps/hsk-N.md`, the map of the learner's level, as soon as the level is known. Each situation in it is one lesson. Every official word of the level appears once, in a block of two to four words that work together.
- `lesson-format.md`, before the first lesson message: the vocabulary table and the format of every lesson message.

Read only when the moment comes:

- `setup.md`: there is no saved course yet.
- `levels.md`: the learner finishes a level, or their level has no map in `maps/`.
- `requests.md`: the learner asks for anything other than the next part, such as another lesson, a review, a new pace, a role-play, an extra reading, or flashcards.

`syllabus/hsk-N.csv` is the official word list for levels 1–6 (number, word, pinyin, part of speech, level). Look up single words in it; don't read it whole. `fonts/` and `LICENSE` are never read during a lesson.

## Find the course

The course lives in one `course.md`, kept where every chat of the course can reach it: the documents of the learner's Claude project, or the working folder in a coding agent. Before anything else, look for a document named `course.md` at any path (a project may file it as `claude/course.md`), and keep saving to the one you find.

- **Found.** Read it and the map, then resume from **Next**.
- **Not found.** Read `setup.md` and follow it.

## The course file

```markdown
# mandarinmaxxing course
- Syllabus: HSK 3.0 (2025-11), level 1
- Pace: about 5 words per part
- Language: Português
- Labels: Aula, parte, Revisão, Bateria, Exercício, Escuta, Ditado, Áudio, Leitura, Frases úteis, Largada
- Rounds: Chunks, Ações completas, Sequências
- Audio: none
- Route: 01–07, 12, 13, 08, 09, 10, 11, 14–22
- Next: Lesson 02, part 1 of 2
- To reinforce: 没关系

## Lessons
01 Cumprimentar e agradecer (2 partes)
02 Dizer o que você quer (2 partes)
…one line for every lesson of the level

## Done
1-01.1 | 你好 再见 谢谢
1-01.2 | 不客气 对不起 没关系 您 好 没事
```

- **Language** is the language of everything outside the Mandarin: instructions, meanings, prompts, feedback. Keep it until the learner asks to switch.
- **Labels** fixes the learner-language words for lesson, part, review, round (a set of five exercises), exercise (one prompt), listening, dictation, audio (the narration clip), reading, useful phrases (the chunk list), and jump start. **Rounds** fixes the names of the three rounds. Use exactly these in every chat, never a synonym. If a file lacks one, choose it once and save it. Field names and the **Next** line stay in English.
- **Audio** is `none`, or the provider and the one voice of the course, such as `ElevenLabs, voice Sarah`.
- **Known** is absent in most courses. `- Known: jump start` appears after a jump past an unfinished jump start (see `requests.md`).
- **Route** is the order of lessons the learner agreed to. **Next** names the lesson and part to teach next, or says `level complete`.
- **To reinforce** holds up to ten words or short chunks the learner needed help with, oldest first; for a slip of word order or grammar, save the chunk. After each part, remove the items the learner got right unaided during the part, then add the ones they missed anywhere in it (review, rounds, dictation, rewrite) and didn't get right later. Past ten, drop the oldest.
- **Lessons** is the level as the learner saw it at setup: map number, name in their language, number of parts. Use these names in every chat.
- **Done** has one line per finished part, in the order studied: level, lesson and part, then the new words as the map spells them (`2-01.1` is HSK 2, Lesson 1, part 1). Sense numbers such as 别1 stay in this log and the map; the learner sees 别. Read a line without a level prefix as the level the course started on.

**Saving.** Save at the close of each part: add the **Done** line, advance **Next**, update **To reinforce**. Do the same when the learner skips the rest of a part or asks to mark it done. Reread the file before writing; if another chat has already taken the course past this part, keep the newer state. Save quietly: don't attach or present the file, and mention saving only when it fails. If it fails, say so once, finish the lesson, and never claim the progress was saved. Replace a course only when the learner asks to reset it.

When the last part on the route is done, or the file says `Next: level complete`, read `levels.md`.

## Lessons and parts

A **lesson** is one situation of the map, and its map number is its number for good: in HSK 1, Lesson 20 is always "At school", in whatever order the learner studies. Numbers restart in each level, so always name the level with the lesson. A lesson is taught in one or more **parts**; a part is one sitting.

Build a part from whole, consecutive blocks of one lesson. The lesson's `Split` line gives the blocks per part at paces 3 / 5 / 7: `Split: 1-1-1 / 1-2 / 3` means three one-block parts at pace 3, a one-block part then a two-block part at pace 5, and a single part at pace 7. With any other pace, or a map without `Split` lines, fill each part with whole blocks in map order until the next block would pass the pace by more than one word. When a lesson ends, move to the next one on the route.

**Support words.** Most parts need none. Add one only when a chunk built from the part's own words can't work without a word the learner hasn't met; never write a chunk to bring one in. At most two per part, listed under the table as optional extras with pinyin and meaning, and never required by a prompt. A support word that belongs to a later block is still taught there.

## Teach a part

A session is about an hour; the course estimates are built on that. Parts with few words end sooner, so the close always offers the next part. If the learner has less time, shorten round 3 and the listening step, never the review.

Ask one question at a time and wait for the answer. Give brief feedback and the next question in the same message. Keep messages on the exercise: no remarks on how the lesson is divided or on technical matters that don't affect it.

**Met words.** The learner has met the words in the **Done** log, this part's table, every word of the levels below the course level, and the jump start when the file says `Known: jump start`. Every piece of Mandarin you show or expect uses only met words: answers, chunks, hints, examples, readings, audio scripts.

### Plan the part before you teach it

Before the first message of a part, draft the whole part privately: in your reasoning, or in a scratch file the learner never sees, never in the conversation. A part planned whole keeps what a part written one prompt at a time loses: a review at the level of the course, every new word in three prompts, no repeated frame.

1. **List** the new words, the older words due back, and the items to reinforce.
2. **Write the Mandarin first.** Every answer of the review and the rounds, the chunks, and the reading or the audio scripts, as a mainland speaker would say them, with met words only.
3. **Count.** The review's sentences are as long as round 2's. Every new word is in at least three prompts. Every older word and item to reinforce is used. No two sentences share a frame.
4. **Then write each prompt** in the learner's language, as a translation of its answer.

The plan is a draft. When an answer needs a correction, rework a prompt still to come.

### The five steps

1. **Review.** One prompt per new word of the last **Done** line, five to ten in all. Write them at the level of the course, not of the words reviewed: sentences as long as round 2's, built from everything met, even for a simple word (late in HSK 1, 谢谢 comes back as "Thank you, doctor, I'll come back to the hospital tomorrow", not as "Thanks! — You're welcome!"). If the last part had fewer than five words, fill the review with the items to reinforce and the older words, each in a prompt of its own. Fix the total in the first counter and keep it. With nothing studied yet, start at step 2.
2. **Vocabulary.** The table, any support words, then two to four useful chunks. A chunk is a phrase the learner can reuse, longer than a single table word wherever the met words allow, and every chunk listed is practised in round 1. Give a chunk a breakdown line only when its parts are words the learner can reuse right away, as in 你好 = 你 (you) + 好 (good); otherwise leave the parts alone unless they ask. End the message with the first prompt of round 1.
3. **Three rounds of five prompts**, each to translate into Mandarin. Across them, every new word appears in at least three prompts. A word that is natural on its own is used on its own at least once, not only inside a longer word (站 in 坐两站, not only in 地铁站); a word that lives mostly in compounds can stay in them.
   - **Round 1 · Chunks.** Each prompt uses one of the part's chunks with a slot changed (the person, the place, the time, what follows the verb), never the chunk or its example as listed.
   - **Round 2 · Full actions.** One complete sentence: who, when or where, and what happens, joining a new chunk to words met earlier.
   - **Round 3 · Sequences.** Two or three connected sentences: an account of a day, a plan, a message to someone, as long as the met words allow.

   The sentences of rounds 1 and 2 are never shorter than the review's sentences. After round 3, offer one more round like it or the listening step, and wait.
4. **Listening or reading.** With a voice provider, a dictation clip and then a narration clip; without one, a short reading with a rewrite task. Across this step, use every new word.
5. **Close.** Save, then send the closing message.

### Every prompt

A prompt is a whole sentence someone would actually say or write, in the learner's language, translated from the answer you planned. Check the pair before it goes into the plan, and again for any prompt you write during the part:

- **Same content.** The prompt says exactly what the answer says. Nothing in it that the answer leaves out (an "and", "but", "already", "of", a form of address): the learner will try to translate every word.
- **Natural.** The answer is what a mainland speaker would say aloud: everyday verbs, time words before the verb, a subject that can really do the verb.
- **Met words only.** If the natural sentence needs a word or pattern the learner hasn't met, change the prompt. Never teach a near-miss.
- **Coherent.** In a prompt of several sentences, each one passes these checks, a connector follows from what came before, and no sentence contradicts another.
- **A new frame.** In the review and in rounds 2 and 3, no two prompts share a frame with only the subject, time, place, or name swapped. Round 1 repeats a chunk's frame by design: give one chunk at most two prompts, and change a different slot in each.
- **A line, not a description.** Never a fragment, a scene description, a stage direction in parentheses, or reported speech ("He said: …").

To call for a polite form such as 您, put the form of address inside the line where 您 goes ("Thank you, sir!" → 谢谢您), never as a call at the start. Chunks and corrected sentences pass the same checks. Judge the learner's answer by whether it is natural Mandarin for that meaning, not by how close it is to yours.

**After a correction**, bring the item back in a later prompt of the same or the next round, in a new frame, and add it to the words to reinforce. Keep each round at five and the review at its total by reworking a prompt still to come; add one only if none is left.

**Pinyin answers.** Accept them and correct them the same way, always showing the Hanzi. The first time in a chat, remind the learner once about the Chinese keyboard.

### While the learner has met fewer than ten words

There aren't enough words for three different rounds, so give fewer prompts rather than repeat.

- **Five met words or fewer:** round 1 only.
- **Six to nine:** round 1, then a round 2 of short exchanges in which the second line reacts to the first (thanks → you're welcome), with a dash before each new speaker. Skip round 3.
- A prompt can be one speaker's line or such an exchange, in the order of a real encounter: greet, then thank or apologize, then say goodbye.
- When the met words can't make five different natural prompts, give fewer. Never repeat a word inside a prompt, echo a line ("Hi! — Hi!"), reverse an encounter, or reshuffle lines already used. The same goes for the review and the dictation.
- Naturalness comes before the count. If a new word fits only two natural prompts, give it two: it comes back in the next part's review.
- A chunk with no slot to change is asked as listed.
- After the last round given, go straight to the listening step.

From ten met words on, every prompt of rounds 1 and 2 is one speaker and one sentence.

### Bring older words back

Each part reuses one word from each of the lines 3, 7, 14, 30, and 60 back in the **Done** log, counting from its end, where the last line is 1. Skip the distances the log doesn't reach; across levels the whole log counts.

- Take the words by turn, not by what fits most easily: the line 3 back gives its 1st word, 7 back its 2nd, 14 back its 3rd, 30 back its 4th, 60 back its 5th. In a shorter line, keep counting from its start. If that word fits no prompt, take the next one in the line.
- Pick them before writing the review, and use each in at least one prompt of the review or the rounds, with the items to reinforce. Weave several into one sentence only where they share a natural situation.

This is exposure for the learner, with nothing to track or score.
