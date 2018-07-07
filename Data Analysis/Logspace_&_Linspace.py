import numpy as np

#this will divide 10 to 50 in 5 numbers
x = np.linspace(10,50,5)
print (x)

#this won't consider the endpoint i.e. 50 here.
x = np.linspace(10,50,5, endpoint=False)
print (x)

#this will print value of 10 to 100 in equal logarithmic space
a = np.logspace(1.0,2.0,num=10)
print (a)

#this will print the same as above but with base=2
a = np.logspace(1.0,2.0,num=10,base=2)
print (a)