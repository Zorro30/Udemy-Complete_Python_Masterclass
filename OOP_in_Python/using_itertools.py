from itertools import count, accumulate, takewhile

for i in count(3,2):
    print (i)

    if i >= 20:
        break

#==================Accumulate===================================

numbers = list(accumulate(range(8)))
print(numbers)

#====================Takewhile=================================

print (list(takewhile(lambda x: x <=10, numbers)))