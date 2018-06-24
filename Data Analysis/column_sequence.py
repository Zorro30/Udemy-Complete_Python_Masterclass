from pandas import DataFrame

data = {'Name': ['John','Ricky','Kieron'],
        'Age' : ['25','27','28'],
        'Salary':['3000','5000','7000']
        }

#adding extra column 
new_frame = DataFrame(data, columns = ['Age','Name','Salary','Profile'])
print (new_frame)

#to retrive salary:
print (new_frame['Salary'])

#to retrive value from x axis.
print(new_frame.ix[2])
