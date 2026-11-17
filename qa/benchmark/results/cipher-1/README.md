# Benchmark cipher-1: o aluno cifrado (jump start do HSK 1, skill 0.5.3, 17/11/2026)

As 19 partes do jump start do HSK 1 (aulas 01 a 07, ritmo 5) em sequência, cada uma num "chat novo", com o `course.md` passando de uma para a outra. O professor (Sonnet) ensina chinês de verdade com a skill. O aluno (Sonnet) só vê as mensagens depois da cifra: cada palavra chinesa vira um código terminado em "q" e o pinyin some. O aluno só sabe o que anotou no caderno.

## Como foi rodado (e o que mudou no caminho)

- **Piloto (parte 01).** Primeiro com SendMessage: eu revezava, e depois um coordenador por parte. Os dois funcionaram nos primeiros turnos. Achei dois bugs na cifra (português virando hanzi na decifração, e títulos com acento sumindo). O Eduardo corrigiu os dois (commit `0a39d80`), e a parte 01 foi refeita do zero com a cifra nova.
- **Limite do ambiente.** Os subagentes têm um teto conjunto de retomadas por SendMessage a cada mensagem do usuário (cerca de 12). Na parte 01 refeita, o coordenador travou no turno 8, e um segundo coordenador nem conseguiu começar. A conversa principal não tem esse teto, então terminei a parte 01 à mão. Subagentes também não conseguem criar agentes, então o "coordenador cria professor e aluno" da missão não funciona aqui.
- **Partes 02 a 19: troca por arquivo, sem SendMessage.** Um vigia (`harness/watcher.sh`) cifra cada `t-K.md` pronto em `s-K.enc.md` e decifra cada `a-K.enc.md` em `a-K.md`, com escrita atômica. Professor e aluno rodam em paralelo, cada um num turno só, esperando o próximo arquivo com `harness/waitfor.sh`. A instrução mudou só no transporte; o resto do `tutor.md` e do `student.md` valeu como estava. Para o vigia não cifrar um arquivo pela metade, pedi a cada agente que escrevesse cada arquivo de uma vez, sem editar depois. Na parte 13, isso impediu o professor de corrigir um erro de digitação (高先 por 高兴); ele escreveu uma linha de correção logo abaixo.
- **Duas correções minhas na cifra durante a rodada** (feitas localmente durante a rodada; a `main` já tem as duas no commit `1f7a99d`, junto com a retirada do pinyin entre parênteses):
  1. Desde a parte 02: o `is_pinyin` recusava qualquer trecho com `à`, que também é o 4º tom do "a" (jiào, zài, bàba). Isso deixaria passar boa parte do pinyin. Tirei o `à` da lista de letras do português.
  2. Desde a parte 10: o `is_pinyin` não reconhecia o erhua (`nǎr`). A linha inteira em itálico ficava visível, e nas partes 08 e 09 o aluno viu `Nǐ qù nǎr?` e `Zuótiān nǐ qù nǎr?`. Agora aceita um "r" depois da sílaba.

## Números

| Parte | Aula | Turnos | Palavras novas | Revisão | [NÃO SEI] | Minutos |
|---|---|---|---|---|---|---|
| 01 | 01.1 | 19 | 3 | — | 0 | 9,3* |
| 02 | 01.2 | 31 | 6 | 3 | 0 | 4,7 |
| 03 | 02.1 | 49 | 7 | 6 | 1 | 8,4 |
| 04 | 02.2 | 51 | 7 | 7 | 2 | 8,6 |
| 05 | 03.1 | 51 | 4 | 7 | 0 | 10,1 |
| 06 | 03.2 | 47 | 5 | 5 | 0 | 8,2 |
| 07 | 04.1 | 49 | 3 | 5 | 0 | 8,3 |
| 08 | 04.2 | 49 | 6 | 5 | 1 | 8,2 |
| 09 | 04.3 | 51 | 5 | 6 | 1 | 8,9 |
| 10 | 05.1 | 49 | 4 | 5 | 0 | 8,3 |
| 11 | 05.2 | 53 | 6 | 7 | 0 | 9,0 |
| 12 | 05.3 | 49 | 6 | 5 | 0 | 8,2 |
| 13 | 06.1 | 51 | 4 | 6 | 0 | 9,1 |
| 14 | 06.2 | 51 | 4 | 6 | 2 | 10,3 |
| 15 | 06.3 | 53 | 4 | 7 | 0 | 11,0 |
| 16 | 06.4 | 49 | 4 | 5 | 1 | 9,9 |
| 17 | 07.1 | 51 | 4 | 6 | 0 | 9,1 |
| 18 | 07.2 | 53 | 7 | 7 | 1 | 9,0 |
| 19 | 07.3 | 53 | 6 | 7 | 0 | 11,3 |

