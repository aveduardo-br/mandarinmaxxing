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
- `maps/hsk-N.md`: o mapa de um nível. Existem os do HSK 1 a 4 (os do 2 a 4 ainda não foram publicados, ver abaixo).
- `syllabus/hsk-1..6.csv`: lista oficial de novembro de 2025.
- `fonts/`: fonte Kaiti (LXGW WenKai GB Lite) recortada para os 1.940 hanzi do HSK 1 a 6.

**Aula e parte**

- Cada situação do mapa é uma **aula**, com número fixo. A aula 20 é sempre "Na escola", em qualquer ordem de estudo.
- A aula é dada em **partes**. O ritmo (3, 5, 7 ou outro número) conta palavras novas por parte.
- O mapa agrupa as palavras em blocos de 2 a 4. A linha `Split` de cada aula diz quantos blocos entram em cada parte nos ritmos 3 / 5 / 7.
- HSK 1: 300 palavras, 22 aulas, 98 blocos. Partes nos ritmos 3 / 5 / 7: 97 / 58 / 42. As aulas 01 a 07 são o jump start.
- HSK 2: 200 palavras, 19 aulas. Partes: 66 / 38 / 29. Jump start 01 a 04.
- HSK 3: 500 palavras, 37 aulas. Partes: 168 / 94 / 69. Jump start 01 a 04.
- HSK 4: 1.000 palavras, 56 aulas. Partes: 319 / 173 / 130. Jump start 01 a 05.
- A numeração recomeça em 01 a cada nível. Para o aluno, o título sempre leva o nível: "HSK 2 · Aula 1". No registro `Done` do `course.md` a linha leva o prefixo do nível (`2-01.1`).
- Ao terminar um nível, a skill oferece o seguinte no mesmo `course.md` e mantém o registro `Done`, para as palavras do nível anterior continuarem voltando.

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
2. `python3 tools/check_anchors.py 1` (e 2, 3, 4) confere as frases-âncora contra o mapa.
3. `sh tools/build.sh` gera `download/mandarinmaxxing-claude.zip`.
4. No Claude: **Customize → Skills → + → Create skill → Upload a skill**. Criar um projeto vazio com a linha de instruções do README e escrever "start mandarinmaxxing".
5. Fazer uma parte inteira, abrir um segundo chat no mesmo projeto e pedir a próxima.

Para depurar, peça à skill um relatório do que ela leu e fez em vez de adivinhar por capturas de tela.

## Ao publicar

- Publicar é automático: mude a versão em `plugin.json`, atualize o `release-notes.md` e envie para o `main`. A automação em `.github/workflows/release.yml` confere os mapas, gera o ZIP e cria a release com a tag. O README aponta para `releases/latest`.
- Mudança na skill sem mudar a versão não gera release nova: quem baixa continua recebendo o ZIP da última versão.
- As sessões do Claude não conseguem criar tags nem releases direto neste repositório. É a automação que faz isso.
- A tabela de vocabulário carrega a fonte pelo jsDelivr, de um commit fixo deste repositório. Se o arquivo da fonte mudar, atualize o endereço em `lesson-format.md`.
- Avisar o que mudou, para a copy do site ser reescrita.

## O que falta

1. **Publicar os mapas do HSK 2 a 4 e o HSK 1 revisado.** Estão na branch `hsk-maps-2-4`, sem versão nova. O que já foi feito está em "Como os mapas foram conferidos", abaixo. Falta o teste com aluno de verdade. Para publicar: subir a versão em `plugin.json`, atualizar `release-notes.md` e a seção "What it covers" do README, e juntar no `main`. O HSK 1 mudou só dentro dos blocos: números, nomes e totais de partes (97 / 58 / 42) são os mesmos da versão publicada.
2. **Mapas do HSK 5 e 6.** Sem mapa, a skill monta um na hora a partir da lista oficial, sem revisão humana.
3. **Site.** Reescrever a copy para esta versão e fazer a página de instalação: os quatro passos e uma seção "Áudio (opcional)", com os nomes reais dos botões.
4. **Confirmar com uma conta gratuita do ElevenLabs** que o conector funciona. Os testes foram feitos numa conta Creator.
5. **Formulação sobre a prova**, ainda em aberto no `messaging.md`.

## Como fazer o mapa de um nível

O mapa do HSK 1 (`skills/mandarinmaxxing/maps/hsk-1.md`) é o modelo. Os outros níveis seguem o mesmo formato, com as palavras de `syllabus/hsk-N.csv`.

**Formato do arquivo**

- Cabeçalho com a fonte, o número de aulas e o total de partes nos ritmos 3 / 5 / 7.
- Uma aula por situação: `## NN | jump-start ou situation | Nome`.
- Abaixo, a linha `Split:` e uma linha `- ` por bloco, na ordem em que as palavras são ensinadas.
- As palavras ficam com a grafia oficial, incluindo o número de sentido (como `本1`).

**Critérios que o Eduardo aprovou no HSK 1**

