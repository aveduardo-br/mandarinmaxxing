# Setup: starting a course, and the course screen

Read this when there is no `course.md` yet, or when the learner writes "setup" (or "/setup") in a course that exists: then go to "The course screen" at the end.

## Is there a place to save?

If this chat can save a document where later chats will find it (a Claude project, or a working folder in a coding agent), go to the welcome card.

If it can't, for example a chat outside any project, send the message below in the learner's language and wait. Describe the steps without naming menus or buttons, since the app changes.

> Before we start, let's give your course a place to live. It takes a minute:
>
> 1. In Claude, create a new project, for example "Mandarin".
> 2. In the project's instructions, paste: `Use the mandarinmaxxing skill. My course is saved in course.md.`
> 3. Open a chat inside the project and write "start mandarinmaxxing".
>
> From then on I keep your progress myself, on any device. If you'd like to try it first, I can give you a trial lesson right here, without saving.

For the trial lesson, teach HSK 1, Lesson 1, part 1, at a pace of 5, without saving, and say at the end that the course starts once the project is set up.

## The welcome card

Write to the learner in the language they ask for, or the one they are writing in. "start mandarinmaxxing" and the pasted project line say nothing about their language. With too little text to tell, use the language of the interface, of the project's name, or of what you know about the learner, and ask in one short line only if none of these tells. Don't offer to switch.

Send the card below as the whole setup message, drawn with the chat's inline HTML or widget tool, in the conversation, never as an artifact or a file. Copy it character for character, including the `<script>` line, and change only the text: translate every visible text into the learner's language, and the `data-value` and `data-note` texts with it. Keep `for Claude`, the name mandarinmaxxing, and every tag and attribute as they are. Add no `<style>` and no other script: the script line loads the card's look, the banner, and what the buttons do. If the rendering tool has its own design guidance, this template still wins.

```html
<section id="mandarinmaxxing-setup">
  <div data-wordmark="ascii">for Claude</div>
  <h2>Welcome to mandarinmaxxing!</h2>
  <p>The same HSK words, reorganized around everyday conversations. You learn one situation at a time (saying hello, ordering food, shopping), you answer in Mandarin from the first lesson, and your progress is saved from one chat to the next.</p>
  <p>Choose your level and pace below. Nothing here is final: type "setup" to come back to this screen.</p>
  <h3>Before you start</h3>
  <details><summary>What does a lesson look like?</summary>
    <p>A review of last time, new words inside ready-to-use phrases, three rounds of translation from your language into Mandarin with feedback right away, and a listening or reading step to close. About an hour.</p>
  </details>
  <details><summary>Do I need audio?</summary>
    <p>No. With audio, you hear a short dictation and a short story in a natural voice, through your own ElevenLabs account, which has a free plan. Without audio, you read a text instead and there's nothing to set up.</p>
  </details>
  <details><summary>How do I type Chinese?</summary>
    <p>You answer in Mandarin from the first lesson. You can start in pinyin and, when you want, turn on the Chinese keyboard (Pinyin, Simplified): you type the sound and pick the character.</p>
  </details>
  <h3>Your choices</h3>
  <fieldset><legend>Level<small>HSK</small></legend>
    <button data-on data-value="HSK 1">1</button><button data-value="HSK 2">2</button><button data-value="HSK 3">3</button><button data-value="HSK 4">4</button><button data-value="HSK 5" data-note="HSK 5 isn't mapped yet. Its lessons are built on the spot from the official word list: it takes a few minutes the first time and can come out rougher than levels 1 to 4.">5</button><button data-value="HSK 6" data-note="HSK 6 isn't mapped yet. Its lessons are built on the spot from the official word list: it takes a few minutes the first time and can come out rougher than levels 1 to 4.">6</button>
  </fieldset>
  <fieldset><legend>Pace<small>new words a day</small></legend>
    <button>Light<small>about 3</small></button><button data-on>Recommended<small>about 5</small></button><button>Intense<small>about 7</small></button>
  </fieldset>
  <fieldset><legend>Audio</legend>
    <button data-on data-value="off, reading instead">Off</button><button data-value="on, with ElevenLabs">On<small>ElevenLabs</small></button>
  </fieldset>
  <button data-start>See my lessons</button>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@1aabecc2fa8efb78a801b0764149745900aaa09e/skills/mandarinmaxxing/web/setup.js"></script>
```

- `data-on` marks the choice that starts selected: HSK 1, recommended, audio off. If the learner already named a level, a pace or audio, move `data-on` to what they said.
- Name the learner's own language where the card says "your language".
- The button sends the three choices as a message, such as `Level: HSK 1. Pace: Recommended (about 5). Audio: off, reading instead.` A learner can also just type them: take either, and go on once level, pace and audio are clear, with recommended and no audio for whatever they leave open.
- Save light, recommended and intense as a **Pace** of 3, 5 and 7, and any other number as the learner gives it.
- For HSK 5 or 6, read `levels.md` before the overview.

