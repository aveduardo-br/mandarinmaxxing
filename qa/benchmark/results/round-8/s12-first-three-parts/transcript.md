# Transcript · sim3/new · HSK 1, Aula 1 (partes 1 e 2) e Aula 2 (parte 1)

Comments of the form `<!-- sim: ... -->` are the simulator's notes on what the tutor did off-screen (files read, scripts run, saves). `<!-- expected: ... -->` is the hidden expected answer. Neither is seen by the student.

## T1 · STUDENT
start mandarinmaxxing

## T2 · TUTOR
<!-- sim: read SKILL.md; looked for course.md in course/ (not found); read setup.md. The chat can save to course/, so straight to the welcome card. Language: Portuguese (app interface, project name "Mandarim"). -->

```html
<section id="mandarinmaxxing-setup">
  <div data-wordmark="ascii">for Claude</div>
  <h2>Boas-vindas ao mandarinmaxxing!</h2>
  <p>As mesmas palavras do HSK, reorganizadas em torno de conversas do dia a dia. Você aprende uma situação de cada vez (cumprimentar, pedir comida, fazer compras), responde em mandarim desde a primeira aula, e o seu progresso fica salvo de uma conversa para a outra.</p>
  <p>Escolha o seu nível e o seu ritmo abaixo. Nada aqui é definitivo: digite "setup" para voltar a esta tela.</p>
  <h3>Antes de começar</h3>
  <details><summary>Como é uma aula?</summary>
    <p>Uma revisão da última vez, palavras novas dentro de frases prontas para usar, três rodadas de tradução do português para o mandarim com correção na hora, e uma etapa de escuta ou leitura para fechar. As primeiras aulas levam dez ou quinze minutos, porque você ainda quase não conhece palavras. Depois, de meia hora a uma hora, conforme a quantidade de palavras da parte.</p>
  </details>
  <details><summary>Preciso de áudio?</summary>
    <p>Não. Com áudio, você ouve um ditado curto e uma história curta em uma voz natural, pela sua própria conta do ElevenLabs, que tem plano gratuito. Sem áudio, você lê um texto no lugar e não há nada para configurar.</p>
  </details>
  <details><summary>Como eu digito em chinês?</summary>
    <p>Você responde em mandarim desde a primeira aula. Pode começar em pinyin e, quando quiser, ativar o teclado chinês (Pinyin, Simplificado): você digita o som e escolhe o caractere.</p>
  </details>
  <h3>Suas escolhas</h3>
  <fieldset><legend>Nível<small>HSK</small></legend>
    <button data-on data-value="HSK 1">1</button><button data-value="HSK 2">2</button><button data-value="HSK 3">3</button><button data-value="HSK 4">4</button>
  </fieldset>
  <fieldset><legend>Ritmo<small>palavras novas por dia</small></legend>
    <button>Leve<small>cerca de 3</small></button><button data-on>Recomendado<small>cerca de 5</small></button><button>Intenso<small>cerca de 7</small></button>
  </fieldset>
  <fieldset><legend>Áudio</legend>
    <button data-on data-value="desligado, leitura no lugar">Desligado</button><button data-value="ligado, com ElevenLabs">Ligado<small>ElevenLabs</small></button>
  </fieldset>
  <button data-start>Ver minhas aulas</button>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@21cffbbd132031ae19f2248d9b1688ce254dc0cb/skills/mandarinmaxxing/web/setup.js"></script>
```

## T3 · STUDENT
Nível: HSK 1. Ritmo: Recomendado (cerca de 5). Áudio: desligado, leitura no lugar.

<!-- sim: worked out from web/setup.js: for each fieldset, `<legend first text node>: <data-value, or label + " (" + small + ")">`, joined with ". " and a final "."; no data-lead on the welcome card. -->

## T4 · TUTOR
<!-- sim: ran `course.py overview 1 5`; translated the lesson names; saved course/course.md (copy: course-after-setup.md). -->

**HSK 1 · o seu percurso**

São 22 aulas, em 58 partes: cerca de 8 semanas fazendo uma parte por dia (é uma estimativa). Cada aula é uma situação, estudada uma parte de cada vez.

**Largada** (as aulas de que todas as outras dependem; vêm primeiro e nesta ordem)

- **01** Cumprimentar e agradecer (2 partes)
- **02** Dizer o que você quer (2 partes)
- **03** Dizer quem você é (2 partes)
- **04** De onde você é e onde você está (3 partes)
- **05** Apresentar alguém (3 partes)
- **06** Dizer a idade (4 partes)
- **07** Quem mora em casa (3 partes)

