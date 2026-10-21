C={}
for l in open("C.txt"):
    k,v=l.split(); C[int(k)]=int(v)
def c(k): return C[k] if k>=0 else 0
def gl(n):
    s=c(n); t=1
    while 2**(t-1)+1<=n: s+=c(n-2**(t-1)-1); t+=1
    return s
def agl(n):
    s=c(n); t=1
    while 2**(t-1)<=n: s+=c(n-2**(t-1)); t+=1
    return s
N=max(C)
open("../impl2.txt","w").write("".join(f"{n} {gl(n)}\n" for n in range(1,min(N,72)+1)))
open("../../A062766/impl2.txt","w").write("".join(f"{n} {agl(n)}\n" for n in range(1,min(N,71)+1)))
for A,f in (("A053651",gl),("A062766",agl)):
    bad=[]
    for l in open(f"../../{A}/conocidos.txt"):
        if l[0]=='#':continue
        n,v=map(int,l.split())
        if f(n)!=v: bad.append((n,v,f(n)))
    print(A,"mismatch",bad)
