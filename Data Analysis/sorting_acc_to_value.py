from pandas import Series,DataFrame

series_2 = Series([3,7,8,5,6,2],index=[2,3,5,6,7,1])

print (series_2.sort_values())

#sorting dataframe by value
data_2 = {'Speed' : [200,300,400],
          'Temp'  : [35,37,39],
          'Humidity': [48,63,45]}          
frame_2 = DataFrame(data_2)

print (frame_2.sort_values(by='Humidity'))