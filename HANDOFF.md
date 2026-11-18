# Handoff: skill mandarinmaxxing

Estado da skill na versão 0.5.6 (novembro de 2026) e o que vem depois. Leia inteiro antes de mexer.

**Revisão de lançamento (18/11/2026):** o que foi conferido, o que foi corrigido e o que falta para divulgar está em `LAUNCH.md`, no repositório `aveduardo-br/mandarinmaxxing-site`.

**Situação:** 0.5.6 publicada (as aulas são as da 0.5.5; a 0.5.6 só leva a licença para dentro do ZIP). Passou por quatro rodadas de benchmark com aulas simuladas e pelo aluno cifrado (o jump start do HSK 1 inteiro, 19 partes, com um aluno que não sabia a língua) (`qa/benchmark/results/`), cobrindo HSK 1 a 4, mas ainda não por uma pessoa fazendo um curso inteiro. O Eduardo testou a 0.5.1 e achou a revisão simples demais depois de pular para uma aula adiantada; a 0.5.2 corrige isso (rodada 3). Os ajustes finais de cada versão entraram sem nova rodada, e o README de cada rodada diz quais.

- **Converse com o Eduardo em português.** O `SKILL.md`, o `lesson-format.md` e o README são em inglês.
- **Mostre opções antes de mudanças grandes** e teste com aulas reais. O Eduardo valida vendo.
- **Julgue as ideias do Eduardo.** Ele traz ideias para alinhar juntos, não ordens: diga quando discordar e por quê.
- **Publicar é decisão dele.** Mudar a versão no `plugin.json` e subir na `main` publica uma release; faça só quando ele pedir.
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
- `maps/hsk-N.md`: o mapa de um nível. Existem os do HSK 1 a 4.
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

**Uma parte, cerca de uma hora**

A meta é 1 hora por dia (decisão do Eduardo: menos que isso não dá progresso de verdade). Se a parte acaba antes, como no jump start e no ritmo 3, a skill oferece a próxima parte na mesma sessão.

1. Revisão: uma frase longa por palavra da parte anterior, de 5 a 10, com as palavras antigas e as de reforço dentro dessas frases.
2. Vocabulário: tabela e chunks. A decomposição (你好 = 你 + 好) só aparece quando as peças servem agora; senão, nem como curiosidade.
3. Três baterias de 5: chunks, ação completa, sequência (2–3 frases ligadas). Cada palavra nova aparece em pelo menos três frases, porque cinco a sete recuperações fixam melhor que uma a três (Nakata, 2017). O aluno pode pedir mais uma bateria.
4. Escuta: ditado e narração de uma pessoa só, em primeira pessoa, sem diálogo. A narração só entra quando o vocabulário dá para uns 20 segundos. Sem áudio, leitura com reescrita, também de uma pessoa só.
5. Fechamento: o que vem depois e, no fim de uma aula com duas ou mais partes, o role-play da situação.

**Revisão**

- Sem fila nem pontuação. A parte anterior volta na revisão, e uma palavra de cada linha 3, 7, 14, 30 e 60 atrás no registro `Done` volta dentro dos exercícios (no máximo cinco por parte). A skill escolhe essas palavras antes de escrever a revisão.
- As palavras antigas são escolhidas por rodízio (a linha de 3 atrás dá a 1ª palavra, a de 7 atrás a 2ª…), não pelo que encaixa mais fácil. Simulação nos mapas, ritmo 5: com a regra da 0.4.0, 13 a 18% das palavras voltavam depois da revisão da parte seguinte; com a da 0.5.1, de 49 a 73% (`tools/review_coverage.py`). A 0.5.0 tinha duas palavras por visita (68 a 80% no papel), mas no benchmark o professor usou só 2 a 4 das 6 previstas; a regra simples troca cobertura no papel por uma regra que o modelo segue. Repetição espaçada de verdade para cada palavra não cabe numa aula; para isso a skill entrega cartões para o Anki quando o aluno pede.
- `To reinforce` guarda até dez palavras ou chunks em que o aluno precisou de ajuda. O item só sai quando o aluno acerta sem ajuda.
- Ao terminar uma aula com duas ou mais partes, a skill oferece um fechamento: role-play da situação, de quatro a seis falas, sem mudar `Next`.

**Onde o curso fica salvo**

- Um único `course.md` nos documentos do projeto do Claude (a ferramenta do projeto costuma gravar em `claude/course.md`). Acompanha o aluno em qualquer aparelho.
- Uma pasta do computador ligada ao projeto serve só de leitura, não de gravação. Não depender dela.
- Fora de um projeto, a skill mostra os três passos para criar um e oferece uma aula de teste sem salvar.

**Áudio**

