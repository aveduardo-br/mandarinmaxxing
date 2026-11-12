# Handoff: nova versão da skill mandarinmaxxing

Ponto de partida para o chat que vai melhorar a skill. Leia este arquivo inteiro antes de começar.

- **Converse com o Eduardo em português.** O `SKILL.md` e o README são em inglês.
- **Primeiro a skill, depois o site.** A copy do site vai descrever esta nova versão, então nada de prometer no site o que ainda não estiver aqui.

## Leia antes

- `skills/mandarinmaxxing/SKILL.md`: o comportamento atual.
- No repositório do site (`aveduardo-br/mandarinmaxxing-site`):
  - `docs/messaging.md`: objetivo, frase principal, pilares e o que não dizer.
  - `docs/research.md`: números do HSK 3.0 e pesquisa sobre o método.

## O norte

> The same HSK words, reorganized around everyday conversations.

- A skill segue o HSK (mesma lista oficial), mas organiza as aulas em torno de **situações** do dia a dia, com foco em conversa.
- Quem termina um nível passou pelas mesmas palavras desse nível, em outra ordem.
- Nenhum método está errado: é uma opção para quem prefere estudar assim.

## O que a skill já faz

- Setup com nível, ritmo (1–4 / 5–7 / 8–10), idioma, áudio e fonte.
- Índice numerado por situação, cobrindo cada palavra oficial uma vez e conferido contra a fonte.
- Aula em 4 etapas: revisão, vocabulário e chunks, tradução escrita, diálogo.
- Revisão espaçada (cerca de 3, 7 e 14 aulas depois) e prática extra nas palavras com dificuldade.
- Progresso salvo num único `mandarinmaxxing-course.md`, quando o chat tem pasta compartilhada.

## O que o Eduardo quer que ela passe a fazer

1. **Syllabus novo por padrão.** Usar o HSK 3.0 de novembro de 2025 (300 / 500 / 1.000 / 2.000 / 3.600 / 5.400 palavras acumuladas nos níveis 1–6), ou outra lista bem documentada.
2. **Índice aprovado antes de começar.** Montar o índice do nível inteiro, mostrar ao aluno e só começar depois da aprovação.
3. **Uma situação ao longo de várias aulas.** Ex.: "arrumar a casa" em 3–4 aulas, cada dia uma parte com o vocabulário de apoio. A pesquisa apoia distribuir palavras parecidas (ex.: nomes de cômodos) por aulas diferentes.
4. **Completar a situação agora.** Trazer na hora as palavras que completam a situação, em vez de esperar o livro apresentá-las. Palavras de outros níveis entram por importância, quando a situação pede.
5. **Extras em segundo plano.** Não marcar na aula de que nível cada palavra vem. Explicar só se o aluno perguntar. (O Eduardo quer testar isso antes de fechar.)
6. **Um arquivo por aula.** Salvar `aula-01.md`, `aula-02.md`… com o vocabulário e os chunks de cada aula, para sempre poder voltar a uma aula. Pensar também num modelo de estudo de chunks e em como retomar.
7. **Setup mais personalizado.** Mais perguntas no início: palavras por dia, quantidade de revisão, quantidade de chunks. O Eduardo ainda não definiu quais perguntas são essas; desenhe com ele.
8. **Install e setup mais simples.** O Eduardo quer melhorar o caminho de instalação também.
9. **Palavra extra opcional.** O ritmo (1–4 / 5–7 / 8–10) continua como referência, mas não precisa ser rígido. Se uma palavra a mais completar um chunk da aula, a skill a apresenta junto com o vocabulário, diz que é uma palavra a mais e pergunta se o aluno quer estudá-la. O aluno decide. Isso também pode substituir as faixas fixas por um número-alvo ("umas 5 palavras por aula").
10. **Revisão espaçada que se adapta.** Não existe intervalo perfeito; a pesquisa (ver `docs/research.md` do site) indica que o melhor espaçamento depende de por quanto tempo se quer lembrar. Proposta, para validar com o Eduardo:
    - **Por desempenho, sem o aluno configurar intervalos.** Errou ou precisou de ajuda: a palavra volta cedo, na próxima aula. Acertou sem ajuda: o intervalo cresce (por exemplo 1 → 3 → 7 → 14 aulas). Acertou várias vezes seguidas: sai da fila.
    - **No setup, só uma pergunta simples de intensidade** ("pouca, média ou muita revisão"), que muda quantos itens antigos entram por aula, não a matemática.
11. **Um arquivo de revisão com os erros.** Em vez de um arquivo de erros separado, um `revisao.md` com uma linha por palavra ou chunk: aula em que foi aprendido, próxima revisão, quantas vezes errou e o tipo de erro (ex.: classificador, ordem da frase, palavra trocada). É a "memória" da revisão espaçada: a skill lê esse arquivo para montar a revisão e pode criar exercícios para os erros que se repetem.

Estrutura de arquivos sugerida: `curso.md` (configurações, índice e progresso), `aulas/aula-NN.md` (vocabulário e chunks de cada aula) e `revisao.md` (fila de revisão e erros). Desenhar e testar antes de fechar.

## Regras

- Não inventar palavras nem números do HSK. Conferir contra o syllabus.
- Não prometer fluência, aprovação nem avaliação de pronúncia.
- Testar com aulas reais antes de dar por pronto. O Eduardo valida vendo.
- Ao terminar: atualizar README, gerar a release e avisar o que mudou, para a copy do site ser reescrita.

## Sugestão de modelo

Usar o Claude Fable para desenhar e escrever o novo `SKILL.md`, que é o trabalho de raciocínio mais pesado. Para rodadas de teste e ajustes pequenos, o Opus basta.

## Mensagem para abrir o novo chat

> Quero fazer a nova versão da skill mandarinmaxxing. O repositório é `aveduardo-br/mandarinmaxxing`. Leia o `HANDOFF.md` de lá e os arquivos `docs/messaging.md` e `docs/research.md` do repositório `aveduardo-br/mandarinmaxxing-site`. Vamos começar desenhando juntos o novo setup e a organização das aulas antes de editar o SKILL.md. Converse comigo em português.
