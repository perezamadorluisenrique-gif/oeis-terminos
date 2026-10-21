# impl1 for A053773: #{X in GL(n,2): X^8 = I}.
# In characteristic 2, X^8 - I = (X - I)^8, so X = I + N with N nilpotent and N^8 = 0
# (and every such X is invertible). Nilpotent orbits <-> partitions lambda of n (Jordan type);
# N^8 = 0 <=> all parts <= 8. Orbit size = |GL_n(q)| / |C(lambda)| with
# |C(lambda)| = q^(sum_i (lambda'_i)^2) * prod_i prod_{k=1}^{m_i} (1 - q^-k)  (m_i = multiplicity of part i).
from fractions import Fraction
import sys
q = 2
def partitions(n, maxpart):
    if n == 0:
        yield []
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield [p] + rest
def gl(n):
    r = 1
    for i in range(n):
        r *= q**n - q**i
    return r
def cent(lam):
    conj = [sum(1 for p in lam if p > i) for i in range(lam[0])] if lam else []
    c = Fraction(q) ** sum(x * x for x in conj)
    from collections import Counter
    for part, m in Counter(lam).items():
        for k in range(1, m + 1):
            c *= (1 - Fraction(1, q**k))
    return c
def count(n, k=8):
    g = gl(n)
    tot = Fraction(0)
    for lam in partitions(n, k):
        tot += g / cent(lam)
    assert tot.denominator == 1
    return tot.numerator
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
for n in range(N + 1):
    if n <= 12:  # sanity: all nilpotents when n <= 8
        assert count(n, n if n else 1) == q**(n*(n-1)), n
    print(n, count(n))
