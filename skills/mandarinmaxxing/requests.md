# Requests: anything other than the next part

Read this when the learner asks for something other than the next part. Every change to the course goes through a `course.py` command, which writes `course.md`; put the file back where the course is kept after it.

## Another lesson

- **Practising a lesson or part** ("let me practise Lesson 9 again"). `python3 course.py part <course.md> plan.txt --lesson 9 --part 1` gives its brief. It is practice: there is nothing to close.
- **Going to another lesson** ("go to Lesson 22", "start at 19"). Run `python3 course.py jump <course.md> 22`: the lesson goes first on the route, keeps its number, and the lessons jumped over follow it. Say in one line what comes after it, without waiting for an answer.

## Skip lessons the learner already knows

Where to start is the learner's choice: the first lesson, the middle of the jump start, or any lesson after it. When a jump leaves jump-start lessons unstudied, the command lists them. Name those lessons, with a few of the words each one teaches (`python3 course.py overview <level> <pace>` has them), and ask once which of them the learner already knows.

- **The ones they know:** run `python3 course.py known <course.md> 01 02` with their numbers. Do the same for any other lesson the learner says they know. Their words count as met, and the brief of each part lists them so you can remind the learner.
- **The ones they don't:** those jump-start lessons come first, before the lesson they asked for: the later lessons are built on their words. Run `python3 course.py jump` to the first of them.

A lesson marked `(known)` can still be studied later: `python3 course.py study <course.md> 03` puts it back, first on the route, at its first part not yet studied.

## Review a lesson

Use the lesson's lines in the **Done** log: a review-style set of prompts for its words, at the level of the course, one prompt per word and ten at most; in a longer lesson, take the words by turn across its lines. For extra practice on one point, give more prompts on it during the lesson.

## Change the pace

Run `python3 course.py pace <course.md> 7` (3, 5 or 7). It takes effect at the next lesson: a lesson already begun finishes at the old pace. Tell the learner the new number of parts it prints.

## Change the audio

Run `python3 course.py audio <course.md> none`, or with the provider and voice in place of `none`. Turning it on follows "Audio" in `setup.md`; turning it off takes effect at the next listening step.

## Change the level

Changing level replaces the route, so confirm it first in one line: the course moves to the new level, and the words already studied keep coming back. When the learner confirms, follow the steps of "When a level ends" in `levels.md`; if they want to start at another lesson, run `course.py jump` after it. Words of the levels below the new one count as met.

## The course screen

When the learner writes "setup" or "/setup", read `setup.md` and send the course screen described at its end.

## Back after a break

When the learner says they have been away for weeks, offer a review of the last two or three lessons studied, then go on from **Next**. They decide.

## Wrap-up role-play

Offered once, in the close of the last part of a lesson with two or more parts. When the learner accepts, now or in a later chat, set the scene in one line in their language, then play the other person in the lesson's situation: write in Mandarin with the meaning under each line, and let the learner reply in Mandarin, for four to six turns that call on blocks from every part of the lesson. Accept any natural reply, not only the one you expected, and correct the rest as a written translation. Close it in one line and offer the next part. If the learner moves on instead, don't bring it up again.

## Extra reading

A short text in the reading format of `lesson-format.md`, written only with met words, with a rewrite task.

## Flashcards

The words of the parts asked for, and their chunks, in one code block with one card per line: Hanzi, a tab, pinyin, a tab, meaning in the learner's language. Say in one line that it can be saved as a text file and imported into Anki or another flashcard app.
