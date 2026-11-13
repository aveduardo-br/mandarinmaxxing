# mandarinmaxxing

**The same HSK words, reorganized around everyday conversations.**

A Claude skill for learning Mandarin vocabulary. The words are the same as the official HSK. What changes is the order: instead of a list, you learn by situation. Saying hello, introducing yourself, ordering food, shopping.

I built this skill for myself. The textbook order felt slow to me, with words that didn't belong together in the same lesson, and I wanted to be able to talk about one thing at a time. I keep improving it as I study, and I'm sharing it in case it helps you too. No method is wrong. This is one option for people who like to study this way.

## How a lesson works

Each lesson is one situation, such as **Shopping and paying**. You study it in short parts, a few new words at a time.

1. **Quick review.** You translate a few sentences with the words from your last part. Older words come back too, so you don't forget them.
2. **New words.** A table with Hanzi, pinyin, and the meaning in your language.
3. **Translation.** You get one sentence at a time in your language and write it in Mandarin. If something is off, you see what to change and the corrected sentence.
4. **A short text.** You read it and rewrite it with a few changes. With audio turned on, you listen to it instead and answer what you understood.

Your progress is saved, so you can open a new chat on any device and say "next lesson".

## Install

You need a Claude account where you can add skills and create projects. It takes about five minutes.

1. **Download the skill.** [mandarinmaxxing-claude.zip](https://github.com/aveduardo-br/mandarinmaxxing/raw/main/download/mandarinmaxxing-claude.zip)
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
- **Pace.** How many new words each time you study: 3 is light, 5 is the recommended pace, 7 is intense. Any other number works too.
- **Audio.** Optional. See below.

Then the skill shows you the full list of lessons for your level and how long it should take. You can move lessons around before you start, for example to study food before phone calls.

The skill writes in the language you write in. Ask if you want another one.

**Keyboard.** You answer in Mandarin from the first lesson. You can start by typing pinyin. When you want the next step, turn on your device's Chinese keyboard (Pinyin, Simplified): you type the sound and pick the character.

## Audio (optional)

Every lesson closes with a short text. With audio, you hear it in a natural voice without seeing it written, then answer questions about it. It's the course's listening practice.

Most people use ElevenLabs, which has a free account:

1. Create an account at [elevenlabs.io](https://elevenlabs.io).
2. In Claude, open **Customize → Connectors**, find **ElevenLabs**, and connect it.
3. Tell the skill you want audio.

Each lesson generates one short clip in one voice. The skill uses a voice called Sarah by default, and you can ask for another. You can also bring a different voice provider.

Without audio there is nothing to set up. You read the text instead.

## What it covers

- **HSK 1 is ready.** All 300 words of the level, in 22 lessons. The first seven lessons are a jump start: greetings, saying what you want, saying who you are.
- **HSK 2 to 6.** The official word lists are included. Their lesson maps aren't written yet, so the skill builds a map for your level when you start it. Hand-checked maps are coming, HSK 2 first.
- **The word list** is the HSK syllabus released in November 2025, levels 1 to 6. Every word of a level appears once in its map.

## What it doesn't do

- It doesn't check your pronunciation or tones. Speaking practice is up to you.
- It doesn't replace flashcards for long-term memory. Older words come back inside lessons, but the skill doesn't track every word you've missed.
- It doesn't promise fluency or a passing exam score. It covers the vocabulary. The exam also tests grammar, handwriting, and speaking.

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
| `tools/` | Scripts that check a map against the word list and build the ZIP |

To check a map and rebuild the ZIP in `download/`, run these from the repository root:

```sh
python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md
sh tools/build.sh
```

## Credits

- Word lists: the HSK syllabus published by the Center for Language Education and Cooperation, converted from the mirror at [ofou/hsk](https://github.com/ofou/hsk) (MIT License). Details in [`syllabus/SOURCE.md`](skills/mandarinmaxxing/syllabus/SOURCE.md).
- Hanzi font: [LXGW WenKai GB](https://github.com/lxgw/LxgwWenkaiGB), under the SIL Open Font License. Details in [`fonts/SOURCE.md`](skills/mandarinmaxxing/fonts/SOURCE.md).
