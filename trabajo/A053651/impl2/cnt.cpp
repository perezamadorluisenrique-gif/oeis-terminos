// layers D_k = odd o with c(o)==k ; prints |C_k| cumulative
#include <bits/stdc++.h>
using namespace std;
typedef unsigned __int128 u128;
static u128 gcd128(u128 a,u128 b){ if(!a)return b; if(!b)return a;
  int s=__builtin_ctzll((unsigned long long)a? (unsigned long long)a : 0);
  // odd numbers only: simple binary gcd
  while(b){ while(!(b&1)) b>>=1; if(a>b) swap(a,b); b-=a; }
  return a; }
int main(int argc,char**argv){
  int K=atoi(argv[1]);
  vector<vector<u128>> prim(K+1);
  { FILE*f=fopen("prim.txt","r"); long long d; char buf[64]; while(fscanf(f,"%lld %63s",&d,buf)==2){ u128 e=0; for(char*p=buf;*p;p++) e=e*10+(*p-'0'); if(d<=K) prim[d].push_back(e);} fclose(f);}
  vector<vector<u128>> D(K+1);
  D[0]={1};
  vector<u128> Call={1}; // sorted cumulative C_{k-1}
  printf("0 1\n");
  for(int k=1;k<=K;k++){
    vector<u128> cand;
    for(int d=2;d<=k;d++){
      for(int j=0;j<=k-d;j++){
        for(u128 x:D[j]) for(u128 e:prim[d]){
          u128 g=gcd128(x,e); if(g==e) continue; // e|x
          cand.push_back(x/g*e);
        }
      }
      if(cand.size()>200000000){ sort(cand.begin(),cand.end()); cand.erase(unique(cand.begin(),cand.end()),cand.end()); }
    }
    sort(cand.begin(),cand.end()); cand.erase(unique(cand.begin(),cand.end()),cand.end());
    vector<u128> nw; nw.reserve(cand.size());
    set_difference(cand.begin(),cand.end(),Call.begin(),Call.end(),back_inserter(nw));
    vector<u128>().swap(cand);
    vector<u128> merged; merged.reserve(Call.size()+nw.size());
    merge(Call.begin(),Call.end(),nw.begin(),nw.end(),back_inserter(merged));
    Call.swap(merged); D[k]=move(nw);
    printf("%d %zu\n",k,Call.size()); fflush(stdout);
  }
}
