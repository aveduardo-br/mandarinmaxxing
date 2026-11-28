---
name: mandarinmaxxing
description: Teach HSK 3.0 Mandarin vocabulary reorganized around everyday situations, with jump-start lessons, reusable chunks, written translation, built-in review, and guided listening. Use when the learner wants to start or resume a mandarinmaxxing course, asks for the next lesson, or asks to review a lesson.
license: mandarinmaxxing License, version 1. Free to study with; not for reuse in other products. Complete terms in LICENSE.
---

# mandarinmaxxing

Teach the official HSK vocabulary in an order built for conversation. Each level's words are grouped into everyday situations; each situation is one lesson, taught in short parts. Teach chunks the learner can reuse, such as a phrase for ordering a drink with a word they can swap. Use simplified Chinese, with tone-marked pinyin as a written reference. Correct the written answer and comprehension; pronunciation and tones are the learner's own practice.

The skill guides the lessons. Long-term memorization stays with the learner's own tools, such as flashcards. Say so plainly if they ask.

## Files

In every chat that teaches a part:

- Run `python3 course.py part <course.md> plan.txt`, giving each file its full path (the scripts sit in this skill's folder). It does the course's bookkeeping and prints the **brief** of the part: its new words, what the review covers, older words to bring back, how many exercises each step has, and what to save at the close. If the chat holds `course.md` as a project document and not as a file where code runs, save a copy first and pass the copy. When the script stops with a message about the file, fix what it names in `course.md` and run it again.
- If the chat can't run code, say that the skill needs code execution turned on, and offer the trial lesson of `setup.md` meanwhile: without the script there is no course to keep.
- Read `lesson-format.md` before the first lesson message: the vocabulary table and the format of every lesson message.

Read only when the moment comes:

- `setup.md`: there is no saved course yet, or the learner writes "setup" to see their course screen.
- `first-parts.md`: the brief says the part is an early one.
- `audio.md`: **Audio** in the course file names a provider.
- `levels.md`: the learner finishes a level.
- `requests.md`: the learner asks for anything other than the next part, such as another lesson, skipping lessons they know, a review, a new pace or level, a role-play, an extra reading, or flashcards.

`check_plan.py` checks a planned part's vocabulary. `syllabus/hsk-N.csv` is the official word list for levels 1–6 (number, word, pinyin, part of speech, level): look up single words in it, never read it whole. You don't need to read `maps/`: `course.py` reads them for you. `fonts/`, `web/` and `LICENSE` are never read during a lesson.

## Find the course

The course lives in one `course.md`, kept where every chat of the course can reach it: the documents of the learner's Claude project, or the working folder in a coding agent. Before anything else, look for a document named `course.md` at any path (a project may file it as `claude/course.md`), and keep saving to the one you find.

- **Found.** Read it, then teach the part in **Next**. "Next lesson", "continue" and the like all ask for that part. If the learner says they stopped it halfway in another chat, ask whether to start it again or go on from the step they name; nothing is saved before a part closes.
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
03 Dizer quem você é (known)
…one line for every lesson of the level

## Done
1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系
1-01.2 | 您 好 没事
```

- **Pace** is 3, 5 or 7.
- **Language** is the language of everything outside the Mandarin: instructions, meanings, prompts, feedback. Keep it until the learner asks to switch.
- **Labels** fixes the learner-language words, in this order, for lesson, part, review, round, exercise, listening, dictation, audio (the narration clip), reading, useful phrases (the chunk list), and jump start. **Rounds** fixes the names of the three rounds. Use exactly these in every chat, never a synonym. If a file lacks one, choose it once and save it. Field names and the **Next** line stay in English.
- **Audio** is `none`, or the provider and the one voice of the course, such as `ElevenLabs, voice Yun`.
- **Route** is the order of lessons the learner agreed to. **Next** names the lesson and part to teach next, or says `level complete`.
- **To reinforce** holds words or short chunks the learner still gets wrong: five at most, separated by commas, or `none`. For a slip of word order or grammar, save the short chunk as it should be said. Each review asks every item once. At the close, take out the items the learner got right unaided in this part's review, and add what they got wrong in this part and didn't get right later in it. Past five, the oldest leaves.
- **Lessons** is the level as the learner saw it at setup: map number, name in their language, number of parts. Use these names in every chat. A lesson the learner skipped because they already know it ends in `(known)` in place of its parts: it is off the route, out of the progress count, and its words count as met (see `requests.md`).
- **Done** has one line per finished part, in the order studied: level, lesson and part, then the new words as the map spells them. Sense numbers such as 别1 stay in this log; the learner sees 别.

**Saving.** Save at the close of each part: add the **Done** line and set the **Next** the brief gives, and update **To reinforce**. The first time in a course, read the saved document again to confirm the new line is there. Do the same when the learner skips the rest of a part or asks to mark it done. Reread the file before writing; if another chat has already taken the course past this part, keep the newer state. Save quietly: don't attach or present the file, and mention saving only when it fails. If it fails, say so once, finish the lesson, and never claim the progress was saved. Replace a course only when the learner asks to reset it.

When the last part on the route is done, or the file says `Next: level complete`, read `levels.md`.

## Lessons and parts

A **lesson** is one situation of the map, and its map number is its number for good: in HSK 1, Lesson 20 is always "At school", in whatever order the learner studies. Numbers restart in each level, so always name the level with the lesson. A lesson is taught in one or more **parts**. A part is one sitting: about ten minutes for the very first ones, up to about an hour later on. The brief says which words a part brings, in the blocks of words that work together.

## Teach a part

Give one exercise at a time and wait for the answer. Give brief feedback and the next exercise in the same message. Keep messages on the exercise: no remarks on how the lesson is divided or on technical matters that don't affect it. If the learner has less time, shorten round 3 and the listening step, never the review.

**Met words.** The learner has met every word of the levels below the course level, the words in the **Done** log, and the words of the lessons marked `(known)`. This part's table counts from the vocabulary step on: the review comes before it and never uses its words. Every piece of Mandarin you show or expect uses only met words: answers, chunks, hints, examples, readings, audio scripts.

**One or two extra words.** When a natural chunk needs a word the learner hasn't met, such as a measure word, you may add it: two at most in a part, listed under the table with pinyin and meaning, and used only in that chunk's prompts. Put them on a `SUPPORT` line of the plan.

**Naturalness comes before every count.** The brief's numbers are what a part aims for. When the met words can't make that many different natural prompts, give fewer. Never repeat a prompt, pad one, or bend a sentence to reach a number or to fit in a word.

### Plan the part before you teach it

Before the first message of a part, draft the whole part privately, never in the conversation, in the `plan.txt` the brief started. A part planned whole keeps what a part written one prompt at a time loses: a review at the level of the course, every new word practised enough, no repeated frame.

1. **Write the Mandarin first**, one sentence or text per line under `PLAN`, labelled `review:`, `round1:`, `round2:`, `round3:`, `chunk:` or `listening:`. Every answer of the review and the rounds, the chunks, and the reading or the audio scripts, as a mainland speaker would say them.
2. **Run `python3 check_plan.py plan.txt`.** It fails on characters no met word covers, new words in fewer than three round lines, a round with no line, and a repeated sentence. Rewrite what it reports and run it again, twice at most; what still stands after that is your call. What it prints under CHECK is advice: a stretch that is also a word the learner hasn't met (要是 from 要 and 是), a met word with another reading taught later, a new word never used on its own. It can't tell which sense of a word a sentence uses, nor whether the sentence is natural: that stays with you.
3. **Then write each prompt** in the learner's language, as a translation of its answer, on a line under the answer that starts with `prompt:`. Teach from that file.

The plan is a draft. When an answer needs a correction, rework a prompt still to come.

### The five steps

1. **Review**, as the brief lists it. Write the prompts at the level of the course, not of the words reviewed: full sentences built from everything met before this part, even for a simple word (late in HSK 1, 谢谢 comes back as "Thank you, doctor, I'll come back to the hospital tomorrow", not as "Thanks! — You're welcome!"). Fix the total in the first counter and keep it.
2. **Vocabulary.** The table, any extra words, a reminder line for the words of `(known)` lessons this part uses (pinyin and meaning: the course never showed them), then two to four useful chunks, no more than round 1 has prompts. A chunk is a phrase the learner can reuse, longer than a single table word wherever the met words allow, and every chunk listed is practised in round 1. Give a chunk a breakdown line only when its parts are words of this part's table or words met before, as in 开车 = 开 (drive) + 车 (car). End the message with the first prompt of round 1.
3. **Three rounds**, each prompt to translate into Mandarin, as many as the brief says. A part of two or three words can have more prompts a round, up to five, when its words have that many really different contexts. A word that is natural on its own is used on its own at least once, not only inside a longer word (站 in 坐两站, not only in 地铁站).
   - **Round 1 · Chunks.** Each prompt uses one of the part's chunks with a slot changed (the person, the place, the time, what follows the verb), never the chunk as listed. Spread the prompts across the chunks. These sentences can be short.
   - **Round 2 · Full actions.** One complete sentence: who does what, with a time or a place when the learner has the words for one, joining a new chunk to words met earlier.
   - **Round 3 · Sequences.** Two or three connected sentences: an account of a day, a plan, a message to someone, as long as the met words allow.

   After a full round 3, offer one more round like it or the listening step, and wait.
4. **Listening or reading**, as `audio.md` or `lesson-format.md` describes. Across this step, use every new word that fits.
5. **Close.** Save, then send the closing message.

**Older words.** The brief lists older words to bring back, two candidates from each of a few earlier parts. Use one from each line in the review or the rounds, the one that fits a sentence naturally; skip a line when neither fits. It is exposure for the learner, with nothing to track.

### Every prompt

A prompt is a whole sentence someone would actually say or write, in the learner's language, translated from the answer you planned. Check the pair before it goes into the plan, and again for any prompt you write during the part:

- **Same content.** The prompt says exactly what the answer says. Nothing in it that the answer leaves out (an "and", "but", "already", "of", a form of address): the learner will try to translate every word.
- **Natural.** The answer is what a mainland speaker would say aloud: everyday verbs, time words before the verb, a subject that can really do the verb.
- **Met words only.** If the natural sentence needs a word or pattern the learner hasn't met, change the prompt. Never teach a near-miss.
- **Coherent.** In a prompt of several sentences, each one passes these checks, a connector follows from what came before, and no sentence contradicts another.
- **A new frame.** In the review and in rounds 2 and 3, no two prompts are the same sentence with one piece swapped (the subject, the object, the time, the place, a name). Round 1 repeats a chunk's frame by design: when a chunk comes up twice, change a different slot each time.
- **A line, not a description.** Never a fragment, a scene description, a stage direction in parentheses, or reported speech ("He said: …").

To call for a polite form such as 您, use the polite pronoun or put the form of address inside the line where 您 goes ("Thank you, sir!" → 谢谢您), never as a call at the start. Chunks and corrected sentences pass the same checks. Judge the learner's answer by whether it is natural Mandarin for that meaning, not by how close it is to yours.

**After a correction**, bring the item back once, in a later prompt of the part where it fits naturally: rework a prompt still to come, in a new frame, and never add a prompt or force the item into a sentence. If no prompt left fits it, leave it: at the close it goes to **To reinforce**, and the next part's review brings it back.

**Pinyin answers.** Accept them and correct them the same way, always showing the Hanzi. The first time in a chat, remind the learner once about the Chinese keyboard.
