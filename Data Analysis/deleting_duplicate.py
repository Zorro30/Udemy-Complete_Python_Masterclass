from pandas import Series
series = Series([100,200,300], index= ['a','b','b'])
print (series)
print (series.index.is_unique) #this helps to identify if there is an unique index value.
#False means duplicate index is present
#True means no duplicate index.