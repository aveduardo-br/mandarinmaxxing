# Benchmark, rodada 6 (branch v0.6-lean, 18/11/2026)

Uma simulação só, do cenário `s1` (curso novo, HSK 1, aula 1 partes 1 e 2 e o role-play), para ver se a reescrita enxuta e o passo de planejamento quebraram alguma coisa. Mesmo roteiro, script e juiz das rodadas anteriores. O juiz não leu as notas da simulação.

## O que mudou na skill

- `SKILL.md` e `lesson-format.md`, lidos em toda aula, foram de 7.226 para 4.090 palavras. Setup, troca de nível e pedidos do aluno foram para `setup.md`, `levels.md` e `requests.md`, lidos só quando preciso.
- Passo novo: planejar a parte inteira em privado antes da primeira mensagem, com o mandarim escrito primeiro.

## Resultado

| | 0.5.4 (rodada 5) | v0.6-lean |
|---|---|---|
| Nota do juiz (/35) | 27 | 29 |
| Mandarim natural | 3 | 3 |
| Frases inteiras | 3 | 4 |
| Progressão das baterias | 4 | 4 |
| Só palavras vistas | 5 | 5 |
| Correções | 4 | 4 |
| Escuta | 3 | 4 |
| Fluxo e fechamento | 5 | 5 |
| Adequação ao nível (fora do total) | 3 | 4 |

Na rodada 2 (0.5.1), o mesmo cenário tirou 33, 30 e 30. Com uma simulação só, 29 está dentro da variação entre simulações: a leitura segura é que a reescrita não quebrou nada, não que melhorou.

Pelo script: nenhuma palavra não vista nas respostas esperadas, nenhum `[NÃO SEI]`, cada palavra nova em pelo menos três exercícios, próxima parte e role-play oferecidos, `course.md` certo no fim.

## O que ficou

- **Naturalidade nas primeiras partes continua em 3.** Cerca de um terço das falas são palavras de reação coladas para bater a contagem (你好！谢谢！再见！, 好，对不起！). O planejamento não resolve: com três palavras, "cada palavra nova em três exercícios" e "dê menos em vez de repetir" não cabem juntos, e a skill não diz qual ganha.
- **Bateria 1 com chunk de uma palavra só:** "mudar um slot" não tem como valer. O chunk 好，谢谢！ foi listado e nunca praticado.
- **Ditado da parte 1:** "não repetir exercício da parte" e "usar toda palavra nova" se contradizem com três palavras.
- **Idioma:** "start mandarinmaxxing" não revela a língua, e a skill gastou uma troca perguntando.
- **Role-play:** 没关系 como resposta a 谢谢 foi marcado errado; e a skill não diz se erro do role-play entra no `To reinforce`.

As doze dúvidas de instrução que a simulação anotou estão em `s1/run-1/run-notes.md`; as três mudanças que o juiz faria primeiro, no fim de `s1/judge.md`.

## s11: meio do HSK 2, as duas versões lado a lado

O Eduardo apontou que o `s1` é fraco para medir naturalidade (com três palavras não há frase natural possível). Cenário novo, `s11`: HSK 2 com as aulas 1 a 9 feitas (19 partes, mais o HSK 1 inteiro), aula 10 parte 1 (地铁 站 离 远), parte completa. A mesma aula foi simulada com a 0.5.6 (`s11/run-a`, skill no commit `571b0cb`) e com a `v0.6-lean` (`s11/run-b`). Um juiz só leu as duas sem saber qual era de qual versão.

| | 0.5.6 (run-a) | v0.6-lean (run-b) |
|---|---|---|
| Nota do juiz (/35) | 32 | 35 |
| Mandarim natural | 4 | 5 |
| Frases inteiras | 5 | 5 |
| Progressão das baterias | 4 | 5 |
| Só palavras vistas | 5 | 5 |
| Correções | 5 | 5 |
| Escuta | 4 | 5 |
| Fluxo e fechamento | 5 | 5 |
| Adequação ao nível (fora do total) | 4 | 5 |
| Frases em mandarim apontadas pelo juiz | 6 de ~46 | 3 de ~45 |
| Duração estimada | ~55 min | ~50 min |

Pelo script, nas duas: nenhuma palavra não vista, nenhum `[NÃO SEI]`, as três palavras antigas do rodízio usadas, ditado e narração, `course.md` certo. Os três candidatos a palavra não vista (十分, 就是, 车站) são falsos positivos de 十分钟, 旁边就是 e 火车站.

**Como ler.** A diferença aparece onde o planejamento deveria agir: a 0.5.6 repetiu estruturas (8 dos 15 exercícios das baterias giram em "X 离 Y 远") e o ditado reaproveitou frases da parte; a versão nova variou as estruturas e o ditado veio todo novo. Mas é uma simulação de cada, e no HSK 2 a mesma versão já tirou 33 e 28 (rodada 4). O resultado aponta na direção certa; não é prova.

**O que as duas têm em comum** (problema da skill, não da simulação): 站 quase só aparece dentro de 地铁站; o padrão 离…远 domina; e a skill não diz se erro do ditado entra no `To reinforce` (cada simulação decidiu de um jeito).

## s11 de novo, depois das correções (`s11/run-c`)

Depois das duas análises externas e do teste de mesa, a skill ganhou o `check_plan.py` e várias correções de regra. Uma simulação do `s11` para ver se o conferidor funciona dentro de uma aula. Só o script, sem juiz: não há nota para comparar com as de cima.

- A skill gravou o rascunho (`s11/run-c/scratch/plan.txt`, 28 linhas) e rodou o conferidor duas vezes; as duas deram OK. Entre uma e outra, trocou sozinha uma frase da revisão que repetia a estrutura de outra.
- Nenhuma palavra não vista, nenhum `[NÃO SEI]`, cada palavra nova em pelo menos seis exercícios, rodízio 3 de 3, ditado e narração, `course.md` certo.
- Tamanho médio das respostas: revisão 17,4, bateria 1 7,6, bateria 2 15,4, bateria 3 23,4. A bateria 1 ficou curta, como a regra nova permite; a bateria 2 ficou um pouco abaixo da revisão.
- As frases refeitas no meio da aula, depois de um erro do aluno, foram conferidas à mão e não pelo script.
