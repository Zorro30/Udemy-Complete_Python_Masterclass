#data can be loaded from excel, cxv, json files

import pandas 

data_frame = pandas.read_csv("sample.csv")

#print (data_frame)

#----json file

data_frame = pandas.read_json("sample.json",lines= True)

#print (data_frame)

#-----excel file

data_frame = pandas.read_excel("sample.xlsx")

print (data_frame)