Method: Jordan decomposition g=s*u; s semisimple, order n' coprime to 3, split into set partition of prime powers, cost sum ord_r(3); unipotent part of order 3^e needs a block of multiplicity 3^(e-1)+1 (extra d*3^(e-1) or fresh trivial block 3^(e-1)+1). Minimised over partitions (a086087.py, run.sh).
Reproduces known values n=2..24.
Brute force (brute.c, all matrices of GL(m,3), m=1..4, ~40 s for m=4): set of element orders equals {n : a(n)<=m} exactly for m=1,2,3,4 (orders up to 3000 compared).
