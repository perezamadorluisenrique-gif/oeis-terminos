import sys
q,K,cf,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4]
T={}
for l in open(cf):
    k,s=l.split(); T[int(k)]=int(s)
p=2 if q==4 else 3
res=[]
for n in range(1,K+1):
    tot=T[n]; t=1
    while p**(t-1)+1<=n: tot+=T[n-p**(t-1)-1]; t+=1
    res.append(f"{n} {tot}")
open(out,"w").write("\n".join(res)+"\n")
