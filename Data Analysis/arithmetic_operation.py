#addtion between two series

from pandas import Series, DataFrame

#Adding two Series
series_1 = Series([1,2,3,4,5])
series_2 = Series([100,200,300,400,500,600]) # if one series exceeds value more than other it will show NaN
print (series_1 + series_2)

#Adding two DataFrames
data_1 = {'Speed': [100,200,300],
          'Temp' : [34,35,37]}
frame_1 = DataFrame(data_1)
print (frame_1)

data_2 = {'Speed' : [200,300,400],
          'Temp'  : [35,37,39],
          'Humidity': [42,43,45]}
frame_2 = DataFrame(data_2)

print (frame_1 + frame_2)