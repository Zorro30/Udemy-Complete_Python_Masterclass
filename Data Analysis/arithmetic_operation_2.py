from pandas import Series, DataFrame

series_2 = Series([100,200,300],index=['Speed','Temp','Humidity'])
print (series_2)

data_2 = {'Speed' : [200,300,400],
          'Temp'  : [35,37,39],
          'Humidity': [42,43,45]}
frame_2 = DataFrame(data_2)

print (frame_2 - series_2)