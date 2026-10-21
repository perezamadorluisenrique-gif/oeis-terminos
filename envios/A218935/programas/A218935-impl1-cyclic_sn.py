#!/usr/bin/env python3
"""impl1 for A218932, A218935, A218949, A218975 (cyclic subgroup classes of S_n, A_n).

Conjugacy classes of cyclic subgroups of S_n <-> cycle types (a generator's powers
coprime to the order keep the type).  <g> < <h> properly (up to conjugacy) iff
type(g) = type(h)^k with gcd(k, ord h) > 1; it suffices to take k = p prime dividing
ord(h).  Power map: an L-cycle raised to k gives gcd(L,k) cycles of length L/gcd(L,k).
In A_n an S_n-class of cyclic subgroups <g> splits in two iff N_{S_n}(<g>) <= A_n.
The centralizer is even only if the cycle lengths are distinct and odd (1 at most
once); then an element normalizing <g> acts on each L-cycle as x -> kx on Z/L, whose
sign is the Jacobi symbol (k|L) (Zolotarev), so the normalizer is even iff
(k | prod L) = 1 for every k prime to the lengths, i.e. iff prod L is a perfect square.
'Connected' (A218975): graph on the parts, edge iff gcd > 1, is connected.
Usage: cyclic_sn.py NMAX outdir   (writes A218932.txt A218935.txt A218949.txt A218975.txt)
"""
import sys
from math import gcd, lcm, isqrt


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def primes_of(x):
    ps, d = [], 2
    while d * d <= x:
        if x % d == 0:
            ps.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        ps.append(x)
    return ps


def power(lam, k):
    out = []
    for L in lam:
        g = gcd(L, k)
        out += [L // g] * g
    return tuple(sorted(out, reverse=True))


def even(lam):
    return sum(1 for L in lam if L % 2 == 0) % 2 == 0


def splits(lam):
    if len(set(lam)) != len(lam) or any(L % 2 == 0 for L in lam):
        return False
    P = 1
    for L in lam:
        P *= L
    return isqrt(P) ** 2 == P


def connected(lam):
    if len(lam) == 0:
        return True
    seen, stack = {0}, [0]
    while stack:
        i = stack.pop()
        for j in range(len(lam)):
            if j not in seen and gcd(lam[i], lam[j]) > 1:
                seen.add(j)
                stack.append(j)
    return len(seen) == len(lam)


N, outdir = int(sys.argv[1]), sys.argv[2]
res = {k: [] for k in ("A218932", "A218935", "A218949", "A218975")}
for n in range(0, N + 1):
    parts = list(partitions(n))
    notmax_s, notmax_a = set(), set()
    for mu in parts:
        o = lcm(*mu) if mu else 1
        ev = even(mu)
        for p in primes_of(o):
            nu = power(mu, p)
            notmax_s.add(nu)
            if ev:
                notmax_a.add(nu)
    s32 = s35 = s49 = s75 = 0
    for lam in parts:
        if lam not in notmax_s:
            s32 += 1
        if even(lam):
            w = 2 if n >= 2 and splits(lam) else 1  # A_n = S_n for n <= 1
            s35 += w
            if lam not in notmax_a:
                s49 += w
            if connected(lam):
                s75 += w
    for k, v in zip(res, (s32, s35, s49, s75)):
        res[k].append((n, v))
    print(f"# n={n}", file=sys.stderr, flush=True)
for k, v in res.items():
    with open(f"{outdir}/{k}.txt", "w") as f:
        for n, x in v:
            f.write(f"{n} {x}\n")
