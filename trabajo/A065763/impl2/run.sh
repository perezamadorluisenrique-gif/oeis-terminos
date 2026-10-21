#!/bin/bash
cd /home/claude/work/impl2/A065763
for n in 25 26 27; do
  s=$(date +%s)
  nice -n 10 ./impl2 $n 0 2 > p_${n}_0.txt & nice -n 10 ./impl2 $n 1 2 > p_${n}_1.txt & wait
  e=$(date +%s); echo "$n $((e-s))s" >> timings.txt
done
echo done >> timings.txt
