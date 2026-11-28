# Benchmark runner with a fixed student

One simulated session of the skill, where the learner's answers are not the tutor's to choose. Use it in place of `runner.md` when comparing versions.

## Setup

- Skill: the folder given in your task (read `SKILL.md` first, then the other files exactly when it says to, and none it tells you not to read).
- Output directory: given in your task. Its `course/` folder is where the learner's `course.md` is kept: a real folder where code runs, which later chats find.
- Write the session to `transcript.md` as you go.

## The tutor

- Play the tutor exactly as Claude would with the skill installed. Run every script the skill tells you to, for real, with full paths.
- The chat shows inline HTML: write the HTML the tutor would send in a fenced `html` block. For a click on a card's button, work out from `web/setup.js` the message it sends.
- Audio, when the course has it: don't generate anything. Write `[AUDIO CLIP · voice <name>]` and the script in a block tagged `audio-script`.
- After each exercise, add a comment with the answer you expect: `<!-- expected: 我七点起床。 -->`.

## The student

The student is `qa/benchmark/student.py` in the repository. For every exercise, in the review, the rounds, the dictation and the reading task alike:

1. Count it: N is 1 for the first exercise of the session and goes up by one each time, across parts and chats.
2. Run `python3 <path>/student.py N "<the answer you expect>"`.
3. The learner's message is exactly what it prints. Don't soften it, complete it or skip it.

What the learner says at other moments (accepting an offer, asking for something) is fixed by the scenario. When the scenario is silent, the learner takes the first option offered.

## Transcript format

```
## T1 · STUDENT
start mandarinmaxxing

## T2 · TUTOR
...the tutor's whole message...
```

## Notes

Write `notes.md` with: every script run with its output; where the skill's text was unclear, silent or contradictory, with the file and sentence; rules you could not satisfy, with the case; Mandarin a mainland speaker would not say, and what caused it; how the tutor handled each kind of student reply (the grammar question, the natural alternative, the missing word, pinyin, the wrong order, "I don't know"); exercises per step and estimated minutes.
