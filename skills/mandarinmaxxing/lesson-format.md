# Lesson format

Formats for the parts of a lesson. Read this once per chat, before the first lesson message.

## Format each vocabulary table

Use the selectable HTML table below whenever the chat can display it alongside the message. Replace the heading and sample row with the lesson title and vocabulary. Localize the meaning header and the font notice. Keep the markup, sizes, and font rules as written.

The Hanzi use a handwriting-style Kaiti in mainland standard forms, so the first shape the learner sees is close to what they will write in a notebook. The table uses the font from the learner's computer when it is installed and otherwise loads it from the web. The notice appears only when neither works.

```html
<section id="mandarinmaxxing-vocab" aria-labelledby="mandarinmaxxing-vocab-title">
  <h2 id="mandarinmaxxing-vocab-title">Shopping and paying</h2>
  <table class="table">
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Meaning</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">商店</span></td><td>shāngdiàn</td><td>shop</td></tr></tbody>
  </table>
  <p id="mandarinmaxxing-font-notice" role="status" hidden>Using the system font for Hanzi because the handwriting-style font could not load.</p>
</section>
<style>
  @font-face {
    font-family: "Mandarinmaxxing Kaiti";
    src: local("LXGW WenKai GB"), local("LXGW WenKai GB Lite"),
      url("https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@338b81599301cc40b92b882af7d7e301efa15c7b/skills/mandarinmaxxing/fonts/kaiti-hsk-1-6.woff") format("woff");
    font-style: normal;
    font-weight: 400;
    font-display: swap;
  }
  #mandarinmaxxing-vocab { --mmx-soft: var(--text-secondary, color-mix(in srgb, currentColor 65%, transparent)); --mmx-line: var(--border, color-mix(in srgb, currentColor 15%, transparent)); padding: 4px 0 24px; }
  #mandarinmaxxing-vocab h2 { font-size: 16px; font-weight: 500; margin: 0 0 8px; }
  #mandarinmaxxing-vocab table { width: 100%; border-collapse: collapse; }
  #mandarinmaxxing-vocab th, #mandarinmaxxing-vocab td { text-align: left; padding: 10px 64px 10px 0; border-bottom: 1px solid var(--mmx-line); vertical-align: middle; }
  #mandarinmaxxing-vocab th { font-size: 13px; font-weight: 500; color: var(--mmx-soft); }
  #mandarinmaxxing-vocab td { font-weight: 400; user-select: text; }
  #mandarinmaxxing-vocab th:nth-child(-n+2), #mandarinmaxxing-vocab td:nth-child(-n+2) { width: 1%; white-space: nowrap; }
  #mandarinmaxxing-vocab td:nth-child(2) { color: var(--mmx-soft); }
  #mandarinmaxxing-vocab td span[lang="zh-Hans"] {
    font-family: "Mandarinmaxxing Kaiti", "Kaiti SC", "STKaiti", "KaiTi", serif;
    font-size: 32px;
    font-weight: 400;
    line-height: 1.2;
    font-synthesis: none;
    white-space: nowrap;
  }
  #mandarinmaxxing-font-notice { font-size: 13px; color: var(--mmx-soft); margin: 12px 0 0; }
</style>
<script>
  (() => {
    const table = document.getElementById('mandarinmaxxing-vocab');
    const notice = document.getElementById('mandarinmaxxing-font-notice');
    if (!document.fonts?.load) return;
    const hanzi = Array.from(table.querySelectorAll('td span[lang="zh-Hans"]'), cell => cell.textContent).join('');
    document.fonts.load('32px "Mandarinmaxxing Kaiti"', hanzi).then(
      faces => { if (!faces.some(face => face.status === 'loaded')) notice.hidden = false; },
      () => { notice.hidden = false; }
    );
  })();
</script>
```

If the chat can’t embed HTML, use a selectable Markdown table in the message. Enlarge Hanzi through inline math where rendering and selection are confirmed, for example `$\LARGE\text{公交车}$` in Codex desktop. Use bold Hanzi when the interface supports standard text formatting only.

## Respond to a written translation

For a model or corrected sentence, use a native Markdown subheading for the Hanzi, with tone-marked pinyin directly below in normal text. Use plain Markdown for all feedback: quote the learner’s wrong word or chunk as plain text and bold the replacement. Never strike through Hanzi, since the line reads as an extra stroke. Whenever you gloss individual words or chunks, put the pinyin beside each Hanzi item before its meaning.

- **Correct and natural.** Confirm briefly and move to the next prompt. Accept any natural version that meets the request. If a valid alternative uses a different expression, acknowledge it and bring the intended chunk back in a later prompt.
- **Correct meaning, noticeably unnatural phrasing.** Acknowledge that the meaning is right. Show a more natural version in Hanzi with pinyin directly below it and briefly explain the change.
- **Incorrect.** Point at the part that went wrong and nothing else: quote the word or chunk the learner wrote, give the one to use in its place with pinyin and meaning, and add a short reason when it helps, in the shape “you wrote X, use Y”. Then show the full corrected sentence once. Leave out a word-by-word breakdown of the parts the learner got right.

## Prepare each dialogue

1. **Draft the script.** Give the two speakers a practical reason to talk and write short turns that respond to each other. Aim for around 20 seconds at a clear speaking pace. Let the length vary with the conversation and split crowded scenes.
2. **Review before generating.** Read the full exchange. Check that the turns make sense together, the Mandarin sounds natural, the intended chunks fit the scene, and the questions can be answered from what’s said. Revise awkward or overloaded lines before sending the script to the provider.

If an authorized provider can deliver audio, generate the clip and share it with the full question set so the learner can read it before playback. Label clips by number and scene, for example **Audio 01 · At the train station**. Include the duration if the provider reports it.

If no provider is available, switch to **Reading practice** without comment, apart from the one-time note described in the setup. Show the conversation directly in the chat in Hanzi only, followed by the full question set.
