# Handoff: skill mandarinmaxxing

Estado da skill em 18/11/2026 e o que vem depois. Leia inteiro antes de mexer.

**Onde está cada coisa**

- **`main` e a release publicada: 0.8.0** (28/11/2026, commit `64e2d19`). O Eduardo mandou publicar depois das rodadas abaixo; a branch `review-fixes` foi juntada na `main` e onde as notas dizem "ainda sem publicar" leia "publicado". O site subiu no mesmo dia com os fatos da 0.8.0. No mesmo dia o Eduardo testou a versão publicada num projeto real: fez uma parte, pediu para salvar, abriu um chat novo e pediu para continuar; a skill deu a aula certa e revisou a parte anterior. Salvar e retomar está verificado. Falta saber se o fechamento (`course.py close`) acontece sem o aluno pedir.
- **Rodada de 28/11/2026 (mesma branch `review-fixes`, 0.8.0, ainda sem publicar):** o `course.py` passou a ser o único que escreve o `course.md` (formato 2: `Format: 2`, rótulos nomeados, `Route`, `Next`, `To reinforce`, `Lessons` sem contagem de partes, `Done`). Comandos: `new`, `part`, `close` (`--missed`, `--recovered`), `jump`, `known`, `study`, `pace`, `level`, `audio`, `migrate`, `check`, `progress`, `overview`. Arquivos antigos passam por `migrate`. `tools/test_scripts.py` tem 52 testes e roda na release. Simulações com aluno fixo (`qa/benchmark/student.py`, roteiro em `runner-fixed.md`): resultados em `qa/benchmark/results/round-9/`, com os cinco defeitos que acharam e que já estão corrigidos. Em aberto: começo do HSK 1 ainda ralo; palavras naturais faltando em algumas situações (张, 银行 na aula 18 do HSK 3); a lista de reforço esvazia fácil; `tools/check_urls.py` nunca rodou contra os endereços reais (o sandbox bloqueia o jsDelivr); o texto lido por aula está em cerca de 3.800 palavras (a meta era 3.500); salvar e retomar num projeto real do Claude nunca foi testado; nenhum nativo leu as frases. A mensagem do commit `127b555` saiu sem duas palavras (crases executadas pelo shell); o conteúdo do commit está certo. O site tem uma branch `skill-0.8` com os fatos da 0.8.0, para subir no dia da publicação, e uma proposta de novo norte em https://claude.ai/artifact/EzZSrh8NCVbGych3Pc49wj.
- **Segunda revisão independente (27/11/2026, feita por outra IA no Codex, aplicada na mesma branch):** achou defeitos de estado que as simulações não pegaram. Corrigido: `course.py` reconstrói o andamento de cada aula pelas palavras que estão no `Done` (uma aula começada num ritmo mantém a divisão daquele ritmo), valida rota repetida, `Done` duplicado ou sem palavras e `Next` ilegível ou apontando para aula `(known)`, só fecha o nível quando toda a rota está feita, e ganhou `course.py progress` para a tela do curso. `check_plan.py` exige rótulo em toda linha com hanzi (enunciado em linha `prompt:`), acusa bateria sem linha, frase repetida, mais de dois apoios e `KNOWN` vazio, aceita verbo separado (洗了澡) e deixa o `CHECK` só como conselho. A lista de reforço voltou a carregar itens entre partes (até cinco). `tools/test_scripts.py` tem 36 testes de regressão e roda na release; `tools/check_themes.py` dá avisos editoriais dos mapas; `tools/review_coverage.py` usa a mesma seleção do `course.py`. Resultados das simulações s12 a s14 em `qa/benchmark/results/round-8/`. Não testado: salvar e retomar num projeto real do Claude.

- **Enxugamento de 27/11/2026 (mesma branch `review-fixes`, versão 0.8.0 no `plugin.json`, ainda sem publicar):** a contabilidade da parte saiu do texto e foi para `course.py` (`part` dá o resumo da parte e o cabeçalho do `plan.txt`; `overview` dá as aulas e partes do nível); o professor não lê mais os mapas. Regras das primeiras partes em `first-parts.md` e as de áudio em `audio.md`, lidas só quando valem. Ritmo só 3, 5 e 7. HSK 5 e 6 fora do cartão até terem mapa (o `check_map.py` saiu da pasta da skill; o de `tools/` continua). `To reinforce` guarda só os erros da última parte (até cinco). Palavras antigas por sugestão (duas candidatas por linha). Os modelos carregam os scripts pela tag da versão (`@v0.8.0`); `sh tools/build.sh test` gera um ZIP de teste que usa o commit atual. O texto lido em toda aula caiu de cerca de 5.000 para cerca de 3.500 palavras, e os mapas deixaram de ser lidos.