**Depois, as situações**

- **08** Ligações telefônicas (1 parte)
- **09** Filhos, parceiros e animais de estimação (2 partes)
- **10** Datas e dias da semana (2 partes)
- **11** Horas e rotina diária (4 partes)
- **12** Comer e beber (3 partes)
- **13** Fazer compras e pagar (4 partes)
- **14** Escolher roupas e coisas (3 partes)
- **15** Onde ficam as coisas (4 partes)
- **16** Ir e vir (2 partes)
- **17** Tempo livre (3 partes)
- **18** Falar do tempo (2 partes)
- **19** Estudar chinês (3 partes)
- **20** Na escola (3 partes)
- **21** Falar de trabalho (2 partes)
- **22** Ficar doente (1 parte)

A qualquer momento você pode pedir para revisar uma aula, mudar o ritmo, uma leitura extra só com as palavras que você já conhece, ou flashcards das palavras de uma parte.

Começando do zero, o ponto de partida é a Aula 1. Quer começar por ela, ou prefere adiantar ou adiar alguma aula?

## T5 · STUDENT
Pode ser assim mesmo. Vamos começar pela Aula 1.

## T6 · TUTOR
<!-- sim: ran `course.py part course/course.md plan-L1p1.txt`; brief: early part, no review. Read lesson-format.md and first-parts.md. Wrote the plan, ran check_plan.py (OK). -->

```html
<section id="mandarinmaxxing-vocab">
  <h2>HSK 1 · Aula 1 · Cumprimentar e agradecer · parte 1 de 2</h2>
  <table>
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Significado</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">你好</span></td><td>nǐ hǎo</td><td>olá</td></tr><tr><td><span lang="zh-Hans">再见</span></td><td>zàijiàn</td><td>tchau, até logo</td></tr><tr><td><span lang="zh-Hans">谢谢</span></td><td>xièxie</td><td>obrigado(a)</td></tr><tr><td><span lang="zh-Hans">不客气</span></td><td>bú kèqi</td><td>de nada</td></tr><tr><td><span lang="zh-Hans">对不起</span></td><td>duìbuqǐ</td><td>desculpa</td></tr><tr><td><span lang="zh-Hans">没关系</span></td><td>méi guānxi</td><td>não tem problema</td></tr></tbody>
  </table>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@21cffbbd132031ae19f2248d9b1688ce254dc0cb/skills/mandarinmaxxing/web/vocab.js"></script>
```

**Frases úteis**

**— 谢谢！ — 不客气。**  
*— Xièxie! — Bú kèqi.*  
— Obrigado(a)! — De nada.

**— 对不起！ — 没关系。**  
*— Duìbuqǐ! — Méi guānxi.*  
— Desculpa! — Não tem problema.

**Rodada 1**

O que significa?

**Rodada 1 · 1 de 5**

**你好！** *Nǐ hǎo!*

<!-- expected: Olá! -->

## T7 · STUDENT
Olá!

## T8 · TUTOR
Isso!

**Rodada 1 · 2 de 5**

**再见！** *Zàijiàn!*

<!-- expected: Tchau! / Até logo! -->

## T9 · STUDENT
Tchau

## T10 · TUTOR
Certo.

O que você responde?

**Rodada 1 · 3 de 5**

**谢谢！**  
*Xièxie!*  
Obrigado!

<!-- expected: 不客气。 -->

## T11 · STUDENT
没关系

## T12 · TUTOR
Quase. Você escreveu:

> 没关系

**不客气** (*bú kèqi*): é o que se responde a um agradecimento; 没关系 responde a um pedido de desculpa.

**不客气。**  
*Bú kèqi.*  
De nada.

**Rodada 1 · 4 de 5**

**没关系。** *Méi guānxi.*

<!-- expected: Não tem problema. -->

## T13 · STUDENT
Não tem problema

## T14 · TUTOR
Isso.

**Rodada 1 · 5 de 5**

**对不起！**  
*Duìbuqǐ!*  
Desculpa!

<!-- expected: 没关系。 -->

## T15 · STUDENT
没关系。

## T16 · TUTOR
Perfeito.

**Rodada 2**

Traduza para o mandarim.

**Rodada 2 · 1 de 4**

Olá!

<!-- expected: 你好！ -->