**Where the chat can't show HTML**, send the same content as plain text, in this order: the title, the two opening paragraphs, then three numbered questions (level, pace, audio) each with its options on the line below, and one line on the keyboard.

**Audio.** If the learner wants audio, they connect a text-to-speech provider to the chat themselves, usually ElevenLabs through its connector. If it isn't connected yet, tell them how, use reading meanwhile, and switch once it appears. Save the choice in **Audio**.

## Show the level and agree on the route

Read the map, then show a compact overview before the first part:

- The number of lessons and the total number of parts at the learner's pace, from the map header, and what that means in weeks at one part a day, about an hour each. Present it as an estimate. Say once, in one sentence, that each lesson is one situation studied a part at a time.
- The jump start, when the level has one: the lessons every later lesson depends on, taught first and in order.
- The other lessons, in map order.

Write both lists as bullets, one lesson per line: the map's two-digit number in bold, the lesson name, and its number of parts at the learner's pace from the `Split` line, such as `- **08** Phone calls (1 part)`. Never a numbered list, which adds a second set of numbers. This list is the source of truth for the whole course: never renumber it.

Then:

1. Save `course.md` in the shape given in `SKILL.md`: the settings, the route in map order, the full lesson list in the learner's language, and `Next` at part 1 of the first lesson.
2. Add one sentence on what they can ask for at any time: review a lesson, change the pace, an extra reading with only the words they know, or flashcards of a part's words.
3. Ask where they want to start and whether to move any lesson earlier or later. A learner starting from zero starts at Lesson 1. A learner who has studied before reads the list and picks the lesson to start from: "start at 19" puts Lesson 19 first, and it is still called Lesson 19 (see "Another lesson" in `requests.md`). Only lessons after the jump start can move. Save again if the route changes.

Start the first part once the learner agrees.

## The course screen

When a learner with a saved course writes "setup" or "/setup", send this card, filled from `course.md`. The same rules as the welcome card: copy it exactly, translate only the text.

```html
<section id="mandarinmaxxing-setup" data-home>
  <h2>Your course</h2>
  <p data-progress="10/58">HSK 1 · 10 of 58 parts done</p>
  <h3>Next lesson</h3>
  <p><b>Lesson 5 · Introduce someone</b> · part 2 of 3</p>
  <nav>
    <button data-primary data-send="continue my course">Continue</button><button data-send="I want to review a lesson">Review a lesson</button><button data-send="I want to jump to another lesson">Jump to a lesson</button>
  </nav>
  <h3>Settings</h3>
  <fieldset><legend>Level<small>HSK</small></legend>
    <button data-on data-value="HSK 1">1</button><button data-value="HSK 2">2</button><button data-value="HSK 3">3</button><button data-value="HSK 4">4</button><button data-value="HSK 5" data-note="HSK 5 isn't mapped yet. Its lessons are built on the spot from the official word list: it takes a few minutes the first time and can come out rougher than levels 1 to 4.">5</button><button data-value="HSK 6" data-note="HSK 6 isn't mapped yet. Its lessons are built on the spot from the official word list: it takes a few minutes the first time and can come out rougher than levels 1 to 4.">6</button>
  </fieldset>
  <fieldset><legend>Pace<small>new words a day</small></legend>
    <button>Light<small>about 3</small></button><button data-on>Recommended<small>about 5</small></button><button>Intense<small>about 7</small></button>
  </fieldset>
  <fieldset><legend>Audio</legend>
    <button data-on data-value="off, reading instead">Off</button><button data-value="on, with ElevenLabs">On<small>ElevenLabs</small></button>
  </fieldset>
  <button data-start data-lead="Change my course." data-same="Nothing changed yet.">Save changes</button>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@1aabecc2fa8efb78a801b0764149745900aaa09e/skills/mandarinmaxxing/web/setup.js"></script>
```

- `data-progress` is the parts done and the parts in the level, as two numbers: the **Done** lines of the current level, and the sum of the parts in the **Lessons** list. The script writes the percentage; don't write one yourself.
- The lesson line comes from **Next** and the **Lessons** list. With `Next: level complete`, say so in that line and make the first button offer the next level.
- Put `data-on` on the level, pace and audio the file holds. A pace other than 3, 5 or 7 gets no `data-on` in that group; name it in the group's small text.
- The three buttons at the top send their `data-send` text, translated: answer each as the request it is. "Continue" asks for the part in **Next**.
- "Save changes" sends only what the learner changed, after the line `Change my course.` Apply each change as `requests.md` says under "Change the pace", "Change the audio" and "Change the level".

Where the chat can't show HTML, send the same content as a short plain-text summary and ask what they want to change.
