from pandas import DataFrame

data = {'Name'  : ['Tim', 'Jhonty', 'Ricky'],
        'Age'   : [34,23,42],
        'Salary': [3000,5000,7000]
        }

frame = DataFrame (data)
print (frame)