\* A parte 01 inclui as retomadas manuais e os coordenadores que travaram.

- **95 palavras** ensinadas. O `Next` termina em `Lesson 08, part 1 of 1`, exatamente onde o jump start acaba, e o `course.md` não quebrou em nenhuma parte.
- **Custo:** cerca de 170 minutos no relógio. Nos `subagent_tokens` que o ambiente informa, o professor teve de 122 mil a 157 mil por parte, e o aluno de 103 mil a 127 mil. Somando as partes 02 a 19, são 4,6 milhões, mais uns 0,3 milhão da parte 01 (`usage.log`). Esse número parece ser o tamanho final do contexto de cada agente, não o total cobrado. Com 50 turnos por agente, o gasto real deve ser bem maior.
- **Palavras que nunca voltaram:** nenhuma (0 de 89 ensinadas antes da última parte). As que voltaram menos: 妹妹 (1 vez), 没事, 汉语, 她们, 七, 大, 口, 两 e 没有 (2 vezes cada). Veja o `report.md`.
- **Rodízio de palavras antigas:** todas as agendadas foram usadas em todas as partes.
- **To reinforce:** nunca passou de 1 item (中国朋友, 对不起, 多大). Não cresceu.
- **Revisão × bateria 2:** em média 8,0 × 9,7 caracteres por resposta esperada. A revisão saiu mais de 10% mais curta em 11 das 17 partes. A regra (`SKILL.md`, linha 177) pede revisão do tamanho da bateria 2.
- **Escuta:** só ditado nas partes 01 a 06, e ditado mais narração a partir da 07, como pede a linha 189 do `SKILL.md`.

## O que funcionou

- **A cifra cumpriu o papel.** Nenhum hanzi chegou ao aluno em 19 partes. O pinyin chegou em três partes: na 05 (nomes entre parênteses, não corrigido) e nas 08 e 09 (erhua, corrigido a partir da 10). O aluno respondeu sempre em códigos, e a decifração fez sentido para o professor em todos os turnos.
- **O jump start é ensinável do zero.** Com 95 palavras, o aluno só travou 9 vezes, e quase todas as travadas vieram de palavras do português que a resposta esperada dispensa (ver os furos). Ele montou frases de bateria 3 com 15 a 20 caracteres a partir só do caderno.
- **A continuidade do `course.md`** aguentou 19 chats: Done, Next, To reinforce, o rodízio e os rótulos (com uma exceção, ver furo 5).
- **As correções** foram curtas e mostraram a forma natural, como em 中国人朋友 → 中国朋友 (parte 10). Viraram regra no caderno do aluno.

## Os [NÃO SEI], separados

