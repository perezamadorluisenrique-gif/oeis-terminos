// usage: cnt q K prim.txt ; prints k |T_k| , T_k={o coprime to p : P(o)<=k}
#include <bits/stdc++.h>
using namespace std;
typedef unsigned __int128 u128;  // safe: o < q^K <= 4^40=2^80 or 3^55<2^88
static inline u128 gcd128(u128 a,u128 b){ if(!a)return b; if(!b)return a;
  int sa=0; { unsigned long long lo=(unsigned long long)a; sa = lo? __builtin_ctzll(lo): 64+__builtin_ctzll((unsigned long long)(a>>64)); }
  int sb=0; { unsigned long long lo=(unsigned long long)b; sb = lo? __builtin_ctzll(lo): 64+__builtin_ctzll((unsigned long long)(b>>64)); }
  int sh=min(sa,sb); a>>=sa; b>>=sb;
  while(a!=b){ if(a>b){a-=b; unsigned long long lo=(unsigned long long)a; a>>= lo? __builtin_ctzll(lo): 64+__builtin_ctzll((unsigned long long)(a>>64));}
    else {b-=a; unsigned long long lo=(unsigned long long)b; b>>= lo? __builtin_ctzll(lo): 64+__builtin_ctzll((unsigned long long)(b>>64));} }
  return a<<sh; }
int main(int argc,char**argv){
  int q=atoi(argv[1]), K=atoi(argv[2]);
  vector<vector<u128>> prim(K+1);
  { FILE*f=fopen(argv[3],"r"); long long d; char buf[64]; while(fscanf(f,"%lld %63s",&d,buf)==2){ u128 e=0; for(char*p=buf;*p;p++) e=e*10+(*p-'0'); if(d<=K) prim[d].push_back(e);} fclose(f);}
  vector<vector<u128>> L(K+1);
  for(int x=1;x<q;x++) if((q-1)%x==0) L[0].push_back(x);   // divisors of q-1 (free, d=1)
  vector<u128> T=L[0];
  printf("0 %zu\n",T.size());
  for(int k=1;k<=K;k++){
    vector<u128> cand;
    for(int d=2;d<=k;d++){
      for(u128 x:L[k-d]) for(u128 e:prim[d]){ u128 g=gcd128(x,e); cand.push_back(x/g*e); }
      if(cand.size()>150000000){ sort(cand.begin(),cand.end()); cand.erase(unique(cand.begin(),cand.end()),cand.end()); }
    }
    sort(cand.begin(),cand.end()); cand.erase(unique(cand.begin(),cand.end()),cand.end());
    vector<u128> nw; set_difference(cand.begin(),cand.end(),T.begin(),T.end(),back_inserter(nw));
    vector<u128>().swap(cand);
    vector<u128> m; m.reserve(T.size()+nw.size()); merge(T.begin(),T.end(),nw.begin(),nw.end(),back_inserter(m));
    T.swap(m); L[k]=move(nw);
    printf("%d %zu\n",k,T.size()); fflush(stdout);
  }
}
