#include <bits/stdc++.h>
using namespace std;
int n;
typedef unsigned long long u64;
static inline u64 mul(u64 a,u64 b){ // rows packed n bits each
  u64 r=0; u64 m=(1ULL<<n)-1;
  for(int i=0;i<n;i++){ u64 row=(a>>(i*n))&m, acc=0;
    for(int j=0;j<n;j++) if(row>>j&1) acc^=(b>>(j*n))&m;
    r|=acc<<(i*n);} return r;}
int main(){
  for(n=1;n<=5;n++){
    u64 tot=1ULL<<(n*n); u64 I=0; for(int i=0;i<n;i++) I|=1ULL<<(i*n+i);
    vector<bool> sq(tot,false); u64 nun=0, cnt=0;
    for(u64 a=0;a<tot;a++){
      u64 N=a^I, P=N; for(int k=1;k<n;k++) P=mul(P,N);
      if(P==0){ nun++; u64 s=mul(a,a); if(!sq[s]){sq[s]=true;cnt++;} }
    }
    printf("%d unipotent=%llu squares_of_unipotent=%llu\n",n,nun,cnt);
  }
}
