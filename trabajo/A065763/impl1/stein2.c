// impl1 for A065763: count Steinhaus matrices of order n (n<=32) with nonzero real determinant.
// Gaussian elimination (fraction-free, rank only) modulo three 31-bit primes.
// Nonzero mod any prime => det != 0. Zero mod all three => det = 0, because
// |det| <= (n-1)^(n/2) < 2^80 < p1*p2*p3 (~2^93) by Hadamard's inequality.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64;
#define DEF(NAME,P) static int NAME(int n, const unsigned char A[32][32]){ \
  u64 M[32][32]; for(int i=0;i<n;i++)for(int j=0;j<n;j++)M[i][j]=A[i][j]; \
  for(int c=0;c<n;c++){ int piv=-1; for(int k=c;k<n;k++) if(M[k][c]){piv=k;break;} \
    if(piv<0) return 0; \
    if(piv!=c) for(int j=c;j<n;j++){u64 t=M[c][j];M[c][j]=M[piv][j];M[piv][j]=t;} \
    u64 pv=M[c][c]; \
    for(int k=c+1;k<n;k++){ u64 f=M[k][c]; if(!f) continue; \
      for(int j=c;j<n;j++){ M[k][j]=(M[k][j]*pv + M[c][j]*(P-f))%P; } } } \
  return 1; }
DEF(ns1,2147483647ULL)
DEF(ns2,2147483629ULL)
DEF(ns3,2147483587ULL)
int main(int argc,char**argv){
  int n=atoi(argv[1]); u64 nth=argc>2?atoll(argv[2]):1, id=argc>3?atoll(argv[3]):0;
  if(n<2||n>32) return 1;
  u64 cnt=0, total=1ULL<<(n-1);
  unsigned char A[32][32];
  for(u64 m=id;m<total;m+=nth){
    for(int j=1;j<n;j++) A[0][j]=(m>>(j-1))&1;
    for(int i=1;i<n;i++)for(int j=i+1;j<n;j++)A[i][j]=A[i-1][j-1]^A[i-1][j];
    for(int i=0;i<n;i++){A[i][i]=0;for(int j=0;j<i;j++)A[i][j]=A[j][i];}
    if(ns1(n,A)||ns2(n,A)||ns3(n,A)) cnt++;
  }
  printf("%llu\n",(unsigned long long)cnt); return 0;
}
