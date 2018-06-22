from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height =200)
canvas.pack()

newline = canvas.create_line(0,0,100,200)
otherline = canvas.create_line(122,145,9,6, fill = "green")
root.mainloop()