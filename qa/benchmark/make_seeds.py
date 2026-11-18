"""Write the starting course.md files for the benchmark scenarios."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from review_coverage import parts

PT = ['Cumprimentar e agradecer', 'Dizer o que você quer', 'Dizer quem você é', 'De onde você é e onde está',
      'Apresentar alguém', 'Dizer a idade', 'Quem mora na sua casa', 'Ligações', 'Filhos, parceiros e bichos',
      'Datas e dias da semana', 'Horário e rotina', 'Comer e beber', 'Compras e pagamento', 'Escolher roupas e coisas',
      'Onde as coisas estão', 'Ir e vir', 'Tempo livre', 'Falar do clima', 'Estudar chinês', 'Na escola',
      'Falar do trabalho', 'Ficar doente']
MAP = 'skills/mandarinmaxxing/maps/hsk-1.md'

PT3 = ['Dar sua opinião', 'Contar o que aconteceu', 'Fazer um plano', 'Falar dos seus hábitos', 'Pôr a conversa em dia',
       'Família e vizinhos', 'Descrever um amigo', 'Dizer como você se sente', 'Dizer quando foi', 'Feriados e visitas',
       'Comer fora', 'Comprar comida', 'Comer em casa', 'Provar roupas', 'Mudar de casa', 'Arrumar e se aprontar',
       'Cuidar da saúde', 'Perder o celular ou o cartão', 'E-mail e mensagens', 'Falar das estações', 'Um dia ao ar livre',
       'No zoológico', 'Achar o caminho', 'Lugares no mapa', 'Pegar trem ou avião', 'No hotel', 'Ler placas e avisos',
       'Sua turma', 'Fazer a lição de casa', 'Falar das suas notas', 'Na biblioteca', 'Estudar fora', 'No escritório',
       'Resolver um problema', 'Esportes e jogos', 'Shows e música', 'Do que você gosta']

def lessons(pace_idx=1, path=None):
    out, cur = [], None
    for line in open(path or MAP, encoding='utf-8'):
        if line.startswith('## '):
            cur = {'n': int(line[3:5]), 'blocks': []}; out.append(cur)
        elif line.startswith('Split:'):
            cur['split'] = [int(x) for x in line[6:].split('/')[pace_idx].split('-')]
        elif line.startswith('- ') and cur:
            cur['blocks'].append(line[2:].split())
    return out

def course(done_until, next_line, route='01–22', extra='', reinforce='', level=1):
    ls = lessons(path=f'skills/mandarinmaxxing/maps/hsk-{level}.md')
    if level == 1: names = PT
    elif level == 3: names = PT3
    else: names = [n for n in (line.split('|')[2].strip() for line in open(f'skills/mandarinmaxxing/maps/hsk-{level}.md', encoding='utf-8') if line.startswith('## '))]
    done = []
    for l in ls:
        i = 0
        for p, size in enumerate(l['split'], 1):
            ws = sum(l['blocks'][i:i + size], []); i += size
            done.append((f"{level}-{l['n']:02d}.{p}", ws))
    lines = [d for d in done][:done_until]
    head = f"""# mandarinmaxxing course
