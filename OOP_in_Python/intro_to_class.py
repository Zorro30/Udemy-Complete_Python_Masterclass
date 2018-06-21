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
    
obj = Students("Gaurang", 0)

obj.getdata()
obj.putdata()