def square(x):
    return x**x

print (square(4))

result = (lambda x: x**2) (30)
print (result)

print ((lambda x: x**2) (30)) #more efficient way