- Syllabus: HSK 3.0 (2025-11), level {level}
- Pace: about 5 words per part
- Language: Português
- Labels: Aula, parte, Revisão, Bateria, Exercício, Escuta, Leitura, Frases úteis, Largada
- Audio: ElevenLabs, voice Sarah
- Route: {route}
- Next: {next_line}
- To reinforce: {reinforce}
{extra}
## Lessons
""" + '\n'.join(f"{l['n']:02d} {names[l['n']-1]} ({len(l['split'])} {'parte' if len(l['split'])==1 else 'partes'})" for l in ls) + "\n\n## Done\n" + '\n'.join(f"{k} | {' '.join(w)}" for k, w in lines) + '\n'
    return head.replace('\n\n## Lessons', '\n## Lessons'), len(lines)

if __name__ == '__main__':
    d = os.path.join(os.path.dirname(__file__), 'scenarios')
    # S2: everything up to and including 11.1 done; next is 11.2
    ls = lessons(); k = 0
    for l in ls:
        if l['n'] < 11: k += len(l['split'])
    s2, n2 = course(k + 1, 'Lesson 11, part 2 of 4', reinforce='几点 没关系')
    open(os.path.join(d, 's2-course.md'), 'w', encoding='utf-8').write(s2)
    # S5: lesson 01 done (2 parts); next is 02.1
    s5, n5 = course(2, 'Lesson 02, part 1 of 2')
    open(os.path.join(d, 's5-course.md'), 'w', encoding='utf-8').write(s5)
    print('s2 done lines', n2, '| s5 done lines', n5)
    # S6: HSK 3, lessons 01-17 done; next is 18.1 (learner started at HSK 3, so HSK 1-2 count as met)
    l3 = lessons(path='skills/mandarinmaxxing/maps/hsk-3.md')
    k6 = sum(len(l['split']) for l in l3 if l['n'] <= 17)
    p18 = len(next(l for l in l3 if l['n'] == 18)['split'])
    s6, n6 = course(k6, f'Lesson 18, part 1 of {p18}', route='01–37', level=3, reinforce='一定 打算')
    open(os.path.join(d, 's6-course.md'), 'w', encoding='utf-8').write(s6)
    # S7: HSK 3, lessons 01-06 done (jump start finished); learner jumps to 30
    k7 = sum(len(l['split']) for l in l3 if l['n'] <= 6)
    p7 = len(next(l for l in l3 if l['n'] == 7)['split'])
    s7, n7 = course(k7, f'Lesson 07, part 1 of {p7}', route='01–37', level=3)
    open(os.path.join(d, 's7-course.md'), 'w', encoding='utf-8').write(s7)
    print('s6 done lines', n6, '| s7 done lines', n7)
    # S8: HSK 2 right after its jump start (lessons 01-04 done); next is 05.1. HSK 1 counts as met.
    l2 = lessons(path='skills/mandarinmaxxing/maps/hsk-2.md')
    k8 = sum(len(l['split']) for l in l2 if l['n'] <= 4)
    p5 = len(next(l for l in l2 if l['n'] == 5)['split'])
    s8, n8 = course(k8, f'Lesson 05, part 1 of {p5}', route='01–19', level=2)
    open(os.path.join(d, 's8-course.md'), 'w', encoding='utf-8').write(s8)
    # S9: middle of HSK 4 (lessons 01-27 done); next is 28.1. HSK 1-3 count as met.
    l4 = lessons(path='skills/mandarinmaxxing/maps/hsk-4.md')
    k9 = sum(len(l['split']) for l in l4 if l['n'] <= 27)
    p28 = len(next(l for l in l4 if l['n'] == 28)['split'])
    s9, n9 = course(k9, f'Lesson 28, part 1 of {p28}', route='01–56', level=4)
    open(os.path.join(d, 's9-course.md'), 'w', encoding='utf-8').write(s9)
    print('s8 done lines', n8, '| s9 done lines', n9)
    # S10: HSK 1, Lesson 04 parts 1-2 done; next is 04.3, which teaches 中文 and 汉语 together
    l1 = lessons()
    k10 = sum(len(l['split']) for l in l1 if l['n'] <= 3) + 2
    s10, n10 = course(k10, 'Lesson 04, part 3 of 3', reinforce='什么')
    open(os.path.join(d, 's10-course.md'), 'w', encoding='utf-8').write(s10)
    print('s10 done lines', n10)
    # S11: middle of HSK 2 (lessons 01-09 done); next is 10.1. HSK 1 counts as met.
    k11 = sum(len(l['split']) for l in l2 if l['n'] <= 9)
    p10 = len(next(l for l in l2 if l['n'] == 10)['split'])
    s11, n11 = course(k11, f'Lesson 10, part 1 of {p10}', route='01–19', level=2, reinforce='虽然 得')
    open(os.path.join(d, 's11-course.md'), 'w', encoding='utf-8').write(s11)
    print('s11 done lines', n11)
