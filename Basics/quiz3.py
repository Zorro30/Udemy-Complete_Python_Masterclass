def divide( a, b):
    try:
        return a/b
    except:
        print ("Please enter non zero values at both places.")
        return 0

a = int(input("Enter first value:"))
b = int(input("Enter second value:"))
print(divide(a,b))