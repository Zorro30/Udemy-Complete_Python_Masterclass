import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (a)

#integer indexing on multidimensional array

b = a [[0,1,2],[0,1,0]]
print(b) #this will print element 0 from 0th row, element 1 form 1st row and element 0th from 2nd row


x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print (x)

row = np.array([[0,0],[3,3]])
cols = np.array ([[0,2],[0,2]])
y = x[row,cols]
print (y)

#boolean indexing
print (x[x>5])