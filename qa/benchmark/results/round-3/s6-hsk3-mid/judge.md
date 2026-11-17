# Judge report: s6-hsk3-mid (round 3)

Scenario: HSK 3, Lessons 1 to 17 done (47 Done lines), first message `próxima aula`. Expected part: HSK 3 · Lesson 18 · Perder o celular ou o cartão · part 1 of 2, new words 丢 卡 以为 (block 1, split 1-2 at pace 5). Expected review: 6 prompts, one per word of 3-17.2 (出院 健康 病人 脚 锻炼 坚持). Older words due by turn: line 3 back (3-16.2) → 起, line 7 back (3-14.4) → 种, line 14 back (3-12.1) → 斤, line 30 back (3-06.3) → 男人; line 60 not reached. To reinforce: 一定 打算. HSK 1 and HSK 2 count as met.

Every word used in the expected answers, chunks and scripts of all three runs was checked against `hsk-1.csv`, `hsk-2.csv` and the Done log. None was unmet, and there are no `[NÃO SEI]` markers in any run.

Two conventions are shared by all three runs and were not counted against any one of them. The vocabulary table is a Markdown table (the fallback), probably because the harness has no inline HTML tool. The `audio-script` blocks under `[AUDIO CLIP]` are read as the harness's record of the generation request, not as text shown to the learner.

## Scores

| Dimension | run-1 | run-2 | run-3 |
|---|---|---|---|
| 1. Natural Mandarin | 3 | 3 | 4 |
| 2. Whole sentences | 5 | 5 | 5 |
| 3. Round progression | 4 | 4 | 5 |
| 4. Only met words | 5 | 5 | 5 |
| 5. Corrections | 4 | 4 | 5 |
| 6. Listening | 5 | 5 | 4 |
| 7. Flow and closing | 5 | 5 | 5 |
| **Total (/35)** | **31** | **31** | **33** |
| 8. Session length (est.) | ~45 min, fits | ~40 min, fits | ~45 min, fits |
| 9. Level fit (not in total) | 5 | 4 | 5 |

---

## run-1

**1. Natural Mandarin: 3.** Most sentences are natural and at HSK 3 level. Problems:
- T38/T39 (Bateria 3 · 3): expected `我很着急，快去学校了。` "快去学校了" means "about to go to school", not "went quickly to school". The tutor accepted the student's identical answer (T40 "Certo."). Fix with met words: `我很着急，很快就去学校了。`
- T33 (Bateria 2 · 5): `我以为他一定会来我家，可是他十点才到。` The logic contradicts itself: he did come, so "I thought he would definitely come" doesn't contrast with "he only arrived at ten". Fix: `我以为他九点会到我家，可是他十点才到。`
- T19 (Bateria 1 · 3): `我以为今天放假，可是不是。` Clunky. Fix: `我以为今天放假，其实不放假。`
- T43 (Bateria 3 · 5): `我一定把手机和卡放在书包里` → a resolution reads better as `我一定要把手机和卡放在书包里`.
- Minor: T6 `医生现在要检查他` → `医生现在要给他检查一下`. T23 `所以没有打电话` → `所以没给你打电话`. T37 says 超市 three times. Better: `……所以下午我还要再去一次。`

**2. Whole sentences: 5.** Every prompt is a line someone would say. There are no fragments or stage directions. Example: T2 "Meu avô teve alta do hospital ontem, e hoje de manhã ele foi sozinho ao supermercado comprar comida."

**3. Round progression: 4.** Round 1 swaps the chunk slots well (T16 "Perdi meu cartão no metrô" swaps the place in 我把卡丢在出租车上了). Round 3 has real two- or three-sentence accounts (T34, T40, T42). Round 2 has two weak spots. T28 "Este cartão é do meu irmão mais velho, você não pode usar." has no when or where. T24 and T32 share the same 以为…才 frame ("Eu achava que a loja abria às nove, mas só abre às dez" / "…mas ele só chegou às dez").

**4. Only met words: 5.** 0 prompts need an unmet word, and there are 0 `[NÃO SEI]` markers. All four older words appear: 种 (T4), 男人 (T6, T30, T40), 斤 (T10, T36, narration), 起 via 起床 (T38). Both reinforce items appear: 一定 (T12, T32, T42) and 打算 (T26, T34).

