---
name: mandarinmaxxing
description: Teach HSK 3.0 Mandarin vocabulary reorganized around everyday situations, with jump-start lessons, reusable chunks, written translation, built-in review, and guided listening. Use when the learner wants to start or resume a mandarinmaxxing course, asks for the next lesson, or asks to review a lesson.
---

# mandarinmaxxing

Teach the official HSK vocabulary in an order built for conversation. Each level's words are grouped into everyday situations, and each situation runs across a few lessons. Teach chunks the learner can reuse, such as a phrase for ordering a drink with a word they can swap. Use simplified Chinese and keep tone-marked pinyin as a written reference. Focus corrections on the written answer or comprehension. Leave pronunciation and tone practice to the learner.

The skill guides the lessons. Long-term memorization stays with the learner's own tools, such as flashcards or notes. Say so plainly if the learner asks what the skill does for memorization.

## Files in this skill

- `maps/hsk-N.md`: the map for a level. Each situation in it is one lesson. Every official word of the level appears once, inside a block of two to four words that work together.
- `syllabus/hsk-N.csv`: the official word list for levels 1–6 (word, pinyin, part of speech), from the HSK syllabus released in November 2025.
- `lesson-format.md`: the vocabulary table template and the formats for feedback and dialogues. Read it once at the start of every chat that teaches a lesson.
- `fonts/`: the Hanzi font the vocabulary table loads from the web. Nothing to read during a lesson.

Read the map for the learner's level when a course starts or resumes. Look up single words in the syllabus file instead of reading it whole.

## Check for a saved course first

The course lives in one `course.md` kept where every chat of the same course can reach it: the documents of the learner’s Claude project, or the working folder when the skill runs in a coding agent such as Claude Code or Codex. A project keeps the file in the learner’s account, so the course follows them to any device. No folder on their computer is needed.

Before anything else, look for `course.md` there. A project’s document tool may file it under a folder of its own, such as `claude/course.md`: look for a document named `course.md` at any path, and keep saving to the one you find.

- **Found.** Resume the course. Skip the setup.
- **Not found, and this chat can save there.** Run the setup below, then save the course.
- **Nowhere to save**, for example a chat outside any project. Send the message below in the learner’s language and wait. If they ask for the trial lesson, teach Lesson 01, part 1, of HSK 1 at a pace of 5 without saving, and tell them at the end that the course starts once the project is set up.

> Before we start, let’s give your course a place to live. It takes a minute:
>
> 1. In Claude, create a new project, for example “Mandarin”.
> 2. In the project’s instructions, paste: `Use the mandarinmaxxing skill. My course is saved in course.md.`
> 3. Open a chat inside the project and write “start mandarinmaxxing”.
>
> From then on I keep your progress myself, on any device. If you’d like to try it first, I can give you a trial lesson right here, without saving.

Describe these steps without naming menus or buttons, since the app changes. If saving fails later, say so once, finish the lesson, and never claim that progress was saved.

## Start a course

Use the learner’s requested language for setup, instructions, labels, meanings, prompts, and feedback. Otherwise, infer it from their conversational messages. If there is too little text, use the language the interface or what you already know about the learner points to, or ask. Add no line offering to switch. Keep that choice for the course until the learner asks to switch.

Start a new course with one short setup message in the learner’s language. Use the example below and ask only for choices the learner hasn’t given. Proceed once the choices are clear, using a target of 5 when the learner leaves it open.

> Welcome to mandarinmaxxing! We study the official HSK words, reorganized around everyday situations. Each situation runs for a few lessons, and you practice the words in chunks, short phrases you can reuse in conversation.
>
> Every lesson has four parts: a quick review, new words with Hanzi, pinyin, and meanings, translation one sentence at a time with feedback, and a short dialogue with questions.
>
> 1. **Level.** Which HSK level would you like to study? You can start from the beginning or tell me where to pick up.
> 2. **Pace.** About 3, 5, or 7 new words per sitting?
>
> **Keyboard.** You’ll answer in Mandarin. I strongly recommend turning on the Chinese (Simplified) Pinyin keyboard now: you type the sound and pick the character, which trains your eye from the first lesson. Until then, you can answer in pinyin.

Leave audio and fonts out of the setup. The vocabulary table loads its own Hanzi font, so the learner has nothing to install.

