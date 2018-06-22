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

root.mainloop()