**5. Corrections: 4.** The format is right throughout: blockquote, then one bold fix line with pinyin, then the full sentence once (T8, T14, T20, T26, T32, T38, T44). The reasons are accurate (一定 before the verb, 了 after the place in 丢在…了, the missing 把). Corrected items come back: 一定 at T32 and T42, 丢在…了 at T36, 才 at T32. Pinyin answers are confirmed with the Hanzi, and the keyboard reminder appears once (T10). One point off for accepting the wrong `快去学校了` at T40.

**6. Listening: 5.** The dictation (T46) has five single-turn sentences and covers 丢 卡 以为. The feedback gives only the blockquote and fix line, then the script once (T48). The narration (T48, "Áudio 1 · No supermercado") is first person and six sentences long, with no listener and no quotes. The script stays hidden until the learner answers. The four questions cover what happened, what the speaker wanted and what 我以为 meant. Marking is correct (T50: Q3 incorrect).

**7. Flow and closing: 5.** The steps come in order: review, vocabulary, three rounds, the offer of an extra round, listening, close. The title opens the review and is repeated above the table. The close (T50) reads "Próxima vez: HSK 3, Aula 18, parte 2. Quer começar a parte 2 agora…". There is no role-play offer, which is correct because this isn't the last part, and no comment on how the lesson was divided.

**8. Session length: about 45 minutes.** That's 6 review prompts, 15 round prompts with fairly long Round 3 items, a 5-sentence dictation and a narration with 4 questions. A 3-word part ending under the hour fits, and the close offers the next part.

**9. Level fit: 5.** The review prompts are as long as round 2 or longer (T12: "Meu avô é paciente deste hospital; se ele insistir em se exercitar todo dia, com certeza vai ficar mais saudável"). The rounds use 才, 把, 如果, 其实 and 一点儿也不.

**Verdict.** A learner gets a solid, intermediate-level part. The review uses all of HSK 1 to 3, 以为 vs 认为 is drilled with a clear contrast, and the 把…丢在…了 pattern is corrected and recycled until it sticks. The weak spots are in the tutor's own sentences: one wrong answer was accepted as correct (`快去学校了`), and one prompt had self-contradicting logic. The single most useful change to the skill is to extend the pre-send check on prompts so the tutor verifies that the clauses fit together logically and that the expected answer means what the prompt says.

---

## run-2

**1. Natural Mandarin: 3.** Problems:
- T28/T29 (Bateria 2 · 3): `弟弟的卡丢了，可是他坚持每天走路上学。` The connector is wrong. Losing the card is the reason he walks, so 可是 doesn't follow. Fix: `弟弟的卡丢了，所以他每天走路上学。` (or drop 坚持).
- T34/T35 (Bateria 3 · 1): `今天早上我在公交车上把手机丢了。我以为手机在家里，可是没找到。` The sentences contradict each other. If you know you lost it on the bus, you can't think it's at home. Fix: `今天早上我的手机丢了。我以为手机在家里，可是没找到。我想可能丢在公交车上了。`
- T4 (Revisão 2): `为了健康，我一定每天六点起床。` A resolution needs 要: `为了健康，我一定要每天六点起床。`
- T48 narration: `我想了很久，可能卡丢在公交车上了。` The word order is off. Fix: `我想了想，卡可能丢在公交车上了。`
- Minor: the Portuguese "Meu irmão" (T10, T28, T36) doesn't say older or younger, and the expected answers switch between 哥哥 and 弟弟.

**2. Whole sentences: 5.** All prompts are real lines (T16 "Mãe, desculpe, eu perdi o cartão."). T2 "o médico disse que ele ainda precisa descansar em casa" is a natural indirect clause, not a reported dialogue, so it is not counted against the run.

**3. Round progression: 4.** T18 (Bateria 1 · 3) repeats chunk 3 word for word ("Achei que você estava em casa, mas na verdade você não estava") instead of swapping its slot. T14 "Meu relógio sumiu!" is very thin for an HSK 3 learner. Round 2 has who, when or where, and what in most prompts (T24 "Ontem à noite perdi meu cartão no ônibus…"). Round 3 has good two- and three-sentence accounts (T36, T40), apart from the logic issue at T34.

