#!/bin/bash
# usage: relay.sh NN t K   (encode t-K.md -> s-K.enc.md)   |   relay.sh NN a K   (decode a-K.enc.md -> a-K.md)
cd /home/claude/mandarinmaxxing
P=/home/claude/mm-bench/cipher-1/part-$1
K=$(printf %03d $3)
if [ "$2" = t ]; then
  [ -f $P/t-$K.md ] || { echo "MISSING t-$K.md"; exit 1; }
  python3 qa/benchmark/cipher/cipher.py encode $P/t-$K.md $P/s-$K.enc.md
  echo "t-$K ok END=$(grep -c '\[END OF PART\]' $P/t-$K.md)"
else
  [ -f $P/a-$K.enc.md ] || { echo "MISSING a-$K.enc.md"; exit 1; }
  python3 qa/benchmark/cipher/cipher.py decode $P/a-$K.enc.md $P/a-$K.md
  echo "a-$K ok"
fi
