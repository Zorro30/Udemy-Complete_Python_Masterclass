from pandas import Series

salary = {'John' : 3000, 'Tim' : 5000, 'Rob' : 7000}
#print (salary) 

#input the dictionary to the Series() to convert Dict to Series.
se3 = Series(salary)  
print (se3)