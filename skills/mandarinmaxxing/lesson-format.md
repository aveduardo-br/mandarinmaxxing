# Lesson format

Formats for the parts of a lesson. Read this once per chat, before the first lesson message.

## Label lessons and prompts

- **Title.** Open each part with one bold line in this shape, in the learner’s language: `HSK 1 · Lesson 20 · At school · part 1 of 2`. The level comes first, because lesson numbers restart at 1 in each level. Write the number without a leading zero. The lesson number is the map’s and never changes. Leave out “part 1 of 1” when a lesson has a single part.
- **Title once.** When a part starts with the vocabulary table, the table’s heading is the title and no title line goes above it. When a part starts with review, the title line opens the review and the table’s heading repeats it later. With the Markdown fallback, the title goes in a bold line above the table.
- **No commentary on the plan.** State the title and teach. Leave out remarks about how the lesson is divided, why a part has the number of words it has, or what the map says, unless the learner asks. One short line before the table, such as “Here are the new words”, is fine.
- **Same words every time.** Use one word for “lesson”, one for “part”, and one name for each lesson through the whole course. Take them from the **Labels** line and the **Lessons** list in `course.md`.
- **Prompts.** Put the counter on its own bold line and the sentence to translate as plain text under it, with a blank line between them. In the review the counter counts the whole review, such as **Review 2 of 7**. In the rounds it names the round and counts to five, such as **Round 2 · 3 of 5**, using the saved label for round. Open each round with one bold line that names it with the saved round name, such as **Round 2 · Full actions**. Keep the prompt out of blockquotes so it reads at full strength. Say “Translate into Mandarin” before the first review prompt and again before the first prompt of round 1, and nowhere else.

## Write Mandarin the same way everywhere

Outside the vocabulary table, every piece of Mandarin follows one pattern: **Hanzi in bold**, *pinyin in italics*, meaning in plain text.

- A chunk or a corrected sentence takes three lines: the Hanzi in bold, the pinyin in italics under it, and the meaning in the learner’s language under that. Use hard line breaks so the three lines don’t run together. Put the chunk list under one bold line with the saved label for useful phrases; when a word in a chunk can be swapped, say which in its meaning line. A breakdown, when the chunk has one, is a fourth line in plain text: 你好 = 你 (you) + 好 (good).
- A word inside a sentence is written inline: **超市** (*chāoshì*, supermarket). A word the learner has known since earlier parts needs only the bold Hanzi, unless it is the point of the correction.
- Reading texts stay as plain Hanzi, with no pinyin.
- Never italicize or strike through Hanzi.

## Format each vocabulary table

Use the selectable HTML table below whenever the chat can display it alongside the message. Copy the whole block character for character, including the `<style>` with its `@font-face` rule. Change only three things: the heading, the rows, and the localized column headers. The heading is the lesson title line, such as `HSK 1 · Lesson 10 · Dates and weekdays · part 1 of 2`. Keep every Hanzi inside `<span lang="zh-Hans">`. If the tool that renders the table comes with its own design guidance, this template still wins: don’t restyle it, simplify it, or drop the font.

The Hanzi use a handwriting-style Kaiti in mainland standard forms, so the first shape the learner sees is close to what they will write in a notebook. The font loads from the web, or from the learner’s computer when it is installed there.

```html
<section id="mandarinmaxxing-vocab">
  <h2>HSK 1 · Lesson 13 · Shopping and paying · part 1 of 3</h2>
  <table>
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Meaning</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">商店</span></td><td>shāngdiàn</td><td>shop</td></tr></tbody>
  </table>
</section>
<style>
  @font-face {
    font-family: "Mandarinmaxxing Kaiti";
    src: local("LXGW WenKai GB"), local("LXGW WenKai GB Lite"),
      url("https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@338b81599301cc40b92b882af7d7e301efa15c7b/skills/mandarinmaxxing/fonts/kaiti-hsk-1-6.woff") format("woff");
    font-display: swap;
  }
  #mandarinmaxxing-vocab { --soft: var(--text-secondary, color-mix(in srgb, currentColor 65%, transparent)); --line: var(--border, color-mix(in srgb, currentColor 15%, transparent)); padding: 4px 0 24px; }
  #mandarinmaxxing-vocab h2 { font-size: 16px; font-weight: 500; margin: 0 0 8px; }
  #mandarinmaxxing-vocab table { width: 100%; border-collapse: collapse; }
  #mandarinmaxxing-vocab th, #mandarinmaxxing-vocab td { text-align: left; font-weight: 400; padding: 10px 64px 10px 0; border-bottom: 1px solid var(--line); vertical-align: middle; user-select: text; }
  #mandarinmaxxing-vocab th { font-size: 13px; font-weight: 500; color: var(--soft); }
  #mandarinmaxxing-vocab th:nth-child(-n+2), #mandarinmaxxing-vocab td:nth-child(-n+2) { width: 1%; white-space: nowrap; }
  #mandarinmaxxing-vocab td:nth-child(2) { color: var(--soft); }
  #mandarinmaxxing-vocab span[lang="zh-Hans"] { font-family: "Mandarinmaxxing Kaiti", "Kaiti SC", "STKaiti", "KaiTi", serif; font-size: 32px; line-height: 1.2; font-synthesis: none; }
</style>
```

