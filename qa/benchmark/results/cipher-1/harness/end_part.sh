#!/bin/bash
R=/home/claude/mm-bench/cipher-1; P=$R/part-$1
mkdir -p $P/course && cp $R/course/course.md $P/course/course.md
cd /home/claude/mandarinmaxxing && python3 qa/benchmark/cipher/audit.py assemble $P
echo "secs=$(( $(date +%s) - $(cat $P/.t0) ))"
python3 - "$P" <<'PY'
import re,sys,json,subprocess,os
P=sys.argv[1]
s=open(P+'/transcript.student.md',encoding='utf-8').read()
print('student_han',len(re.findall(r'[一-鿿]',s)),'pinyin_tones',sorted(set(re.findall(r'\w*[āǎēěīǐōǒūǔǖǘǚǜ]\w*',s)))[:10])
print('nao_sei',len(re.findall(r'NÃO SEI',s)))
c=open(P+'/course/course.md',encoding='utf-8').read()
print([l for l in c.splitlines() if l.startswith('- Next') or l.startswith('- To reinforce')])
print('done_last',[l for l in c.splitlines() if '|' in l][-1:])
PY
