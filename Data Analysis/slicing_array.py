import numpy as np

a = np.arange(10)
print (a)

#slicing numpy array

s = slice(2,7,2) #(from,to,step)
print (a[s])

#another way to slice array
b = a[2:7:2]
print (b)

#another way to slice from some point to end
print (a[2:])

#slicing multidimensional array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (a)

#slicing it
print (a[2:])