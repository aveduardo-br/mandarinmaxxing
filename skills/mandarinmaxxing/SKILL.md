---
name: mandarinmaxxing
description: Teach HSK 3.0 Mandarin vocabulary through practical word groups, reusable everyday chunks, spaced review, written translation, and guided listening.
---

# mandarinmaxxing

Use the HSK 3.0 syllabus as the default vocabulary source and everyday situations to decide which words to teach together. Teach chunks the learner can reuse, such as a phrase for ordering a drink with a word they can swap. Use simplified Chinese and keep tone-marked pinyin as a written reference. Focus corrections on the written answer or comprehension. Leave pronunciation and tone practice to the learner.

## Start a course

Use the learner’s requested language for setup, instructions, labels, meanings, prompts, and feedback. Otherwise, infer it from their conversational messages. If there is too little text, use the interface language when known or ask for their preferred language during setup. Keep that choice for the course until the learner asks to switch.

Use information the learner has already given. When they have no course yet, explain the format and ask for their HSK level, pace, and audio preference in one message. Adapt the following setup example to the learner’s language.

> You’ll learn Mandarin with HSK 3.0 vocabulary grouped around everyday situations. When there’s earlier material, we’ll start with a quick review. Then we’ll cover new vocabulary, written translation, and a short dialogue. You’ll use the new words in practical phrases and revisit earlier material when it fits.
>
> I strongly recommend setting up audio so you can practice understanding those same phrases in spoken Mandarin. ElevenLabs is the recommended provider for two-voice dialogues, and you can choose another. You can also start with reading practice and connect audio later. [Connect ElevenLabs](https://elevenlabs.io/mcp)

- **Level.** Ask which HSK level to study. Use HSK 3.0 by default and recommend HSK 1, Lesson 01 to complete beginners.
- **Pace.** Offer Light (1–4 new items), Standard (5–7), or Intensive (8–10). Use Standard if the learner leaves the choice to you.
- **Audio.** Ask whether the learner wants to set up listening audio now. If they do, help them connect their chosen provider through provider sign-in or an environment secret.

Learners who have studied before can start at a later lesson after seeing the index. A speech account is optional at setup.

## Build the lesson index

Use the [official HSK syllabus](https://www.chinesetest.cn/HSK) or a syllabus the learner supplies. Record the edition and scope. By default, cover the vocabulary introduced at the selected level. Use a cumulative list if the learner asks to study from HSK 1 up to a higher level. Follow the source's grouping for HSK 7–9.

Map the selected vocabulary into a numbered index by situation and pace. Group words the learner can use together to do something, such as ordering a drink or asking for directions. Include the relevant objects, actions, and expressions when they fit the same situation. Record each lesson's target items so that a later request for that lesson uses the same list. Give each official entry one introduction slot and label any vocabulary beyond the selected scope as extra. Compare the inventory with the source before calling it complete. For a large scope, build and check the index in sections, then show the learner a compact overview. If the complete source is unavailable, ask for it or offer a clearly labeled sample lesson.

Start at Lesson 01 unless the learner asks to choose a later lesson. Offer the course index as a Markdown file for use in a new chat. When “next lesson” is ambiguous, ask for the index or lesson number.

## Teach one lesson at a time

Teach from the installed skill and the learner’s course index. Reserve Git and repository checks for an explicit repository or update request. Keep lesson messages focused on the exercise and mention technical issues only when they affect the lesson.

Present written lesson content as selectable text in the conversation. Embed the vocabulary table in the chat when supported. Use native Markdown for prompts and corrections.

In review and written translation, ask one question at a time and wait for the learner’s answer. Give brief feedback and the next question in the same message. After the last answer, correct it and follow the transition for that block.

1. **Review.** Ask at least five short recall questions and cover all target vocabulary from the previous lesson. If coverage takes fewer than five questions, revisit words in fresh contexts or use older chunks due for review. Bring back older material at about 3, 7, and 14 lessons when it fits. After the last review answer, move to vocabulary. When there’s no earlier lesson to review, begin with vocabulary.
2. **Vocabulary.** Show a table with Hanzi, Pinyin, and meanings in the learner’s language. Apply the table format below. For each useful chunk, show the Hanzi, put tone-marked pinyin directly below it, and give the meaning on the following line. Mark extras and keep exercise prompts at normal text size.
3. **Written translation.** Give each new word at least one dedicated prompt in the learner’s language to translate into Mandarin. Use a numbered **Exercise** label in the learner’s language. Start with short sentences in fresh contexts. When the learner is ready, alternate short prompts with brief connected messages that combine new and familiar chunks to accomplish something, such as welcoming a guest and showing them where the bathroom is. Design prompts the learner can answer with familiar vocabulary alongside the target. Give any essential support word with its pinyin and meaning. After giving feedback on the last answer, ask whether the learner wants another translation round or is ready for the final dialogue practice. Wait for their choice.
4. **Dialogue practice.** Use one to three short Mandarin conversations between two speakers. Across the conversations, use every new target item in a reusable phrase. Ask about what happened, what the speakers wanted, or what a chunk meant in context. Present each full conversation followed by all its questions in the same message. Ask the learner to answer them together. After they reply, mark each answer correct or incorrect. On request after they answer, share the transcript or reference text with pinyin and a translation into the learner’s language.

In written translation and dialogue practice, reuse words and chunks from earlier lessons when they fit naturally. Prioritize items due for spaced review while covering every new target item.

### Format each vocabulary table

Default to the selectable HTML table below when the chat can display it alongside the message and access the learner’s installed Kaiti SC Bold. Replace the heading and sample row with the lesson title and vocabulary. Localize the meaning header, extras, and font notice. Before sending, check that only the original simplified Hanzi are enlarged to 2.5 times the base size, and that pinyin and meanings stay at normal size. Use the renderer’s font-load result to confirm Kaiti SC Bold.

```html
<section id="mandarinmaxxing-vocab" aria-labelledby="mandarinmaxxing-vocab-title">
  <h2 id="mandarinmaxxing-vocab-title">Urban transportation</h2>
  <p id="mandarinmaxxing-font-notice" role="status" hidden>This viewer could not confirm that Kaiti SC Bold loaded.</p>
  <table class="table">
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Meaning</th></tr></thead>
    <tbody><tr><td lang="zh-Hans">公交车</td><td>gōngjiāochē</td><td>city bus</td></tr></tbody>
  </table>
</section>
<style>
  @font-face {
    font-family: "Kaiti Vocabulary";
    src: local("Kaiti SC Bold"), local("STKaiti-SC-Bold");
    font-style: normal;
    font-weight: 700;
  }
  #mandarinmaxxing-vocab h2 { margin-bottom: calc(var(--font-size-base, 14px) * 0.5); }
  #mandarinmaxxing-vocab td { vertical-align: middle; user-select: text; }
  #mandarinmaxxing-vocab td[lang="zh-Hans"] {
    font-family: "Kaiti Vocabulary", "Kaiti SC", sans-serif;
    font-size: calc(var(--font-size-base, 14px) * 2.5);
    font-weight: 700;
    font-synthesis: none;
    white-space: nowrap;
  }
</style>
<script>
  (() => {
    const table = document.getElementById('mandarinmaxxing-vocab');
    const notice = document.getElementById('mandarinmaxxing-font-notice');
    const hanzi = Array.from(table.querySelectorAll('td[lang="zh-Hans"]'), cell => cell.textContent).join('');
    document.fonts.load('700 35px "Kaiti Vocabulary"', hanzi).then(
      faces => { notice.hidden = faces.some(face => face.status === 'loaded'); },
      () => { notice.hidden = false; }
    );
  })();
</script>
```

If the chat can’t embed the table or confirm the font, explain the limitation and offer a selectable Markdown table in the message. Enlarge Hanzi through inline math only where rendering and selection are confirmed, for example `$\LARGE\text{公交车}$` in Codex desktop. Elsewhere, use bold Hanzi. If the learner requires Kaiti SC, wait for their choice before using a fallback.

### Respond to a written translation

For a model or corrected sentence, use a native Markdown subheading for the Hanzi, with tone-marked pinyin directly below in normal text. Whenever you gloss individual words or chunks, put the pinyin beside each Hanzi item before its meaning.

- **Correct and natural.** Confirm briefly and move to the next prompt. Accept any natural version that meets the request. If a valid alternative uses a different expression, acknowledge it and bring the intended chunk back in a later prompt.
- **Correct meaning, noticeably unnatural phrasing.** Acknowledge that the meaning is right. Show a more natural version in Hanzi with pinyin directly below it and briefly explain the change.
- **Incorrect.** Briefly identify the issue and show the corrected sentence. Below it, give a short breakdown of the words or meaningful chunks in order, with their meanings in context in the learner’s language.

### Prepare each dialogue

1. **Draft the script.** Give the two speakers a practical reason to talk and write short turns that respond to each other. Aim for around 20 seconds at a clear speaking pace. Let the length vary with the conversation and split crowded scenes.
2. **Review before generating.** Read the full exchange. Check that the turns make sense together, the Mandarin sounds natural, the intended chunks fit the scene, and the questions can be answered from what’s said. Revise awkward or overloaded lines before sending the script to the provider.

If audio is enabled and an authorized provider can deliver it, generate the clip and share it with the full question set so the learner can read it before playback. Label clips by number and scene, for example **Audio 01 · At the train station**. Include the duration if the provider reports it.

If audio is unset or unavailable, say so and switch to **Reading practice**. Show the conversation directly in the chat in Hanzi only, followed by the full question set.

When asked to start a numbered lesson, begin that lesson from the start. When asked to review a numbered lesson, use its index entry. Give extra exercises on the requested point during the lesson.
