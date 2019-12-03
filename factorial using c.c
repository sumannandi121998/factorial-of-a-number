#include <stdio.h>
#include <time.h>
double f(int n) //function for calculating factorial
{
  if (n>=1)
    return n*f(n-1); //using recursion
  else
    return 1;
}
int main()
{
  int n;
  printf("Give the value of a positive integer: ");
  scanf("%d",&n);
  clock_t t;
  if (n<0)
      printf("This is not a positive integer.Give a positive integer");
  else
  {
    t=clock();
    printf("The value of factorial %d is %10e\n",n,f(n)); //the output calling function
    t=clock()-t;
    double time=((double)t)/CLOCKS_PER_SEC; //time for execution
    printf("The time taken for execution is %10e\n",time);
  }
  return 0;
}