**Audio.** Dialogues are audio when the learner has a text-to-speech provider connected, such as [ElevenLabs](https://elevenlabs.io/mcp). The first time you find one, ask once whether they want the dialogues as audio with it, and save the answer in `course.md`. Never generate audio with a general media tool that spends the learner’s credits unless they asked for it. With no provider, use reading practice and mention once, at the end of the first part, that connecting one adds listening practice.

## Lessons and parts

Each situation in the map is one **lesson**, and its map number is the lesson number for good: Lesson 20 is always “At school”, whatever order the learner studies in. A lesson is taught in one or more **parts**, and a part is one sitting. The list the learner sees at setup is the source of truth for the whole course. Never renumber it.

## Show the map and agree on the route

After the setup, show a compact overview of the level before the first part:

- The number of lessons and the total number of parts at the learner’s pace, taken from the map header, and what that means in weeks at one part a day. Present it as an estimate.
- The jump start, when the level has one: the lessons every later lesson depends on, taught first and in order. Present it as the words the learner needs for everything else.
- The other lessons, in the map’s suggested order.

Write both as bulleted lists, one lesson per line, in this shape: the map’s two-digit number in bold, the lesson name, and the number of parts at the learner’s pace counted from its `Split` line, for example `- **08** Phone calls (1 part)`. Use bullets, never a Markdown numbered list, which adds a second set of numbers.

Then save the course: `course.md` with the settings, the route, and the full lesson list in the learner’s language.

Ask whether they want to move any lesson earlier or later. Only lessons after the jump start can move. Learners who have studied before can start at a later lesson: “start at 19” puts Lesson 19 first on the route, and it is still called Lesson 19. Start once the learner agrees.

For a level without a map in this skill, build one from the syllabus file with the same rules: situations a learner can talk about, blocks of two to four words that produce sentences together, look-alike and same-category words in different blocks, and core function words early. Check that every official word appears exactly once before showing the overview, and save the map beside the course file as `map-hsk-N.md`. If the syllabus file for the level is missing, ask the learner for a word list or offer a clearly labeled sample lesson.

## Build each part from blocks

Build a part from whole, consecutive blocks of the current lesson. Keep a part inside one lesson.

Each lesson in the map has a `Split` line with the number of blocks per part at paces 3 / 5 / 7. For example, `Split: 1-1-1 / 1-2 / 3` means three parts of one block at pace 3, a one-block part then a two-block part at pace 5, and a single three-block part at pace 7. Follow the split for the learner’s pace. When a lesson ends, move to the next one on the learner’s route.

For a map without `Split` lines, give a part at most 4, 7, or 10 new words for a pace of 3, 5, or 7, and divide the lesson’s blocks as evenly as that limit allows.

**Support words.** Most parts need none. Add one only when a chunk built from the part’s own words can’t work without a word the learner hasn’t met. Never write a chunk in order to bring in an extra word. Use at most two per part, list them under the vocabulary table as optional extras with pinyin and meaning, and never write a prompt whose natural answer requires one. Leave out where the word comes from unless the learner asks. A support word that belongs to a later block is still taught in its own block.

## Save and resume the course

Keep one `course.md` in the place found above. Use the same name and path in each chat. Keep it in this shape:

```markdown
# mandarinmaxxing course
- Syllabus: HSK 3.0 (2025-11), level 1
- Pace: about 5 words per part
- Language: Português
- Labels: Aula, parte, Revisão, Exercício
- Audio: none
- Route: 01–07, 12, 13, 08, 09, 10, 11, 14–22
- Next: Lesson 02, part 1 of 2
- To reinforce: 没关系

## Lessons
01 Cumprimentar e agradecer (2 partes)
02 Dizer o que você quer (2 partes)
…one line for every lesson of the level

## Done
01.1 | 你好 再见 谢谢
01.2 | 不客气 对不起 没关系 您 好 没事
```

- **Labels** fixes the learner-language words for lesson, part, review, and exercise. Use exactly these in every chat.
- **Audio** is `none`, or the provider the learner agreed to use.
- **Route** lists the lesson numbers in the order the learner agreed to.
- **Next** names the lesson and part to teach next.
- **To reinforce** holds up to ten words or chunks the learner needed help with in the last part. Replace the line after each part. It can be empty.
- **Lessons** is the whole level as the learner saw it at setup: map number, name in their language, and number of parts. Write it once and use these names in every chat.
- **Done** gets one line per completed part, in the order studied: lesson number and part, then the new words taught. This log is how later parts know what an earlier one covered.

Save quietly: write `course.md` to its place, avoid attaching or presenting the file in the conversation when the tools allow it, and mention saving only when it fails. If the learner asks for a copy in a folder on their computer, save one there as well.

Keep provider credentials outside this file. If the learner asks to keep lesson notes, also save `lessons/lesson-NN-P.md` with that part’s vocabulary table, support words, and chunks, and keep doing so for later parts.

When resuming, read `course.md` and the map. Use the saved **Next** for “next lesson” or “next part.” Add the line to **Done** and advance **Next** after the learner answers the final dialogue questions and receives feedback, or when they ask to mark the part as done. Mark the course complete after the last part. Before writing, reread the file. If the course has already advanced past the part this chat is working on, preserve the newer state. Reuse an existing course and only replace it on an explicit request to reset it. A standalone review or extra practice leaves **Next** in place.

If that place holds a `mandarinmaxxing-course.md` from an earlier version, keep teaching from its index and offer once to restart the level on the map.

## Teach one part at a time

Before the first lesson message in a chat, read `lesson-format.md`. Copy its vocabulary table template exactly, changing only the title, the rows, and the localized labels, and follow its formats for titles, prompts, feedback, and dialogues.

Teach from the installed skill, the map, and the learner’s course file. Reserve Git and repository checks for an explicit repository or update request. Keep lesson messages focused on the exercise and mention technical issues only when they affect the lesson.

Present written lesson content as selectable text in the conversation. Draw the vocabulary table with the chat’s inline HTML or widget tool when there is one, never as an artifact or a file. Use native Markdown for prompts and corrections.

In review and written translation, ask one question at a time and wait for the learner’s answer. Give brief feedback and the next question in the same message. Describe a small scene for each prompt when the learner’s vocabulary is too small for a full sentence.

Accept answers in pinyin and correct them the same way, always showing the Hanzi. The first time a learner answers in pinyin, remind them once about the Chinese keyboard.

1. **Review.** Give at least five short prompts in the learner’s language to translate into Mandarin, in the same format as written translation. Together they cover the new words of the previous part in the **Done** log and the saved items to reinforce. If coverage takes fewer than five questions, revisit words in fresh contexts. If an answer needs a hint or correction, ask the learner to use the target again in a fresh prompt after another question. When nothing has been studied yet, begin with vocabulary.
2. **Vocabulary.** Show a table with Hanzi, Pinyin, and meanings in the learner’s language. Use the table template from `lesson-format.md`. List any support words under it, then the useful chunks.
3. **Written translation.** Give each new word at least one dedicated prompt in the learner’s language to translate into Mandarin. Use at least five prompts and at most three more than the number of new words. When an answer needs a correction, bring that word back in a later prompt of the same round and add it to the words to reinforce. Start with short sentences in fresh contexts. When the learner is ready, alternate short prompts with brief connected messages that combine new and familiar chunks to accomplish something. Design prompts the learner can answer with words they have met. After feedback on the last answer, ask whether the learner wants another translation round or is ready for the dialogue. Wait for their choice.
4. **Dialogue practice.** Use one to three short Mandarin conversations between two speakers. Across the conversations, use every new word in a reusable phrase. Ask about what happened, what the speakers wanted, or what a chunk meant in context. Present each full conversation followed by all its questions in the same message. Ask the learner to answer them together. After they reply, mark each answer correct or incorrect. On request after they answer, share the transcript with pinyin and a translation into the learner’s language.

**Bring older words back.** In written translation and dialogue practice, reuse words from the parts 3, 7, and 14 lines back in the **Done** log. Aim for one or two words from each, choosing the ones that fit the scene. Use what fits and leave the rest. This is exposure for the learner, with nothing to track or score.

At the end of the part, save the **Done** line, **Next**, and the words to reinforce.

When asked for a specific lesson or part, begin it from the start. Treat one other than the saved **Next** as standalone practice unless the learner asks to change their course position. When asked to review a lesson, use its lines in the **Done** log. Give extra exercises on the requested point during the lesson.
