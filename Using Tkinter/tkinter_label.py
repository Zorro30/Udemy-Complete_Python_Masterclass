from tkinter import *

root = Tk()

label1 = Label(root, text = "First", bg= "Blue", fg= "White")
label1.pack(fill = X) #adjust label to the width of the window.

label2 = Label(root, text="Second", bg = "Red" ,fg = "White")
label2.pack(side = LEFT, fill = Y)
root.mainloop()