# usage: prim.py q D out  -> lines "d e" : e is an "indecomposable" root order for degree d>=2:
# ord_e(q)=d, e coprime to p, d1=free prime powers removed, and no partition of e's prime powers beats cost d.
import sys, itertools
from math import lcm
from sympy import factorint
from sympy.ntheory import n_order
q=int(sys.argv[1]); D=int(sys.argv[2]); out=open(sys.argv[3],"w")
def setparts(lst):
    if not lst: yield []; return
    first,rest=lst[0],lst[1:]
    for p in setparts(rest):
        yield [[first]]+p
        for i in range(len(p)):
            yield p[:i]+[[first]+p[i]]+p[i+1:]
def P(dl):  # dl: list of d(prime power) (d=1 free). min partition cost
    dl=[x for x in dl if x>1]
    if not dl: return 0
    return min(sum(lcm(*g) for g in part) for part in setparts(dl))
for d in range(2,D+1):
    f=factorint(q**d-1)
    opts=[]
    for p,a in f.items():
        opts.append([(1,1)]+[(p**k,n_order(q,p**k)) for k in range(1,a+1)])
    cnt=0; seen=set()
    for combo in itertools.product(*opts):
        e=1; ds=[]
        for qq,od in combo:
            if qq>1:
                if od==1: continue   # free prime power (divides q-1): dropped
                e*=qq; ds.append(od)
        if not ds or lcm(*ds)!=d: continue
        if P(ds)!=d: continue
        if e in seen: continue
        seen.add(e)
        cnt+=1; out.write(f"{d} {e}\n")
    print(d,cnt,flush=True)
