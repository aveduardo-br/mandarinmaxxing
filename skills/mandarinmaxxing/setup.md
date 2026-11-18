# Setup: starting a new course

Read this when there is no `course.md` yet.

## Is there a place to save?

If this chat can save a document where later chats will find it (a Claude project, or a working folder in a coding agent), go to the welcome message.

If it can't, for example a chat outside any project, send the message below in the learner's language and wait. Describe the steps without naming menus or buttons, since the app changes.

> Before we start, let's give your course a place to live. It takes a minute:
>
> 1. In Claude, create a new project, for example "Mandarin".
> 2. In the project's instructions, paste: `Use the mandarinmaxxing skill. My course is saved in course.md.`
> 3. Open a chat inside the project and write "start mandarinmaxxing".
>
> From then on I keep your progress myself, on any device. If you'd like to try it first, I can give you a trial lesson right here, without saving.

For the trial lesson, teach HSK 1, Lesson 1, part 1, at a pace of 5, without saving, and say at the end that the course starts once the project is set up.

## The welcome message

Write to the learner in the language they ask for, or the one they are writing in. With too little text to tell, use what the interface or what you know about them points to, or ask in one short line first. Don't offer to switch.

Send one setup message, localized from the example below. Ask only for the choices the learner hasn't given, and go on once they are clear: a pace of 5 and no audio when they leave those open.

> **Welcome to mandarinmaxxing!**
>
> The words are the same as the official HSK. What changes is the order: instead of a list, you learn by situation. Saying hello, introducing yourself, ordering food, shopping. Each lesson teaches a few words inside ready-to-use phrases, has you translate from your language into Mandarin with feedback right away, and brings older words back so you don't forget them.
>
> The course is yours. Below are my suggestions, and you can change anything, now or later.
>
> **1. Level**
> Starting from zero? I suggest HSK 1, lesson 1. If you've studied before, tell me the level or the lesson you want to pick up from.
>
> **2. Pace**
> How many new words each time you study? 3 is light, **5 is what I recommend**, 7 is intense. If you'd rather have another number, just say so.
>
> **3. Audio** (optional)
> Each study session closes with listening practice. With audio, you hear a short dictation and a short story in a natural voice, without seeing them written: you write what you heard and answer what you understood. Most people use ElevenLabs, which has a free account, but you can bring another voice provider. Without audio, you read the text and there's nothing to set up. Do you want audio?
>
> **Keyboard.** You'll answer in Mandarin from the first lesson. You can start by typing in pinyin to get practicing right away. When you want the next step, turn on the Chinese keyboard (Pinyin, Simplified): you type the sound and pick the character.

Keep this structure, order, and length: the two opening paragraphs, three numbered headings each on its own line with its text below (use a hard line break), and the keyboard note. Name the learner's own language where the example says "your language". Don't mention fonts: the table loads its own.

**Audio.** If the learner wants audio, they connect a text-to-speech provider to the chat themselves, usually ElevenLabs through its connector. If it isn't connected yet, tell them how, use reading meanwhile, and switch once it appears. Save the choice in **Audio**.

## Show the level and agree on the route

Read the map, then show a compact overview before the first part:

- The number of lessons and the total number of parts at the learner's pace, from the map header, and what that means in weeks at one part a day, about an hour each. Present it as an estimate. Say once, in one sentence, that each lesson is one situation studied a part at a time, and that the pace is a target: a part brings about that many new words, sometimes one or two more or fewer.
- The jump start, when the level has one: the lessons every later lesson depends on, taught first and in order.
- The other lessons, in map order.

Write both lists as bullets, one lesson per line: the map's two-digit number in bold, the lesson name, and its number of parts at the learner's pace from the `Split` line, such as `- **08** Phone calls (1 part)`. Never a numbered list, which adds a second set of numbers. This list is the source of truth for the whole course: never renumber it.

Then:

1. Save `course.md` in the shape given in `SKILL.md`: the settings, the route in map order, the full lesson list in the learner's language, and `Next` at part 1 of the first lesson.
2. Add one sentence on what they can ask for at any time: review a lesson, change the pace, an extra reading with only the words they know, or flashcards of a part's words.
3. Ask whether they want to move any lesson earlier or later. Only lessons after the jump start can move. A learner who has studied before can start at a later lesson: "start at 19" puts Lesson 19 first, and it is still called Lesson 19 (see "Another lesson" in `requests.md`). Save again if the route changes.

Start the first part once the learner agrees.