- **Revisão de 27/11/2026 (branch `review-fixes`, ainda sem publicar):** revisão completa da 0.7.0 em quatro camadas (texto, dados, simulações, revisor de fora). Relatório: https://claude.ai/artifact/HR1iFdWsV78QSpwV6ui8kD. O Eduardo aprovou todas as correções; a branch traz: (1) primeiras partes do curso (menos de vinte palavras vistas) mais curtas, com exercícios de significado e de resposta além da tradução, sem a regra das três aparições; (2) quantidade de exercícios proporcional às palavras novas (um por palavra em cada bateria, até cinco; escuta com um clipe só até quatro palavras); (3) aulas puladas marcadas `(known)` na lista `Lessons` no lugar do antigo `Known: jump start`, fora da rota e do progresso, com lembrete das palavras na tabela; (4) `check_plan.py` e `check_map.py` corrigidos; (5) revisão sem as palavras novas da parte, palavra de apoio, volta do erro e fechamento com uma pergunta só; (6) HSK 5 e 6 como experimentais; (7) som da tabela tolerante ao pinyin, três leituras sem gravação ficam mudas (过 guo, 得 děi, 着 zháo); (8 a 11) cartões, arquivo do curso, documentação e ZIP sem a fonte. Falta: o Eduardo testar uma parte de verdade, gravar as três leituras, ouvir as sílabas suspeitas, e decidir versão e publicação.

- **`main` e a release publicada: 0.7.0** (27/11/2026). A 0.7.0 traz o som na tabela (clique no hanzi, gravações do repositório `mandarinmaxxing-audio`, HSK 1–4) e a Yun como voz padrão do ditado. Foi publicada a pedido do Eduardo antes do teste do ZIP numa aula: o clique na tabela e o ditado com a Yun ainda não foram verificados em uso real. Antes: **`main` e a release publicada: 0.6.1** (22/11/2026). A 0.6.1 só muda a aula 1 do HSK 1: o Eduardo testou a aula 1 inteira numa sessão (nove palavras) e achou vocabulário demais; ela voltou a duas partes nos ritmos 3 e 5, seis palavras e depois três (`Split: 2-1 / 2-1 / 3`), como a aula 1 do HSK Standard Course, que tem seis palavras. Totais do HSK 1: 96 / 58 / 41. A 0.6.0 saiu no mesmo dia. O Eduardo testou a branch `v0.6-lean` no app (tela de setup, botões, aula) e mandou publicar. A branch foi juntada na `main`; o que este documento descreve como "a branch" é a versão publicada.
- **O site ainda descreve a 0.5:** totais do HSK 1 (agora 96 / 58 / 41; o 58 do ritmo recomendado já bate, o 97 e o 42 não), ritmo como "3, 5, 7" (agora leve 3 ou 4, recomendado 5 a 7, intenso 7 a 10), e não mostra a tela de setup nem a animação de traços.
- **Revisão de lançamento do site:** `LAUNCH.md`, no repositório `aveduardo-br/mandarinmaxxing-site`.

**Como trabalhar com o Eduardo**

- **Converse em português.** Os arquivos da skill e o README são em inglês.
- **Mostre o plano antes de mudanças grandes** e espere o ok. Ele valida vendo.
- **Julgue as ideias dele.** Ele traz ideias para alinhar juntos, não ordens: diga quando discordar e por quê.
- **Publicar é decisão dele.**
- **Pesquise antes de afirmar.** Limites de ferramenta, de conector ou de plano só valem depois de testados.
- **Ele não lê hanzi com fluência:** mostre sempre o significado ao lado.

## O norte

> The same HSK words, reorganized around everyday conversations.

