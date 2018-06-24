from pandas import DataFrame

data = {'Name': ['John','Ricky','Kieron'],
        'Age' : ['25','27','28'],
        'Salary':['3000','5000','7000']
        }

#adding new column
new_frame = DataFrame(data, columns = ['Age','Name','Salary','Profile'])
print (new_frame)

#adding value to Profile column
new_frame ['Profile'] = 'Doctor'
print (new_frame)

#adding new column and value
new_frame ['Education'] = 'MS'
print (new_frame)

#Transposing a DataFrame
new_frame = new_frame.T
print (new_frame)

#making everything same like before
new_frame = new_frame.T
print (new_frame)