## T17 · STUDENT
你好！

## T18 · TUTOR
Certo.

**Rodada 2 · 2 de 4**

— Obrigado!  
— De nada.

<!-- expected: 谢谢！——不客气。 -->

## T19 · STUDENT
— Xièxie! — Bú kèqi.

## T20 · TUTOR
Certo: **— 谢谢！ — 不客气。**

Pode continuar em pinyin se quiser; quando der, vale ativar o teclado chinês (Pinyin, Simplificado): você digita o som e escolhe o caractere.

**Rodada 2 · 3 de 4**

— Desculpa!  
— Não tem problema.

<!-- expected: 对不起！——没关系。 -->

## T21 · STUDENT
对不起！——不客气。

## T22 · TUTOR
<!-- sim: plan reworked: the third moment of the last step now calls for 没关系 (it was 对不起), to bring the item back once. -->

Quase. Você escreveu:

> 对不起！——不客气。

**没关系** (*méi guānxi*): a resposta a um pedido de desculpa; 不客气 é só para agradecimento.

**— 对不起！ — 没关系。**  
*— Duìbuqǐ! — Méi guānxi.*  
— Desculpa! — Não tem problema.

**Rodada 2 · 4 de 4**

Obrigado, tchau!

<!-- expected: 谢谢，再见！ -->

## T23 · STUDENT
谢谢，再见！

## T24 · TUTOR
Certo.

**Leitura 1**

Você está num hotel. O que você diz, em mandarim, em cada momento?

1. Você chega à recepção.
2. A recepcionista entrega a sua chave.
3. No corredor, alguém pisa no seu pé e pede desculpa.
4. Você vai embora.

<!-- expected: 1. 你好！ 2. 谢谢！ 3. 没关系。 4. 再见！ -->

## T25 · STUDENT
1. 你好！
2. 谢谢！
3. 没关系。
4. 再见！

## T26 · TUTOR
<!-- sim: saved course/course.md: Done + `1-01.1 | 你好 再见 谢谢 不客气 对不起 没关系`, Next: Lesson 01, part 2 of 2, To reinforce: none (both slips were answered correctly later in the part). Copy: course-after-L1p1.md. -->

Tudo certo, os quatro.

Da próxima vez: HSK 1, Aula 1, parte 2. Quer começar essa parte agora?

## T27 · STUDENT
Sim, vamos.

## T28 · TUTOR
<!-- sim: ran `course.py part course/course.md plan-L1p2.txt`; brief: new words 您 好 没事, review "one prompt per word of 1-01.1" (6), early part. Wrote the plan (review of 4), ran check_plan.py (OK). -->

**HSK 1 · Aula 1 · Cumprimentar e agradecer · parte 2 de 2**

O que significa?

**Revisão 1 de 4**

**谢谢！** *Xièxie!*

<!-- expected: Obrigado(a)! -->

## T29 · STUDENT
Obrigado!

## T30 · TUTOR
Isso.

**Revisão 2 de 4**

**对不起！** *Duìbuqǐ!*

<!-- expected: Desculpa! -->

## T31 · STUDENT
Desculpa

## T32 · TUTOR
Certo.

**Revisão 3 de 4**

**不客气。** *Bú kèqi.*

<!-- expected: De nada. -->

## T33 · STUDENT
Não tem problema

## T34 · TUTOR
<!-- sim: plan reworked: the second moment of the last step now calls for 不客气 (it was 谢谢您). -->

Quase. Você escreveu:

> Não tem problema

**不客气** (*bú kèqi*): "de nada", a resposta a **谢谢**. "Não tem problema" é **没关系** (*méi guānxi*).

**不客气。**  
*Bú kèqi.*  
De nada.

Traduza para o mandarim.

**Revisão 4 de 4**

Tchau!

<!-- expected: 再见！ -->

## T35 · STUDENT
Zàijiàn!

## T36 · TUTOR
Certo: **再见！**

```html
<section id="mandarinmaxxing-vocab">
  <h2>HSK 1 · Aula 1 · Cumprimentar e agradecer · parte 2 de 2</h2>
  <table>
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Significado</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">您</span></td><td>nín</td><td>você (a um senhor ou a uma senhora)</td></tr><tr><td><span lang="zh-Hans">好</span></td><td>hǎo</td><td>bom, bem</td></tr><tr><td><span lang="zh-Hans">没事</span></td><td>méishì</td><td>não foi nada</td></tr></tbody>
  </table>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@21cffbbd132031ae19f2248d9b1688ce254dc0cb/skills/mandarinmaxxing/web/vocab.js"></script>
```

