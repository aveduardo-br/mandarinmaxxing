#!/bin/bash
# usage: start_part.sh NN
R=/home/claude/mm-bench/cipher-1; P=$R/part-$1
mkdir -p $P
if [ "$1" = 01 ]; then echo "start mandarinmaxxing" > $P/a-000.md; else cp $R/course/course.md $P/course-start.md; echo "próxima aula" > $P/a-000.md; fi
cp $P/a-000.md $P/a-000.enc.md
date +%s > $P/.t0
nohup setsid /home/claude/watcher.sh $1 > $P/.watcher.log 2>&1 < /dev/null &
echo "started part $1"
