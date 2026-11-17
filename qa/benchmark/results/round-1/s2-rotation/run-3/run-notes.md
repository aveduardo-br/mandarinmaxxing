# Run notes: s2-rotation, run-3

- Scenario: s2-rotation (starting course.md: 25 parts done, next Lesson 11 part 2 of 4; first message "próxima aula").
- Turns: 50 (T1 to T50, 25 student, 25 tutor). Part taught: HSK 1, Lesson 11, part 2 (早 起床 上午 晚 时候 下午).
- Final state: course.md has Done line `1-11.2`, Next: Lesson 11, part 3 of 4, To reinforce: 不在家 去朋友家.
- Older words by turn: line 3 back (1-10.1, six words) gave 月 号; line 7 back (1-07.3, six words) gave 爱 家人; line 14 back (1-05.1) gave 朋友; lines 30 and 60 not reached. Total five, under the limit of six.

## Unclear points in the skill

1. Older-word turns for lines with more than five words. Quote: "Line 3 back gives its 1st word, 7 back its 2nd, 14 back its 3rd... A line with more than five words gives two words per visit: the 1st and 2nd, then the 3rd and 4th". I read this as: at 3 back, words 1-2; at 7 back, words 3-4; at 14 back, words 5-6. Not sure whether "visit" means distance slot (as I did) or a count of earlier visits; with no tracking the two readings can differ.
2. Review total changing mid-review. Quote: "If an answer needs a hint or correction, ask the learner to use the target again in a fresh prompt after another question" together with "at least five and at most ten" and the counter "counts the whole review". I started with "de 5", added a sixth retry prompt after the first correction, and switched the counter to "de 6" from Review 4. Unsure whether the total should be fixed up front.
3. To reinforce. Quote: "remove the items the learner used correctly without help during that part, then add the new ones at the end. An item stays until it is answered right". Unclear whether a slip that was corrected and then answered right in a bring-back prompt in the same part still counts as new. I added only items not retried correctly afterwards (不在家, 去朋友家) and dropped 几点 and 没关系, which were answered correctly without help.
4. Student answer counting for the policy (every fourth answer in pinyin, a slip about every third). I counted translation prompts only, starting at review 1, and kept dictation/narration separate with one slip each.
5. Table fallback. Quote: "Use bold Hanzi when the interface supports standard text formatting only." The runner says Markdown table, so I used bold Hanzi and put the title in a bold line above the table.
6. Clip titles. lesson-format.md gives English examples (Dictation 1, Audio 1 · scene); the Labels line has no word for dictation or audio, so I used "Ditado 1" and "Áudio 1 · Domingo em casa".
7. Closing. "Send one short closing message after the last exercise" does not say whether the final feedback and the closing share a turn. I put the narration feedback, script and closing line in one tutor turn (T50) because no student turn can come between them.
8. The audio-script fenced block for the dictation stood in for the clip, as the runner says. The dictation script was therefore visible in the transcript but is not part of the message the student "reads"; the student was given the script as the runner states.
