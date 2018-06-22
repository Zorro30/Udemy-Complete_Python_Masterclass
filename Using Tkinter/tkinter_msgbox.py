from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Error", "This is awesome!")

response = tkinter.messagebox.askquestion("Question1", "Do you like cricket:")

if response == 'yes':
    print ("Okay that's good!")
else:
    print ("You are junk!")
root.mainloop()