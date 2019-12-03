from math import*
import timeit
def f(n): #function for calculating factorial
  if n>=1:
    return n*f(n-1); #using recursion
  else:
    return 1;
m=1
n1=input("Give the value of a positive integer:")
n=int(n1) #converting the input into integer
if n<0:
    print ("This is not a positive integer.Give a positive integer")
else:
    print ("The value of factorial ",n1," is ",f(n)) #the output by calling function
    print ("The time taken for execution is ",timeit.timeit()) #time for execution
