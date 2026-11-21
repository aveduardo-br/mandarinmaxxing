# Run notes: round 7, s1 (adapted), run 1

## Scenario

s1-new-course, adapted. No starting `course.md`. First message `start mandarinmaxxing`; setup answer `Começo do zero. HSK 1, ritmo recomendado. Quero áudio, já conectei o ElevenLabs.`; route accepted as shown, start at Lesson 1. Two parts taught in full; stop after the closing message of the second.

- "Ritmo recomendado" was saved as pace 5 (`setup.md`: "Save light, recommended and intense as a Pace of 3, 5 and 7").
- At pace 5 the map's Split line for Lesson 01 is `3`: one part with all nine words. So the two parts taught were **HSK 1 Lesson 1 (single part)** and **HSK 1 Lesson 2, part 1 of 2** (我 要 水 茶 你 吗 不).
- Lesson 1 has a single part and Lesson 2 was not finished, so the wrap-up role-play was never offered (it is offered only "after the last part of a lesson with two or more parts"). Nothing to decline.
- Turns: **76** (T1 to T76). 30 translation answers by the student (pinyin on answers 4, 8, 12, 16, 20, 24, 28; slips on answers 3, 6, 9, 13, 18, 23, 27, 29), plus two dictations with one slip each. No `[NÃO SEI]` was needed.

Files read, in order: `SKILL.md`; `setup.md` (no course found); `maps/hsk-1.md` (level known); `lesson-format.md` (before the first lesson message); six single-word lookups in `syllabus/hsk-1.csv` for pinyin. `requests.md` and `levels.md` were never read. Of `check_plan.py` I read only the docstring at the top (the plan format), as `SKILL.md` step 4 points to it.

Final state: `course/course.md` has `Next: Lesson 02, part 2 of 2`, `To reinforce: 您`, `Audio: ElevenLabs, voice Sarah`, two Done lines.

## check_plan.py

Both parts were **taught from the plan file**. No prompt was improvised: the two corrections that needed the item back "in a later prompt" were already served by prompts still to come in the plan (see below), so nothing was reworked mid-part.

### Part 1: `plan-lesson-01-1.txt`, 2 runs

Run 1 printed:

```
NEW WORDS IN FEWER THAN THREE ROUND LINES:
  不客气: 2
  你好: 2
  再见: 2
  对不起: 2
  没事: 2
  没关系: 2
```

I changed one round 2 exchange (`— 对不起！ — 没关系。` became `— 对不起，再见！ — 没关系。`) to give 再见 a third line. Run 2 printed:

```
NEW WORDS IN FEWER THAN THREE ROUND LINES:
  不客气: 2
  你好: 2
  对不起: 2
  没事: 2
  没关系: 2
```

I stopped there ("twice at most; what still stands after that is your call") and kept two prompts for those five words, under "Naturalness comes before the count. If a new word fits only two natural prompts, give it two". No NOT MET and no CHECK lines on either run. Prompts in Portuguese were added to the file after run 2 and the file was not run again.

### Part 2: `plan-lesson-02-1.txt`, 1 run

Run 1 printed only CHECK lines, all for the same stretch:

```
CHECK (met words cover it, but it is also a word not met yet; keep it only if you mean the parts):
  不要  in chunk: 我不要茶。
  不要  in round1: 我不要水。
  不要  in round1: 我不要，谢谢。
  不要  in round2: 对不起，我不要茶。
  不要  in round2: 谢谢，我不要茶，我要水。
  不要  in round3: 对不起，我不要水。你要吗？
  不要  in round3: 您好！您要茶吗？我不要。
  不要  in round3: 我要水，你要茶。你不要茶吗？对不起！
  不要  in round3: 你不要水吗？好，没事。再见！
  不要  in listening: 我不要，谢谢你。
  不要  in listening: 您不要茶吗？
```

I kept all of them: every one is 不 + 要, "not want", which is the point of the part, not the word 不要 "don't". No NOT MET, no word under three round lines. No second run; prompts were added to the file afterwards.

Observation: the CHECK on 不要 is noise for this part. The map puts 不 and 要 in the same part, so 不要 as "not want" is unavoidable, and the checker flags it eleven times.