**4. Only met words: 5.** 0 prompts need an unmet word, and there are 0 markers. The older words appear in the review: 起 via 起床 (T4), 种 (T6, again at T32 and T38), 斤 (T10), 男人 (T12). The reinforce items appear: 一定 (T4) and 打算 (T8, T40, dictation).

**5. Corrections: 4.** The format is followed throughout (T8, T14, T20, T26, T38, T44). T8 is a good example: 这种 vs 这个, "种 conta tipos". At T32 the missing 了 in 已经四十岁 is handled as "meaning right, phrasing off", which works. At T26 the reason given, "O lugar vem antes do verbo", is not accurate. The student's real slip was 了 before 在, and `把卡丢在公交车上了` was also correct. The fix steers the learner to a different structure without saying so. Corrected items come back: 以为 at T22 and T26, time before 把 at T38.

**6. Listening: 5.** The dictation (T46) has four single-turn sentences, including one question that a single speaker would say. It covers 丢 以为 卡, and the feedback format is right (T48). The narration (T48, "Áudio 1 · No ônibus") is a first-person account of about 25 seconds, with no listener and no quotes. It has five questions across the three kinds, and the script is shown only after the answers (T50). Marking is correct.

**7. Flow and closing: 5.** The steps are in order and the title is placed correctly. The extra round is offered (T44). The close (T50) reads "Próxima vez: HSK 3, Aula 18, parte 2. Quer começar agora?" There is no commentary on how the lesson was divided.

**8. Session length: about 40 minutes.** Rounds 1 and 2 are shorter than in the other runs, and the dictation has four sentences. That fits for a 3-word part, and the close offers the next part.

**9. Level fit: 4.** The review is at level (T12 "Aquele homem insiste em correr todos os dias, mesmo quando chove"). Round 1 drops to first-lesson length (T14 "Meu relógio sumiu!", T22 "Achei que ele fosse seu irmão"). T6 "Os pacientes do hospital precisam tomar este tipo de remédio" is shorter than round 2.

**Verdict.** A learner gets a usable part, with good coverage of 以为 and the older words and clean listening. They also get two story prompts whose logic falls apart (可是 where 所以 belongs, and a phone "lost on the bus" that the speaker then thinks is at home), plus a Round 1 that copies a chunk word for word. The most useful change is the same as for run-1: make the pre-send check cover whether the sentences of a prompt fit together, not only word choice and word order.

---

## run-3

**1. Natural Mandarin: 4.** Problems:
- T2 (Revisão 1): `我们打算都去他家一起吃晚饭。` 都 is in the wrong place. Fix: `我们都打算去他家一起吃晚饭。` or `我们打算一起去他家吃晚饭。`
- T48 narration: `他说明天跟我一起去找` is natural Mandarin, but see dimension 6.
- Minor: T8 insists on 位, though `那个医生` is just as natural. Everything else reads as natural mainland speech (T34 `我只有十块钱，所以只买了一个苹果`, T38 `你能帮我找一下吗？`).

**2. Whole sentences: 5.** All prompts are real lines. T38 "Mãe, perdi meu cartão! … Você pode me ajudar a procurar?" is written as the learner's own line.

**3. Round progression: 5.** Round 1 swaps the chunk slots (T16 the time slot, T20 "Minha mãe perdeu o cartão no supermercado", T22 the 以为 clause). Each Round 2 prompt has who, when or where, and what, with no repeated frame (T24, T26, T28, T30, T32). Round 3 has full two- or three-sentence accounts and a message to someone (T34–T42).

**4. Only met words: 5.** 0 prompts need an unmet word, and there are 0 markers. The older words appear: 起 via 起床 (T10), 种 (T30), 斤 (T32, narration), 男人 (T26). There is also 邻居/热情 from the same 30-back line. The reinforce items appear: 一定 (T12) and 打算 (T2, T36, dictation).

**5. Corrections: 5.** Every correction follows the format and points only at the slip: the classifier at T8, the time word at T14, 以为 vs 觉得 at T20, the missing 上 at T26, 把 order at T32, 跟我一起 at T38 and 了 at T44. Corrected items come back: 以为 at T26, 公交车上 at T32, 把 at T38, 每天 order at T40. Pinyin answers are confirmed with the Hanzi, and the keyboard reminder appears once (T10).

