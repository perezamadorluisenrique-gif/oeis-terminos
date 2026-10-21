# for each d<=70 list divisors e of 2^d-1 with ord_e(2)==d exactly
import itertools
from math import lcm
from sympy import factorint
from sympy.ntheory import n_order
out=open("prim.txt","w")
for d in range(2,73):
    f=factorint(2**d-1)
    opts=[]
    for p,a in f.items():
        opts.append([(1,1)]+[(p**k,n_order(2,p**k)) for k in range(1,a+1)])
    cnt=0
    for combo in itertools.product(*opts):
        e=1;o=1
        for q,od in combo: e*=q;o=lcm(o,od)
        if o==d: out.write(f"{d} {e}\n");cnt+=1
    print(d,cnt,flush=True)
