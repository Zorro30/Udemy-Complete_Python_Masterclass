numbers = {
    1:"one",
    2:"two",
    3:"three",
    4:"four"
}

#print (1 in numbers)
print (numbers.get(2))
print (numbers.get(5, "Key not found")) #if a key is not present, write that in the second argument.