**6. Listening: 4.** The dictation (T46) is correct in form and covers all three new words, and the feedback format is right. The narration (T48) is first person, about 25 seconds long, with five questions, and the script stays hidden until the answers. But it ends with `他说明天跟我一起去找`, a report of what someone said, and Q5 asks "O que o irmão disse". That goes against the rule that the narration never quotes anyone.

**7. Flow and closing: 5.** The steps are in order and the title is placed correctly. The close (T50) reads "Próxima vez: HSK 3, Aula 18, parte 2. Quer começar a próxima parte agora?" "Primeiro, a revisão." (T2) and "Terminamos as três baterias." (T44) are harmless signposts, not comments on how the lesson was divided.

**8. Session length: about 45 minutes.** The review and round prompts are long, and the narration has five questions. That fits for a 3-word part, and the close offers the next part.

**9. Level fit: 5.** The review is fully at HSK 3 level (T8 "Meu pé está doendo muito, então hoje de manhã eu não pude correr e só pude descansar em casa"; T10 "Aquele vizinho se levanta às seis… para se exercitar, e depois toma o café da manhã"). The rounds build on that.

**Verdict.** This is the strongest run. The review sounds like an intermediate learner, the rounds rise cleanly from chunks to full actions to connected accounts, and every correction is accurate and recycled. The only real flaws are one misplaced 都 and a narration that ends by reporting what the brother said. The most useful change to the skill is to make the narration rule explicitly ban indirect reports (他说…) too, not only quotes.

---

## Cross-run summary

**Problems in more than one run (likely caused by the skill's instructions):**
- **Multi-clause prompts whose logic doesn't hold** (run-1 T33, run-2 T28 and T34). The pre-send check covers naturalness, word order and met words, but not whether the clauses connect. It also missed a wrong expected answer that the tutor later accepted (run-1 T38–T40).
- **Prompts for 以为 that don't force 以为.** Run-3 T18 and T22 and run-2 T22 ("Achei que ele fosse seu irmão") have no contrast clause, so 觉得 or 认为 would also fit. The student's slip landed on 以为 in all three runs. Where the prompt carried a contrast (run-1 T19, run-2 T18), the correction was clear. Where it didn't (run-3 T18), marking 觉得 wrong is harder to justify.
- **Reported speech sneaking in** (run-2 T2 `医生说…`, run-3 narration `他说…`). The prompt rule bans "a report of what someone said" with a dialogue example, and the narration rule bans "quotes". Both are read as allowing indirect speech.
- **Reused scenes.** The "avô paciente deste hospital… 坚持锻炼" sentence appears in both run-1 (T12) and run-3 (T40), and every run's rounds revolve around losing a card on a bus or taxi. This is minor.

**Problems seen only once:** run-1 accepted a wrong answer (`快去学校了`). Run-2's Round 1 copied a chunk word for word, and its "irmão" was ambiguous. Run-2 gave an inaccurate reason in one correction (T26). Run-3 misplaced 都 (T2).

**Three changes to make first:**
1. `SKILL.md`, the line "Before sending a prompt, have its Mandarin answer ready and check it as you would a listening script: natural, mainland usage, time words before the verb, only met words." Add: "…only met words, and the sentences hang together: each 可是, 所以 or 其实 follows from what came before, and no sentence contradicts another. Check the learner's answer against this answer, not against how close it looks."
2. `lesson-format.md`, the line "When two words of a part translate the same way (没关系 and 没事), give each prompt a context that fits only one, or accept both." Change to: "When a new word translates the same way as another word of the part or a word already met (没关系 and 没事, 以为 and 觉得), give each prompt a context that fits only one, such as the contrast that shows a belief was wrong, or accept both."
3. `lesson-format.md`, the line "The speaker never addresses a listener, asks the listener anything, or quotes anyone; a conversation, or half of one, is not a narration." Change to: "The speaker never addresses a listener, asks the listener anything, quotes anyone or reports what someone said (他说…)…". Add a matching "or what someone said (医生说…)" to the prompt rule in `SKILL.md`.
