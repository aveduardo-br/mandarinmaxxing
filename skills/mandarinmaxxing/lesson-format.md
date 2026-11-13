# Lesson format

Formats for the parts of a lesson. Read this once per chat, before the first lesson message.

## Label lessons and prompts

- **Title.** Open each part with one bold line in this shape, in the learner’s language: `Lesson 20 · At school · part 1 of 2`. The lesson number is the map’s and never changes. Leave out “part 1 of 1” when a lesson has a single part.
- **No commentary on the plan.** State the title and teach. Leave out remarks about how the lesson is divided, why a part has the number of words it has, or what the map says.
- **Same words every time.** Use one word for “lesson”, one for “part”, and one name for each lesson through the whole course. Reuse the wording already in `course.md`.
- **Prompts.** In review and written translation, put the counter on its own bold line, such as **Review 1 of 5** or **Exercise 3 of 7**, and the sentence to translate in a blockquote under it. Say “Translate into Mandarin” only before the first prompt of each part of the lesson.

## Write Mandarin the same way everywhere

Outside the vocabulary table, every piece of Mandarin follows one pattern: **Hanzi in bold**, *pinyin in italics*, meaning in plain text.

- A chunk or a corrected sentence takes three lines: the Hanzi in bold, the pinyin in italics under it, and the meaning in the learner’s language under that.
- A word inside a sentence is written inline: **超市** (*chāoshì*, supermarket).
- Dialogue lines for reading or listening stay as plain Hanzi, with no pinyin.
- Never italicize or strike through Hanzi.

## Format each vocabulary table

Use the selectable HTML table below whenever the chat can display it alongside the message. Copy the whole block character for character, including the `<style>` with its `@font-face` rule. Change only three things: the heading, the rows, and the localized column headers. The heading is the lesson title line, such as `Lesson 10 · Dates and weekdays · part 1 of 2`. Keep every Hanzi inside `<span lang="zh-Hans">`. If the tool that renders the table comes with its own design guidance, this template still wins: don’t restyle it, simplify it, or drop the font.

The Hanzi use a handwriting-style Kaiti in mainland standard forms, so the first shape the learner sees is close to what they will write in a notebook. The font loads from the web, or from the learner’s computer when it is installed there.

```html
<section id="mandarinmaxxing-vocab">
  <h2>Lesson 13 · Shopping and paying · part 1 of 3</h2>
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

If the chat can’t embed HTML, use a selectable Markdown table in the message. Enlarge Hanzi through inline math where rendering and selection are confirmed, for example `$\LARGE\text{公交车}$` in Codex desktop. Use bold Hanzi when the interface supports standard text formatting only.

## Respond to a written translation

Use plain Markdown for all feedback and the Mandarin pattern above. Quote the learner’s wrong word or chunk as plain text, so the bold replacement stands out.

- **Correct and natural.** Confirm briefly and move to the next prompt. Accept any natural version that meets the request. If a valid alternative uses a different expression, acknowledge it and bring the intended chunk back in a later prompt.
- **Correct meaning, noticeably unnatural phrasing.** Acknowledge that the meaning is right. Show a more natural version in Hanzi with pinyin directly below it and briefly explain the change.
- **Incorrect.** Point at the part that went wrong and nothing else: quote the word or chunk the learner wrote, give the one to use in its place with pinyin and meaning, and add a short reason when it helps, in the shape “you wrote X, use Y”. Then show the full corrected sentence once. Leave out a word-by-word breakdown of the parts the learner got right.

## Prepare each dialogue

1. **Draft the script.** Give the two speakers a practical reason to talk and write short turns that respond to each other. Aim for around 20 seconds at a clear speaking pace. Let the length vary with the conversation and split crowded scenes.
2. **Review before generating.** Read the full exchange. Check that the turns make sense together, the Mandarin sounds natural, the intended chunks fit the scene, and the questions can be answered from what’s said. Revise awkward or overloaded lines before sending the script to the provider.

If an authorized provider can deliver audio, generate the clip and share it with the full question set so the learner can read it before playback. Label clips by number and scene, for example **Audio 01 · At the train station**. Include the duration if the provider reports it.

If no provider is available, switch to **Reading practice** without comment, apart from the one-time note described in the setup. Show the conversation directly in the chat in Hanzi only, followed by the full question set.
