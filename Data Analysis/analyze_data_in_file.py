import pandas
from pandas import DataFrame

#load data from a file.
data_frame = pandas.read_csv("sample.csv")
#this will only show the columns asked in the next line
data_frame = DataFrame(data_frame, columns=['Firstname ','Lastname','Username ','Password '])
print (data_frame)

#drop a particular row from the table
data_frame = data_frame.drop([1])
print (data_frame) #row 1 is dropped.

#drop a column
data_frame = data_frame.drop('Password ',axis=1)
print(data_frame) #here password column is removed

#performing arithmetic operation on dataframe
data_frame = data_frame.sort_values(by='Username ')
print(data_frame)

