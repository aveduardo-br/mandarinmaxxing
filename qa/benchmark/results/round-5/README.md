# Benchmark, rodada 5 (skill 0.5.4, 17/11/2026)

Checagem das correções que o aluno cifrado (`../cipher-1/`) motivou. Três simulações: duas do cenário novo `s10` (HSK 1, aula 4 parte 3, que ensina 中文 e 汉语 juntos) e uma do curso novo (`s1`). O juiz contou, além das notas de sempre, os quatro furos que o aluno cifrado achou.

## Os furos do aluno cifrado

| Furo | cipher-1 (0.5.3) | 0.5.4 (3 simulações) |
|---|---|---|
| Enunciado em português com palavra que a resposta não tem | 6 em 19 partes | 1 ("Senhor, o senhor vai…", um vocativo para pedir 您) |
| Mandarim fora da tabela com palavra não vista (dicas, roteiros) | 2 | 0 |
| Sinônimo esquecido | 中文 24 vezes × 汉语 2 | 汉语 pedido 3 vezes em cada simulação, sempre pelo nome quando o aluno escolhia 中文 |
| Resposta aceita sem a palavra nova | 2 | 1, e o professor nomeou a palavra e a trouxe de volta na mesma bateria, como a regra pede |

## Notas do juiz (/35)

| Cenário | Notas |
|---|---|
| s10 sinônimos | 30 e 29 |
| s1 curso novo | 27 (na rodada 2 foram 33, 30 e 30) |

## O que ficou

- **As primeiras partes (3 a 9 palavras) ainda enchem linguiça:** para chegar a 5 exercícios, repetem e embaralham falas, e o ditado dobra palavras (对不起，对不起). Proposta: com tão poucas palavras, aceitar menos de 5 exercícios em vez de repetir.
- **O vocativo para 您** ("Senhor, …") conflita com a regra nova do enunciado. Proposta: o tratamento só entra quando a resposta usa 您 e ele vem na mesma frase ("Obrigado, senhor!" → 谢谢您), nunca como chamado solto no começo.
- A bateria 1 ainda pediu um chunk exatamente como na lista uma vez, e a bateria 2 teve exercícios sem quando nem onde. Já há regra para os dois; é questão de o modelo seguir.