## Unclear, contradictory or hard-to-apply instructions

1. **Language of the first message.** `setup.md`: "With too little text to tell, use the language of the interface, of the project's name, or of what you know about the learner, and ask in one short line only if none of these tells." In a coding-agent working folder there is no interface language, project name or learner information visible, so the tutor spent one exchange asking (T2/T3), in English. The scenario script expects the setup answer right after the first message; the student's `Português.` at T3 is my addition. The skill also doesn't say which language to ask in.

2. **How many rounds and what review when the part itself has nine words.** "While the learner has met fewer than ten words … Six to nine: round 1, then a round 2 of short exchanges … Skip round 3." Clear for Lesson 1. But for the *next* part it is unclear whether "met" counts this part's table. "Met words" is defined as including "this part's table", so Lesson 2 part 1 has 16 met words and gets three full rounds; yet its review comes before the table, when the learner can only produce the nine words of Lesson 1. I applied the under-ten rules to the review only (exchanges allowed, fewer prompts) and the full rules to the rounds.

3. **Review size with nine reviewed words.** "One prompt per new word of the last Done line, five to ten in all" would give nine prompts. With only those nine words available, nine prompts with "no two prompts share a frame" and never "reshuffle lines already used" is impossible. I gave five prompts covering all nine words (two or three words per prompt) and fixed the counter at 5. The skill doesn't say whether "one prompt per word" can be met by one prompt carrying several of the words.

4. **"Sentences as long as round 2's" for that review.** "The review's sentences are as long as round 2's" and "Round 2's sentences are never shorter than the review's" can't hold in the second part of a course: the review can only use 你好/谢谢-type words (two to four words), while round 2 has real sentences (谢谢，我不要茶，我要水。). I kept the review short. Similarly "built from everything met" would technically allow the part's own table words in the review, which the learner hasn't been shown yet.

5. **Round 1 when the chunks have no slot.** "Each prompt uses one of the part's chunks with a slot changed … never the chunk as listed" against "A chunk with no slot to change is asked as listed". With nine greeting words, 您好 and 谢谢您 have no slot, so two of five round 1 prompts were the chunks as listed. For 好，谢谢！ I treated "what comes before or after the comma" as two slots (好，再见！ / 没事，谢谢！ / 好，没关系。); whether that is a "slot" in the skill's sense is a guess. "when a chunk comes up twice, change a different slot each time" could not be fully met: that chunk came up three times with two slots.

6. **"A chunk is … longer than a single table word wherever the met words allow".** With these nine words, any chunk longer than one table word is two reaction words joined by a comma (好，谢谢！). The earlier judge criticised exactly these glued lines; the skill pushes toward them.

7. **Echo rule.** "Never repeat a word inside a prompt, echo a line ('Hi! — Hi!')". I used `— 你好！ — 您好！` (prompt: "— Oi! — Olá, senhora!") because it is the only natural second home for 你好. It is not a literal echo and no word is repeated, but 好 is repeated as a character and the exchange is close to the forbidden example. Unclear whether it is allowed.

8. **"Every new word in at least three prompts" against "give fewer rather than repeat".** Same conflict as in earlier rounds; the checker reports it and the skill leaves it as "your call". Five of nine words ended with two round prompts in part 1.

9. **Name of round 2 in the first parts.** **Rounds** fixes "Ações completas" (Full actions), but under ten words round 2 is "short exchanges". The heading "Bateria 2 · Ações completas" sat above two-line exchanges. The skill says to use the labels exactly, so I did.

10. **Dictation length and coverage with nine words.** "Three to five short sentences … No sentence repeats a chunk or a prompt of the part … or doubles a word to fill a line" against "With very few met words, two or three real lines are enough, and they may be lines the part already used" and "Across this step, use every new word". Nine words in "two or three" lines is not possible without stacking; I used four lines, one of which (没事，没关系。) pairs two synonyms and is arguably "doubling to fill a line", and one (好，谢谢您！) is a round-1-type line. "Very few met words" has no number; I did not treat 16 met words (part 2) as "very few" and wrote four new sentences there.

