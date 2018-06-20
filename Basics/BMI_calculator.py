def bmi():
        
    body = int(input("Please enter your bodyweight:"))
    height = float(input("Please enter your height in meters:"))
    return body/height**2

print(bmi())