- Mesma lista oficial do HSK, em outra ordem: por situação do dia a dia.
- Nenhum método está errado. É uma opção para quem prefere estudar assim.
- Skill enxuta: instalar e usar tem que ser o mais simples possível. Nada de pasta no computador, script ou chave colada no chat.
- Mensagem e tom: `docs/messaging.md` no repositório `aveduardo-br/mandarinmaxxing-site`.

## Como a skill funciona (desde a 0.6.0)

**O princípio da reescrita.** A 0.5.6 tinha crescido por remendo: cada rodada de benchmark acrescentava regras, e o que toda aula lia chegou a 7.226 palavras. A branch corta isso para cerca de 4.400, com o mesmo método e o mesmo formato de `course.md`. **Cuidado para não repetir o ciclo:** toda análise acha alguma coisa e todo achado quer virar regra. Antes de acrescentar uma regra, veja se dá para resolver tirando ou reescrevendo outra.

**Arquivos** (`skills/mandarinmaxxing/`)

| Arquivo | Quando a skill lê | O que tem |
|---|---|---|
| `SKILL.md` | Todo chat | Achar e retomar o curso, o `course.md`, montar a parte, planejar, os cinco passos, regras de enunciado, palavras antigas |
| `lesson-format.md` | Todo chat com aula | Título, tabela com a fonte, correção, leitura, ditado e narração, fechamento |
| `maps/hsk-N.md` | Todo chat | O mapa do nível (HSK 1 a 4) |
| `setup.md` | Só em curso novo | Passos do projeto, mensagem de boas-vindas, visão do nível e rota |
| `levels.md` | Só no fim de um nível ou em nível sem mapa | Passagem de nível, montar o mapa do HSK 5 e 6 |
| `requests.md` | Só quando o aluno pede algo fora da próxima parte | Pular de aula, revisar, trocar o ritmo, volta depois de pausa, role-play, leitura extra, flashcards |
| `check_plan.py` | Nunca lê; roda | Confere o vocabulário da parte planejada |
| `syllabus/hsk-1..6.csv` | Consulta palavra por palavra | Lista oficial de novembro de 2025 |
| `fonts/` | Nunca | Fonte Kaiti recortada para os 1.940 hanzi do HSK 1 a 6 |

**Aula e parte**

- Cada situação do mapa é uma **aula**, com número fixo. A aula é dada em **partes**; o ritmo (3, 5, 7 ou outro número) é a meta de palavras novas por parte.
- O mapa agrupa as palavras em blocos de 2 a 4, e a linha `Split` diz quantos blocos entram em cada parte nos ritmos 3 / 5 / 7. Para outro ritmo, ou mapa sem `Split`, a skill enche a parte com blocos inteiros até passar do ritmo em mais de uma palavra.
- **O ritmo é meta, não contagem.** Medido nos mapas: no ritmo 5 o tamanho mais comum de parte é 6 palavras (vai de 3 a 7); no ritmo 7 vai até 10 (no HSK 4, 54 de 130 partes têm 9 ou 10). O `setup.md` diz isso ao mostrar o nível; a mensagem de boas-vindas aprovada continua com "3 leve, 5 recomendado, 7 intenso".
- Totais: HSK 1, 300 palavras, 22 aulas, partes 96 / 58 / 41, jump start 01 a 07. HSK 2, 200 palavras, 19 aulas, 66 / 38 / 29, jump start 01 a 04. HSK 3, 500 palavras, 37 aulas, 168 / 94 / 68, jump start 01 a 04. HSK 4, 1.000 palavras, 56 aulas, 319 / 173 / 130, jump start 01 a 05.
- A numeração recomeça em 01 a cada nível; o título sempre leva o nível. No `Done` a linha leva o prefixo do nível (`2-01.1`).

**Uma parte, cerca de uma hora**

0. **Planejamento (novo).** Antes da primeira mensagem, a skill monta a parte inteira em privado: lista as palavras, escreve todo o mandarim primeiro, confere as contagens, roda o `check_plan.py` e só então escreve os enunciados como tradução das respostas.
1. **Revisão:** uma frase por palavra da parte anterior, de 5 a 10, no nível do curso.
2. **Vocabulário:** tabela, palavras de apoio e de dois a quatro chunks. O chunk diz qual pedaço pode trocar, sem dar a troca pronta.
3. **Três baterias de 5:** chunks (pode ser curta), ação completa (nunca mais curta que a revisão), sequência. Cada palavra nova em pelo menos três exercícios.
4. **Escuta:** ditado e narração de uma voz; sem áudio, leitura com reescrita. Nas primeiras partes, quando o vocabulário não dá para um relato, a leitura vira "o que tu diria em cada momento da situação".
5. **Fechamento:** salvar, dizer o que vem depois e oferecer a próxima parte.

