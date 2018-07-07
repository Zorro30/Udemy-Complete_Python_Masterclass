#Broadcasting refers to the ability of numpy to treat arrays of different shapes doing arithmetic operations.

import numpy as np

#multiplication when two arrays have same dimension
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b

print (c)

#Broadcasting comes into picture when dimensions of two arrays are different

a = np.array ([[1,2,3],[4,5,6],[7,8,9]])
b = np.array ([1,2,3])

#broadcasting expands the smaller array, hence here b becomes [1,2,3],[1,2,3],[1,2,3]
print (a+b)