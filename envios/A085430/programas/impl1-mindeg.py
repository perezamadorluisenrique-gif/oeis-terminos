#!/usr/bin/env python3
"""impl1 for A085430: minimal m with an element of order n in GL(m,2).
n = 2^a * o, o odd.  m(n) = u(a) + c(o), u(0)=0, u(a)=2^(a-1)+1 (unipotent Jordan
block on x+1), c(o) = min over set partitions of the prime powers of o of
sum over blocks B of ord_{prod B}(2) (one irreducible polynomial per block, its
order being prod B; degree = multiplicative order of 2).  See A053651/impl1 for the
justification.  Usage: mindeg.py NMAX > impl1.txt"""
import sys
from math import lcm
from sympy import factorint, n_order

def partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]

def c(o):
    if o == 1:
        return 0
    pp = [p ** k for p, k in factorint(o).items()]
    ords = {q: n_order(2, q) for q in pp}
    return min(sum(lcm(*[ords[q] for q in B]) for B in P) for P in partitions(pp))

N = int(sys.argv[1])
for n in range(2, N + 1):
    a = (n & -n).bit_length() - 1
    o = n >> a
    print(n, (0 if a == 0 else 2 ** (a - 1) + 1) + c(o))
