from tkinter import *

class MyButtons():

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.button1 = Button(frame, text = "Click Me!", command = self.printMessage)
        self.button1.pack()

        self.button2 = Button(frame, text = "Click me to Exit!", command = frame.quit)  # inbuilt function to quit
        self.button2.pack (side = LEFT)

    def printMessage(self):
        print ("Button Clicked")

root = Tk()

b = MyButtons(root)

root.mainloop()