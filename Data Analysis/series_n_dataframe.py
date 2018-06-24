#reindexing series and dataframes

from pandas import Series, DataFrame
obj = Series([100,200,300,400,500], index = ['d','a','b','e','c'])
print (obj)

#reindexing Series
obj = obj.reindex(['a','b','c','d','e'])
print (obj)

#----------------------------------------------------------
data = { 'Name' : ['John','Kevin','Sam'],
         'Age'  : [32,42,54],
         'Salary':[300,400,500] 
        }
frame = DataFrame(data)
print(frame)

#reindexing row of DataFrame

frame = frame.reindex([0,2,1])
print (frame)

#reindexing column of DataFrame

fields = ['Age','Name','Salary'] 
frame =frame.reindex(columns=fields)
print (frame)