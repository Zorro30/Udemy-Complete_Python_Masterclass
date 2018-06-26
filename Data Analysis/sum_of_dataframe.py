from pandas import DataFrame

data = {'Speed' : [101,109,106],
        'Temp'  : [34,32,45],
        'Humidity' : [4500,2300,5800]}
frame = DataFrame(data)
print (frame)

print(frame.sum()) #to calculate sum of all columns

print (frame.sum(axis=1))# to calculate sum of rows

print (frame.idxmax())# to calculate max value at particular index value.

print (frame.idxmin())