from ctypes import*
fact=CDLL('factorial.so')
def f(n):
    a=fact.f(n)
    if (a==-1):
        return "Give another value"
    else:
        return a
n1=input("Give a positive integer")
n=int(n1)
print ("The value of factorial ",n1," is ",f(n))
    