| Parte, arquivo | Pediu | O que era | Tipo |
|---|---|---|---|
| 03, a-011 | "Não, obrigado. Eu não quero chá." | 不 sozinho como resposta. A tabela deu 不 = "não (antes de verbo)" | **Furo** (o enunciado pede um uso que o significado da tabela exclui) |
| 04, a-005 | "Tudo bem com você?" (revisão) | 你好吗, nunca mostrado como chunk. O aluno acertou no palpite | **Furo leve** (revisão pede uma frase nova a partir de peças conhecidas) |
| 04, a-006 | "Eu quero água, **e** você quer chá?" | a resposta esperada não tem "e" | **Furo** (palavra do enunciado que a resposta esperada omite) |
| 08, a-005 | "chá **da** China" | 中国茶, sem 的 (que só vem na parte 10) | **Furo** (o mesmo) |
| 09, a-018 | "...**mas** ele sabe" | a resposta esperada não tem 可是/但是 | **Furo** (o mesmo) |
| 14, a-001 | "Com licença, **menino**..." | a resposta esperada omite "menino" | **Furo** (o mesmo) |
| 14, a-024 | narração: 今天我去中国朋友的**家** | 家 só é ensinado na parte 17 | **Furo** (palavra não ensinada no roteiro do áudio) |
| 16, a-002 | "...e **já** sabe falar chinês?" | a resposta esperada omite "já" | **Furo** (o mesmo) |
| 18, a-019 | "...**mas** tem duas irmãs" | o mesmo "mas" da parte 09, que o professor explicou na hora | **Limite do aluno** (não anotou no caderno) |

Resultado: 8 furos da skill, 1 limite do aluno. Seis dos oito são o mesmo padrão: **o enunciado em português traz uma palavra que a resposta esperada deixa de fora** (e, mas, já, de, menino). O professor sempre aceitou e explicou depois, mas o aluno real trava antes de responder.

## Outros furos encontrados (sem [NÃO SEI])

1. **Palavra não ensinada na dica de troca** (parte 02, t-004). "您好！ Olá! (para senhor ou senhora). Troque 您 por outra pessoa, como 你." Só que 你 vem na parte 03. O aluno anotou: "gereq = outra pessoa (significado exato não explicado)". O script não pega esse caso porque 你 está dentro de 你好.
2. **Sinônimos da mesma parte, e o aluno escolhe sempre um.** 中文 e 汉语 entraram juntos (1-04.3). 汉语 aparece 14 vezes nas respostas esperadas do professor, o aluno usou 中文 em 24 respostas e 汉语 em 2, e o professor aceitou todas. Na prática, 汉语 nunca foi produzido. Aconteceu o mesmo, em escala menor, com 多大了 → 几岁 (parte 16), mas aí o 多大 foi para o To reinforce e voltou.
3. **Resposta que pula a palavra nova, aceita como certa.** Em 你的朋友今天在哪儿 → 今天你朋友在哪儿 (parte 10), o 的, que era palavra nova, ficou de fora. Em 我九岁了，你多大了？ → 我九岁。你呢？你几岁？ (parte 16), saíram 多, 大 e 了, as três novas. Como resposta, está natural. Mas a linha 62 do `lesson-format.md` manda nomear o chunk esperado e trazê-lo de volta num exercício seguinte, e isso só aconteceu com 多大.
4. **Revisão mais curta que a bateria 2** em 11 de 17 partes (ver os números).
5. **Rótulo trocado** (parte 10). O professor usou "Rodada 1/2/3" em vez de "Bateria", que é o rótulo salvo em `Labels`. A linha 137 do `SKILL.md` já manda usar exatamente os rótulos salvos. Uma parte em 19, mas é justamente o que a linha proíbe.

## Problemas da cifra (não da skill)

- **Pinyin fora do itálico passava** (a `main` já corrige, no `1f7a99d`). Na parte 05, o professor escreveu nomes próprios com pinyin entre parênteses, sem itálico: "Eu me chamo 李明 (Lǐ Míng)". A cifra só tira pinyin em itálico. É só a pronúncia de nomes, mas fere a regra de formato da linha 15 do `lesson-format.md` (pinyin sempre em itálico).
- **Palavras compostas viram um código só.** 不要 e 做饭 estão no syllabus como palavras e ganharam um código próprio, sem ligação com 不 + 要 e 做 + 饭, que foi como a skill ensinou. O aluno anotou "nogoloq = 'não querer' (penaq + febaq fundidos)". Ele percebeu a fusão pelo contexto, mas um aluno de verdade veria 不要 como 不 + 要.
- **Os dois bugs corrigidos durante a rodada** (o `à` e o erhua) estão descritos acima. Pelo `is_pinyin`, "Exercício" em itálico seria lido como pinyin e apagado. Na skill, o itálico é só para pinyin, e isso não aconteceu nesta rodada.

