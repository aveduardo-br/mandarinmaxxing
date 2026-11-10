# mandarinmaxxing

**Learn Mandarin with HSK 3.0 vocabulary grouped by topic.**

In a textbook-based HSK course, related words can appear in different lessons. Mandarinmaxxing uses the HSK 3.0 syllabus as its base and groups related words by topic and everyday use. You’ll practice them in everyday chunks, such as short phrases and sentence patterns you can reuse in real conversations.

## Install

**Claude Code.** Run this from your study folder in a terminal with Node.js installed.

```sh
npx skills add aveduardo-br/mandarinmaxxing --skill mandarinmaxxing -a claude-code
```

Then open Claude Code in that folder and type `/mandarinmaxxing`. [Claude Code skills](https://code.claude.com/docs/en/skills)

**Claude on the web.** Enable code execution and file creation in **Settings → Capabilities**. Upload the ZIP as a custom skill under **Plugins** or **Customize → Skills**, depending on your interface. [Download the Claude skill](https://github.com/aveduardo-br/mandarinmaxxing/releases/download/v0.1.2/mandarinmaxxing-claude.zip) · [Claude upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

**Codex.** Use the same install command with `-a codex`, then start with `$mandarinmaxxing`. [Codex skills](https://learn.chatgpt.com/docs/build-skills)

## Start your course

Choose your **HSK level** and **how many new words you want per lesson**. Start with HSK 1 if you’re new to Mandarin. The skill teaches in English.

| Pace | New items per lesson |
|---|---:|
| Light | 1–4 |
| Standard | 5–7 |
| Intensive | 8–10 |

The skill builds a numbered lesson index from your chosen level and pace. Start at Lesson 01 or pick a later lesson if you’ve already studied some of the vocabulary. To resume in a new chat, attach your saved index and give the lesson number. If the skill can’t access the syllabus, you can attach a copy. [Official HSK syllabus](https://www.chinesetest.cn/HSK)

Try **“Use mandarinmaxxing to start HSK 1 at a Standard pace.”**

## How lessons work

1. **Quick review.** Recall words and phrases from the previous lesson. Older material comes back at spaced intervals. If you’re starting fresh, go straight to the new vocabulary.
2. **New vocabulary.** Learn a group of related words in a table with simplified Chinese characters, tone-marked pinyin, and English meanings.
3. **Written translation.** Translate short prompts from English into Mandarin and get feedback after you try.
4. **Guided listening.** Read a few questions, then listen for the new words in clear two-person dialogues of around 20 seconds each. Check the transcript after you answer.

Earlier words also come back in translation prompts and dialogues whenever they fit naturally. Every new word is practiced in both formats.

**Hanzi display.** The vocabulary table uses larger, selectable hanzi where supported. It uses **Kaiti SC** when available and the default Chinese font otherwise. Exercises use standard text. [About regular script](https://asia-archive.si.edu/learn/chinas-calligraphic-arts/standard-script/)

**Audio setup.** ElevenLabs is recommended for two-voice dialogues. You can connect it or another provider at any time. If audio generation is unavailable in your chat, ask for a separate dialogue script to use with a speech provider. [Connect ElevenLabs](https://elevenlabs.io/mcp)

## Build the packages

Run these commands from the repository root.

```sh
mkdir -p dist
(cd skills && zip ../dist/mandarinmaxxing-claude.zip mandarinmaxxing/SKILL.md)
zip dist/mandarinmaxxing-chatgpt.zip plugin.json skills/mandarinmaxxing/SKILL.md
```

Both packages use the same skill instructions. The ChatGPT ZIP includes the plugin manifest for local desktop testing. Public installation on ChatGPT requires a listing in the Plugins Directory. [Skill instructions](skills/mandarinmaxxing/SKILL.md) · [ChatGPT plugin setup](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually)