- Opcional. Até dois clipes por parte (ditado e narração), uma voz, uma geração cada, uma tomada. No teste, cada clipe gastou de 18 a 45 créditos: uns 3 mil por mês num ritmo diário, dentro da conta gratuita.
- Padrão: ElevenLabs pelo conector do Claude, voz Sarah (`EXAVITQu4vr4xnSDxMaL`), idioma marcado como chinês.
- A skill nunca gera áudio com ferramenta que o aluno não escolheu e nunca repete uma geração por conta própria.

## Decisões e por quê

- **Diálogo com duas vozes foi descartado.** Os conectores do ElevenLabs não têm a ferramenta de diálogo da API (`/v1/text-to-dialogue`). Dá para juntar falas com o nó de composição do conector completo, mas é uma geração por fala e as falas ficam empilhadas se a ordem não for escrita à mão. Uma voz só funciona em qualquer conector.
- **Script local com chave de API foi descartado.** O terminal do app do Claude é isolado e só acessa a internet se a conta liberar. Exigiria pasta, chave e configuração de rede de cada aluno.
- **O botão "ler em voz alta" do Claude não serve** para mandarim: lê hanzi com os sons errados.
- **Correção em texto simples.** Cartões e cores ficaram pesados. Hanzi em negrito, pinyin em itálico, significado normal. Nunca riscar nem italicizar hanzi. A resposta do aluno aparece em citação só na correção.
- **A lista do setup é a fonte da verdade.** Os números das aulas nunca mudam, e a skill não comenta como a aula foi dividida.
- **Sem caderno de aulas por padrão.** A skill só salva `lessons/lesson-NN-P.md` se o aluno pedir.
- **Uma hora por dia é o padrão** (0.5.0). Decisão do Eduardo: menos que isso não dá progresso de verdade, e a skill não promete aprender em 20 minutos. A conta bate com os livros: o HSK Standard Course 1 sugere de 30 a 34 horas-aula para 150 palavras, e o HSK 1 novo tem 300 palavras em 58 partes no ritmo 5. A meta é da sessão, não da parte: parte curta oferece a próxima.
- **Abrir com 你好, com decomposição** (0.5.0). Os dois livros oficiais abrem com cumprimentos. A ideia de começar por 我/你 foi descartada porque mudaria a numeração e os totais do HSK 1. A decomposição do chunk (你好 = 你 + 好) entrega o "eu, você" desde a aula 1. Ela só aparece quando as peças servem na hora; 没关系 não é decomposto nem como curiosidade.
- **Três baterias com nível pelo vocabulário** (0.5.0). "Frase complexa" quer dizer a mais longa que as palavras já vistas permitem, nunca palavras novas. A frase "acordei às 7 e fui trabalhar no hospital" só fica possível depois da aula 11 do HSK 1.
- **Ditado antes da narração** (0.5.0). Na aula 1 o áudio tinha 5 segundos, porque três palavras não fazem uma narração. O ditado funciona com pouco vocabulário. No teste, uma narração saiu como meia conversa (uma atendente falando com um cliente subentendido); a regra agora proíbe falar com alguém ou citar alguém.
- **Revisão espaçada dentro da aula tem limite** (0.5.0). Simulação nos quatro mapas: para cada palavra voltar duas vezes, cada parte precisaria de 10 a 14 palavras antigas. O rodízio de uma palavra por linha faz de 49 a 73% das palavras voltarem pelo menos uma vez, contra 13 a 18% na regra da 0.4.0. A repetição espaçada de cada palavra fica com o Anki, e a skill entrega os cartões quando o aluno pede. Para refazer a conta depois de mudar um mapa ou a regra: `python3 tools/review_coverage.py skills/mandarinmaxxing/maps/hsk-N.md 5`.

## Como testar

1. `python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md` confere o mapa contra a lista oficial.
2. `python3 tools/check_anchors.py 1` (e 2, 3, 4) confere as frases-âncora contra o mapa.
3. `sh tools/build.sh` gera `download/mandarinmaxxing-claude.zip`.
4. No Claude: **Customize → Skills → + → Create skill → Upload a skill**. Criar um projeto vazio com a linha de instruções do README e escrever "start mandarinmaxxing".
5. Fazer uma parte inteira (cerca de 1 hora), abrir um segundo chat no mesmo projeto e pedir a próxima. Para ver o rodízio de palavras antigas sem fazer 15 partes, colocar no projeto um `course.md` já adiantado, com umas 20 linhas no `Done`.

Para depurar, peça à skill um relatório do que ela leu e fez em vez de adivinhar por capturas de tela.

