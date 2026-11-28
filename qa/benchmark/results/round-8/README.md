# Benchmark, rodada 8 (branch review-fixes, commit 21cffbb, 27/11/2026)

Três simulações dos cenários novos (`s12`, `s13`, `s14` em `../../scenarios.md`), rodadas na versão enxuta da 0.8.0, antes das correções dos commits seguintes. Cada pasta tem a transcrição, as notas da simulação e o `course.md` final.

Método e limites: um agente só fez o professor e o aluno, fora do app do Claude (HTML escrito como bloco de código, áudio como texto). Não houve juiz separado nesta rodada. As notas listam o que a simulação achou; os defeitos de script apontados nelas (próxima parte depois de reabrir uma aula, contagem de palavras em dobro, verbo separado) foram corrigidos depois, e os testes que os cobrem estão em `tools/test_scripts.py`.

| Cenário | Exercícios | Tempo estimado |
|---|---|---|
| s12, três primeiras partes do HSK 1 | 36 | 25 a 33 min |
| s14, parte de 3 palavras do HSK 3 | 17 e um ditado | 25 a 30 min |
| s13, pulo com aulas conhecidas (HSK 2, aula 12, parte 1) | 23 e uma leitura | cerca de 45 min |
