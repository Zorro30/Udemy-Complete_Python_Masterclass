#Deleting rows and Column in DataFrame

from pandas import DataFrame

data = { 'Name' : ['John','Kevin','Sam'],
         'Age'  : [32,42,54],
         'Salary':[300,400,500] 
        }
frame = DataFrame(data)
print(frame)

# deleting a particular row.
frame_2 = frame.drop([2,1])
print (frame_2)

#deleting a particular row
frame_3 = frame.drop('Salary',axis=1)
print (frame_3)