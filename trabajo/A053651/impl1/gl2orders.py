#!/usr/bin/env python3
"""impl1 for A053651, A062766 (and A085430 for orders reachable).

Theory: an element of GL(m,2) decomposes into primary parts. A part on an
irreducible f != x+1 of degree d with Jordan multiplicity r has order
ord(f)*2^ceil(log2 r); ord(f) ranges over e | 2^d-1 with ord_e(2) = d.
The 2-part 2^a (a>=1) is obtained most cheaply by a unipotent block of size
2^(a-1)+1 on x+1 (cost u(a)); attaching it to f of degree d>=2 is never cheaper.
Two f's of the same degree d can be merged into one (lcm of their orders still
has exact order d), so the odd part o has minimal cost
  c(o) = min sum of distinct degrees d with lcm(e_d) = o,
computed by a 0/1 knapsack over degrees.  Then
  orders of GL(n,2)  = { o*2^a : c(o) + u(a) <= n },       u(0)=0
  orders of AGL(n,2) = { o*2^a : c(o) + max(1,u(a)) <= n+1 }  (AGL(n,2) = elements of
  GL(n+1,2) with eigenvalue 1, read off the dual).
"""
import sys
from math import gcd
from sympy import factorint, n_order, divisors

N = int(sys.argv[1])


def u(a):
    return 0 if a == 0 else 2 ** (a - 1) + 1


best = {1: 0}  # odd order -> minimal cost
for d in range(2, N + 1):
    M = 2 ** d - 1
    E = [e for e in divisors(M) if e > 1 and n_order(2, e) == d]
    snap = [(o, c) for o, c in best.items() if c + d <= N]
    for e in E:
        for o, c in snap:
            l = o // gcd(o, e) * e
            nc = c + d
            if best.get(l, N + 1) > nc:
                best[l] = nc
    print(f"# d={d} odd orders so far {len(best)}", file=sys.stderr, flush=True)

cnt = [0] * (N + 2)  # number of odd o with c(o) == k
for c in best.values():
    cnt[c] += 1
pref = [0] * (N + 2)
s = 0
for k in range(N + 2):
    s += cnt[k]
    pref[k] = s

def gl(n):
    tot, a = 0, 0
    while u(a) <= n:
        tot += pref[n - u(a)]
        a += 1
    return tot

def agl(n):
    tot, a = 0, 0
    while max(1, u(a)) <= n + 1:
        tot += pref[n + 1 - max(1, u(a))]
        a += 1
    return tot

with open(sys.argv[2], "w") as f:
    for n in range(1, N + 1):
        f.write(f"{n} {gl(n)}\n")
with open(sys.argv[3], "w") as f:
    for n in range(1, N):  # agl(n) needs costs <= n+1 <= N
        f.write(f"{n} {agl(n)}\n")
