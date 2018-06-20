def mul(a, b):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        print("There is a divide by zero error.")
    finally:
        print ("This will execute no matter of what!")

print(mul(20,0))