import pandas
from pandas import DataFrame

data_frame = pandas.read_csv("sample.csv")
#this will only show the columns asked in the next line
data_frame = DataFrame(data_frame, columns=['Firstname ','Lastname','Username ','Password '])
print (data_frame)