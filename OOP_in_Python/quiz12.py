""" Question:
Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
You can use any specifications which you want.
The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
Make sure that the sub classes have their own methods to get and display their special specification.
Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class."""
class Computer():

    def __init__(self,ram):
        self.ram = ram

    def getspecs(self):
        self.ram = input ("Enter ram detail:")

    def displayspec(self):
        print ("Ram is: "+self.ram)

class Desktop(Computer):
    
    def __init__(self, casecolor):
        self.casecolor= casecolor

    def get_case_details(self):
        self.casecolor = input ("Enter the color of the case:")

    def put_case_deta(self):
        print ("case color is: "+sel.casecolor)

class Laptop(Computer):

    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input("Enter weight:")

    def put_weight(self):
        print ("Weight is: "+self.weight) 

comp = Laptop(Computer)
comp.getspecs()
comp.displayspec()
comp.get_weight()
comp.put_weight()