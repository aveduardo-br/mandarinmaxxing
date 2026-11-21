# Benchmark, rodada 7 (branch v0.6-lean, 21/11/2026)

Uma simulação do `s1` adaptado, depois da revisão de 21/11: a aula 1 do HSK 1 virou uma parte só de nove palavras no ritmo 5 (`Split: 2-1 / 3 / 3`), o plano da parte passou a ficar em arquivo e o `check_plan.py` ganhou `NAMES` e `CHECK`. Partes dadas: aula 1 inteira e aula 2, parte 1. Mesmo roteiro e juiz das rodadas anteriores; o juiz não leu as notas da simulação.

## Resultado

Nas sete dimensões das outras rodadas: **29 de 35**, igual à rodada 6 (mandarim natural 3, frases inteiras 3, progressão 4, só palavras vistas 5, correções 5, escuta 4, fluxo 5). O juiz somou também "duração" (4) e escreveu 33; a conta comparável é 29.

- **O plano em arquivo funcionou:** as duas partes foram dadas a partir do `plan-lesson-*.txt`, sem enunciado improvisado.
- **Nenhuma palavra não vista**, nenhum `[NÃO SEI]`.
- **A primeira sessão maior não resolveu a naturalidade.** 11 de 44 frases apontadas, todas palavras de reação coladas (你好，对不起！ / 没事，没关系。 / 对不起，再见！). Com nove palavras a bateria 2 já tem trocas de verdade (谢谢您！— 不客气。), mas a bateria 1, a revisão seguinte e o ditado ainda colam palavras.
- **`CHECK` acusou 不要 onze vezes** na parte que ensina 不 e 要. Depois da rodada o script passou a listar cada palavra uma vez.

## Mudado depois desta rodada (ainda sem simular de novo)

- Com menos de dez palavras, uma fala tem uma reação, ou duas que as pessoas dizem juntas; cumprimento colado em desculpa ou agradecimento e dois sinônimos na mesma fala ficam proibidos pelo nome.
- A revisão com poucas palavras pode ter menos de cinco frases; duas palavras na mesma frase só em troca entre duas pessoas.
- `To reinforce`: vale a última resposta do item na parte.

As 21 dúvidas de instrução estão em `s1/run-1/run-notes.md`.
