Compile: gcc -O3 -march=native -o impl2 impl2.c -lm
Run: ./impl2 n part nparts   (prints "n part nparts count"); sum counts over parts. run.sh runs n=25..27 as 2 processes.
Timings (2 processes, nice 10): n=25 106s, n=26 241s, n=27 524s; n=24 single process 47s. n=2..24 match known terms.
