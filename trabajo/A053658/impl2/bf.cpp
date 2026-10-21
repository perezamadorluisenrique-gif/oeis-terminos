// bf q n : enumerate all matrices in GL(n,q), q in {3,4}; print sorted set of element orders
#include <bits/stdc++.h>
using namespace std;
int q,n; int ADD[4][4],MUL[4][4],NEG[4],INV[4];
typedef array<unsigned char,16> M;
M mul(const M&a,const M&b){ M c{}; for(int i=0;i<n;i++)for(int j=0;j<n;j++){int s=0;for(int k=0;k<n;k++) s=ADD[s][MUL[a[i*n+k]][b[k*n+j]]]; c[i*n+j]=s;} return c;}
bool invertible(M a){ for(int c=0;c<n;c++){ int p=-1; for(int r=c;r<n;r++) if(a[r*n+c]){p=r;break;} if(p<0) return false;
  for(int j=0;j<n;j++) swap(a[c*n+j],a[p*n+j]); int iv=INV[a[c*n+c]];
  for(int r=c+1;r<n;r++){ int f=a[r*n+c]; if(!f) continue; int m=MUL[f][iv]; for(int j=0;j<n;j++) a[r*n+j]=ADD[a[r*n+j]][NEG[MUL[m][a[c*n+j]]]]; } } return true; }
int main(int argc,char**argv){ q=atoi(argv[1]); n=atoi(argv[2]);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){ if(q==3){ADD[a][b]=(a+b)%3;MUL[a][b]=a*b%3;} else {ADD[a][b]=a^b; // GF(4): 0,1,2=w,3=w+1, w^2=w+1
      int r=0; for(int i=0;i<2;i++) if((b>>i)&1) r^=a<<i; if(r&4) r^=7; MUL[a][b]=r;} }
  for(int a=0;a<q;a++){ for(int b=0;b<q;b++){ if(ADD[a][b]==0) NEG[a]=b; if(MUL[a][b]==1) INV[a]=b; } }
  long long tot=1; for(int i=0;i<n*n;i++) tot*=q;
  set<int> orders; long long cnt=0; M I{}; for(int i=0;i<n;i++) I[i*n+i]=1;
  for(long long x=0;x<tot;x++){ M a{}; long long y=x; for(int i=0;i<n*n;i++){ a[i]=y%q; y/=q; }
    if(!invertible(a)) continue; cnt++; M p=a; int o=1; while(p!=I){ p=mul(p,a); o++; if(o>100000){puts("ERR");return 1;} } orders.insert(o); }
  printf("GL(%d,%d): |G|=%lld distinct orders=%zu :",n,q,cnt,orders.size()); for(int o:orders) printf(" %d",o); puts("");
}