**Com menos de dez palavras vistas** há um bloco próprio de regras: menos baterias, menos exercícios em vez de repetir, e a naturalidade vem antes da contagem de três aparições.

**O conferidor (`check_plan.py`).** A skill grava a parte planejada num rascunho (nível, palavras novas, palavras de apoio, o `Done` colado e as frases) e roda o script. Ele aponta caracteres que nenhuma palavra vista cobre e palavras novas em menos de três linhas das baterias. Confere só vocabulário, não naturalidade. Onde não há execução de código, a skill confere à mão. Testado sozinho nas quatro sessões de um teste de mesa feito por outra IA: achou 杯 (classificador), 房子 e 难 (HSK 3) e a falta de 游泳, sem falso positivo.

**Revisão de palavras antigas**

- Sem fila nem pontuação. A parte anterior volta na revisão, e uma palavra de cada linha 3, 7, 14, 30 e 60 atrás no `Done` volta dentro dos exercícios, escolhida por rodízio.
- `To reinforce` guarda até dez palavras ou chunks em que o aluno precisou de ajuda, em qualquer passo (revisão, baterias, ditado, reescrita, role-play).
- Repetição espaçada de verdade fica com o Anki; a skill entrega os cartões quando o aluno pede.

**Onde o curso fica salvo**

- Um único `course.md` nos documentos do projeto do Claude. A skill só salva no fim da parte.
- Fora de um projeto, a skill mostra os três passos para criar um e oferece uma aula de teste sem salvar.

**Áudio**

- Opcional. Até dois clipes por parte (ditado e narração), uma voz, uma geração cada. Padrão: ElevenLabs pelo conector, voz Yun (`4AfodMgwXps9oZFhHzoj`, nativa, a mesma da tabela); Sarah (`EXAVITQu4vr4xnSDxMaL`) se a conta do aluno não puder usar a Yun, que é voz da biblioteca (não testado em conta gratuita).
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

- **Reescrita enxuta** (18/11/2026). Saíram de vez: o curso da versão antiga (`mandarinmaxxing-course.md`), as notas de cada parte em arquivo, a cópia do curso numa pasta do computador, a tabela com matemática inline e as instruções repetidas. Ninguém usava a skill ainda, então não há curso antigo para manter.
- **Planejar a parte antes de ensinar** (18/11/2026). Regras que valem para a parte inteira (três aparições, estruturas variadas, nível da revisão) eram conferidas no improviso, um exercício por vez. No meio do HSK 2, lado a lado, a versão com planejamento tirou 35 de 35 e a 0.5.6 tirou 32; uma simulação de cada, dentro da variação.
- **Conferidor por script** (18/11/2026). Foi descartado no começo por medo de falso positivo e depois adotado: um teste de mesa de outra IA usou palavra não vista em 3 de 4 partes. A checagem "a frase pode ser montada só com palavras vistas" não dá o falso positivo da busca por palavras de nível acima (今天下午 contém 天下).
- **Sem salvar no meio da parte.** O Eduardo decidiu: o chat fica guardado e o aluno volta nele.
- **Sem acompanhar domínio de cada palavra nem gramática.** Duas análises externas pediram; o Eduardo mantém a skill leve, com o `To reinforce` e o Anki. O ponto da gramática (ensinar 了 uma vez não ensina todos os usos) é verdadeiro e fica para depois do teste com gente.
- **Troca de ritmo vale a partir da próxima aula**, para as partes já feitas não mudarem de número.
- **Palavra fora do composto:** uma palavra que é natural sozinha aparece sozinha ao menos uma vez (站 em 坐两站); a que vive em compostos pode ficar neles. O Eduardo tinha dúvida; ficou a regra branda.

## Revisão de 21/11/2026 (publicada na 0.6.0)

