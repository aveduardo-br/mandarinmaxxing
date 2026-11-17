# Benchmark runner: one simulated session

You run one simulated session of the mandarinmaxxing skill and write it to files. You play two roles, the **tutor** and the **student**, in strict alternation. The point is to see whether the tutor follows the skill, so play the tutor exactly as Claude would with the skill installed, and play the student mechanically by the policy below.

## Setup

- Skill: `/home/claude/mandarinmaxxing/skills/mandarinmaxxing/` (read `SKILL.md` first, then `lesson-format.md` and the map, exactly when `SKILL.md` says to).
- Your output directory is given in your task. It contains a `course/` folder: that is the learner's working folder, where `course.md` lives (as when the skill runs in a coding agent). It may already hold a `course.md`.
- Write the session to `transcript.md` in the output directory as you go, and the final state to `course/course.md`.

## The tutor

- Follow `SKILL.md` and `lesson-format.md` as written. Don't use anything from this file to shape your teaching: the student policy below is hidden from the tutor.
- Environment: there is no HTML widget, so use the Markdown table fallback. The learner's voice provider is ElevenLabs with voice Sarah. Instead of calling a tool, write a line `[AUDIO CLIP · voice Sarah]` followed by the exact script in a fenced block with the language tag `audio-script`. That stands for the clip. Follow the rules on when the script may be shown.
- Benchmark-only addition: right after each translation prompt (review and rounds), add an HTML comment with the answer you expect, such as `<!-- expected: 我七点起床。 -->`. The student never sees it.
- Save `course.md` whenever the skill says to save.

## The student

A Brazilian learner who writes in Portuguese. Known words: the words in the **Done** log of the starting `course.md`, the jump start's words if the course says `Known: jump start` or the tutor offers to count them as known and the student accepts, and every word the tutor teaches during this session. Nothing else.

- Answers translation prompts in Hanzi, except every fourth answer, which is in tone-marked pinyin.
- Makes one real learner mistake in about every third answer: wrong word order, a missing or wrong measure word, a wrong word among those it knows, or a missing particle. Not on purpose-sounding; just the kind of slip a beginner makes.
- Never uses a word it doesn't know. If a prompt needs one, it answers what it can and adds `[NÃO SEI: <the Portuguese word>]`.
- For a dictation, writes what it "heard" from the script, with one slip. For a narration, answers the questions from the script with one wrong answer.
- Keeps replies short. Accepts or declines offers as the scenario says. When asked to choose another round or the listening step, chooses the listening step.

## Transcript format

```
## T1 · STUDENT
start mandarinmaxxing

## T2 · TUTOR
...the tutor's whole message...

## T3 · STUDENT
...
```

Number every turn. Copy every tutor message in full, including tables, the `audio-script` blocks and the `expected` comments. Don't summarize.

## When you finish

Write `run-notes.md` in the output directory: the scenario, the number of turns, and any place where an instruction in `SKILL.md` or `lesson-format.md` was unclear or where you weren't sure how to apply it, with the quote. Then reply with one line: `done <output directory> <number of turns>`.
