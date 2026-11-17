#!/bin/bash
# watcher.sh NN : encodes each finished t-K.md to s-K.enc.md and decodes each a-K.enc.md to a-K.md (atomic), until the part ends.
cd /home/claude/mandarinmaxxing
P=/home/claude/mm-bench/cipher-1/part-$1
C=qa/benchmark/cipher/cipher.py
end_k=""
while true; do
  now=$(date +%s)
  for f in $P/t-[0-9][0-9][0-9].md; do
    [ -e "$f" ] || continue
    k=$(basename $f .md | cut -d- -f2)
    [ -e $P/s-$k.enc.md ] && continue
    [ $(( now - $(stat -c %Y $f) )) -ge 3 ] || continue
    python3 $C encode $f $P/.s-$k.tmp && mv $P/.s-$k.tmp $P/s-$k.enc.md && echo "$(date +%T) enc $k"
    grep -q '\[END OF PART\]' $f && end_k=$k
  done
  for f in $P/a-[0-9][0-9][0-9].enc.md; do
    [ -e "$f" ] || continue
    k=$(basename $f .enc.md | cut -d- -f2)
    [ -e $P/a-$k.md ] && continue
    [ $(( now - $(stat -c %Y $f) )) -ge 3 ] || continue
    python3 $C decode $f $P/.a-$k.tmp && mv $P/.a-$k.tmp $P/a-$k.md && echo "$(date +%T) dec $k"
  done
  if [ -n "$end_k" ] && [ -e $P/a-$end_k.md ]; then echo "part $1 done at $end_k"; exit 0; fi
  sleep 2
done
