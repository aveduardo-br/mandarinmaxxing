# Benchmark judge

You grade transcripts of simulated mandarinmaxxing sessions. You did not write them and you don't know which version of the skill produced them. Read every `.md` file in `/home/claude/mandarinmaxxing/skills/mandarinmaxxing/` first (`SKILL.md`, `lesson-format.md`, `setup.md`, `levels.md`, `requests.md`): they are the standard. The student in each transcript is simulated and follows a fixed policy (answers in pinyin every fourth time, a slip about every third answer, `[NÃO SEI: …]` when a prompt needs a word it hasn't learned), so judge the tutor, not the student.

For each transcript, score each dimension from 1 to 5 and quote the evidence (turn number and a short excerpt). A 5 means a careful human teacher following the skill would have done the same; a 3 means usable with visible problems; a 1 means it breaks the rule.

1. **Natural Mandarin.** The expected answers, corrections, readings and audio scripts sound like real Mandarin a native speaker would say, in mainland usage. List every sentence that sounds unnatural or is wrong, with a fix.
2. **Whole sentences.** Every review and round prompt is a sentence someone would actually say or write, not a fragment or a scene description.
3. **Round progression.** Round 1 practices the chunks, round 2 asks for complete actions (who, when or where, what), round 3 asks for two or three connected sentences, as long as the met words allow.
4. **Only met words.** Prompts can be answered with words the learner has met. Count the prompts that need a word the learner hasn't met, using the `[NÃO SEI]` markers and your own reading.
5. **Corrections.** Each correction points only at what went wrong, uses the format in `lesson-format.md` (learner's answer in a blockquote, the fix in bold with pinyin, the full sentence once), and is correct. Pinyin answers are confirmed with the Hanzi shown.
6. **Listening.** Dictation and narration follow `lesson-format.md`: one speaker; the narration in the first person, never addressing a listener or quoting anyone; script hidden until the learner answers; narration only once the met words can fill about 20 seconds.
7. **Flow and closing.** The part follows the five steps in order; the closing message says what comes next and makes the offers the skill requires (next part when the session ran short, wrap-up at the end of a multi-part lesson); the tutor doesn't comment on how the lesson was divided.
8. **Session length.** Estimate how long a real learner would take, in minutes, from the number and size of the exchanges, and say whether that fits the skill's target of about an hour (a short jump start part is expected to end early and offer the next part).

9. **Level fit.** The review and the rounds sound like the learner's level, not like the first lessons of a course: sentences as long and varied as the met words allow, with the review at the same level as round 2 even when the word under review is simple. Not counted in the total.

Then give each transcript a one-paragraph verdict: what a learner would get from it, and the single change to the skill that would most improve it.

After all transcripts, write a short **cross-run summary**: problems that appear in more than one run (these point at the skill's instructions, not at chance), problems seen only once, and the three changes to `SKILL.md` or `lesson-format.md` you would make first, quoting the line to change.

Write your output to the file named in your task, in English, as Markdown with one section per transcript and a table of scores at the top.
