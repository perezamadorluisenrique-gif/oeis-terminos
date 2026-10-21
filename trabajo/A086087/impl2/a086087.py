"""A086087: minimal m with an element of order n in GL(m,3).
Method: Jordan decomposition g = s*u (commuting), s semisimple of order n' (3 does not divide n'),
u unipotent of 3-power order; ord(g)=ord(s)*ord(u), n=3^e*n'.
s is block-diagonal over F_3: each irreducible factor whose roots have multiplicative order r
(gcd(r,3)=1) has degree d=ord_r(3) and contributes r to the lcm; distinct r's whose lcm is n'.
Optimal r's are pairwise coprime products of the prime powers of n' (a set partition of them),
cost sum ord_r(3). The centralizer of s is prod GL(k_i, 3^d_i); a unipotent element of order 3^e
there needs k_i >= 3^(e-1)+1 (Jordan block size j has order 3^ceil(log3 j)), costing d_i*3^(e-1)
extra on one block, or a fresh trivial (x-1) block of size 3^(e-1)+1. Minimise over partitions.
"""
import sys
def factor(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def ordmod(r):
    if r==1: return 1
    k=1;x=3%r
    while x!=1: x=x*3%r;k+=1
    return k
def partitions(l):
    if not l: yield []; return
    a,rest=l[0],l[1:]
    for p in partitions(rest):
        yield [[a]]+p
        for i in range(len(p)):
            yield p[:i]+[[a]+p[i]]+p[i+1:]
def a(n):
    e=0
    while n%3==0: n//=3; e+=1
    pp=[p**k for p,k in factor(n).items()]
    best=None
    for part in partitions(pp):
        ds=[]
        for g in part:
            r=1
            for x in g: r*=x
            ds.append(ordmod(r))
        tot=sum(ds)
        if e>0:
            t=3**(e-1)
            tot+=min(t+1, min(ds)*t) if ds else t+1
        if best is None or tot<best: best=tot
    return best
if __name__=="__main__":
    with open("../impl2.txt","w") as f:
        for n in range(2,10001): f.write(f"{n} {a(n)}\n")
