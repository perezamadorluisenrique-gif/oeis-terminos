#!/usr/bin/env python3
"""impl1 for A053658 (q=3) and A053660 (q=4): number of distinct element orders
of GL(n,q).  Usage: glq_orders.py q NMAX out.txt

q = p^f.  Primary decomposition: a component on an irreducible f != x of degree d
whose roots have multiplicative order e (e | q^d-1, ord_e(q) = d) with largest
Jordan block r has dimension >= d*r and order e*p^ceil(log_p r).  Writing an order
as p^a * o (p ∤ o):
  * o needs one e_d per used degree d with lcm = o (two of the same degree merge
    into their lcm, still of exact degree d): c(o) = min sum of degrees (0/1 knapsack).
  * p^a (a >= 1) needs a Jordan block of size M = p^(a-1)+1 on some f; on f of degree
    d it costs d*M instead of d (plus nothing else).  d*M vs d + M: equal for d = 1,
    never smaller for d >= 2.  So the cheapest options are a separate block on x-1
    (cost M) or putting the block on a degree-1 component x-c already used by o
    (saves 1): cost(p^a*o) = min(c(o) + M, c1(o) + M - 1), where c1(o) is the
    minimal cost of a decomposition of o that uses a degree-1 part e_1 > 1.
GL(n,q) has an element of order N iff cost(N) <= n (pad with the identity).
"""
import sys
from math import gcd
from sympy import n_order, divisors, factorint

q, N, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
p = min(factorint(q))
INF = 10 ** 9
best = {1: (0, INF)}
for d in range(1, N + 1):
    E = [e for e in divisors(q ** d - 1) if e > 1 and n_order(q, e) == d]
    snap = [(o, c, c1) for o, (c, c1) in best.items() if min(c, c1) + d <= N]
    for e in E:
        for o, c, c1 in snap:
            l = o // gcd(o, e) * e
            nc = c + d
            nc1 = min(c, c1) + d if d == 1 else c1 + d
            oc, oc1 = best.get(l, (INF, INF))
            if nc < oc or nc1 < oc1:
                best[l] = (min(oc, nc), min(oc1, nc1))
    print(f"# d={d} orders {len(best)}", file=sys.stderr, flush=True)

cnt = [0] * (N + 1)
a_max = 0
while p ** a_max + 1 <= N:
    a_max += 1
for o, (c, c1) in best.items():
    for a in range(0, a_max + 2):
        if a == 0:
            k = c
        else:
            M = p ** (a - 1) + 1
            k = min(c + M, c1 + M - 1)
        if k <= N:
            cnt[k] += 1
with open(out, "w") as f:
    s = 0
    for n in range(1, N + 1):
        s += cnt[n] + (cnt[0] if n == 1 else 0)
        f.write(f"{n} {s}\n")
