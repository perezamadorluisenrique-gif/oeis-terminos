#!/usr/bin/env python3
# A086087: minimal m such that GL(m,3) has an element of order n.
# Primary decomposition: an element is a direct sum of blocks J_s(f) with f irreducible
# (f != x), deg f = ord_d(3) where d = multiplicative order of a root of f (gcd(d,3)=1);
# block J_s(f) has dimension s*deg f and order d*3^c, 3^c the least power of 3 >= s.
# Order of the sum = lcm. For n = 3^a * n' only one block needs s > 1 (s = 3^(a-1)+1).
import sys
from math import gcd

def ordmod(d):
    if d == 1: return 1
    k, x = 1, 3 % d
    while x != 1:
        x = x * 3 % d; k += 1
    return k

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def best(np_, start):
    # min sum of ord_d(3) over a set of divisors d of np_ whose lcm with `start` is np_
    D = divisors(np_)
    INF = float('inf')
    dp = {d: INF for d in D}
    dp[start] = 0
    for L in D:                      # ascending: lcm never decreases
        if dp[L] == INF: continue
        for d in D:
            if L % d == 0: continue
            M = L * d // gcd(L, d)
            c = dp[L] + ordmod(d)
            if c < dp[M]: dp[M] = c
    return dp[np_]

def a(n):
    e, np_ = 0, n
    while np_ % 3 == 0: np_ //= 3; e += 1
    if e == 0:
        return best(np_, 1)
    s = 3 ** (e - 1) + 1
    return min(ordmod(d0) * s + best(np_, d0) for d0 in divisors(np_))

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
for n in range(2, N + 1):
    print(n, a(n))
