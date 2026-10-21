import sys
from sympy import factorint
from sympy.ntheory import n_order
from math import lcm
def partitions(lst):
    if not lst: yield []; return
    f=lst[0]
    for p in partitions(lst[1:]):
        for i in range(len(p)):
            yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def c_odd(m):
    ds=[n_order(2,p**k) for p,k in factorint(m).items()]
    if not ds: return 0
    return min(sum(lcm(*g) for g in P) for P in partitions(ds))
def mindim(N):
    t=0
    while N%2==0: N//=2; t+=1
    return c_odd(N)+(0 if t==0 else 2**(t-1)+1)
if __name__=="__main__":
    with open(sys.argv[1],"w") as f:
        for n in range(2,10001): f.write(f"{n} {mindim(n)}\n")
