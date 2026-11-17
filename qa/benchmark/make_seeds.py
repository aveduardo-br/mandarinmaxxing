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

def lessons(pace_idx=1):
    out, cur = [], None
    for line in open(MAP, encoding='utf-8'):
        if line.startswith('## '):
            cur = {'n': int(line[3:5]), 'blocks': []}; out.append(cur)
        elif line.startswith('Split:'):
            cur['split'] = [int(x) for x in line[6:].split('/')[pace_idx].split('-')]
        elif line.startswith('- ') and cur:
            cur['blocks'].append(line[2:].split())
    return out

def course(done_until, next_line, route='01–22', extra='', reinforce=''):
    ls = lessons()
    done = []
    for l in ls:
        i = 0
        for p, size in enumerate(l['split'], 1):
            ws = sum(l['blocks'][i:i + size], []); i += size
            done.append((f"1-{l['n']:02d}.{p}", ws))
    lines = [d for d in done][:done_until]
    head = f"""# mandarinmaxxing course
- Syllabus: HSK 3.0 (2025-11), level 1
- Pace: about 5 words per part
- Language: Português
- Labels: Aula, parte, Revisão, Bateria, Exercício, Escuta, Leitura, Frases úteis, Largada
- Audio: ElevenLabs, voice Sarah
- Route: {route}
- Next: {next_line}
- To reinforce: {reinforce}
{extra}
## Lessons
""" + '\n'.join(f"{l['n']:02d} {PT[l['n']-1]} ({len(l['split'])} {'parte' if len(l['split'])==1 else 'partes'})" for l in ls) + "\n\n## Done\n" + '\n'.join(f"{k} | {' '.join(w)}" for k, w in lines) + '\n'
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
