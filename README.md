# mandarinmaxxing

Learn Mandarin with HSK 3.0 vocabulary grouped by everyday situations and practiced in phrases you can reuse. This English-language skill builds the course around your chosen HSK level and vocabulary pace.

For example, a café lesson brings drinks, quantities, and ordering together. You might practice “I'd like a cup of tea” and reuse the same chunk to order coffee. Each lesson starts with spaced review when there is earlier material, introduces new vocabulary, and uses every target word in everyday chunks in both written translation and guided listening.

Audio setup is optional. ElevenLabs is the recommended provider when two-voice dialogue generation is available. [Connect ElevenLabs](https://elevenlabs.io/mcp)

## Get started

| Platform | Setup |
|---|---|
| Claude | Build the Claude ZIP below and upload it in **Customize → Skills**. |
| Claude Code | Copy the [skill folder](skills/mandarinmaxxing/) into `.claude/skills/` in your project. |
| ChatGPT | Build the plugin ZIP below. Install through a supported plugin setup or submit the package to the plugin directory. |

[Claude skill upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude Code skills](https://code.claude.com/docs/en/skills) · [ChatGPT plugin packaging](https://developers.openai.com/plugins/build/plugins)

Try **“Use mandarinmaxxing to start HSK 1 at a Standard pace.”** Standard introduces 5–7 items per lesson. Save the course index if you want to pick up a lesson in another chat.

The skill uses the [official HSK syllabus](https://www.chinesetest.cn/HSK) or a syllabus you provide. If your chat cannot access the vocabulary list, attach a copy. If your chat cannot generate the listening audio, the skill can provide a separate script for a speech provider.

## Build the packages

From the repository root, run:

```sh
mkdir -p dist
(cd skills && zip ../dist/mandarinmaxxing-claude.zip mandarinmaxxing/SKILL.md)
zip dist/mandarinmaxxing-chatgpt.zip plugin.json skills/mandarinmaxxing/SKILL.md
```

The packages share the same [skill instructions](skills/mandarinmaxxing/SKILL.md). The ChatGPT ZIP adds the plugin manifest. GitHub Releases can host both ZIPs after platform testing.