好 sozinho, como resposta, é "tá bom", "ok".  
没事 e 没关系 respondem as duas a um pedido de desculpa; 没事 é a mais leve.

**Frases úteis**

**您好！**  
*Nín hǎo!*  
Olá! (a um senhor ou a uma senhora)  
您好 = 您 (você, formal) + 好 (bom)

**好，再见！**  
*Hǎo, zàijiàn!*  
Tá bom, tchau!

**— 对不起！ — 没事。**  
*— Duìbuqǐ! — Méishì.*  
— Desculpa! — Não foi nada.

**Rodada 1**

O que significa?

**Rodada 1 · 1 de 3**

**您好！** *Nín hǎo!*

<!-- expected: Olá! (formal, a um senhor ou a uma senhora) -->

## T37 · STUDENT
Olá, mas formal, pra um senhor

## T38 · TUTOR
Isso.

O que você responde?

**Rodada 1 · 2 de 3**

**对不起！**  
*Duìbuqǐ!*  
Desculpa!

<!-- expected: 没事。 (没关系 também é natural) -->

## T39 · STUDENT
没关系。

## T40 · TUTOR
<!-- sim: accepted (natural); names the new word and will ask for it by name in the last step. -->

Certo, **没关系** serve. A palavra nova desta parte para o mesmo momento é **没事** (*méishì*); ela volta mais adiante.

O que significa?

**Rodada 1 · 3 de 3**

**好，再见！** *Hǎo, zàijiàn!*

<!-- expected: Tá bom, tchau! -->

## T41 · STUDENT
Bom, tchau

## T42 · TUTOR
Isso: "Tá bom, tchau!"

**Rodada 2**

Traduza para o mandarim.

**Rodada 2 · 1 de 3**

Olá, senhor!

<!-- expected: 您好！ -->

## T43 · STUDENT
你好，您！

## T44 · TUTOR
Quase. Você escreveu:

> 你好，您！

**您好** (*nín hǎo*): 您 entra no lugar de 你. O "senhor" já está dentro de 您 e não vai de novo no fim.

**您好！**  
*Nín hǎo!*  
Olá, senhor!

**Rodada 2 · 2 de 3**

Obrigada, senhora!

<!-- expected: 谢谢您！ -->

## T45 · STUDENT
谢谢您！

## T46 · TUTOR
Certo.

**Rodada 2 · 3 de 3**

Tá bom, tchau!

<!-- expected: 好，再见！ -->

## T47 · STUDENT
Hǎo, zàijiàn!

## T48 · TUTOR
Certo: **好，再见！**

**Leitura 1**

Você vai à sala da sua professora, uma senhora. O que você diz, em mandarim, em cada momento?

1. Você entra na sala.
2. Você devolve um livro e ela agradece.
3. Ela esbarra na sua mochila e pede desculpa (use **没事** desta vez).
4. Ela diz **再见**; você concorda e se despede.

<!-- expected: 1. 您好！ 2. 不客气。 3. 没事。 4. 好，再见！ -->

## T49 · STUDENT
1. 你好！
2. 不客气。
3. 没事。
4. 好，再见！

## T50 · TUTOR
<!-- sim: saved course/course.md: Done + `1-01.2 | 您 好 没事`, Next: Lesson 02, part 1 of 2 (worked out by hand from Route and Lessons: the brief only says "the first part of the next lesson on the route"), To reinforce: 您好. Copy: course-after-L1p2.md. -->

Quase tudo. Você escreveu:

> 1. 你好！

**您好** (*nín hǎo*): com uma senhora, a professora, o cumprimento é com 您.

**您好！**  
*Nín hǎo!*  
Olá! (a uma senhora)

2, 3 e 4 estão certos.

A Aula 1 está completa. Da próxima vez: HSK 1, Aula 2, parte 1. Quer fechar a aula com uma conversa simulada, usando o que você viu nela?

## T51 · STUDENT
Agora não. Quero a próxima parte.

## T52 · TUTOR
<!-- sim: ran `course.py part course/course.md plan-L2p1.txt`; brief: new words 我 要 水 茶 | 你 吗 不, review "one prompt per word of 1-01.2: 您 好 没事, and one for each item to reinforce: 您好", early part (9 words met). Wrote the plan (review of 3), ran check_plan.py (exit 0, one CHECK on 不要: kept, the parts are meant). -->

