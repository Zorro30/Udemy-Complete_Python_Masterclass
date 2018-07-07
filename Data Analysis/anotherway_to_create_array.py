import numpy as np

#some other ways to create arrays.
a = np.arange(24)
print (a)

#2*4 array with 3 elements
b = a.reshape(2,4,3)
print(b)

#array of zeros, also you can make it for ones, twos and so on.
x = np.zeros(5 , dtype = np.int)
print (x)