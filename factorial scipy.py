import scipy as py
import math
import timeit
n1=input("Give the value of a positive integer:")
n=int(n1) #converting the input into integer
if n<0:
    print ("This is not a positive integer.Give a positive integer")
else:
    f=py.math.factorial(n) #factorial using scipy
    print ("The value of factorial ",n1," is ",f)
    print ("The time taken for execution is ",timeit.timeit()) #time for execution
