# Benchmark, rodada 2 (skill 0.5.1, 17/11/2026)

Os mesmos três cenários da rodada 1, três vezes cada, com o mesmo roteiro de simulação, o mesmo script e o mesmo roteiro do juiz. A skill testada é a 0.5.1, com as correções que a rodada 1 apontou. O método e os limites estão em `../round-1/README.md`.

## Rodada 1 × rodada 2

Notas do juiz, somando as dimensões 1 a 7 (máximo 35), média das três rodadas:

| Cenário | 0.5.0 | 0.5.1 |
|---|---|---|
| s1 curso novo | 25,3 (24 / 23 / 29) | 31,0 (33 / 30 / 30) |
| s2 aula 11 com rodízio | 30,3 (30 / 32 / 29) | 31,7 (34 / 30 / 31) |
| s5 pular para a 22 | 29,0 (30 / 28 / 29) | 31,0 (30 / 33 / 30) |
| **Média** | **28,2** | **31,2** |

Script:

| | 0.5.0 | 0.5.1 |
|---|---|---|
| Ofereceu a próxima parte no fechamento | 3/9 | 9/9 |
| Contador da revisão mudou no meio | 3/9 | 0/9 |
| Palavras antigas do rodízio usadas (s2) | 2, 4 e 4 de 6 | 3, 3 e 3 de 3 |
| Caracteres fora do vocabulário conhecido | 0 | 1 real (o nome 小王, numa narração do s2); o outro alerta era um comentário do benchmark |
| Ditado com os dois lados de uma conversa | 3/3 no s1 | 0/3 |
| Curso novo: trocas por simulação | 98–100 | 68–72 |
| Duração estimada pelo juiz | s1 abaixo de 1 h, s2 45–50 min, s5 40–50 min | s1 30–35 min (oferece a próxima parte), s2 45–50 min, s5 50–55 min |

## O que melhorou

- As primeiras partes do curso: de 25 para 31. As baterias de interjeições embaralhadas sumiram, e o ditado ficou com uma fala por frase.
- A oferta da próxima parte, o contador fixo da revisão e o rodízio de palavras antigas passaram a funcionar sempre.

## O que a rodada 2 apontou (e entrou na 0.5.1 antes de publicar, sem nova rodada)

- **Efeito colateral da correção:** no s5, a bateria 2 continuou usando diálogos com travessão mesmo com o aluno sabendo bem mais de dez palavras. Agora a regra diz que, a partir de dez palavras, as baterias 1 e 2 têm uma frase e um falante por exercício, sem repetir a mesma estrutura trocando só o sujeito.
- **A primeira parte (3 palavras):** a bateria 2 virou eco ("Olá! — Olá!"). Com até cinco palavras conhecidas, agora só há a bateria 1.
- **Revisão de uma parte com 3 palavras e nada mais antigo para trazer:** uma frase por palavra basta.
- **Forma natural fora do alcance** (起得很早 precisa de 得, do HSK 2): mudar a frase, nunca ensinar algo quase certo como 起床很早.
- **Variante padrão** (没有关系 para 没关系) conta como certa.
- **Ditado:** a frase corrigida não se repete inteira antes do roteiro.
- **Narração:** de três a cinco perguntas, uma de cada tipo, sem nomes que o aluno não conhece.

Essas últimas mudanças são ajustes de texto e ainda não passaram por uma rodada. A rodada 3, se houver, deve conferir principalmente a bateria 2 do s5 e a primeira parte do s1.
