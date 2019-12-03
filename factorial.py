from ctypes import*
fact=CDLL('factorial.so') #so file
def f(n):
    a=fact.f(n)
    if (a==-1):
        return "This is not a positive integer.Give a positive integer"
    else:
        return a
n1=input("Give the value of a positive integer:")
n=int(n1) #converting input to a integer
print ("The value of factorial ",n1," is ",f(n))
    
