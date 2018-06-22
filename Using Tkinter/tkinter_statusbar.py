from tkinter import *
def function1():
    print ("Menu item clicked!")
root = Tk()

menu_object = Menu(root)
root.config(menu = menu_object)

sub_menu = Menu(menu_object)

menu_object.add_cascade(label ="File", menu = sub_menu)

sub_menu.add_command(label = "Project" , command = function1)
sub_menu.add_command(label = "Save", command = function1)

sub_menu.add_separator()
sub_menu.add_command(label = "Exit", command = function1)

new_menu_object = Menu(menu_object)
menu_object.add_cascade(label = "Edit", menu = new_menu_object)
new_menu_object.add_command(label="Undo", command=function1)

toolbar = Frame(root, bg = "pink" )
insertbutton = Button (toolbar, text = "Insert files", command= function1)
insertbutton.pack(side=LEFT, padx = 2, pady = 3)

printbutton = Button (toolbar, text = "Print" ,command = function1)
printbutton.pack(side = LEFT, padx = 4, pady = 4)

toolbar.pack(side = TOP, fill = X)

status = Label(root , text = "This is the status", bd = 1, relief=SUNKEN, anchor=W)  # bd =border , relief will give a nice look to the label
status.pack(side = BOTTOM, fill = X)

root.mainloop()