- **A aula precisa de um tema** que dê para conversar: uma situação, não uma categoria. "Compras e pagamento", não "números".
- **Blocos de 2 a 4 palavras que formam frases juntas.** O aluno tem que conseguir dizer algo com o bloco.
- **Palavras parecidas ou da mesma categoria em blocos diferentes**, para não confundir (a pesquisa está em `docs/research.md` do site).
- **Palavras de função cedo.** No HSK 1, as aulas 01 a 07 são o jump start: o que toda aula depois usa. Método "igual um bebê": eu quero, eu gosto, eu sou.
- **Passos pequenos no começo.** As duas primeiras aulas têm partes menores.
- **A aula tem que fazer sentido em qualquer ritmo.** Confira as partes nos ritmos 3, 5 e 7 antes de fechar.
- **Palavra de apoio é exceção**, nunca requisito, e nunca se inventa um chunk para justificar uma.
- Não precisa ser perfeito. O Eduardo prefere fechar um mapa bom e melhorar com o uso.

**Como os mapas foram conferidos**

- `tools/check_map.py`: cada palavra oficial uma vez, blocos de 2 a 4.
- `tools/qa_map.py`: tamanho das partes em cada ritmo, parecidas no mesmo bloco, composta antes da simples.
- `qa/anchors/hsk-N.md` e `tools/check_anchors.py`: uma frase-âncora por bloco (660 blocos nos quatro níveis), usando todas as palavras do bloco e só vocabulário já ensinado no pior caso (jump start mais a própria aula). A skill não lê esses arquivos; eles são a prova de que o bloco funciona e ficam fora do ZIP.
- Duas revisões independentes por nível. A segunda foi bloco por bloco, sem teto, com a frase ao lado: reescreveu mais de 40% das frases e reagrupou blocos em cerca de 50 aulas.
- Quatro ensaios da skill com aluno simulado: curso novo no HSK 2, retomada num segundo chat e fim do HSK 1 com passagem para o HSK 2 (duas vezes). Os buracos que apareceram nas instruções foram corrigidos no `SKILL.md` e no `lesson-format.md`.

**O que os mapas do HSK 2 a 4 ensinaram**

- **Cada nível tem jump start curto**, com as palavras de ligação dentro de aulas com tema (dar opinião, explicar por quê). Gramática central e palavras de uso geral vão para lá mesmo que caibam numa situação: 比, 得, 从, 着, 正, 地, 快 e 慢 no HSK 2; 把, 被 e 用 no HSK 3. O sinal de que uma palavra pede jump start é ela fazer falta nas frases-âncora de várias aulas.
- **A palavra simples vem antes da composta** quando as duas estão na mesma aula (考 antes de 考试). Entre aulas de ordem livre não dá para garantir.
- **Uma palavra de cada família por bloco.** Sinônimos, antônimos e séries (cores, pontos cardeais, 高温 / 低温 / 降温) ficam em blocos diferentes.
- **A lista oficial repete grafias** com sentido e pronúncia diferentes: 过 no HSK 2, 得 no HSK 3, 重 e 空 no HSK 4. Cada uma fica em uma aula, e o cabeçalho do mapa diz quais.
- **No máximo quatro partes por aula no ritmo 5.** Aula maior que isso é dividida em duas situações.
- **Sufixos e palavras presas** (子, 员, 性, 感, 者) vão depois das palavras que os contêm, para o aluno reconhecer o padrão.
- **Números de aula só mudam antes de publicar.** Depois de publicado, o número é para sempre. No HSK 1, já publicado, as correções trocaram palavras de bloco sem mudar o tamanho dos blocos, para os totais de partes não mudarem.
- **Frase que passa no script não é frase natural.** O conferidor só garante o vocabulário. Quem julga se a frase soa como chinês de verdade é um revisor que não a escreveu.
- **Faltas da lista oficial:** não há 切 (cortar), 杯 (copo, como classificador) nem sobrenomes ou nomes de cidade nos níveis 1 a 4. São os casos típicos de palavra de apoio.

**Passo a passo**

1. Ler `syllabus/hsk-N.csv` e montar a lista de situações com as palavras de cada uma. O Eduardo não lê hanzi: mostre sempre o significado ao lado.
2. Montar os blocos e escrever o arquivo.
3. Rodar `python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-N.md`. Ele confere que cada palavra oficial aparece uma vez, que os blocos têm de 2 a 4 palavras, e aponta blocos só com substantivos, numerais ou classificadores, que costumam não formar frase.
4. Rodar `python3 tools/split_map.py skills/mandarinmaxxing/maps/hsk-N.md` para escrever as linhas `Split` e atualizar o número de aulas e o total de partes no cabeçalho. Depois, `python3 tools/qa_map.py` no mesmo arquivo: ele lista o tamanho das partes em cada ritmo, palavras parecidas no mesmo bloco e compostas antes da simples. Por fim, escrever `qa/anchors/hsk-N.md` (uma frase por bloco) e rodar `python3 tools/check_anchors.py N`; bloco sem frase natural é bloco a refazer.
5. Pedir a revisores independentes (subagentes que não viram o mapa nascer), em trechos de umas 20 aulas e sem teto de correções, para ler bloco por bloco com a frase ao lado. Cada um trabalha numa cópia e só entrega com os três conferidores passando.
6. Testar duas ou três aulas de verdade com o Eduardo antes de publicar.
7. Subir a versão em `plugin.json`, atualizar `release-notes.md` e o README (seção "What it covers"). No site, atualizar o FAQ "Which levels" e decidir se a seção 02 mostra os dois níveis.

## Regras

- Não inventar palavras nem números do HSK. Conferir contra o syllabus.
- Não prometer fluência, aprovação nem avaliação de pronúncia.
- Não prometer no site o que a skill ainda não faz.
