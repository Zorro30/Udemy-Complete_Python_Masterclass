#filtering missing data.
import numpy as np
from pandas import Series,DataFrame

ser = Series([1,2,3,4,np.nan], index=['a','b','c','d','e'])
print(ser)

print(ser.dropna())
print (ser)
ser = ser.dropna()
print (ser)

data = {'Speed' : [101,109,106],
        'Temp'  : [34,np.nan,45],
        'Humidity' : [4500,2300,5800]}
frame = DataFrame(data)

print(frame)
#print (frame.dropna())

#we can also fill someother value in place of NAN

print (frame.fillna(0))