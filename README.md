# mandarinmaxxing

Learn Mandarin with HSK 3.0 vocabulary grouped by everyday situations and practiced in phrases you can reuse. This English-language skill builds the course around your chosen HSK level and vocabulary pace.

## Install

**Claude Code.** Run this from your study folder in a terminal with Node.js installed.

```sh
npx skills add aveduardo-br/mandarinmaxxing --skill mandarinmaxxing -a claude-code
```

Then type `/mandarinmaxxing` in Claude Code. For local Codex, use `-a codex` in the install command and start with `$mandarinmaxxing`. [Claude Code skills](https://code.claude.com/docs/en/skills) · [Codex skills](https://learn.chatgpt.com/docs/build-skills)

**Claude on the web.** [Download the skill ZIP](https://github.com/aveduardo-br/mandarinmaxxing/releases/download/v0.1.0/mandarinmaxxing-claude.zip) and upload it as a custom skill under **Plugins** or **Customize → Skills**, depending on your interface. [Claude upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

**ChatGPT on the web.** The plugin is available as a package for local testing. Public installation requires a listing in the Plugins Directory. [ChatGPT plugin packaging](https://developers.openai.com/plugins/build/plugins)

Try **“Use mandarinmaxxing to start HSK 1 at a Standard pace.”** Standard introduces 5–7 items per lesson. Save the course index if you want to pick up a lesson in another chat.

## How lessons work

For example, a café lesson brings drinks, quantities, and ordering together. You might practice “I'd like a cup of tea” and reuse the same chunk to order coffee. Each lesson starts with spaced review when there is earlier material, introduces new vocabulary, and uses every target word in everyday chunks in both written translation and guided listening.

**Hanzi font.** We recommend **Kaiti SC** for vocabulary tables. Its regular-script forms make individual strokes easy to see when copying characters. Use a stroke-order guide for handwriting and practice reading in common screen fonts too. [About regular script](https://asia-archive.si.edu/learn/chinas-calligraphic-arts/standard-script/)

Audio setup is optional. ElevenLabs is the recommended provider when two-voice dialogue generation is available. [Connect ElevenLabs](https://elevenlabs.io/mcp)

The skill uses the [official HSK syllabus](https://www.chinesetest.cn/HSK) or a syllabus you provide. If your chat cannot access the vocabulary list, attach a copy. If your chat cannot generate the listening audio, the skill can provide a separate script for a speech provider.

## Build the packages

Run these commands from the repository root.

```sh
mkdir -p dist
(cd skills && zip ../dist/mandarinmaxxing-claude.zip mandarinmaxxing/SKILL.md)
zip dist/mandarinmaxxing-chatgpt.zip plugin.json skills/mandarinmaxxing/SKILL.md
```

The packages share the same [skill instructions](skills/mandarinmaxxing/SKILL.md). The ChatGPT ZIP adds the plugin manifest.