Decisões do Eduardo: o aluno usa a skill no computador (celular é bônus); HSK 5 e 6 ficam como "ainda não tem", sem mapa montado no chat; quem já estudou escolhe o nível, vê as aulas mapeadas e decide de onde partir; sessão curta só se decide depois do teste dele.

- **O plano da parte fica em `plan.txt`**, com os enunciados embaixo das respostas, e a aula é dada a partir dele. Antes podia ficar só no raciocínio, que não é garantido até o último exercício.
- **`check_plan.py`:** linha `NAMES` para nomes próprios (北京 e 小王 eram acusados) e lista `CHECK` para palavra não vista formada por palavras vistas inteiras (要是, 前天, 后天, 还是 passavam). Nas transcrições do `s11` e do `s8` a lista só acusou 就是.
- **`To reinforce`:** uma regra só, a do fechamento da parte.
- **HSK 5 e 6:** em 21/11 a skill passou a dizer "ainda não tem"; em 22/11 o Eduardo reabriu e eles voltaram a ser montados na hora, agora com `check_map.py` (ver a seção da tela de setup).
- **Primeira sessão maior:** a aula 01 do HSK 1 passou de `1-1-1 / 1-2 / 1-2` para `2-1 / 3 / 3`, para a primeira parte já ter trocas de verdade. Totais do HSK 1: 96 / 57 / 41. **O site ainda mostra 97 / 58 / 42 na seção "Your course".**
- **Ritmo com a faixa real** no setup e no README: leve 3 ou 4, recomendado 5 a 7, intenso 7 a 10 (salvo como Pace 3, 5 e 7). **A copy do site ainda diz 3, 5, 7.**
- **Flashcards:** continuam só quando o aluno pede (decisão do Eduardo).
- **Rodada 7 do benchmark** (`qa/benchmark/results/round-7/`): 29 de 35 nas sete dimensões de sempre, igual à rodada 6. O plano em arquivo funcionou; a naturalidade das primeiras partes continua em 3 (palavras de reação coladas). A regra contra as falas coladas entrou depois e ainda não foi simulada.
- **Ficou para depois:** revisão dos mapas por falante nativo, instalação mais simples (depois da 0.6.0), sessão curta (depois do teste do Eduardo), site (junto com a 0.6.0).

## Tela de setup e tela do curso (21 e 22/11/2026, publicada na 0.6.0)

**O que é.** A mensagem de boas-vindas em texto virou um cartão em HTML, e o mesmo cartão tem um segundo estado, a tela do curso, que o aluno chama escrevendo "setup". Os dois modelos estão em `setup.md`; o visual e o comportamento vêm de `web/setup.js`, carregado pelo jsDelivr de um commit fixo, como a tabela.

- **Curso novo:** letreiro MANDARINMAXXING em ASCII com "for Claude", "Welcome to mandarinmaxxing!", dois parágrafos, três perguntas dobradas (aula, áudio, teclado), as escolhas (nível, ritmo, áudio) e o botão "See my lessons".
- **Tela do curso:** porcentagem e partes feitas, a próxima aula com três atalhos (continuar, revisar uma aula, pular para uma aula) e as mesmas escolhas marcadas como estão no curso. "Save changes" só aparece quando algo muda e manda só o que mudou.
- **Estilo aprovado pelo Eduardo:** opções em texto com um ladrilho pequeno na frente (cinza, laranja quando escolhida, girando como os ladrilhos do site), um só botão cheio por tela, rótulos de seção em maiúsculas pequenas, sem linhas divisórias. Ele rejeitou os botões em bloco cheio ("poluído"), a fileira de ladrilhos do progresso e o FAQ na tela do curso.
- **Os botões mandam mensagens** pelo `sendPrompt` do chat; a skill também aceita a resposta digitada. **Ainda não testado no app:** o envio de verdade (as prévias só mostravam o texto) e se "/setup" chega como mensagem.
- **O chat estiliza todo `<button>`** e ganha de regras comuns: por isso o `setup.js` usa `!important` nos botões. Animações não podem ter `transform` com `!important`.
- **HSK 5 e 6 voltaram a ser montados na hora** (o Eduardo reabriu a decisão de 21/11): no cartão têm marcador tracejado e uma nota ao serem escolhidos; a skill monta o mapa e confere com `check_map.py` (toda palavra oficial uma vez, blocos de 2 a 4).
- **Trocar de nível ou de áudio** pela tela do curso: regras novas em `requests.md`.
- **Tabela de vocabulário:** `web/vocab.js` (estilo, fonte e animação de traços no hover com a Hanzi Writer), testada pelo Eduardo no app.
- **Se `web/setup.js` ou `web/vocab.js` mudar,** suba o commit e atualize o endereço em `setup.md` (duas vezes) ou em `lesson-format.md`.
- No arquivo há também um letreiro em ladrilhos (o MANDARIN do hero do site), sem uso: reduzido para o chat ficou difícil de ler.

