import itertools, math
from math import gcd
def comp(a,b): return tuple(a[i] for i in b)  # a after b: i-> a[b[i]]
def sign(p):
    n=len(p); seen=[0]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=1; j=p[j]
    return (n-c)&1
def cyc_sub(g):
    n=len(g); e=tuple(range(n)); s=[e]; x=g
    while x!=e: s.append(x); x=comp(g,x)
    return frozenset(s)
def cycletype(g):
    n=len(g); seen=[0]*n; t=[]
    for i in range(n):
        if not seen[i]:
            c=0;j=i
            while not seen[j]: seen[j]=1;j=g[j];c+=1
            t.append(c)
    return tuple(sorted(t,reverse=True))
def conn(t):
    if len(t)<=1: return True
    n=len(t); adj=[[gcd(t[i],t[j])>1 for j in range(n)] for i in range(n)]
    seen={0}; st=[0]
    while st:
        i=st.pop()
        for j in range(n):
            if adj[i][j] and j not in seen: seen.add(j); st.append(j)
    return len(seen)==n
def inv(x):
    r=[0]*len(x)
    for i,v in enumerate(x): r[v]=i
    return tuple(r)
def conj(x,H,xi): return frozenset(comp(comp(x,h),xi) for h in H)
def classes(subs,gens):
    subs=set(subs); done=set(); cnt=0
    gi=[(x,inv(x)) for x in gens]
    for H in subs:
        if H in done: continue
        cnt+=1; done.add(H); st=[H]
        while st:
            K=st.pop()
            for x,xi in gi:
                L=conj(x,K,xi)
                if L not in done: done.add(L); st.append(L)
    return cnt
out=open("bruteforce.txt","w")
def P(s): print(s); out.write(s+"\n")
P("# n  A218932 A218935 A218949 A218975  (brute force: subgroups generated as sets, classes by conjugation BFS)")
for n in range(0,9):
    G=list(itertools.permutations(range(n)))
    A=[g for g in G if sign(g)==0]
    e=tuple(range(n))
    gS=[]
    if n>=2: gS=[tuple([1,0]+list(range(2,n))), tuple(list(range(1,n))+[0])]
    gA=[]
    for i in range(2,n): 
        p=list(range(n)); p[0],p[1],p[i]=1,i,0; gA.append(tuple(p))
    subS={}  # subgroup -> generator
    for g in G:
        H=cyc_sub(g)
        if H not in subS: subS[H]=g
    subA={H:g for H,g in subS.items() if sign(g)==0}
    # S_n maximal
    def maxi(subs):
        L=list(subs.items()); res=[]
        for H,g in L:
            if not any(len(K)>len(H) and g in K for K,_ in L): res.append(H)
        return res
    r1=classes(maxi(subS),gS)
    r2=classes(subA.keys(),gA)
    r3=classes(maxi(subA),gA)
    r4=classes([H for H,g in subA.items() if conn(cycletype(g))],gA)
    P(f"{n} {r1} {r2} {r3} {r4}")
