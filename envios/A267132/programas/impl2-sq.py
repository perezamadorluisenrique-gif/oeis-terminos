from collections import Counter
N=60; q=2
# S[n] = Jordan types (partitions of n) of M^2 for nilpotent M (n x n); block m -> (ceil(m/2), floor(m/2))
S=[{()}]
for n in range(1,N+1):
    s=set()
    for m in range(1,n+1):
        blk=tuple(x for x in ((m+1)//2, m//2) if x>0)
        for l in S[n-m]: s.add(tuple(sorted(l+blk,reverse=True)))
    S.append(s)
def gl(n):
    r=1
    for i in range(n): r*=q**n-q**i
    return r
def cent(l):
    conj=[sum(1 for x in l if x>i) for i in range(l[0])] if l else []
    e=sum(c*c for c in conj); r=1
    for m in Counter(l).values():
        e-=m*(m+1)//2
        for j in range(1,m+1): r*=q**j-1
    return q**e*r
with open("../impl2.txt","w") as f:
    for n in range(1,N+1):
        G=gl(n); t=0
        for l in S[n]:
            c=cent(l); assert G%c==0; t+=G//c
        f.write(f"{n} {t}\n")
# sanity: all nilpotents counted over all partitions = q^(n(n-1))
for n in range(1,9):
    from sympy.utilities.iterables import partitions
    tot=sum(gl(n)//cent(tuple(sorted(sum(([k]*v for k,v in p.items()),[]),reverse=True))) for p in partitions(n))
    assert tot==q**(n*(n-1)),n
print("ok")