## Som das palavras na tabela (22/11/2026, publicado na 0.7.0)

- **O que é:** clicar num hanzi da tabela toca a gravação da palavra. O hover continua só desenhando os traços.
- **Onde ficam os áudios:** repositório `aveduardo-br/mandarinmaxxing-audio`, um MP3 por palavra com o próprio hanzi no nome (`audio/你好.mp3`), servido pelo jsDelivr de um commit fixo. O endereço está no começo de `web/vocab.js` (`AUDIO`). Palavra sem gravação fica em silêncio.
- **Como são feitos:** lá, `scripts/generate.py` roda pelo GitHub Actions (botão "Run workflow", por nível, com teto de caracteres), com a chave `ELEVENLABS_API_KEY` nos secrets. Voz Yun (`4AfodMgwXps9oZFhHzoj`) desde 27/11/2026: a Sarah é voz americana e errava palavras soltas (20 ruins só no HSK 4); o idioma `zh` sempre foi aceito, o problema era a voz. HSK 1–4 regravados, 1.989 de 1.992 leituras com áudio (faltam 过 guo, 得 děi, 着 zháo), todas as marcadas ouvidas e aprovadas pelo Eduardo. Duas leituras: grava-se um caractere homófono de leitura única (`special.csv`). Modelo `eleven_v4` (o Eduardo ouviu três modelos e escolheu o v4 "disparado"). Cada arquivo é cortado, nivelado, transcrito para conferência e anotado em `status.csv`.
- **Estado (27/11/2026):** HSK 1 a 4 gravados, 1.978 palavras, 6,8 MB. HSK 1 aprovado de ouvido pelo Eduardo; do 2 ao 4 ele ouviu uma amostra e achou tudo bom, e disse que é coisa demais para revisar sozinho. As 52 suspeitas da conferência foram regravadas com até três tomadas: 32 passaram, 20 continuam marcadas (parte é homófono, como 不便 / 不变; 办理 sai repetida três vezes). HSK 5 e 6 ficam para quando forem mapeados.
- **A régua dele:** o áudio é apoio, não verdade absoluta: o tom muda dentro da frase e a gravação da palavra solta é só referência.
- **Revisão:** feita no chat, com um widget que lê o `status.csv` pelo jsDelivr, toca cada arquivo e devolve a lista das ruins. A conferência por transcrição erra muito em palavra de uma sílaba (ouve 爱 como "I"); essas vão para uma lista "ouvir".
- **Pendente:** as 40 palavras com duas leituras (好, 得, 重…). A leitura que aparece primeiro na lista tem o nome simples; a outra espera uma linha em `special.csv` (arquivo `palavra_pinyin.mp3`, que o `vocab.js` já sabe pedir). Em alguns casos a leitura "padrão" pela ordem da lista não é a que a voz dá ao hanzi sozinho (重, 只): rever antes de gravar o HSK 4.
- **Limite do ambiente:** as sessões do Claude não baixam arquivos do ElevenLabs nem leem os secrets; disparar o workflow e ler o log funcionam pelo `gh`.

## Como testar

1. `python3 tools/check_map.py skills/mandarinmaxxing/maps/hsk-1.md` confere o mapa contra a lista oficial.
2. `python3 tools/check_anchors.py 1` (e 2, 3, 4) confere as frases-âncora contra o mapa.
3. `sh tools/build.sh` gera `download/mandarinmaxxing-claude.zip`.
4. No Claude: **Customize → Skills → + → Create skill → Upload a skill**. Criar um projeto vazio com a linha de instruções do README e escrever "start mandarinmaxxing".
5. Fazer uma parte inteira (cerca de 1 hora), abrir um segundo chat no mesmo projeto e pedir a próxima. Para ver o rodízio de palavras antigas sem fazer 15 partes, colocar no projeto um `course.md` já adiantado, com umas 20 linhas no `Done`.

