from pandas import Series

se = Series([1,3,5,7,9])

print (se)    #print the whole series
print (se[2]) #print by index position
se[2]=10      #change the value of index
print (se)

se2 = Series([100, 200, 300], index=['a', 'b', 'c'])
print (se2)
print (se2['b'])