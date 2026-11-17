# Missão: o aluno cifrado (jump start do HSK 1)

Você vai rodar um benchmark da skill mandarinmaxxing com um aluno que realmente não sabe a língua. Leia este arquivo inteiro antes de começar. Converse com o Eduardo em português.

## Por que existe

Nos benchmarks anteriores (`qa/benchmark/results/`), um agente só fazia professor e aluno, e o aluno já sabia chinês: quando "não conhecia" uma palavra, era fingimento. Aqui o professor ensina chinês de verdade, mas um script troca cada palavra chinesa por um código sem sentido (e apaga o pinyin) antes de a mensagem chegar ao aluno. O aluno só conhece o que o professor ensinou e anota num caderno. Se uma frase exigir uma palavra que nunca foi ensinada, ele trava de verdade.

E, em vez de uma parte solta, são as 19 partes do jump start do HSK 1 (aulas 1 a 7, ritmo 5) em sequência, cada uma num "chat novo", com o `course.md` passando de uma para a outra. Isso mostra furos que só aparecem com o tempo: palavras que nunca voltam, lista de reforço crescendo, rodízio, rota, revisão sempre igual.

## O que a pasta tem

- `cipher.py`: cifra (`encode`) e decifra (`decode`) uma mensagem. Gera `.secret-map.json`, que o aluno nunca pode ler.
- `tutor.md`: instruções do agente professor.
- `student.md`: instruções do agente aluno.
- `audit.py`: `assemble` monta as transcrições de uma parte; `report` faz o relatório final.
- O script de correção por parte é o de sempre, `qa/benchmark/check_run.py`.

## Antes de começar

1. Clone o repositório `aveduardo-br/mandarinmaxxing` em `/home/claude/mandarinmaxxing` e trabalhe a partir dele.
2. Crie a pasta da rodada: `/home/claude/mm-bench/cipher-1/`, com `course/` vazia e `student/notebook.md` vazio.
3. Rode `python3 qa/benchmark/cipher/cipher.py encode` uma vez num arquivo qualquer para gerar o mapa.

## Uma parte, passo a passo

Para cada parte `NN` (de 01 a 19):

1. Crie `part-NN/` e copie `course/course.md` para `part-NN/course-start.md` (na parte 01 ele ainda não existe; pule).
2. Escreva a primeira mensagem do aluno em `part-NN/a-000.md`, e uma cópia igual em `a-000.enc.md`: `start mandarinmaxxing` na parte 01, `próxima aula` nas outras.
3. Crie um agente professor novo (modelo Sonnet), com a tarefa: ler `qa/benchmark/cipher/tutor.md`, `PART=/home/claude/mm-bench/cipher-1/part-NN`, `COURSE=/home/claude/mm-bench/cipher-1/course`, e que a mensagem `a-000.md` chegou.
4. Crie um agente aluno novo (modelo Sonnet), com a tarefa: ler `qa/benchmark/cipher/student.md`, `PART=...part-NN`, `NOTEBOOK=/home/claude/mm-bench/cipher-1/student/notebook.md`, e esperar a primeira mensagem.
5. Repita até a parte acabar:
   - Quando o professor responder `sent`, cifre: `python3 qa/benchmark/cipher/cipher.py encode part-NN/t-K.md part-NN/s-K.enc.md`.
   - Mande ao aluno (SendMessage): "chegou `s-K.enc.md`".
   - Quando o aluno responder `sent`, decifre: `python3 qa/benchmark/cipher/cipher.py decode part-NN/a-K.enc.md part-NN/a-K.md`.
   - Mande ao professor: "chegou `a-K.md`".
   - A parte acaba quando `t-K.md` terminar com `[END OF PART]`. Mande essa última mensagem cifrada ao aluno, para ele atualizar o caderno, e espere o `sent`.
6. Copie `course/course.md` para `part-NN/course/course.md` e rode `python3 qa/benchmark/cipher/audit.py assemble part-NN`.

As mensagens entre os agentes são só avisos curtos ("chegou o arquivo X"). O conteúdo fica nos arquivos, para a sua conversa não encher.

## Primeiro, o piloto

Rode **só a parte 01** e pare. Confira com o Eduardo:
- se a troca de mensagens funcionou do começo ao fim;
- se o `transcript.student.md` não mostra nenhum chinês nem pinyin (só códigos e português);
- se o aluno respondeu em códigos e o `a-K.md` decifrado faz sentido para o professor;
- quanto custou (tokens e minutos).

Se você não conseguir continuar um agente com SendMessage, a alternativa é criar um agente coordenador por parte, que faz a troca lá dentro e só te devolve um resumo. Teste isso também no piloto. Se nada disso funcionar neste ambiente, diga ao Eduardo, e a alternativa é rodar as 19 partes em sequência sem a cifra (`qa/benchmark/runner.md`, um agente só), que ainda pega os furos ao longo do tempo.

## Depois do piloto

Com o OK do Eduardo, rode as partes 02 a 19, uma de cada vez (cada uma depende do `course.md` da anterior). Pare antes se a parte terminar com `Next` na aula 08 ou se o `course.md` quebrar (aí registre onde e por quê).

No fim, rode `python3 qa/benchmark/cipher/audit.py report /home/claude/mm-bench/cipher-1`. O `report.md` mostra:
- as palavras que nunca voltaram depois de ensinadas;
- quantas vezes cada palavra voltou e em que partes;
- cada `[NÃO SEI]` do aluno, com a parte, para você ver qual frase pediu o quê;
- por parte: o registro, o `Next`, o tamanho da revisão contra o da bateria 2, as palavras antigas usadas.

Leia também os `[NÃO SEI]` nas transcrições: cada um é ou um furo da skill (pediu palavra não ensinada) ou um limite do aluno (ensinada, mas ele não anotou). Separe os dois.

## Entrega

1. Copie a rodada para `qa/benchmark/results/cipher-1/` (sem o `.secret-map.json`).
2. Escreva `qa/benchmark/results/cipher-1/README.md` em português, no formato dos READMEs das outras rodadas: como foi rodado, os números, o que funcionou, os furos encontrados (com a parte e a frase), e as mudanças que você proporia na skill, citando a linha.
3. Não mude a skill nem publique versão sem o Eduardo pedir. Mostre as mudanças propostas primeiro.
4. Faça commit e push só da pasta de resultados.

## Limites que o relatório deve dizer

- O aluno não esquece: ele tem o caderno e anota o que quiser. O teste mostra se a skill ensina e traz de volta o que deveria, não quanto uma pessoa reteria.
- Os códigos vêm com espaço entre as palavras, o que facilita para o aluno (em chinês não há espaço).
- O ambiente não é o app do Claude: tabela em Markdown e áudio como texto.
- Custo esperado: perto de 150 mil tokens por parte só para o professor, mais o aluno. As 19 partes devem passar de 3 milhões.
