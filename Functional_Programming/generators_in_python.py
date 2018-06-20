def function():
    count = 0
    while count < 5:
        yield count
        count += 1

for x in function():
    print (x)

# generator to create list of even numbers--------

def even_numbers(x):

    for i in range(x):
        if i % 2 == 0:
            yield i

print (list(even_numbers(10)))