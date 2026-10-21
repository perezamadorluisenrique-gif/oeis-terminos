#include <bits/stdc++.h>
using namespace std;
// matrix of size s: rows as bitmasks (bit j = column j)
typedef vector<unsigned> M;
int S;
M mul(const M&A,const M&B){ M C(S,0); for(int i=0;i<S;i++){ unsigned r=0; for(int k=0;k<S;k++) if(A[i]>>k&1) r^=B[k]; C[i]=r;} return C;}
int ord(const M&A){ M I(S); for(int i=0;i<S;i++)I[i]=1u<<i; M P=A; int o=1; while(P!=I){P=mul(P,A);o++;} return o;}
int rankm(M A){ int r=0; for(int c=0;c<S;c++){ int p=-1; for(int i=r;i<S;i++) if(A[i]>>c&1){p=i;break;} if(p<0) continue; swap(A[r],A[p]); for(int i=0;i<S;i++) if(i!=r&&(A[i]>>c&1)) A[i]^=A[r]; r++;} return r;}
int main(){
  for(int n=1;n<=5;n++){ S=n; set<int> o; long long cnt=0; for(unsigned long long code=0; code<(1ULL<<(n*n)); code++){ M A(S); for(int i=0;i<n;i++) A[i]=(code>>(i*n))&((1u<<n)-1); if(rankm(A)<n) continue; cnt++; o.insert(ord(A)); }
    printf("GL(%d,2) |G|=%lld distinct=%zu orders:",n,cnt,o.size()); for(int x:o)printf(" %d",x); puts(""); }
  for(int n=1;n<=4;n++){ S=n+1; set<int> o; long long cnt=0; for(unsigned long long code=0; code<(1ULL<<(n*n)); code++){ M A(S); for(int i=0;i<n;i++) A[i]=(code>>(i*n))&((1u<<n)-1); if(rankm(A)<n) {continue;} // A block invertible check: rank of top-left
      // rankm over S dims; handle by building with A[n]=1<<n later
      for(unsigned b=0;b<(1u<<n);b++){ M B(S); for(int i=0;i<n;i++) B[i]=A[i]|((b>>i&1)<<n); B[n]=1u<<n; cnt++; o.insert(ord(B)); } }
    printf("AGL(%d,2) |G|=%lld distinct=%zu orders:",n,cnt,o.size()); for(int x:o)printf(" %d",x); puts(""); }
}
