#each and every value in a SET should be unique
numbers = {1, 2, 3, 4, 5, 6}

print (5 in numbers)

numbers.add(10)
numbers.remove(2)
print(numbers)

#------------------------------------------------------------
setA = {1, 2, 3, 4, 5}
setB = {5, 6, 7, 8, 9}

print (setA | setB) #perform union of both set
print (setA & setB) #perform intersection of both set

print (setA - setB) #subtraction of set