import scipy as py
import math
import timeit
n1=input("Give a positive integer")
n=int(n1)
if n<0:
    print ("Give another value")
else:
    f=py.math.factorial(n)
    print ("The value of factorial ",n1," is ",f)
    print ("The time taken for execution is ",timeit.timeit())
