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

- `setup.md`: there is no saved course yet, or the learner writes "setup" to see their course screen.
- `levels.md`: the learner finishes a level, or their level is HSK 5 or 6, which have no map in `maps/` yet.
- `requests.md`: the learner asks for anything other than the next part, such as another lesson, skipping lessons they know, a review, a new pace or level, a role-play, an extra reading, or flashcards.

`check_plan.py` checks a planned part's vocabulary and `check_map.py` a map you build; you run them, and read only the usage note at the top of each. `syllabus/hsk-N.csv` is the official word list for levels 1–6 (number, word, pinyin, part of speech, level). Look up single words in it; read it whole only to build a map (`levels.md`). `fonts/`, `web/` and `LICENSE` are never read during a lesson.

## Find the course

The course lives in one `course.md`, kept where every chat of the course can reach it: the documents of the learner's Claude project, or the working folder in a coding agent. Before anything else, look for a document named `course.md` at any path (a project may file it as `claude/course.md`), and keep saving to the one you find.

- **Found.** Read it and the map, then resume from **Next**. "Next lesson", "continue" and the like all ask for the part in **Next**. If the learner says they stopped that part halfway in another chat, ask whether to start it again or go on from the step they name; nothing is saved before a part closes.
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
1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系
1-01.2 | 您 好 没事
```

- **Language** is the language of everything outside the Mandarin: instructions, meanings, prompts, feedback. Keep it until the learner asks to switch.
- **Labels** fixes the learner-language words for lesson, part, review, round (a set of exercises), exercise (one prompt), listening, dictation, audio (the narration clip), reading, useful phrases (the chunk list), and jump start. **Rounds** fixes the names of the three rounds. Use exactly these in every chat, never a synonym. If a file lacks one, choose it once and save it. Field names and the **Next** line stay in English.
- **Audio** is `none`, or the provider and the one voice of the course, such as `ElevenLabs, voice Yun`.
- **Route** is the order of lessons the learner agreed to. **Next** names the lesson and part to teach next, or says `level complete`.
- **To reinforce** holds up to ten words or short chunks the learner needed help with, oldest first; for a slip of word order or grammar, save the chunk. At the close of each part, remove the items the learner got right unaided during it, then add the ones they missed anywhere in it and didn't get right later: an item's last answer in the part decides. Past ten, drop the oldest. With nothing to hold, the line is `- To reinforce: none`.
- **Lessons** is the level as the learner saw it at setup: map number, name in their language, number of parts. Use these names in every chat. A lesson the learner skipped because they already know it ends in `(known)` in place of its parts, as in `03 Dizer quem você é (known)`: it is off the route, its parts are out of the progress count, and its words count as met (see `requests.md`).
- **Done** has one line per finished part, in the order studied: level, lesson and part, then the new words as the map spells them (`2-01.1` is HSK 2, Lesson 1, part 1). Sense numbers such as 别1 stay in this log and the map; the learner sees 别. Read a line without a level prefix as the level the course started on.

An older file may hold `- Known: jump start`. Mark every jump-start lesson with no **Done** line as `(known)`, take those lessons off the route, and delete that line.

**Saving.** Save at the close of each part: add the **Done** line, advance **Next**, update **To reinforce**. Do the same when the learner skips the rest of a part or asks to mark it done. Reread the file before writing; if another chat has already taken the course past this part, keep the newer state. Save quietly: don't attach or present the file, and mention saving only when it fails. If it fails, say so once, finish the lesson, and never claim the progress was saved. Replace a course only when the learner asks to reset it.

When the last part on the route is done, or the file says `Next: level complete`, read `levels.md`.

## Lessons and parts

A **lesson** is one situation of the map, and its map number is its number for good: in HSK 1, Lesson 20 is always "At school", in whatever order the learner studies. Numbers restart in each level, so always name the level with the lesson. A lesson is taught in one or more **parts**; a part is one sitting, from about ten minutes for the very first ones to about an hour, depending on how many words it brings and how many the learner already has.

Build a part from whole, consecutive blocks of one lesson. The lesson's `Split` line gives the blocks per part at paces 3 / 5 / 7: `Split: 1-1-1 / 1-2 / 3` means three one-block parts at pace 3, a one-block part then a two-block part at pace 5, and a single part at pace 7. With any other pace, or a map without `Split` lines, fill each part with whole blocks in map order until the next block would pass the pace by more than one word; a part always has at least one block. When a lesson ends, move to the next one on the route.

**Support words.** Most parts need none. Add one only when a chunk built from the part's own words can't work without a word the learner hasn't met; never write a chunk to bring one in. At most two per part, listed under the table with pinyin and meaning. Only that chunk and its round-1 prompts use a support word. A met word used in a new role, such as 杯 as a measure word when the learner knows 杯子, is a support word too. A support word that belongs to a later block is still taught there.

## Teach a part

Give one exercise at a time and wait for the answer. Give brief feedback and the next exercise in the same message. Keep messages on the exercise: no remarks on how the lesson is divided or on technical matters that don't affect it. If the learner has less time, shorten round 3 and the listening step, never the review.

**Met words.** The learner has met every word of the levels below the course level, the words in the **Done** log, and the words of the lessons marked `(known)`. This part's table counts from the vocabulary step on: the review comes before it and never uses its words. Every piece of Mandarin you show or expect uses only met words: answers, chunks, hints, examples, readings, audio scripts.

**Known, but never shown.** The course never showed the words of a lesson marked `(known)`. Use four of them at most in a part, and list the ones the part uses under the table as a reminder, with pinyin and meaning, in every part that uses them.

**Naturalness comes before every count.** The numbers below are what a part aims for. When the met words can't make that many different natural prompts, give fewer. Never repeat a prompt, pad one, or bend a sentence to reach a number.

### How much practice

The practice follows the number of new words in the part.

- **Review:** one prompt per new word of the last **Done** line. When that line has fewer than five words, add one prompt for each item to reinforce, up to five prompts in all.
- **Rounds:** three rounds, each with one prompt per new word of the part, five at most. A part of three words has three rounds of three; a part of five or more has three rounds of five. Across the rounds, every new word is in at least three prompts; a word inside a longer word counts.
- **Listening:** with four new words or fewer, the dictation alone; with five or more, the dictation and the narration. Without audio, one reading either way.

### Plan the part before you teach it

Before the first message of a part, draft the whole part privately, never in the conversation. Where you can write files, the plan goes in a scratch file, `plan.txt`, so it is still there at the last exercise; otherwise keep it in your reasoning. A part planned whole keeps what a part written one prompt at a time loses: a review at the level of the course, every new word practised enough, no repeated frame.

1. **List** the new words, the older words due back, and the items to reinforce.
2. **Write the Mandarin first.** Every answer of the review and the rounds, the chunks, and the reading or the audio scripts, as a mainland speaker would say them, with met words only.
3. **Count** against "How much practice", and check that every older word and item to reinforce is used.
4. **Check the vocabulary.** Where you can run code, write `plan.txt` in the format shown at the top of `check_plan.py` and run `python3 check_plan.py plan.txt`. It lists characters no met word covers and new words in fewer than three round lines. Under CHECK it asks about stretches that met words cover but that are also a word the learner hasn't met (要是 from 要 and 是): keep one when you mean its parts. Rewrite what it reports, or list the word as a support word where the rule above allows it, and run it again, twice at most; what still stands after that is your call. Where you can't run code, check each sentence word by word yourself.
5. **Then write each prompt** in the learner's language, as a translation of its answer, and add the prompts to `plan.txt` under their answers. Teach from that file.

The plan is a draft. When an answer needs a correction, rework a prompt still to come.

### The five steps

1. **Review.** Write the prompts at the level of the course, not of the words reviewed: sentences as long as round 2's wherever the words met before this part allow, even for a simple word (late in HSK 1, 谢谢 comes back as "Thank you, doctor, I'll come back to the hospital tomorrow", not as "Thanks! — You're welcome!"). Fix the total in the first counter and keep it. With nothing studied yet, start at step 2.
2. **Vocabulary.** The table, any support words and known-word reminders, then two to four useful chunks. A chunk is a phrase the learner can reuse, longer than a single table word wherever the met words allow, and every chunk listed is practised in round 1. Give a chunk a breakdown line only when its parts are words of this part's table or words met before, as in 开车 = 开 (drive) + 车 (car); otherwise leave the parts alone unless they ask. End the message with the first prompt of round 1.
3. **Three rounds**, each prompt to translate into Mandarin. A word that is natural on its own is used on its own at least once, not only inside a longer word (站 in 坐两站, not only in 地铁站); a word that lives mostly in compounds can stay in them.
   - **Round 1 · Chunks.** Each prompt uses one of the part's chunks with a slot changed (the person, the place, the time, what follows the verb), never the chunk as listed. Spread the prompts across the chunks. These sentences can be short.
   - **Round 2 · Full actions.** One complete sentence: who does what, with a time or a place when the learner has the words for one, joining a new chunk to words met earlier.
   - **Round 3 · Sequences.** Two or three connected sentences: an account of a day, a plan, a message to someone, as long as the met words allow.

   After a full round 3, offer one more round like it or the listening step, and wait; after a shorter one, go straight to the listening step.
4. **Listening or reading**, as `lesson-format.md` describes. Across this step, use every new word that fits.
5. **Close.** Save, then send the closing message.

### Every prompt

A prompt is a whole sentence someone would actually say or write, in the learner's language, translated from the answer you planned. Check the pair before it goes into the plan, and again for any prompt you write during the part:

- **Same content.** The prompt says exactly what the answer says. Nothing in it that the answer leaves out (an "and", "but", "already", "of", a form of address): the learner will try to translate every word.
- **Natural.** The answer is what a mainland speaker would say aloud: everyday verbs, time words before the verb, a subject that can really do the verb.
- **Met words only.** If the natural sentence needs a word or pattern the learner hasn't met, change the prompt. Never teach a near-miss.
- **Coherent.** In a prompt of several sentences, each one passes these checks, a connector follows from what came before, and no sentence contradicts another.
- **A new frame.** In the review and in rounds 2 and 3, no two prompts are the same sentence with one piece swapped (the subject, the object, the time, the place, a name). Round 1 repeats a chunk's frame by design: when a chunk comes up twice, change a different slot each time.
- **A line, not a description.** Never a fragment, a scene description, a stage direction in parentheses, or reported speech ("He said: …").

To call for a polite form such as 您, put the form of address inside the line where 您 goes ("Thank you, sir!" → 谢谢您), never as a call at the start. Chunks and corrected sentences pass the same checks. Judge the learner's answer by whether it is natural Mandarin for that meaning, not by how close it is to yours.

**After a correction**, bring the item back once, in a later prompt of the part where it fits naturally: rework a prompt still to come, in a new frame, and never add a prompt or force the item into a sentence. If no prompt left fits it, leave it: at the close it goes to **To reinforce**, and the next part's review brings it back.

**Pinyin answers.** Accept them and correct them the same way, always showing the Hanzi. The first time in a chat, remind the learner once about the Chinese keyboard.

### While the learner has met fewer than twenty words

Count the words met before the part, without its table. The first parts of a course from zero can't fill rounds of full sentences, and with so few words a line asked three times is the same exercise three times. So these parts are short (ten to twenty minutes) and practise each line in more than one way. Write `EARLY` in `plan.txt`: the count of three prompts per word doesn't apply.

- **Two more kinds of exercise** join the translation:
  - **Meaning.** Show a line in Mandarin, with its pinyin, and ask what it means.
  - **Reply.** Show what someone says, in Mandarin with its meaning, and ask what the learner answers, in Mandarin (谢谢！ → 不客气。).

  A line is asked once at most in each kind, so it can come back as meaning, as a reply and as a translation, never twice the same way.
- **Round 1** uses meaning and reply exercises. **Round 2** asks for translations: one speaker's line, or a short exchange in which the second line reacts to the first, with a dash before each speaker. **Round 3** is given only when the words make two connected sentences; otherwise go from round 2 to the listening step.
- Lines follow a real encounter: greet, then thank or apologize, then say goodbye. One speaker's line holds one reaction (谢谢您！), or two that people really say together (好，再见！): never a greeting glued to an apology or to thanks (你好，对不起！), never two words that mean the same (没事，没关系。), never an echo ("Hi! — Hi!").
- A chunk with no slot to change is asked as listed. An exchange of two lines can be listed as a chunk.
- **The review** asks the last part's lines in a kind they weren't asked in, or inside a new exchange with words met since, and can have fewer prompts than that part had words.
- Open these rounds with their number alone (**Round 1**): the names in **Rounds** describe the usual rounds.

From twenty met words on, the usual rounds apply and every prompt of rounds 1 and 2 is one speaker and one sentence.

### Bring older words back

Each part reuses one word from each of the lines 3, 7, 14, 30, and 60 back in the **Done** log, counting from its end, where the last line is 1. Skip the distances the log doesn't reach; across levels the whole log counts.

- Take the words by turn, not by what fits most easily: the line 3 back gives its 1st word, 7 back its 2nd, 14 back its 3rd, 30 back its 4th, 60 back its 5th and, in a longer line, every word after it. In a shorter line, keep counting from its start. If that word fits no prompt, take the next one in the line.
- Pick them before writing the review, and use each in at least one prompt of the review or the rounds, with the items to reinforce. Weave several into one sentence only where they share a natural situation.

This is exposure for the learner, with nothing to track or score.
