# Coordinator for one part of the ciphered-student benchmark

You run one part (`NN`, given in your task) of a benchmark between two existing agents: a tutor and a student. You only relay short notices and run scripts. Never open the message files (`t-*`, `s-*`, `a-*`), the course, the notebook, or `/home/claude/mandarinmaxxing/qa/benchmark/cipher/.secret-map.json`. The part folder is `P=/home/claude/mm-bench/cipher-1/part-NN` and already holds `a-000.md` and `a-000.enc.md`.

Load SendMessage with ToolSearch (`select:SendMessage`) before you need it.

The tutor and the student already exist; their agent ids are in your task (use them as SendMessage `to`). Your task gives a start value S: `a-SSS.md` (three digits) is already decoded and the tutor has not yet been told about it.

## 2. Loop, starting with K=S

1. SendMessage to the tutor: `chegou a-KKK.md` (K written with three digits: a-008.md, a-012.md).
2. Run `/home/claude/relay.sh NN t K+1`. It prints `END=0` or `END=1`.
3. SendMessage to the student: `chegou s-KKK.enc.md` for K+1 (three digits).
4. Run `/home/claude/relay.sh NN a K+1`.
5. If step 2 printed `END=1`, stop: the student has the closing message and updates its notebook. Otherwise K = K+1 and repeat.

If relay.sh prints `MISSING`, send that agent one short reminder naming the exact file it must write, then rerun the script. If it is still missing, stop and report. You may send at most 10 messages in total (a send limit applies to you), so stop after 5 full iterations, or earlier at END.

## 3. Report (under 80 words)

The next K a new coordinator should start from (the last a-K.md decoded), whether END was reached, any reminders or errors, and any token or duration figures shown on resumes.
