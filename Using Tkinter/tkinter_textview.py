from tkinter import *

root = Tk()

label1 = Label(root, text = "Firstname")
label2 = Label(root, text = "Lastname")

textview1 = Entry(root)
textview2 = Entry(root)

label1.grid(row = 0, column =0)
label2.grid(row = 1, column =0)
textview1.grid(row = 0,column = 1)
textview2.grid(row = 1,column = 1)
root.mainloop()