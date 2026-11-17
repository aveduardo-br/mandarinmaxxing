# Benchmark, rodada 1 (skill 0.5.0, 17/11/2026)

Três cenários, três rodadas cada, com o professor rodando no Sonnet. Os cenários estão em `../../scenarios.md`, o roteiro de cada simulação em `../../runner.md`, o do juiz em `../../judge.md`, e o script de correção em `../../check_run.py`. Cada pasta `run-N` tem a transcrição completa, o `course.md` final, as notas do agente (`run-notes.md`), a correção do script (`check.json`) e o custo (`timing.json`). O `judge.md` de cada cenário é a avaliação do juiz (Opus), que não viu as notas nem os scripts.

## Como foi rodado (e o limite disso)

Cada simulação foi um agente só fazendo os dois papéis: o professor seguindo a skill e o aluno seguindo um roteiro fixo (pinyin a cada quatro respostas, um erro a cada três, `[NÃO SEI]` quando faltasse palavra). O plano era ter outro modelo como aluno, mas isso exigiria passar umas 400 mensagens pela conversa principal. O custo disso: o professor "sabe" o roteiro do aluno, só não deve usá-lo. Por isso o resultado de "só palavras conhecidas" é otimista, e o que vale mais aqui é o que a skill manda fazer e o professor faz ou não.

O ambiente também não é o app do Claude: tabela em Markdown em vez do HTML, e o áudio como um bloco de texto com o roteiro, sem gerar nada.

## Números do script

| | s1 curso novo | s2 aula 11 com rodízio | s5 pular para a 22 |
|---|---|---|---|
| Trocas por simulação | 98–100 | 50–56 | 52–56 |
| Caracteres fora do vocabulário conhecido | 0 nas 3 | 0 nas 3 | 0 nas 3 |
| `[NÃO SEI]` do aluno | 0 | 0 | 0 |
| Baterias com exatamente 5 frases | 3/3 | 3/3 | 3/3 |
| Palavra nova em pelo menos 3 frases | 3/3 | 3/3 | 3/3 |
| Contador da revisão mudou no meio | 0/3 | 1/3 | 2/3 |
| `course.md` avançou certo (Done, Next) | 3/3 | 3/3 | 3/3 |
| Escuta | só ditado (certo: poucas palavras) | ditado + narração, 3/3 | ditado + narração, 3/3 |
| Narração falando com alguém | — | 0/3 | 0/3 |
| Ofereceu o role-play no fim da aula 1 | 3/3 | — | — |
| Perguntou sobre o jump start | — | — | 3/3 |
| Palavras antigas do rodízio usadas (de 6 previstas) | — | 2, 4 e 4 | — (log curto) |
| Custo por simulação | ~150 mil tokens | ~144 mil | ~140 mil |

## Notas do juiz (1 a 5)

| | s1 (rodadas 1/2/3) | s2 | s5 |
|---|---|---|---|
| Mandarim natural | 3 / 2 / 4 | 4 / 4 / 4 | 4 / 4 / 3 |
| Frases inteiras | 2 / 2 / 3 | 4 / 5 / 3 | 5 / 4 / 4 |
| Progressão das baterias | 2 / 2 / 3 | 5 / 5 / 5 | 4 / 4 / 4 |
| Só palavras vistas | 4 / 5 / 5 | 5 / 5 / 5 | 5 / 5 / 5 |
| Correções | 3 / 3 / 4 | 3 / 3 / 4 | 4 / 3 / 4 |
| Escuta | 5 / 5 / 5 | 5 / 5 / 4 | 4 / 4 / 5 |
| Fluxo e fechamento | 5 / 4 / 5 | 4 / 5 / 4 | 4 / 4 / 4 |
| Duração estimada | sessão abaixo de 1 h | ~45–50 min | ~40–50 min |

## O que funcionou

- O vocabulário ficou dentro do que o aluno conhecia nas 9 simulações, inclusive no cenário de pular para a aula 22.
- As três baterias de 5, a cobertura de cada palavra nova, o `course.md` e a pergunta do jump start funcionaram em todas.
- A narração saiu com uma pessoa só, em primeira pessoa, nas 6 em que apareceu. No curso novo, a skill corretamente usou só o ditado.
- A partir da aula 11 (s2), a progressão das baterias ficou nota 5 nas três.

## O que precisa mudar (aparece em mais de uma rodada)

1. **As primeiras partes, com 3 a 9 palavras.** As baterias 2 e 3 viram sequências de interjeições embaralhadas ("Tchau! Obrigado!", "Desculpe! Tudo bem! Obrigado!") e repetem a bateria 1 com outro título. É a pior nota da rodada.
2. **Ditado com os dois lados de uma conversa na mesma frase** (对不起，没关系 / 谢谢，不客气), nas três do curso novo.
3. **Oferta da próxima parte.** O professor não consegue medir o tempo, então não ofereceu nas partes de uma aula só (s5) nem depois da parte 2 (s1). Melhor oferecer sempre.
4. **O contador da revisão muda quando entra uma repetição** (de 6 para 7 e para 8). A regra de manter o total existe para as baterias, mas não para a revisão.
5. **Revisão de uma parte com 3 palavras.** "Uma por palavra, no mínimo 5" fez o professor inventar molduras como "Ele disse: '…' Eu respondi: '…'" para alongar a frase.
6. **Rodízio de palavras antigas.** O professor usou 2 a 4 das 6 previstas. A regra de "duas por visita em linhas com mais de cinco palavras" confundiu nas três notas.
7. **"To reinforce".** Não está claro se uma palavra errada e depois acertada na mesma parte fica na lista. Cada rodada decidiu de um jeito, e uma salvou 8 frases inteiras.
8. **Faltam nomes no Labels**: ditado, áudio e o nome de cada bateria.
9. **Prompt para 您** com rubrica entre parênteses ("a uma pessoa mais velha, com respeito").

## Onde eu discordo do juiz

O juiz do s2 quer aceitar 我起床很晚 como certo. Não aceitaria: em mandarim padrão, o grau vem com 得 (我起得很晚, HSK 2) ou antes do verbo (我很晚起床 / 我很晚才起床). A correção do professor estava certa. A regra geral que o juiz pede ("aceitar qualquer versão natural") já existe e está boa; o exemplo dele é que não serve.
