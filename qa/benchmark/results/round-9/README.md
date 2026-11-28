# Benchmark, rodada 9 (branch review-fixes, commit 750cc03, 28/11/2026)

Os três cenários da rodada 8 (`s12`, `s13`, `s14`), agora com o aluno fixo: as respostas vêm de `qa/benchmark/student.py`, por regra, e o professor não as escolhe (roteiro em `../../runner-fixed.md`). O `s14` ganhou uma troca de ritmo e um chat novo; o `s13`, a tela do curso e a troca de ritmo pelo cartão.

Foi a primeira rodada em que o `course.py` escreve o `course.md` (formato 2). Em todos os passos dos três cenários o `course.py check` deu o arquivo como coerente.

| Cenário | Exercícios | Tempo estimado |
|---|---|---|
| s12, três primeiras partes do HSK 1 | 40 | 8 a 10, cerca de 8 e 15 a 18 min |
| s14, parte de 3 palavras do HSK 3, com áudio | 19 | cerca de 34 min |
| s13, pulo com aulas conhecidas (HSK 2, aula 3, parte 1) | 24 | cerca de 40 min |

Defeitos que a rodada achou e que foram corrigidos no commit seguinte, com teste em `tools/test_scripts.py`:

- a troca de ritmo redividia a aula já começada quando a primeira parte era igual em dois ritmos;
- `close --missed` partia um chunk na vírgula chinesa (不要，谢谢 virava dois itens);
- `check_plan.py` rejeitava 打两次电话 (palavra separável de três caracteres);
- `check` dava como certo um curso em português com rótulos em inglês;
- depois de `known`, nada lembrava que ainda havia aulas do jump start por estudar.

O que continua em aberto está nas notas de cada cenário: o começo do HSK 1 segue ralo, faltam palavras naturais em algumas situações (张 e 银行 na aula do cartão), e a regra de reforço esvazia fácil quando o aluno acerta depois da correção.
