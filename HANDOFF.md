# Handoff: skill mandarinmaxxing

Estado da skill na versão 0.3.0 (novembro de 2026) e o que vem depois. Leia inteiro antes de mexer.

- **Converse com o Eduardo em português.** O `SKILL.md`, o `lesson-format.md` e o README são em inglês.
- **Mostre opções antes de mudanças grandes** e teste com aulas reais. O Eduardo valida vendo.
- **Pesquise antes de afirmar.** Limites de ferramenta, de conector ou de plano só valem depois de testados.

## O norte

> The same HSK words, reorganized around everyday conversations.

- Mesma lista oficial do HSK, em outra ordem: por situação do dia a dia.
- Nenhum método está errado. É uma opção para quem prefere estudar assim.
- Skill enxuta: instalar e usar tem que ser o mais simples possível. Nada de pasta no computador, script ou chave colada no chat.
- Mensagem e tom: `docs/messaging.md` no repositório `aveduardo-br/mandarinmaxxing-site`.

## Como a skill funciona hoje

**Arquivos** (`skills/mandarinmaxxing/`)

- `SKILL.md`: setup, mapa, partes, revisão, salvar e retomar.
- `lesson-format.md`: formato de cada mensagem da aula (título, tabela, correção, leitura, áudio). A skill lê uma vez por chat.
- `maps/hsk-N.md`: o mapa de um nível. Só o HSK 1 existe.
- `syllabus/hsk-1..6.csv`: lista oficial de novembro de 2025.
- `fonts/`: fonte Kaiti (LXGW WenKai GB Lite) recortada para os 1.940 hanzi do HSK 1 a 6.

**Aula e parte**

- Cada situação do mapa é uma **aula**, com número fixo. A aula 20 é sempre "Na escola", em qualquer ordem de estudo.
- A aula é dada em **partes**. O ritmo (3, 5, 7 ou outro número) conta palavras novas por parte.
- O mapa agrupa as palavras em blocos de 2 a 4. A linha `Split` de cada aula diz quantos blocos entram em cada parte nos ritmos 3 / 5 / 7.
- HSK 1: 300 palavras, 22 aulas, 98 blocos. Partes nos ritmos 3 / 5 / 7: 97 / 58 / 42. As aulas 01 a 07 são o jump start.

**Uma parte tem quatro etapas**

1. Revisão: frases para traduzir, cobrindo a parte anterior e as palavras a reforçar.
2. Vocabulário: tabela com hanzi, pinyin e significado.
3. Tradução escrita: uma frase por vez, do idioma do aluno para o mandarim.
4. Texto final: leitura com tarefa de reescrita ou, com áudio, um clipe para ouvir e perguntas.

**Revisão**

- Sem fila nem pontuação. A parte anterior volta na revisão, e palavras de 3, 7 e 14 linhas atrás no registro `Done` voltam dentro dos exercícios.
- `To reinforce` guarda até dez palavras em que o aluno precisou de ajuda na última parte.

**Onde o curso fica salvo**

- Um único `course.md` nos documentos do projeto do Claude (a ferramenta do projeto costuma gravar em `claude/course.md`). Acompanha o aluno em qualquer aparelho.
- Uma pasta do computador ligada ao projeto serve só de leitura, não de gravação. Não depender dela.
- Fora de um projeto, a skill mostra os três passos para criar um e oferece uma aula de teste sem salvar.

**Áudio**

- Opcional. Um clipe por parte, uma voz, uma geração, uma tomada.
- Padrão: ElevenLabs pelo conector do Claude, voz Sarah (`EXAVITQu4vr4xnSDxMaL`), idioma marcado como chinês.
- A skill nunca gera áudio com ferramenta que o aluno não escolheu e nunca repete uma geração por conta própria.

## Decisões e por quê

- **Diálogo com duas vozes foi descartado.** Os conectores do ElevenLabs não têm a ferramenta de diálogo da API (`/v1/text-to-dialogue`). Dá para juntar falas com o nó de composição do conector completo, mas é uma geração por fala e as falas ficam empilhadas se a ordem não for escrita à mão. Uma voz só funciona em qualquer conector.
- **Script local com chave de API foi descartado.** O terminal do app do Claude é isolado e só acessa a internet se a conta liberar. Exigiria pasta, chave e configuração de rede de cada aluno.
- **O botão "ler em voz alta" do Claude não serve** para mandarim: lê hanzi com os sons errados.
- **Correção em texto simples.** Cartões e cores ficaram pesados. Hanzi em negrito, pinyin em itálico, significado normal. Nunca riscar nem italicizar hanzi. A resposta do aluno aparece em citação só na correção.
- **A lista do setup é a fonte da verdade.** Os números das aulas nunca mudam, e a skill não comenta como a aula foi dividida.
- **Sem caderno de aulas por padrão.** A skill só salva `lessons/lesson-NN-P.md` se o aluno pedir.

## Como testar

1. `python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md` confere o mapa contra a lista oficial.
2. `sh tools/build.sh` gera `download/mandarinmaxxing-claude.zip`.
3. No Claude: **Customize → Skills → + → Create skill → Upload a skill**. Criar um projeto vazio com a linha de instruções do README e escrever "start mandarinmaxxing".
4. Fazer uma parte inteira, abrir um segundo chat no mesmo projeto e pedir a próxima.

Para depurar, peça à skill um relatório do que ela leu e fez em vez de adivinhar por capturas de tela.

## Ao publicar

- Publicar é automático: mude a versão em `plugin.json`, atualize o `release-notes.md` e envie para o `main`. A automação em `.github/workflows/release.yml` confere os mapas, gera o ZIP e cria a release com a tag. O README aponta para `releases/latest`.
- Mudança na skill sem mudar a versão não gera release nova: quem baixa continua recebendo o ZIP da última versão.
- As sessões do Claude não conseguem criar tags nem releases direto neste repositório. É a automação que faz isso.
- A tabela de vocabulário carrega a fonte pelo jsDelivr, de um commit fixo deste repositório. Se o arquivo da fonte mudar, atualize o endereço em `lesson-format.md`.
- Avisar o que mudou, para a copy do site ser reescrita.

## O que falta

1. **Mapa do HSK 2**, depois o 3. Os níveis 4 a 6 ficam para mais tarde. Sem mapa, a skill monta um na hora a partir da lista oficial, sem revisão humana.
2. **Site.** Reescrever a copy para esta versão e fazer a página de instalação: os quatro passos e uma seção "Áudio (opcional)", com os nomes reais dos botões.
3. **Confirmar com uma conta gratuita do ElevenLabs** que o conector funciona. Os testes foram feitos numa conta Creator.
4. **Formulação sobre a prova**, ainda em aberto no `messaging.md`.

## Regras

- Não inventar palavras nem números do HSK. Conferir contra o syllabus.
- Não prometer fluência, aprovação nem avaliação de pronúncia.
- Não prometer no site o que a skill ainda não faz.