**Benchmark.** `qa/benchmark/` tem os cenários, o roteiro das simulações, o roteiro do juiz e o script de correção. Rodar antes de cada versão nova: um agente por cenário e rodada (`runner.md`), `check_run.py` em cada pasta, e um juiz independente por cenário (`judge.md`). A rodada 1 (0.5.0) está em `qa/benchmark/results/round-1/`, com o resumo no `README.md` de lá. Cada bug novo vira um cenário. Para um aluno que realmente não sabe a língua, `qa/benchmark/cipher/MISSION.md` descreve o benchmark do aluno cifrado (jump start do HSK 1 em sequência, com as palavras trocadas por códigos); rodado em `qa/benchmark/results/cipher-1/` (95 palavras ensinadas, nenhuma deixou de voltar; 8 furos, corrigidos na 0.5.4). O transporte que funcionou está no README de lá: professor e aluno em paralelo trocando arquivos, com um vigia cifrando; o coordenador por parte travou no limite de retomadas.

## Ao publicar

- Publicar é automático: mude a versão em `plugin.json`, atualize o `release-notes.md` e envie para o `main`. A automação em `.github/workflows/release.yml` confere os mapas, gera o ZIP e cria a release com a tag. O README aponta para `releases/latest`.
- Mudança na skill sem mudar a versão não gera release nova: quem baixa continua recebendo o ZIP da última versão.
- As sessões do Claude não conseguem criar tags nem releases direto neste repositório. É a automação que faz isso.
- A tabela de vocabulário carrega a fonte pelo jsDelivr, de um commit fixo deste repositório. Se o arquivo da fonte mudar, atualize o endereço em `lesson-format.md`.
- Avisar o que mudou, para a copy do site ser reescrita.

## Versões de novembro de 2026

- **0.5.0:** partes de cerca de 1 hora (revisão longa, três baterias de 5, ditado e narração), rodízio de palavras antigas, fechamento com role-play, extras sob pedido (leitura, flashcards para o Anki).
- **0.5.1:** correções da rodada 1 do benchmark: primeiras partes com menos baterias, ditado com uma fala por frase, oferta da próxima parte sempre, contador da revisão fixo, rodízio de uma palavra por linha.
- **0.5.2:** a revisão segue o nível do curso (o Eduardo achou a revisão simples demais depois de pular para uma aula adiantada) e, depois de um pulo antes do fim do jump start, usa as palavras do jump start. Cenários do HSK 3.
- **0.5.3:** sem estrutura repetida na parte, baterias 1 e 2 nunca mais curtas que a revisão, registro falado, escuta com cena nova. Cenários do HSK 2 e 4.
- **0.5.4:** furos achados pelo aluno cifrado: o enunciado diz só o que a resposta diz, palavras vistas também em dicas e roteiros, sinônimos pedidos pelo nome, resposta sem a palavra nova volta na mesma bateria.
- **0.5.5:** com poucas palavras, menos exercícios em vez de repetir; o "senhor" para pedir 您 só dentro da frase.
- **0.5.6:** nada muda nas aulas. O LICENSE passa a ir dentro da pasta da skill (`tools/build.sh` copia o da raiz; edite sempre o da raiz), o `SKILL.md` ganha o campo `license`, e o README avisa do pré-requisito de execução de código (Settings → Capabilities).

Notas do juiz (de 35) ao longo das rodadas: de 25 a 30 na 0.5.0 para 29 a 34 nas versões seguintes. O HSK 4 tirou as melhores (34 e 33); as primeiras partes do curso e o HSK 2 são os mais irregulares. Detalhes em `qa/benchmark/results/`.

## O que falta

**1. Validar com gente (a prioridade).** Tudo acima foi medido com aulas simuladas, que mostram se a skill segue o método, mas não se ele ensina.
- O Eduardo e um amigo fazem umas cinco partes cada, o amigo começando do zero (o começo do curso foi o que mais mudou).
- Pontos a olhar: se uma hora cansa, se as baterias ficam repetitivas depois de alguns dias, se a revisão continua no nível depois de pulos, se o ditado da aula 1 faz sentido.
- Quando algo soar estranho, pedir à skill o relatório do que ela fez e transformar o caso num cenário do benchmark.

**2. Skill: o que ainda não está bom.**
- **Naturalidade do mandarim** é a nota mais baixa em todas as rodadas (3 a 4 de 5): frases com cara de tradução, sequências com 可是 ou 所以 que não fecham. A regra de conferir antes de mandar existe; falta saber se ela basta.
- **As primeiras partes** (3 a 9 palavras) oscilam entre 27 e 33. A 0.5.5 deixa dar menos exercícios em vez de repetir; ainda não testado.
- **O HSK 2** foi o mais irregular (33 e 28): baterias abaixo do nível da revisão e 位 usado onde não cabe.
- **Ajustes sem rodada própria:** os finais da 0.5.1, 0.5.2 e 0.5.3, e os da 0.5.5. Se mexer na skill de novo, rodar ao menos `s1`, `s8` e `s10`.