**HSK 1 · Aula 2 · Dizer o que você quer · parte 1 de 2**

O que significa?

**Revisão 1 de 3**

**谢谢您！** *Xièxie nín!*

<!-- expected: Obrigado(a)! (a um senhor ou a uma senhora) -->

## T53 · STUDENT
Obrigado, senhor

## T54 · TUTOR
Isso.

Traduza para o mandarim.

**Revisão 2 de 3**

Olá, senhora!

<!-- expected: 您好！ -->

## T55 · STUDENT
您好！

## T56 · TUTOR
Certo.

**Revisão 3 de 3**

Na resposta, use **没事**.

— Desculpa!  
— Não foi nada.

<!-- expected: 对不起！——没事。 -->

## T57 · STUDENT
对不气！——没事。

## T58 · TUTOR
Quase. Você escreveu:

> 对不气！——没事。

**对不起** (*duìbuqǐ*): o último caractere é 起 (*qǐ*); 气 (*qì*) é o de 不客气.

**— 对不起！ — 没事。**  
*— Duìbuqǐ! — Méishì.*  
— Desculpa! — Não foi nada.

```html
<section id="mandarinmaxxing-vocab">
  <h2>HSK 1 · Aula 2 · Dizer o que você quer · parte 1 de 2</h2>
  <table>
    <thead><tr><th scope="col">Hanzi</th><th scope="col">Pinyin</th><th scope="col">Significado</th></tr></thead>
    <tbody><tr><td><span lang="zh-Hans">我</span></td><td>wǒ</td><td>eu</td></tr><tr><td><span lang="zh-Hans">要</span></td><td>yào</td><td>querer</td></tr><tr><td><span lang="zh-Hans">水</span></td><td>shuǐ</td><td>água</td></tr><tr><td><span lang="zh-Hans">茶</span></td><td>chá</td><td>chá</td></tr><tr><td><span lang="zh-Hans">你</span></td><td>nǐ</td><td>você</td></tr><tr><td><span lang="zh-Hans">吗</span></td><td>ma</td><td>(no fim da frase, faz dela uma pergunta de sim ou não)</td></tr><tr><td><span lang="zh-Hans">不</span></td><td>bù</td><td>não</td></tr></tbody>
  </table>
</section>
<script src="https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing@21cffbbd132031ae19f2248d9b1688ce254dc0cb/skills/mandarinmaxxing/web/vocab.js"></script>
```

不 vem antes do verbo e, antes de um quarto tom, se diz *bú*: 不要 (*bú yào*).  
Para responder sim ou não a uma pergunta com 吗, repete-se o verbo: 要 (quero), 不要 (não quero).

**Frases úteis**

**我要水。**  
*Wǒ yào shuǐ.*  
Eu quero água. (a bebida pode ser trocada)  
我要水 = 我 (eu) + 要 (querer) + 水 (água)

**我不要茶。**  
*Wǒ bú yào chá.*  
Eu não quero chá. (a bebida pode ser trocada)  
我不要茶 = 我 (eu) + 不 (não) + 要 (querer) + 茶 (chá)

**你要茶吗？**  
*Nǐ yào chá ma?*  
Você quer chá? (a pessoa e a bebida podem ser trocadas)  
你要茶吗 = 你 (você) + 要 (querer) + 茶 (chá) + 吗 (pergunta)

**Rodada 1**

O que significa?

**Rodada 1 · 1 de 5**

**我要茶。** *Wǒ yào chá.*

<!-- expected: Eu quero chá. -->

## T59 · STUDENT
Eu quero chá

## T60 · TUTOR
Isso.

**Rodada 1 · 2 de 5**

**我不要水。** *Wǒ bú yào shuǐ.*

<!-- expected: Eu não quero água. -->

## T61 · STUDENT
Eu não quero água

## T62 · TUTOR
Certo.

O que você responde? Aceite.

**Rodada 1 · 3 de 5**

**你要水吗？**  
*Nǐ yào shuǐ ma?*  
Você quer água?

<!-- expected: 要，谢谢。 (好，谢谢。 também) -->

## T63 · STUDENT
Yào, xièxie.

## T64 · TUTOR
Certo: **要，谢谢。**

Agora recuse.

**Rodada 1 · 4 de 5**

