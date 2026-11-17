#!/bin/bash
# next.sh NN MM tutor_tok student_tok : close part NN (log usage), start part MM if given
R=/home/claude/mm-bench/cipher-1
echo "$1 tutor=$3 student=$4 secs=$(( $(date +%s) - $(cat $R/part-$1/.t0) ))" >> $R/.usage.log
/home/claude/end_part.sh $1 2>&1 | grep -v "^secs"
tail -1 $R/part-$1/.watcher.log
[ -n "$2" ] && /home/claude/start_part.sh $2