11. **When the narration starts.** "Only once the met words can fill about 20 seconds; before that the dictation is the whole step." With 16 met words and 要 as the only verb, a first-person account that "never addresses or questions a listener" is not possible (most natural sentences are questions to 你/您). I skipped the narration in both parts. A word-count threshold would be easier to apply than "about 20 seconds".

12. **Does a dictation slip count for To reinforce, and what does "unaided" mean after it?** "add the ones they missed anywhere in it (review, rounds, dictation, rewrite) and didn't get right later". The student wrote 你 for 您 in both dictations, which is a hearing slip and comes last in the part, so "got right later" can never apply to it. I kept `To reinforce: 您` after both parts, although in part 2 the learner produced 您 unaided three times before the dictation. It is unclear which wins: "remove the items the learner got right unaided during the part" or the later miss.

13. **Word or chunk in To reinforce.** "for a slip of word order or grammar, save the chunk". The slips 我要不水 (order) and a missing 吗 were corrected and then produced right later, so nothing was saved; had they been saved, it is unclear what the "chunk" for a missing 吗 would be.

14. **Bringing a corrected item back "in a new frame" when the plan already has it.** "After a correction, bring the item back in a later prompt of the same or the next round, in a new frame … by reworking a prompt still to come". In every case here a planned prompt still to come already held the item (好 in 1·5, 您 in 2·3, 再见 in 2·5, 您 in round 1·4, 不要 and 吗 in later prompts), so I reworked nothing. The skill doesn't say whether an already planned occurrence counts or a prompt must be reworked on purpose.

15. **没关系 and 没事.** "give each prompt a context that fits only one, or accept both." A one-line prompt has no room for context, so I fixed the Portuguese wording in a usage note ("não tem problema" asks for 没关系, "não foi nada" for 没事) and would have accepted either. In part 2 the prompt "Tá bom, tudo bem." (expected 好，没事) departs from that wording because "não foi nada" did not fit the sentence; either word would have been accepted.

16. **不 in the table.** The syllabus pinyin is `bù`, but every use in this part is 不要 (*bú yào*). The skill says pronunciation is the learner's own practice and gives no rule for tone change in the written pinyin; I wrote *bú yào* in the note and in every pinyin line and left `bù` in the table.

17. **Breakdown lines.** "Give a chunk a breakdown line only when its parts are words the learner can reuse right away". In Lesson 2 part 1 every chunk is made only of such words, so all three chunks got a breakdown, which is repetitive. In Lesson 1 the skill's own example (你好 = 你 + 好) breaks a word into 你, which is not met until Lesson 2; I used 您好 = 您 + 好 instead.

18. **Voice in `Audio` at setup.** `setup.md` says "Save the choice in Audio" at setup; `lesson-format.md` says "On the first clip of a course, choose the voice and save it in Audio". I saved `Audio: ElevenLabs` at setup (T6) and `ElevenLabs, voice Sarah` when the first clip was sent (T28). Only the final state is in `course/course.md`.

19. **`Route` format.** The example in `SKILL.md` shows a moved route (`01–07, 12, 13, 08, …`); `setup.md` says "the route in map order". I wrote `Route: 01–22`.

20. **Plan file name and location.** `SKILL.md` says `plan.txt`; this run was told to write `plan-lesson-NN-P.txt` in the output directory. In a real coding-agent session `plan.txt` would sit in the learner's working folder next to `course.md` and be overwritten each part; the skill doesn't say whether to delete it or where it goes.

21. **Dictation title numbering.** "Send the clip under a bold title, **Dictation 1**". It is not said whether the number restarts in each part. I restarted it (Ditado 1 in both parts), since a part has one dictation.

## Coverage of the two parts

- Part 1 (Lesson 1): round 1 of five, round 2 of five exchanges, no round 3, dictation of four lines, no narration. Round prompts per word: 谢谢 4, 您 4, 好 3 (plus inside 您好), 再见 3, the other five 2 each; all nine in the dictation.
- Part 2 (Lesson 2 part 1): review of five, three rounds of five, dictation of four sentences, no narration. Every new word in at least seven round prompts. No older words were due (the Done log had one line). The item to reinforce, 您, was used in the review (prompts 1 and 3), in rounds 1, 2 and 3, and in the dictation.
