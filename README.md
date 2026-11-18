# mandarinmaxxing

**The same HSK words, reorganized around everyday conversations.**

**Website:** [mandarinmaxxing.vercel.app](https://mandarinmaxxing.vercel.app). See how a lesson works, with examples from every level, before you install.

A Claude skill for learning Mandarin vocabulary. The words are the same as the official HSK. What changes is the order: instead of a list, you learn by situation. Saying hello, introducing yourself, ordering food, shopping.

I built this skill for myself. The textbook order felt slow to me, with words that didn't belong together in the same lesson, and I wanted to be able to talk about one thing at a time. I keep improving it as I study, and I'm sharing it in case it helps you too. No method is wrong. This is one option for people who like to study this way.

## How a lesson works

Each lesson is one situation, such as **Shopping and paying**. You study it in parts, a few new words at a time, and a part is built for about an hour a day. That's roughly what real progress takes; if you have less time, ask for a shorter session.

1. **Review.** One sentence to translate for each word of your last part. Older words come back inside these sentences, so you don't forget them.
2. **New words.** A table with Hanzi, pinyin, and the meaning in your language, plus a few ready-to-use phrases.
3. **Three rounds of exercises.** Five sentences each, from your language into Mandarin. The first round practices the phrases, the second asks for complete sentences, and the third for short sequences, like telling your day or writing a message. If something is off, you see what to change and the corrected sentence.
4. **Listening.** With audio turned on, a short dictation and a short story in a natural voice. Without audio, you read a short text and rewrite it with a few changes.
5. **Wrap-up.** When you finish a lesson, you can play out its situation in a short role-play.

Your progress is saved, so you can open a new chat on any device and say "next lesson".

## Install

You need a Claude account where you can add skills and create projects. It takes about five minutes.

1. **Download the skill.** [mandarinmaxxing-claude.zip](https://github.com/aveduardo-br/mandarinmaxxing/releases/latest/download/mandarinmaxxing-claude.zip)
2. **Add it to Claude.** Open **Customize → Skills**, click **+**, choose **Create skill**, then **Upload a skill**, and pick the ZIP. [Claude's guide to skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
3. **Create a project** for your course, for example "Mandarin". In the project's instructions, paste this line:

   ```text
   Use the mandarinmaxxing skill. My course is saved in course.md.
   ```

4. **Open a chat inside the project** and write:

   ```text
   start mandarinmaxxing
   ```

The project is where your course is saved. Keep all your lessons in it.

If you start the skill outside a project, it shows you these same steps and offers a trial lesson that isn't saved.

## Set up your course

The first message asks three things. They are suggestions, and you can change any of them later by asking.

- **Level.** New to Mandarin? Start with HSK 1, lesson 1. If you've studied before, name the level or the lesson you want to pick up from.
- **Pace.** How many new words each part brings: 3 is light, 5 is the recommended pace, 7 is intense. Any other number works too. A part is built for about an hour; when one ends early, as in the first lessons, the skill offers the next part right away.
- **Audio.** Optional. See below.

Then the skill shows you the full list of lessons for your level and how long it should take. You can move lessons around before you start, for example to study food before phone calls.

The skill writes in the language you write in. Ask if you want another one.

**What you can ask for.** At any time: review a lesson, change the pace, a shorter session, one more round of exercises, an extra reading with only the words you know, flashcards of a part's words ready to import into Anki, or notes of each part.

**Keyboard.** You answer in Mandarin from the first lesson. You can start by typing pinyin. When you want the next step, turn on your device's Chinese keyboard (Pinyin, Simplified): you type the sound and pick the character.

## Audio (optional)

Every part closes with listening practice. With audio, you hear a short dictation and write it down, then a short story in a natural voice and answer questions about it.

Most people use ElevenLabs, which has a free account:

1. Create an account at [elevenlabs.io](https://elevenlabs.io).
2. In Claude, open **Customize → Connectors**, find **ElevenLabs**, and connect it.
3. Tell the skill you want audio.

Each part generates up to two short clips in one voice. The skill uses a voice called Sarah by default, and you can ask for another. You can also bring a different voice provider.

Without audio there is nothing to set up. You read the text instead.

## What it covers

- **HSK 1 to 4 are ready.** 2,000 words in 134 lessons: HSK 1 has 300 words in 22 lessons, HSK 2 has 200 in 19, HSK 3 has 500 in 37, and HSK 4 has 1,000 in 56.
- **How long it takes.** At the recommended pace, HSK 1 is 58 parts, about two months at one part (an hour) a day. HSK 2 is 38 parts, HSK 3 is 94, and HSK 4 is 173. The skill shows the estimate for your own pace when you start.
- **Each level opens with a jump start.** In HSK 1 it's greetings, saying what you want, saying who you are. In the later levels it's the connecting words every other lesson uses, such as "because", "already" and "if".
- **Finish a level and the course moves on to the next.** Words from the level you finished keep coming back.
- **HSK 5 and 6.** The official word lists are included. Their lesson maps aren't written yet, so the skill builds a map for your level when you start it.
- **The word list** is the HSK syllabus released in November 2025, levels 1 to 6. Every word of a level appears once in its map.

## What it doesn't do

- It doesn't check your pronunciation or tones. Speaking practice is up to you.
- It doesn't replace flashcards for long-term memory. Older words come back inside lessons, but the skill doesn't schedule every word for you. Ask for flashcards and it gives you a part's words ready to import into Anki.
- It doesn't promise fluency or a passing exam score. It covers the vocabulary. The exam also tests grammar, handwriting, and speaking.

## How it's made

The course isn't improvised lesson by lesson. Two things are built and checked before anyone studies with them.

**The maps.** Every official word of a level is placed once, in groups of two to four words that make sentences together, inside a situation you can actually talk about. Words that look alike or belong to the same category go in different groups, so they don't blur. A script checks that no word is missing or repeated. Each of the 660 groups in HSK 1 to 4 has a test sentence that uses only words taught by that point, and two independent reviews went through every group.

**The lessons.** Before each version, the skill teaches simulated lessons, and the results are checked two ways: by script (only words you've met, every new word practised at least three times, older words coming back, your progress saved correctly) and by a separate AI reviewer that reads each lesson against the method. So far that's 34 simulated lessons across HSK 1 to 4, plus one run of all 19 parts of the HSK 1 jump start with a simulated student who saw the language as made-up words, so it really knew nothing but what it was taught. In that run, 95 words were taught and every one came back in later parts.

What this shows: the lessons follow the method. What it doesn't show: how much you'll remember. That part comes from people using it, which is why feedback matters. Everything is in [`qa/benchmark/`](qa/benchmark/), including every simulated lesson.

## Help improve it

This is a personal project, and it gets better with use. If a lesson felt off, a word landed in the wrong situation, or the install steps didn't match what you saw, [open an issue](https://github.com/aveduardo-br/mandarinmaxxing/issues). Corrections to a lesson map are especially welcome.

## Other ways to run it

The skill is a folder of plain files, so it also runs in coding agents such as Claude Code and Codex. There the course is saved in your working folder. I test it mostly in the Claude app, so expect rougher edges here.

```sh
npx skills add aveduardo-br/mandarinmaxxing --skill mandarinmaxxing -a claude-code
```

Use `-a codex` for Codex. The installer needs Node.js 22.20.0 or newer.

## What's in this repository

| Path | What it is |
|---|---|
| `skills/mandarinmaxxing/SKILL.md` | How the course works: setup, lessons, review, saving |
| `skills/mandarinmaxxing/lesson-format.md` | How each message of a lesson looks |
| `skills/mandarinmaxxing/maps/` | The lesson map for each level |
| `skills/mandarinmaxxing/syllabus/` | The official word lists, levels 1 to 6 |
| `skills/mandarinmaxxing/fonts/` | The Hanzi font used in the vocabulary table |
| `qa/anchors/` | One test sentence for every group of words in a map. The skill doesn't read these |
| `qa/benchmark/` | Simulated lessons used to test each version: scenarios, scripts, results |
| `tools/` | Scripts that check the maps and the test sentences, and build the ZIP |

To check a map and build the ZIP locally, run these from the repository root:

```sh
python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md
python3 tools/check_anchors.py 1
sh tools/build.sh
```

## Credits

- Word lists: the HSK syllabus published by the Center for Language Education and Cooperation, converted from the mirror at [ofou/hsk](https://github.com/ofou/hsk) (MIT License). Details in [`syllabus/SOURCE.md`](skills/mandarinmaxxing/syllabus/SOURCE.md).
- Hanzi font: [LXGW WenKai GB](https://github.com/lxgw/LxgwWenkaiGB), under the SIL Open Font License. Details in [`fonts/SOURCE.md`](skills/mandarinmaxxing/fonts/SOURCE.md).
