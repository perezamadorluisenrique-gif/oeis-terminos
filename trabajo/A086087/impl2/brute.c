#include <stdio.h>
#include <string.h>
int m;
int main(int c,char**v){m=v[1][0]-'0';int N=m*m;long tot=1;for(int i=0;i<N;i++)tot*=3;
 static char seen[100000];
 for(long x=0;x<tot;x++){int A[16],t=x;for(int i=0;i<N;i++){A[i]=t%3;t/=3;}
  int B[16];memcpy(B,A,sizeof(int)*N);int ok=1;
  for(int col=0;col<m&&ok;col++){int p=-1;for(int r=col;r<m;r++)if(B[r*m+col]){p=r;break;}
   if(p<0){ok=0;break;}
   if(p!=col)for(int k=0;k<m;k++){int s=B[p*m+k];B[p*m+k]=B[col*m+k];B[col*m+k]=s;}
   int inv=B[col*m+col];/* 1->1,2->2 self inverse */
   for(int r=col+1;r<m;r++){int f=B[r*m+col]*inv%3;if(f)for(int k=0;k<m;k++)B[r*m+k]=((B[r*m+k]-f*B[col*m+k])%3+3)%3;}}
  if(!ok)continue;
  int P[16];memcpy(P,A,sizeof(int)*N);int o=1;
  for(;;){int id=1;for(int i=0;i<m&&id;i++)for(int j=0;j<m;j++)if(P[i*m+j]!=(i==j)){id=0;break;}
   if(id)break;int Q[16];for(int i=0;i<m;i++)for(int j=0;j<m;j++){int s=0;for(int k=0;k<m;k++)s+=P[i*m+k]*A[k*m+j];Q[i*m+j]=s%3;}
   memcpy(P,Q,sizeof(int)*N);o++;}
  seen[o]=1;}
 for(int i=1;i<100000;i++)if(seen[i])printf("%d ",i);printf("\n");}
