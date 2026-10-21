"""A053773: #{X in M_n(GF(2)) : X^8 = I}.
Derivation: over GF(2), X^8-1=(X-1)^8, so X^8=I <=> N=X-I satisfies N^8=0 (X->X+I bijection).
So a(n)=#{N in M_n(F_q): N^8=0}, q=2.  Count by kernel dimension d with a recursion on the image:
 g_k(n,d) = #{N on F_q^n : N^k=0, dim ker N = d}.
 N has image W of dim r=n-d. N^k=0 <=> M=N|_W satisfies M^(k-1)=0 (W is N-stable).
 Given W (Gaussian binomial [n,r] choices) and M=N|_W with dim ker M = c, the rest of N is a map
 E: V/W (dim d) -> W, and N surjects onto W iff M(W)+E(V/W)=W iff E composed with W->W/M(W) (dim c)
 is onto: #(surjections F^d->F^c) * q^{d(r-c)} choices.  Hence
 g_k(n,d)=[n,n-d]_q * sum_c g_{k-1}(n-d,c) * prod_{i<c}(q^d-q^i) * q^{d(n-d-c)},
 g_0(0,0)=1.  a(n)=sum_d g_8(n,d).  (Nilpotency of N follows from M nilpotent.)
Also brute force for n<=4."""
from functools import lru_cache
q=2
def gb(n,k):
    if k<0 or k>n: return 0
    num=den=1
    for i in range(k):
        num*=q**(n-i)-1; den*=q**(i+1)-1
    return num//den
def surj(d,c):
    r=1
    for i in range(c): r*=q**d-q**i
    return r
@lru_cache(None)
def g(k,n,d):
    if k==0: return 1 if (n==0 and d==0) else 0
    if d<0 or d>n: return 0
    r=n-d
    return gb(n,r)*sum(g(k-1,r,c)*surj(d,c)*q**(d*(r-c)) for c in range(0,r+1)) if r>0 or True else 0
def a(n,k=8): return sum(g(k,n,d) for d in range(n+1))
def brute(n):
    cnt=0
    full=(1<<n)-1
    def mul(A,B): # rows as bitmasks: (AB) row i = xor of B rows j where A[i] bit j
        out=[]
        for r in A:
            v=0;j=0
            while r:
                if r&1: v^=B[j]
                r>>=1;j+=1
            out.append(v)
        return out
    I=[1<<i for i in range(n)]
    for m in range(1<<(n*n)):
        X=[(m>>(n*i))&full for i in range(n)]
        for _ in range(3): X=mul(X,X)
        if X==I: cnt+=1
    return cnt
known=[1,1,4,64,4096,1048576,1073741824,4398046511104,72057594037927936,1989505896802466922496,164384949539438492410445824,47902612878717208996830483841024]
if __name__=="__main__":
    for n in range(5): assert brute(n)==a(n),(n,brute(n),a(n))
    print("brute force n<=4 OK")
    for n,v in enumerate(known): assert a(n)==v,n
    print("known terms n=0..11 OK")
    with open("impl2.txt","w") as f:
        for n in range(41): f.write(f"{n} {a(n)}\n")
    print(a(12),a(13))