Para depurar, peça à skill um relatório do que ela leu e fez em vez de adivinhar por capturas de tela.

**Benchmark.** `qa/benchmark/` tem os cenários, o roteiro das simulações, o roteiro do juiz e o script de correção. Rodar antes de cada versão nova: um agente por cenário e rodada (`runner.md`), `check_run.py` em cada pasta, e um juiz independente por cenário (`judge.md`). A rodada 1 (0.5.0) está em `qa/benchmark/results/round-1/`, com o resumo no `README.md` de lá. Cada bug novo vira um cenário. Para um aluno que realmente não sabe a língua, `qa/benchmark/cipher/MISSION.md` descreve o benchmark do aluno cifrado (jump start do HSK 1 em sequência, com as palavras trocadas por códigos); rodado em `qa/benchmark/results/cipher-1/` (95 palavras ensinadas, nenhuma deixou de voltar; 8 furos, corrigidos na 0.5.4). O transporte que funcionou está no README de lá: professor e aluno em paralelo trocando arquivos, com um vigia cifrando; o coordenador por parte travou no limite de retomadas.

## Ao publicar

- Publicar é automático: mude a versão em `plugin.json`, atualize o `release-notes.md` e envie para o `main`. Para a branch: juntar `v0.6-lean` na `main`, com a versão 0.6.0. A automação em `.github/workflows/release.yml` confere os mapas, gera o ZIP e cria a release com a tag. O README aponta para `releases/latest`.
- Mudança na skill sem mudar a versão não gera release nova: quem baixa continua recebendo o ZIP da última versão.
- As sessões do Claude não conseguem criar tags nem releases direto neste repositório. É a automação que faz isso.
- A tabela de vocabulário carrega `web/vocab.js` pelo jsDelivr, de um commit fixo deste repositório (21/11/2026). O script traz o estilo, a fonte Kaiti (da pasta `fonts/` do mesmo commit) e a animação de traços no hover, com a biblioteca Hanzi Writer. A skill escreve só o título, as linhas e a linha do `<script>`. **Se `web/vocab.js` ou a fonte mudar, suba o commit e atualize o endereço em `lesson-format.md`.** Testado pelo Eduardo no app em 21/11: tabela, hover e fonte funcionaram. Próxima ideia no mesmo caminho: o setup em tópicos colapsáveis com botões (protótipos no chat de 21/11, desenho ainda em aberto).
- Avisar o que mudou, para a copy do site ser reescrita.

## Versões de novembro de 2026

- **0.5.0:** partes de cerca de 1 hora (revisão longa, três baterias de 5, ditado e narração), rodízio de palavras antigas, fechamento com role-play, extras sob pedido (leitura, flashcards para o Anki).
- **0.5.1:** correções da rodada 1 do benchmark: primeiras partes com menos baterias, ditado com uma fala por frase, oferta da próxima parte sempre, contador da revisão fixo, rodízio de uma palavra por linha.
- **0.5.2:** a revisão segue o nível do curso (o Eduardo achou a revisão simples demais depois de pular para uma aula adiantada) e, depois de um pulo antes do fim do jump start, usa as palavras do jump start. Cenários do HSK 3.
- **0.5.3:** sem estrutura repetida na parte, baterias 1 e 2 nunca mais curtas que a revisão, registro falado, escuta com cena nova. Cenários do HSK 2 e 4.
- **0.5.4:** furos achados pelo aluno cifrado: o enunciado diz só o que a resposta diz, palavras vistas também em dicas e roteiros, sinônimos pedidos pelo nome, resposta sem a palavra nova volta na mesma bateria.
- **0.5.5:** com poucas palavras, menos exercícios em vez de repetir; o "senhor" para pedir 您 só dentro da frase.
- **0.5.6:** nada muda nas aulas. O LICENSE passa a ir dentro da pasta da skill (`tools/build.sh` copia o da raiz; edite sempre o da raiz), o `SKILL.md` ganha o campo `license`, e o README avisa do pré-requisito de execução de código (Settings → Capabilities).
- **Branch `v0.6-lean` (não publicada, futura 0.6.0):** reescrita enxuta, arquivos `setup.md`, `levels.md` e `requests.md`, planejamento da parte, `check_plan.py`, correções de duas análises externas e de um teste de mesa. Detalhes acima e em `qa/benchmark/results/round-6/README.md`.

