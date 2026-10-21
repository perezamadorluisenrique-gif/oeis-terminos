#!/usr/bin/env python3
"""impl1 for A267132: unipotent n X n matrices over GF(2) that are squares of
unipotent matrices.  Uses the characterization proved by V. S. Miller
(arXiv:1606.09299, quoted in the OEIS entry): a(n)/|GL_n(2)| = sum over partitions
lambda of n whose conjugate has every odd part with multiplicity <= 1 of 1/|C(lambda)|,
where |C(lambda)| = q^{sum (lambda'_i)^2} prod_i prod_{k=1}^{m_i} (1 - q^-k) is the order of
the centralizer of a nilpotent of Jordan type lambda (m_i = multiplicity of i).
Note: the %F line as printed omits the q-power and starts k at 0 (a factor 0);
read literally it does not reproduce the data, so the standard centralizer is used.
Exact rational arithmetic.
"""
import sys
from fractions import Fraction
from collections import Counter


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def conj(lam):
    return tuple(sum(1 for x in lam if x > i) for i in range(lam[0])) if lam else ()


def gl(n, q=2):
    r = 1
    for i in range(n):
        r *= q ** n - q ** i
    return r


N = int(sys.argv[1])
for n in range(1, N + 1):
    s = Fraction(0)
    for lam in partitions(n):
        c = Counter(conj(lam))
        if any(v > 1 for k, v in c.items() if k % 2 == 1):
            continue
        C = Fraction(2 ** sum(x * x for x in conj(lam)))
        for i, m in Counter(lam).items():
            for k in range(1, m + 1):
                C *= 1 - Fraction(1, 2 ** k)
        s += 1 / C
    v = s * gl(n)
    assert v.denominator == 1
    print(n, v.numerator, flush=True)