**3. Skill: ideias aprovadas que ainda não foram feitas.**
- **Prova de fechamento:** no fim de uma aula ou de um nível, uma prova curta com palavras antigas sorteadas do registro. Serve ao aluno e dá dado real de retenção.
- **Instalação mais simples** que o ZIP (o Eduardo acha o ZIP e o `npx` complicados para o aluno).
- **Mapas do HSK 5 e 6:** hoje a skill monta o mapa na hora, com as nossas regras. Um cenário de benchmark que confira o mapa gerado com `check_map.py` ainda não foi feito; é barato e é onde a skill trabalha sem rede.

**4. Site** (repositório `aveduardo-br/mandarinmaxxing-site`).
- **Card 04 (áudio):** o texto já fala em ditado e narração de uma pessoa, mas o exemplo ainda é o diálogo de duas vozes. Gerar o áudio novo com a Sarah e refazer os tempos em `DialogueCard.astro`.
- **"Lesson" × "part":** no site, "lesson" é o que se faz num dia; no README da skill, isso é "part". Alinhar, provavelmente adaptando o README.
- **Seção "Your course":** ainda fala em uma aula por dia; o Eduardo decidiu não mudar por enquanto.
- **Formulação sobre a prova**, ainda em aberto no `messaging.md`: a lista da skill (syllabus de novembro de 2025) vale para as provas regulares do HSK 1 a 6 a partir de 13 de dezembro de 2026.

- **Seção 07 "How it's being built"** está no site desde 17/11/2026 (versão A2, tom de projeto em andamento, antes do FAQ). Falta criar a seção no Paper (páginas "Site — versão final (proposta)" e "Site — estilo referência (grafite + sálvia)"): o arquivo não estava aberto no Paper quando a seção foi ao ar.

**5. Conferências pendentes.**
- O conector do ElevenLabs numa **conta gratuita** (os testes foram numa conta Creator).

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

## Outros projetos parecidos (pesquisa de novembro de 2026)

Ninguém faz o que a skill faz: a lista oficial inteira de cada nível, cada palavra uma vez, reorganizada num mapa fixo e conferido, com a aula dada no chat. O que existe:

- **New HSK Course (o livro oficial do HSK 3.0).** Também é situacional, com "dramas" de personagens em cenas reais. O HSK 1 tem 15 lições com as 300 palavras. Por isso o site não deve dizer que o livro é uma lista solta: a diferença é o jeito, reorganizado do nosso jeito (aulas curtas, blocos que formam frase, ritmo do aluno, grátis e melhorando aos poucos). O contraste "lista solta" ainda vale para o HSK Standard Course antigo.
- **Skills de agente (ClawHub/OpenClaw, para Claude Code):** chinese-tutor (conteúdo real empurrado em horários, sem lista do HSK, revisão de 1, 3, 7 e 14 aulas atrás, e propaganda de um app e de aulas no TikTok), Mandarin Chinese Daily Drill (sessão gerada na hora, sem progresso salvo), hsk-learning (controle de domínio e quizzes), xuezh (motor com CLI local) e chinese-learning-assistant (fluência para HSK 4 ou mais). Nenhuma funciona só subindo um ZIP no app do Claude.
- **Chunking Chinese.** É o mais próximo na ideia de chunks: combina chunks falando em voz alta, por nível do HSK e contexto. É pago (US$ 30 por mês) e não serve para iniciante.
- **Mandarin Temple** (curso completo de HSK com vozes de IA, pago), **LearnChinese.ai** (projeto pessoal que segue a ordem do livro), listas e PDFs "por tema" (categorias como cores e animais, que é a aula de categoria que o Eduardo rejeitou), e GPTs e prompts genéricos sem mapa nem progresso.
- **O que pegamos deles na 0.5.0:** a lista do que o aluno pode pedir (comandos do chinese-tutor), o fechamento da aula (o prompt russo "Laoshi" faz um diálogo a cada sete aulas) e a ponte para o Anki.
- **O que ficou de fora:** avaliação de fala (Chunking Chinese) e ajuste automático de nível (chinese-tutor). A fala exigiria reconhecimento de voz.

A prova: a lista da skill (syllabus de novembro de 2025) vale para as provas regulares do HSK 1 a 6 a partir de 13 de dezembro de 2026. Até 7 de novembro de 2026, as provas usavam o HSK 2.0.

## Regras

- Não inventar palavras nem números do HSK. Conferir contra o syllabus.
- Não prometer fluência, aprovação nem avaliação de pronúncia.
- Não prometer no site o que a skill ainda não faz.
