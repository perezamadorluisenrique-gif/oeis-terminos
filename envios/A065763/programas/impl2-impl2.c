/* A065763: count Steinhaus matrices of order n with det != 0 over the reals.
 * RIGOR: det is an integer. Hadamard: |det| <= prod ||row_i|| <= (n-1)^(n/2)
 * (rows are 0/1 with zero diagonal, so each row norm <= sqrt(n-1)).
 * For each matrix we test det mod p (Gaussian elimination over GF(p), division-free:
 * rank deficiency mod p <=> p | det). If det != 0 mod some prime p, det != 0 exactly.
 * If det == 0 mod ALL of primes p1..pk with p1*...*pk > 2*(n-1)^(n/2) (checked at
 * startup with long double, margin huge; primes verified by trial division), then
 * p1..pk | det and |det| < product, so det = 0 exactly (CRT / divisibility by the
 * product of coprime primes). Hence classification is exact; no probabilistic step.
 * Usage: ./impl2 n part nparts   (processes the part-th slice of the 2^(n-1) first rows)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64;
static const u64 PR[3] = {2147483647ULL, 2147483629ULL, 2147483587ULL};
#define MAXN 32
static inline __attribute__((always_inline)) int nonsing(const unsigned char *A, int n, u64 p){
  u64 M[MAXN][MAXN];
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)M[i][j]=A[i*MAXN+j];
  for(int c=0;c<n;c++){
    int r=c; while(r<n && M[r][c]==0) r++;
    if(r==n) return 0;
    if(r!=c) for(int j=c;j<n;j++){u64 t=M[c][j];M[c][j]=M[r][j];M[r][j]=t;}
    u64 piv=M[c][c];
    for(int i=c+1;i<n;i++){
      u64 f=M[i][c]; if(!f) continue;
      u64 g=p-f;
      for(int j=c;j<n;j++) M[i][j]=(M[i][j]*piv+g*M[c][j])%p;
    }
  }
  return 1;
}
static int isprime(u64 x){ if(x<2)return 0; for(u64 d=2;d*d<=x;d++) if(x%d==0) return 0; return 1; }
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage: n part nparts\n");return 1;}
  int n=atoi(argv[1]), part=atoi(argv[2]), np=atoi(argv[3]);
  for(int i=0;i<3;i++) if(!isprime(PR[i])){fprintf(stderr,"bad prime\n");return 1;}
  long double lb = 1.0L + 0.5L*n*log2l((long double)(n-1)); /* log2(2*(n-1)^(n/2)) */
  long double lp = 0; int k=0; while(k<3 && lp<=lb+1){ lp+=log2l((long double)PR[k]); k++; }
  if(lp<=lb+1){fprintf(stderr,"not enough primes\n");return 1;}
  u64 total=1ULL<<(n-1);
  u64 lo=total/np*part, hi=(part==np-1)?total:total/np*(part+1);
  u64 cnt=0;
  static unsigned char A[MAXN*MAXN];
  for(u64 r=lo;r<hi;r++){
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)A[i*MAXN+j]=0;
    for(int j=1;j<n;j++)A[j]=(r>>(j-1))&1;
    for(int i=1;i<n;i++)for(int j=i+1;j<n;j++)A[i*MAXN+j]=A[(i-1)*MAXN+j-1]^A[(i-1)*MAXN+j];
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)A[j*MAXN+i]=A[i*MAXN+j];
    int nz = nonsing(A,n,2147483647ULL);
    if(!nz && k>1) nz = nonsing(A,n,2147483629ULL);
    if(!nz && k>2) nz = nonsing(A,n,2147483587ULL);
    cnt+=nz;
  }
  printf("%d %d %d %llu\n",n,part,np,(unsigned long long)cnt);
  return 0;
}
