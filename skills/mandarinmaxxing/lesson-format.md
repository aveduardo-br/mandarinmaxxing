# Lesson format

How each message of a lesson looks. Take the words for lesson, part, review, round and the rest from **Labels** and **Rounds** in `course.md`, and lesson names from its **Lessons** list.

## Titles and prompts

- **Title.** Each part opens with one bold line in the learner's language: `HSK 1 · Lesson 20 · At school · part 1 of 2`. Level first, no leading zero, and no "part 1 of 1" for a single-part lesson. When a part starts with the vocabulary table, the table's heading is the title and no line goes above it. When it starts with the review, the title opens the review and the table's heading repeats it.
- **Prompts.** The counter goes on its own bold line and the sentence to translate in plain text under it, after a blank line, never in a blockquote. In the review the counter counts the whole review: **Review 2 of 7**. In the rounds it names the round and counts to five: **Round 2 · 3 of 5**. Open each round with one bold line naming it: **Round 2 · Full actions**. Say "Translate into Mandarin" before the first review prompt and before the first prompt of round 1, and nowhere else.

## Mandarin, written the same way everywhere

Outside the vocabulary table: **Hanzi in bold**, *pinyin in italics*, meaning in plain text. Italics are for pinyin only. Never italicize or strike through Hanzi.

- **A chunk or a corrected sentence** takes three lines, with hard line breaks: the Hanzi, the pinyin, the meaning. Put the chunk list under one bold line with the label for useful phrases. When a word in a chunk can be swapped, say which in its meaning line, with a met word as the example. A breakdown, when the chunk has one, is a fourth line in plain text: 你好 = 你 (you) + 好 (good).
- **A word inside a sentence** is written inline: **超市** (*chāoshì*, supermarket). A word known since earlier parts needs only the bold Hanzi, unless it is the point of the correction.
- **Reading texts** stay as plain Hanzi, with no pinyin.

## The vocabulary table

Draw the table with the chat's inline HTML or widget tool, in the conversation, never as an artifact or a file. Copy the block below character for character, including the `<style>` and its `@font-face` rule, and change only the heading (the title line), the rows, and the column headers in the learner's language. Keep every Hanzi inside `<span lang="zh-Hans">`. If the rendering tool has its own design guidance, this template still wins: don't restyle it, simplify it, or drop the font. If the chat can't show HTML, use a Markdown table with the Hanzi in bold, under a bold title line.

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

Under the table, add a one-line usage note only for a word whose use the meaning can't show: two words that translate the same way (帮 and 帮忙), a word that needs a pattern (让 + person + verb), or a word the exercises will use in a role the meaning doesn't show (不 alone as a reply: "no"). Give a polite form a meaning that says who it is for, such as 您 = "you (to sir or madam)".

**Words that translate the same way** (没关系 and 没事, 中文 and 汉语): give each prompt a context that fits only one, or accept both. When the learner keeps choosing one, ask for the other by name in the next prompt that fits and again in the next part's review.

## Feedback on a translation

Plain Markdown. Blockquotes are reserved for showing back what the learner wrote.

- **Correct and natural.** Confirm briefly and go to the next prompt. For a right answer in pinyin, show the sentence in Hanzi on one line. Accept any natural version, including a standard variant such as 没有关系 for 没关系. If the accepted answer leaves out a new word of the part, or uses another expression than the chunk you were after, name the word or chunk in one line and bring it back in a prompt of the same round.
- **Right meaning, unnatural phrasing.** Say the meaning is right, show a more natural version with its pinyin, and explain the change briefly.
- **Incorrect.** In this order: a short opener and "You wrote:", then the learner's whole answer in a blockquote. One line per fix, pointing only at what went wrong: the word or chunk to use in bold, its pinyin in italics, a short reason; for word order, the stretch in the right order. Then the full corrected sentence once, on three lines. Then the next prompt. No breakdown of the parts the learner got right.

## Listening or reading

Use what **Audio** in `course.md` says, and only that. Never generate audio with a tool the learner didn't choose, or with a general media tool that spends their credits. Don't suggest the chat app's read aloud button: its voice reads Hanzi with the wrong sounds, and say so if they ask. If the provider fails or runs out of credits, say so once and use reading for the rest of the part.

### Reading (Audio: none)

One message, in this order:

- A bold title with the label for reading and its number: **Reading 1**.
- The text: three to six short sentences in plain Hanzi, one person telling in the first person what they did, plan, or what happened. No dialogue, quoted lines, pinyin, or translation.
- A bold line such as **Your turn**, then the task: rewrite the text with a few changes you name (another day, another thing to buy, another price), chosen so the learner writes the part's new words again. No comprehension questions: the learner can see the text.

Correct the rewrite as a written translation. One text per part, with every new word in it; a second only when the new words don't fit one scene.

### Listening (with a voice provider)

Up to two clips, sent one at a time, each with one speaker in the course's voice.

- **Check the script** before generating: natural Mandarin, the part's new words in it, and every word met. Check them one by one.
- **Generate once**, a single take, with the language set to Chinese when the provider has that setting. Never run a generation again unless the learner asks: each run spends their credits. On the first clip of a course, choose the voice and save it in **Audio**: with ElevenLabs, Sarah (voice ID `EXAVITQu4vr4xnSDxMaL`) unless the learner asks for another; otherwise one clear, neutral voice from the provider's list.
- **Keep the script out of the message.** Show it, with pinyin and meaning, only after the learner answers or if they ask.

**Dictation.** Three to five short sentences, each a thing one person says in a single turn, at the level of round 2, written as separate sentences so the voice pauses. No sentence repeats a chunk or a prompt of the part, holds both sides of an exchange (not 谢谢，不客气), or doubles a word to fill a line. With very few met words, two or three real lines are enough, and they may be lines the part already used. Send the clip under a bold title, **Dictation 1**, and ask the learner to write each sentence they hear, numbered, in Hanzi or pinyin. For each wrong sentence give the blockquote and the fix line, then show the full script once with pinyin and meaning.

**Narration.** Only once the met words can fill about 20 seconds; before that the dictation is the whole step. One person speaking in the first person about their day, a plan, or something that happened, in a concrete scene that is new to the part: three to eight sentences, 20 to 40 seconds. The speaker never addresses or questions a listener and never quotes anyone. Send the clip as **Audio 1 · At the tea shop**, with three to five questions in the same message so the learner reads them first: what happened, what the speaker wanted or plans, what a chunk meant in context, at least one of each, with no names the learner hasn't met. Ask for all the answers together, then mark each right or wrong.

## Close a part

One short message after the last exercise; it can share a message with the feedback on it.

- What comes next: "Next time: HSK 1, Lesson 11, part 3."
- After the last part of a lesson with two or more parts, one line saying the lesson is complete and offering a wrap-up role-play, now or next time (it is described in `requests.md`).
- An offer to start the next part now.

No summary of the part.
