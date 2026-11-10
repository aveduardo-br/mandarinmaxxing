# mandarinmaxxing

**Learn Mandarin with HSK 3.0 vocabulary grouped by topic.**

In a textbook-based HSK course, related words can appear in different lessons. Mandarinmaxxing uses the HSK 3.0 syllabus as its base and groups related words by topic and everyday use. You’ll practice them in everyday chunks, such as short phrases and sentence patterns you can reuse in real conversations.

## Install

### Claude chat on the web or desktop

Download the ZIP and upload it as a custom skill under **Plugins** or **Customize → Skills**, depending on your interface. Enable code execution and file creation in **Settings → Capabilities** if needed. [Download the Claude skill](https://github.com/aveduardo-br/mandarinmaxxing/releases/download/v0.1.4/mandarinmaxxing-claude.zip) · [Claude upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

If your Claude chat supports saving skills, you can also try pasting this prompt. Review the skill and click **Save** if a card appears.

```text
Create a custom skill named mandarinmaxxing using this SKILL.md as written. Show me the card to save it to my account if available.
https://raw.githubusercontent.com/aveduardo-br/mandarinmaxxing/main/skills/mandarinmaxxing/SKILL.md
```

### Local Claude Code and Codex

Run these checks in your study folder using a terminal on your computer.

```sh
node --version
npx --version
```

If you’re installing as an AI assistant, confirm you’re in the local study folder and run both checks there. Continue only if both commands print a version. If either fails, report the command and its error. For a Claude chat running in the cloud, use the ZIP or chat prompt above.

**Claude Code.** Run this from the same folder.

```sh
npx skills add aveduardo-br/mandarinmaxxing --skill mandarinmaxxing -a claude-code
```

Then open Claude Code in that folder and type `/mandarinmaxxing`. [Claude Code skills](https://code.claude.com/docs/en/skills)

**Codex.** Use the same install command with `-a codex`, then start with `$mandarinmaxxing`. [Codex skills](https://learn.chatgpt.com/docs/build-skills)

## Start your course

Choose your **HSK level**, **how many new words you want per lesson**, and **whether you want to set up audio**. Start with HSK 1 if you’re new to Mandarin. The skill teaches in English.

| Pace | New items per lesson |
|---|---:|
| Light | 1–4 |
| Standard | 5–7 |
| Intensive | 8–10 |

The skill builds a numbered lesson index from your chosen level and pace. Start at Lesson 01 or pick a later lesson if you’ve already studied some of the vocabulary. To resume in a new chat, attach your saved index and give the lesson number. If the skill can’t access the syllabus, you can attach a copy. [Official HSK syllabus](https://www.chinesetest.cn/HSK)

Try **“Use mandarinmaxxing to start HSK 1 at a Standard pace.”**

## How lessons work

In review and written translation, the skill asks one question at a time and gives feedback with the next question.

1. **Quick review.** Answer at least five questions covering the previous lesson’s vocabulary. Older material comes back at spaced intervals. If you’re starting fresh, go straight to the new vocabulary.
2. **New vocabulary.** Learn a group of related words in a table with simplified Chinese characters, tone-marked pinyin, and English meanings.
3. **Written translation.** Translate at least one sentence per new word from English into Mandarin. After the last correction, choose another translation round or move on to dialogue practice.
4. **Dialogue practice.** Listen to a short two-person conversation of around 20 seconds or read it in Hanzi when audio is unavailable. All the questions come with the dialogue. Answer them together and see which answers were correct. You can ask for the transcript, pinyin, and translation after you answer.

Earlier words also come back in translation prompts and dialogues whenever they fit naturally. Every new word is practiced in both formats. Pronunciation and tone practice are self-directed.

**Hanzi display.** Where custom visuals are supported, the vocabulary table uses larger, selectable hanzi. It uses **Kaiti SC** when available and the default Chinese font otherwise. The standard chat table uses bold hanzi. Exercises use standard text. [About regular script](https://asia-archive.si.edu/learn/chinas-calligraphic-arts/standard-script/)

**Audio setup.** We strongly recommend audio for practicing how everyday phrases sound in conversation. ElevenLabs is the recommended provider for two-voice dialogues. You can use another provider or start with reading and connect audio later. [Connect ElevenLabs](https://elevenlabs.io/mcp)

## Build the packages

Run these commands from the repository root.

```sh
mkdir -p dist
(cd skills && zip ../dist/mandarinmaxxing-claude.zip mandarinmaxxing/SKILL.md)
zip dist/mandarinmaxxing-chatgpt.zip plugin.json skills/mandarinmaxxing/SKILL.md
```

Both packages use the same skill instructions. The ChatGPT ZIP includes the plugin manifest for local desktop testing. Public installation on ChatGPT requires a listing in the Plugins Directory. [Skill instructions](skills/mandarinmaxxing/SKILL.md) · [ChatGPT plugin setup](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually)
