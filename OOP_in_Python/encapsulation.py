class MyClass():
    __hiddenVariable = 0  # double underscore used to hide the variable, and hence data hiding is done.

    def add(self,increment):
        self.__hiddenVariable+= increment
        print (self.__hiddenVariable)

object = MyClass()
object.add(5)
print (object.__hiddenVariable) #this won't be printed.
