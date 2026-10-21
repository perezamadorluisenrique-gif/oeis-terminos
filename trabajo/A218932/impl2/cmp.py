import sys
a=sys.argv[1]
k={}
for l in open(f"/home/claude/reto-oeis/trabajo/{a}/conocidos.txt"):
    if l[0]!='#' and l.strip(): x,y=l.split(); k[int(x)]=y
m={int(l.split()[0]):l.split()[1] for l in open(f"/home/claude/reto-oeis/trabajo/{a}/impl2.txt")}
bad=[(x,y,m.get(x)) for x,y in k.items() if m.get(x)!=y]
print(a,"known",len(k),"mismatch",bad,"max n",max(m))
