"""Question: Using the concept of operator overloading in Python, change the behavior of the multiplication operator in a way that 
   multiplication operator behaves like an addition operator."""
class quiz():

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = (self.x + other.x)
        return x

obj1= quiz(4)
obj2= quiz(5)
print (obj1* obj2)