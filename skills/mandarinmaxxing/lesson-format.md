# Lesson format

How each message of a lesson looks. Take the words for lesson, part, review, round and the rest from **Labels** and **Rounds** in `course.md`, and lesson names from its **Lessons** list.

## Titles and prompts

- **Title.** Each part opens with one bold line in the learner's language: `HSK 1 · Lesson 20 · At school · part 1 of 2`. Level first, no leading zero, and no "part 1 of 1" for a single-part lesson. When a part starts with the vocabulary table, the table's heading is the title and no line goes above it. When it starts with the review, the title opens the review and the table's heading repeats it.
- **Prompts.** The counter goes on its own bold line and the sentence to translate in plain text under it, after a blank line, never in a blockquote. In the review the counter counts the whole review: **Review 2 of 7**. In the rounds it names the round and counts to the round's total: **Round 2 · 3 of 4**. Open each round with one bold line naming it: **Round 2 · Full actions**. Say "Translate into Mandarin" before the first translation prompt of the review and before the first one of the rounds, and nowhere else.
- **Meaning and reply exercises**, in the first parts of a course, take the same counter. Say what to do in one short line before the first of each kind ("What does it mean?", "What do you answer?"). A meaning exercise shows the line as **Hanzi** and *pinyin*. A reply exercise shows the other person's line on three lines: Hanzi, pinyin, meaning.

## Mandarin, written the same way everywhere

Outside the vocabulary table: **Hanzi in bold**, *pinyin in italics*, meaning in plain text. Italics are for pinyin only. Never italicize or strike through Hanzi.

- **A chunk or a corrected sentence** takes three lines, with hard line breaks: the Hanzi, the pinyin, the meaning. Put the chunk list under one bold line with the label for useful phrases. When a word in a chunk can be swapped, say which in its meaning line, without giving the swap: round 1 is where the learner tries it. A breakdown, when the chunk has one, is a fourth line in plain text: 开车 = 开 (drive) + 车 (car).
- **A word inside a sentence** is written inline: **超市** (*chāoshì*, supermarket). A word known since earlier parts needs only the bold Hanzi, unless it is the point of the correction.
- **Reading texts** stay as plain Hanzi, with no pinyin.

## The vocabulary table

Draw the table with the chat's inline HTML or widget tool, in the conversation, never as an artifact or a file. Copy the block below character for character, including the `<script>` line, and change only the heading (the title line), the rows, and the column headers in the learner's language. Keep every Hanzi inside `<span lang="zh-Hans">`, one span per word. Add no `<style>` and no other script: the script line loads the table's look, its Hanzi font, the stroke-order animation the learner sees when they point at a word, and the word's sound when they click it. If the rendering tool has its own design guidance, this template still wins. If the chat can't show HTML, use a Markdown table with the Hanzi in bold, under a bold title line.

```html
<section id="mandarinmaxxing-vocab">
  <h2>HSK 1 · Lesson 13 · Shopping and paying · part 1 of 3</h2>
  <table>
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Meaning</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">商店</span></td><td>shāngdiàn</td><td>shop</td></tr></tbody>
  </table>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@v0.8.0/skills/mandarinmaxxing/web/vocab.js"></script>
```

Under the table, add a one-line usage note only for a word whose use the meaning can't show: two words that translate the same way (帮 and 帮忙), a word that needs a pattern (让 + person + verb), a word the exercises will use in a role the meaning doesn't show (不 alone as a reply: "no"), or a word whose tone changes in the chunks (不 is said *bú* before a fourth tone). Give a polite form a meaning that says who it is for, such as 您 = "you (to sir or madam)".

**Words that translate the same way** (没关系 and 没事, 中文 and 汉语): give each prompt a context that fits only one, or accept both. When the learner keeps choosing one, ask for the other by name in the next prompt that fits and again in the next part's review.

## Feedback on a translation

Plain Markdown. Blockquotes are reserved for showing back what the learner wrote.

- **Correct and natural.** Confirm briefly and go to the next prompt. For a right answer in pinyin, show the sentence in Hanzi on one line. Accept any natural version, including a standard variant such as 没有关系 for 没关系. If the accepted answer leaves out a new word of the part, or uses another expression than the chunk you were after, name the word or chunk in one line and bring it back as "After a correction" in `SKILL.md` says.
- **Right meaning, unnatural phrasing.** Say the meaning is right, show a more natural version with its pinyin, and explain the change briefly.
- **Incorrect.** In this order: a short opener and "You wrote:", then the learner's whole answer in a blockquote. One line per fix, pointing only at what went wrong: the word or chunk to use in bold, its pinyin in italics, a short reason; for word order, the stretch in the right order. Then the full corrected sentence once, on three lines. Then the next prompt. No breakdown of the parts the learner got right.

## Listening or reading

Use what **Audio** in `course.md` says, and only that. With a provider, read `audio.md`. With `none`, the step is the reading below. Don't offer the chat app's read aloud button in place of audio: it isn't made for Mandarin, and its tones can come out wrong.

### Reading

One message, in this order:

- A bold title with the label for reading and its number: **Reading 1**.
- The text: three to six short sentences in plain Hanzi, one person telling in the first person what they did, plan, or what happened. No dialogue, quoted lines, pinyin, or translation.
- A bold line such as **Your turn**, then the task: rewrite the text with a few changes you name (another day, another thing to buy, another price), chosen so the learner writes the part's new words again. No comprehension questions: the learner can see the text.

Correct the rewrite as a written translation. One text per part, with every new word that fits; a second only when the new words don't fit one scene.

## Close a part

One short message after the last exercise; it can share a message with the feedback on it.

- What comes next: "Next time: HSK 1, Lesson 11, part 3."
- One offer, as a single question. After the last part of a lesson with two or more parts: one line saying the lesson is complete, and the wrap-up role-play (it is described in `requests.md`). After any other part: starting the next part now.

No summary of the part.
