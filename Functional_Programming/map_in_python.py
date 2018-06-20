def add(x):
    return x + 2

new_list = [10, 20, 30 ,40 ,50]

result = list(map(add,new_list))
print (result)

#using lambda

result = list(map(lambda x: x+2,new_list))
print (result)