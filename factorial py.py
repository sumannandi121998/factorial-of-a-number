from math import*
import timeit
def f(n):
  if n>=1:
    return n*f(n-1);
  else:
    return 1;
m=1
n1=input("Give a positive integer:")
n=int(n1)
if n<0:
    print ("Give another value")
else:
    print ("The value of factorial ",n1," is ",f(n))
    print ("The time taken for execution is ",timeit.timeit())
