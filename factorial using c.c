#include <stdio.h>
#include <time.h>
double f(int n)
{
  if (n>=1)
    return n*f(n-1);
  else
    return 1;
}
int main()
{
  int n;
  printf("Give a positive integer: ");
  scanf("%d",&n);
  clock_t t;
  if (n<0)
      printf("Give a positive integer");
  else
    t=clock();
    printf("The value of factorial %d is %10e\n",n,f(n));
    t=clock()-t;
    double time=((double)t)/CLOCKS_PER_SEC;
    printf("The time taken for execution is %10e\n",time);
  return 0;
}
