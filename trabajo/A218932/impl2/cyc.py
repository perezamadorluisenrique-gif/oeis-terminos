import sys, math
from math import gcd
from multiprocessing import Pool

PR = {}
def primes_of(m):
    if m in PR: return PR[m]
    s=set(); x=m; p=2
    while p*p<=x:
        while x%p==0: s.add(p); x//=p
        p+=1
    if x>1: s.add(x)
    PR[m]=s; return s

def parts(n, mx=None):
    if mx is None: mx=n
    if n==0: yield (); return
    for k in range(min(n,mx),0,-1):
        for r in parts(n-k,k): yield (k,)+r

def lcm_of(l):
    o=1
    for m in l: o=o*m//gcd(o,m)
    return o

def power_p(l,p):
    out=[]
    for m in l:
        if m%p==0: out.extend([m//p]*p)
        else: out.append(m)
    out.sort(reverse=True); return tuple(out)

def perm_sign_mult(k,m):
    # sign of i -> k*i mod m on Z/m (computed by cycle count)
    seen=[False]*m; c=0
    for i in range(m):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=(j*k)%m
    return (m-c)&1

def splits(l):
    # l: even type. A_n-class of <g> splits iff N_S(<g>) subset A_n
    if sum(l)<2: return False   # S_n=A_n for n<=1: nothing to split
    if len(set(l))!=len(l) or any(m%2==0 for m in l): return False   # centralizer has odd element
    o=lcm_of(l)
    ps=[m for m in l if m>1]
    for k in range(2,o):
        if gcd(k,o)!=1: continue
        s=0
        for m in ps: s^=perm_sign_mult(k%m,m) if k%m else 0
        if s: return False      # odd element in the normalizer
    return True

def connected(l):
    if len(l)<=1: return True
    if 1 in l: return False
    vals=sorted(set(l)); par={v:v for v in vals}
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i,a in enumerate(vals):
        for b in vals[i+1:]:
            if gcd(a,b)>1: par[f(a)]=f(b)
    return len({f(v) for v in vals})==1

def run(n):
    P=list(parts(n))
    NS=set(); NA=set()
    for l in P:
        o=lcm_of(l); ev=(n-len(l))%2==0
        for p in set().union(*[primes_of(m) for m in l]) if l else ():
            q=power_p(l,p); NS.add(q)
            if ev: NA.add(q)
    a=b=c=d=0
    for l in P:
        if l not in NS: a+=1
        if (n-len(l))%2: continue
        w=2 if splits(l) else 1
        b+=w
        if l not in NA: c+=w
        if connected(l): d+=w
    return n,a,b,c,d

if __name__=="__main__":
    N=int(sys.argv[1])
    with Pool(8) as pool:
        res=sorted(pool.imap_unordered(run,range(N,-1,-1)))
    for i,name in enumerate(["A218932","A218935","A218949","A218975"]):
        with open(f"/home/claude/reto-oeis/trabajo/{name}/impl2.txt","w") as f:
            for r in res: f.write(f"{r[0]} {r[i+1]}\n")
    print("done")