## Mudanças que eu proporia na skill (não apliquei nada)

1. **`SKILL.md`, linha 171** (conferência antes de mandar o exercício). Acrescentar: *"The prompt in the learner's language holds nothing the Mandarin answer leaves out: no 'and', 'but', 'already', 'of' or form of address that the answer drops. Rewrite the prompt without it, or use a word the learner has met."* Resolve 6 dos 8 furos.
2. **`lesson-format.md`, linha 17** (dica de troca no chunk). Trocar *"when a word in a chunk can be swapped, say which"* por *"…say which, and give as an example only a word the learner has met"*. Esse é o furo 1.
3. **`lesson-format.md`, linha 54** (palavras que traduzem igual). Hoje a linha termina em *"or accept both"*. Proposta: *"or accept both; when the learner keeps choosing one, ask for the other by name in the next prompt that fits, and in the next part's review"*. Esse é o furo 2.
4. **`lesson-format.md`, linha 62** (alternativa válida). Deixar explícito que vale para palavra nova: *"If the accepted answer leaves out a new word of the part, name it and bring it back within the same round"*. Esse é o furo 3.
5. **`lesson-format.md`, linha 54** (nota de uso). Quando um exercício vai usar a palavra num papel que a célula de significado não mostra, como 不 sozinho como resposta, isso entra na nota de uso ou num chunk. Esse é o [NÃO SEI] da parte 03.
6. **`lesson-format.md`, linha 84** (conferir o roteiro). A regra "uses only words the learner has met" já existe e falhou uma vez (家, parte 14). Proposta: *"check each word of the script against the Done log and this part's table"*.
7. **`lesson-format.md`, linha 11** (contador dos exercícios). Lembrar ali que o nome da bateria vem de `Labels`. Esse é o furo 5. Os outros 18 chats acertaram, então é ajuste fino.

Sobre o tamanho da revisão (linha 177): o problema é antigo, já apareceu na rodada 3, e esta rodada só confirma.

## Limites deste teste

- O aluno não esquece: ele tem o caderno (384 linhas no fim) e anota o que quiser. O teste mostra se a skill ensina e traz de volta o que deveria, não quanto uma pessoa reteria.
- Os códigos vêm com espaço entre as palavras, o que em chinês não há, e isso facilita para o aluno.
- A cifra troca só as palavras. A ordem e a gramática continuam sendo do mandarim, e as palavras gramaticais (了, 的, 吗, classificadores) também viram códigos. O modelo que faz o aluno conhece chinês e pode perceber o disfarce. Por isso, acerto de regra nunca mostrada não prova ensino; o sinal confiável é o erro ou o `[NÃO SEI]`.
- O ambiente não é o app do Claude: tabela em Markdown e áudio como texto. O ditado aparece escrito para o aluno, então vira cópia e não mede nada aqui.
- O transporte por arquivo e a regra de escrever cada arquivo uma vez só são do teste, não da skill.

## Arquivos

- `part-NN/`: mensagens reais (`t-*`, `a-*`), o que o aluno viu e escreveu (`s-*.enc.md`, `a-*.enc.md`), `transcript.md`, `transcript.student.md`, `course-start.md`, `course/course.md`, `check.json`, `watcher.log`.
- `student/notebook.md`: o caderno final do aluno.
- `report.md`: o relatório do `audit.py`.
- `harness/`: os scripts e as instruções usadas (vigia, espera, prompts, coordenador do piloto).
- O `.secret-map.json` não está aqui.
