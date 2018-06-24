from pandas import Series, DataFrame

#sorting a series
series_2 = Series([3,7,8,5,6,2],index=[2,3,5,6,7,1])
print(series_2.sort_index())

#sorting a dataframe
data_2 = {'Speed' : [200,300,400],
          'Temp'  : [35,37,39],
          'Humidity': [42,43,45]}          
frame_2 = DataFrame(data_2)
frame_2 =frame_2.reindex([2,1,0]) #shuffled the dataframe cz its always sorted.

print(frame_2.sort_index())

#sorting the column of dataframe.
frame_2 = frame_2.reindex(columns=['Speed','Humidity','Temp'])

print(frame_2.sort_index(axis=1,ascending = False))