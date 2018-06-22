#On Click listener

from tkinter import *

root = Tk()

def doSomething():
    print ("Button is been clicked!")

button1 = Button(root, text = "Click here!", command = doSomething)
button1.pack()

root.mainloop()