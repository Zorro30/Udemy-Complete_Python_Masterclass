class Students():
    
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info

    def getdata(self):
        print ("Accepting Data.")
        self.name = input ("Enter name:")
        self.contact_info = input ("Enter contact:")

    def putdata(self):
        print ("The Data I have is:")
        print ("Name: "+self.name)
        print ("Contact: "+self.contact_info)

class ScienceStudent(Students):   # <---Real inheritance is here

    def __init__(self, age):
        self.age = age
    
    def science(self):
        print ("I am a Science Student!")

obj = ScienceStudent(20)
obj.science()
obj.getdata()
obj.putdata()