Under the table, add a one-line usage note only for a word whose use the meaning cell can’t show: two words that translate the same way (帮 and 帮忙), or a word that needs a pattern (让 + person + verb). Give a polite form a meaning that says who it is for, such as 您 = “you (to sir or madam)”, so a prompt can call for it. When two words of a part translate the same way (没关系 and 没事), give each prompt a context that fits only one, or accept both.

If the chat can’t embed HTML, use a selectable Markdown table in the message. Enlarge Hanzi through inline math where rendering and selection are confirmed, for example `$\LARGE\text{公交车}$` in Codex desktop. Use bold Hanzi when the interface supports standard text formatting only.

## Respond to a written translation

Use plain Markdown for all feedback and the Mandarin pattern above. Blockquotes are reserved for one thing: showing back what the learner wrote in a correction.

- **Correct and natural.** Confirm briefly and move to the next prompt. Accept any natural version that meets the request, including a standard variant such as 没有关系 for 没关系; if you wanted the other form, name it in one line. If a valid alternative uses a different expression, acknowledge it, name the chunk you were after, and bring it back in a later prompt.
- **Correct meaning, noticeably unnatural phrasing.** Acknowledge that the meaning is right. Show a more natural version in Hanzi with pinyin directly below it and briefly explain the change.
- **Incorrect.** Use this order. First a short opener and “You wrote:”, then the learner’s whole answer in a blockquote. Next, one line that points only at the part that went wrong: the word or chunk to use in its place in bold, its pinyin in italics, and a short reason. For a slip of word order, show the stretch in the right order. Use one such line per fix, even when one fix settles two slips. Then the full corrected sentence once, as bold Hanzi, italic pinyin, and plain meaning on three lines. Follow with the next prompt. Leave out a word-by-word breakdown of the parts the learner got right.

## Reading, when there is no voice provider

Send one message in this order:

- A bold title with the saved label for reading and its number, such as **Reading 1**.
- The text: three to six short Mandarin sentences in plain Hanzi, one person telling in the first person what they did, what they plan, or what happened. No dialogue, no quoted lines, no pinyin and no translation.
- A bold line such as **Your turn**, then the task in the learner’s language.

The task is to rewrite the text with a few changes you name, for example another day, another thing to buy, another price. Choose changes that make the learner write the part’s new words again, not only swap older ones. Skip comprehension questions here: the learner can see the text, so they only test finding a word. Correct the rewrite with the same format as a written translation.

Use one text per part, with every new word of the part in it. Add a second only when the new words don’t fit one scene.

## Listening, with a voice provider

Up to two clips, sent one at a time: the dictation first, then the narration. Each clip has one speaker, in the voice saved for the course.

**Before any clip.**

- **Review the script.** Read it through: the Mandarin sounds natural, it uses only words the learner has met, and the new words of the part are in it.
- **Generate once.** Ask the provider for a single take. On the first clip of a course, choose the voice and save it in `course.md`: with ElevenLabs, use Sarah (voice ID `EXAVITQu4vr4xnSDxMaL`) unless the learner asks for another; with another provider, or if Sarah isn’t in the voice list, pick one clear, neutral voice from the provider’s own list. Set the language to Chinese when the provider has that setting. Never run a generation again to retry or to get a variation unless the learner asks: each run spends their credits.
- **Keep the script out of the message.** Share it with pinyin and a translation only after the learner answers, or if they ask.

**Dictation.** Three to five short sentences, each a thing one person says in a single turn, built from the part’s words and older ones. Never put both sides of an exchange in one sentence (not 谢谢，不客气). Write them as separate sentences so the voice pauses between them. Send the clip under a bold title with the saved label for dictation and its number, such as **Dictation 1**, and ask the learner to write each sentence they hear, numbered, in Hanzi or pinyin. They can replay it as often as they like. For each wrong sentence, give the blockquote and the fix line only, then show the full script once with pinyin and meaning: the script stands for the corrected sentences.

**Narration.** One person speaking in the first person about their own day, plan, or something that happened, in a concrete scene: three to eight sentences, 20 to 40 seconds at a clear pace. The speaker never addresses a listener, asks the listener anything, or quotes anyone; a conversation, or half of one, is not a narration. Send the clip labeled with the saved label for audio, its number and the scene, such as **Audio 1 · At the tea shop**, with the questions in the same message so the learner can read them before playing: what happened, what the speaker wanted or plans, what a chunk meant in context. Ask three to five questions, at least one of each kind, and use no names the learner hasn’t met. Ask for all the answers together, then mark each correct or incorrect.

Use the narration only once the learner has met enough words to fill about 20 seconds. Before that, the dictation alone is the listening step.

## Close a part

Send one short closing message after the last exercise:

- What comes next, such as “Next time: HSK 1, Lesson 11, part 3.”
- When the part was the last part of a lesson with two or more parts, one line saying the lesson is complete and offering the wrap-up role-play, now or next time, such as “Lesson 11 is complete. Want a quick role-play of this situation now, or next time?”
- An offer to start the next part now. The learner decides; parts with few words end well before the hour.

Leave out a summary of the part and any comment on how it was divided.
