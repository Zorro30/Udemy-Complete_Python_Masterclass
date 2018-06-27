class Gaurang():

    def __init__(self,any,one):
        self.any=any
        self.one= one
        print ("I was called")
    
    def call(self):
        print ("I am called!")
        print (self.any)
    
    def notacall(self):
        print("I am also called!")

class patel(Gaurang):

    def __init__(self,any):
        self.any = any

    def also(self):
        print("I am missing")


obj = patel('hello')
obj.also()
obj.call()