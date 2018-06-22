from tkinter  import *

root = Tk()

newframe = Frame(root) # Frame creation
newframe.pack() # packing the frame created 

otherframe = Frame(root)
otherframe.pack(side = BOTTOM)

button1 = Button(newframe, text = "Click here!" ,fg = "Red") # Button creation
button1.pack() # Packing the button created.

button2 = Button(otherframe, text = "Click here!" ,fg = "Blue")
button2.pack()

root.mainloop() 