# explicit set check: orders predicted by characterization vs brute force
import re,sys
from math import lcm
from sympy.ntheory import n_order
from sympy import factorint
def pred(q,n):
    p=2 if q==4 else 3
    # enumerate o up to bound by brute: components (e,d) with e|q^d-1, ord_e(q)=d, d<=n; cost via partitions (small n)
    comps=[(1,1)] if False else []
    for d in range(1,n+1):
        for e in range(1,q**d):
            if (q**d-1)%e==0 and n_order(q,e)==d if e>1 else d==1: comps.append((e,d))
    # P-cost: min total d of component set with lcm o ; free: d=1 comps (e|q-1) cost 0
    best={1:0}
    for e,d in comps:
        c=0 if d==1 else d
        for o,k in list(best.items()):
            pass
    # DP closure
    best={1:0}; ch=True
    while ch:
        ch=False
        for e,d in comps:
            c=0 if d==1 else d
            for o,k in list(best.items()):
                l=lcm(o,e)
                if k+c<=n and best.get(l,99)>k+c: best[l]=k+c; ch=True
    S=set()
    for o,k in best.items():
        S.add(o)
        t=1
        while k+p**(t-1)+1<=n: S.add(o*p**t); t+=1
    return S
for l in open("bruteforce.txt"):
    m=re.match(r"GL\((\d),(\d)\).*:(.*)",l)
    if m:
        n,q=int(m[1]),int(m[2]); bf=set(map(int,m[3].split()))
        print(f"GL({n},{q})", "OK" if pred(q,n)==bf else ("MISMATCH",sorted(pred(q,n)^bf)))