**您要茶吗？**  
*Nín yào chá ma?*  
O senhor quer chá?

<!-- expected: 不要，谢谢。 -->

## T65 · STUDENT
不，谢谢。

## T66 · TUTOR
<!-- sim: 不要，谢谢 is already in Rodada 2 · 2 of the plan, so the item comes back there without rework. -->

O sentido está certo. Mais natural:

**不要，谢谢。**  
*Bú yào, xièxie.*  
Não quero, obrigado.

Em mandarim se recusa repetindo o verbo com 不; 不 sozinho soa seco.

O que significa?

**Rodada 1 · 5 de 5**

**我不要茶，我要水。** *Wǒ bú yào chá, wǒ yào shuǐ.*

<!-- expected: Eu não quero chá, eu quero água. -->

## T67 · STUDENT
Eu não quero chá, quero água

## T68 · TUTOR
Isso.

**Rodada 2**

Traduza para o mandarim.

**Rodada 2 · 1 de 4**

Eu quero chá, obrigado.

<!-- expected: 我要茶，谢谢。 -->

## T69 · STUDENT
我要茶，谢谢。

## T70 · TUTOR
Certo.

**Rodada 2 · 2 de 4**

— Você quer água?  
— Não quero, obrigada.

<!-- expected: 你要水吗？——不要，谢谢。 -->

## T71 · STUDENT
你要水？——不要，谢谢。

## T72 · TUTOR
<!-- sim: 吗 comes back in the next prompt, already planned as a question. -->

Quase. Você escreveu:

> 你要水？——不要，谢谢。

**吗** (*ma*): sem ela no fim, a primeira frase não é uma pergunta.

**— 你要水吗？ — 不要，谢谢。**  
*— Nǐ yào shuǐ ma? — Bú yào, xièxie.*  
— Você quer água? — Não quero, obrigada.

**Rodada 2 · 3 de 4**

Você não quer chá?

<!-- expected: 你不要茶吗？ -->

## T73 · STUDENT
Nǐ bú yào chá ma?

## T74 · TUTOR
Certo: **你不要茶吗？**

**Rodada 2 · 4 de 4**

Eu não quero chá, eu quero água.

<!-- expected: 我不要茶，我要水。 -->

## T75 · STUDENT
我不要茶，我要水。

## T76 · TUTOR
Certo.

**Rodada 3**

**Rodada 3 · 1 de 2**

Olá! Eu quero chá. Você quer chá?

<!-- expected: 你好！我要茶。你要茶吗？ -->

## T77 · STUDENT
你好！我要水。你要茶吗？

## T78 · TUTOR
Quase. Você escreveu:

> 你好！我要水。你要茶吗？

**茶** (*chá*): na segunda frase você pediu 水, que é água.

**你好！我要茶。你要茶吗？**  
*Nǐ hǎo! Wǒ yào chá. Nǐ yào chá ma?*  
Olá! Eu quero chá. Você quer chá?

**Rodada 3 · 2 de 2**

Desculpa, eu não quero água. Eu quero chá, obrigada.

<!-- expected: 对不起，我不要水。我要茶，谢谢。 -->

## T79 · STUDENT
对不起，我不要水。我要茶，谢谢。

## T80 · TUTOR
Certo.

**Leitura 1**

Você está num café com um amigo. O que você diz, em mandarim, em cada momento?

1. Você chega ao balcão e pede água.
2. O atendente oferece chá; você recusa.
3. Você pergunta ao seu amigo se ele quer chá.
4. Você recebe a água e vai embora.

<!-- expected: 1. 你好，我要水。 2. 不要，谢谢。 3. 你要茶吗？ 4. 谢谢，再见！ -->

## T81 · STUDENT
1. Nǐ hǎo, wǒ yào shuǐ.
2. Bú yào, xièxie.
3. Nǐ yào chá ma?
4. Xièxie, zàijiàn!

## T82 · TUTOR
<!-- sim: saved course/course.md: Done + `1-02.1 | 我 要 水 茶 你 吗 不`, Next: Lesson 02, part 2 of 2, To reinforce: none (对不起, 不要, 吗 and 茶 were all answered correctly later in the part). Copy: course-after-L2p1.md. -->

Tudo certo, os quatro:

**你好，我要水。**  
**不要，谢谢。**  
**你要茶吗？**  
**谢谢，再见！**

Da próxima vez: HSK 1, Aula 2, parte 2. Quer começar essa parte agora?