Notas do juiz (de 35) ao longo das rodadas: de 25 a 30 na 0.5.0 para 29 a 34 nas versões seguintes, e 29 (`s1`) e 35 (`s11`) na branch. O HSK 4 tirou as melhores (34 e 33); as primeiras partes do curso e o HSK 2 são os mais irregulares. Detalhes em `qa/benchmark/results/`.

## O que falta

**1. O Eduardo testar uma parte de verdade com a branch (a prioridade).** É o que falta para publicar a 0.6.0. O ZIP de teste sai de `sh tools/build.sh`. O `course.md` dele continua valendo, porque o formato não mudou. O que só o app mostra:
- Se o Claude abre `setup.md`, `levels.md` e `requests.md` na hora certa.
- Se ele grava o rascunho e roda o `check_plan.py` sozinho, e quanto isso atrasa a primeira mensagem da parte.
- Se uma hora cansa e se as baterias ficam repetitivas depois de alguns dias (pendência antiga).
- Depois dele, um amigo começando do zero: o começo do curso foi o que mais mudou.
- Quando algo soar estranho, pedir à skill o relatório do que ela fez e transformar o caso num cenário do benchmark.

**2. Skill: o que foi medido e o que não foi** (rodada 6, `qa/benchmark/results/round-6/`).
- **`s1` (curso novo, HSK 1):** 29 de 35, contra 27 da 0.5.4. Naturalidade segue em 3 nas primeiras partes; com três palavras não há frase natural possível, e o Eduardo considera o HSK 1 fraco para medir isso.
- **`s11` (meio do HSK 2), lado a lado, juiz às cegas:** 0.5.6 tirou 32, a branch tirou 35. Uma simulação de cada; no HSK 2 a mesma versão já tirou 33 e 28.
- **`s11` de novo, depois de todas as correções (`run-c`), só pelo script, sem juiz:** a skill gravou o rascunho e rodou o conferidor por conta própria (duas vezes, as duas OK), nenhuma palavra não vista, cada palavra nova em pelo menos seis exercícios, rodízio 3 de 3, `course.md` certo.
- **Sem simulação própria:** a leitura das primeiras partes sem áudio (o `s1` roda com áudio), a troca de ritmo, a volta depois de pausa, os níveis 3 e 4, a passagem de nível e o mapa gerado do HSK 5 e 6. Se mexer na skill de novo, rodar ao menos `s1` e `s11`.
- **Ambiguidades conhecidas, deixadas como estão de propósito** (anotadas pelas simulações; resolver só se aparecerem em uso real): duas frases sobre quando um item entra no `To reinforce` (na hora da correção ou só no fechamento); erro na narração não é citado; os cenários antigos têm nomes de aula em inglês com curso em português.
- **Gramática:** o `Done` registra palavras, não construções. Ensinar 了 uma vez não ensina todos os usos. Fica para depois do teste com gente.

**3. Skill: ideias aprovadas que ainda não foram feitas.**
- **Prova de fechamento:** no fim de uma aula ou de um nível, uma prova curta com palavras antigas sorteadas do registro. Serve ao aluno e dá dado real de retenção.
- **Instalação mais simples** que o ZIP (o Eduardo acha o ZIP e o `npx` complicados para o aluno).
- **Mapas do HSK 5 e 6:** hoje a skill monta o mapa na hora, com as nossas regras. Um cenário de benchmark que confira o mapa gerado com `check_map.py` ainda não foi feito; é barato e é onde a skill trabalha sem rede.

**4. Site** (repositório `aveduardo-br/mandarinmaxxing-site`).
- **Card 04 (áudio):** o texto já fala em ditado e narração de uma pessoa, mas o exemplo ainda é o diálogo de duas vozes. Gerar o áudio novo com a Yun e refazer os tempos em `DialogueCard.astro`.
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
