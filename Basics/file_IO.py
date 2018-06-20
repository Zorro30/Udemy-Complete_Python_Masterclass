#----------------------WRITING------------------------------
file = open('demo1.txt', 'w+')
text = input("Enter what you want to write to the file:")
file.write(text)

file.close()
#----------------------READING--------------------------------
file = open('demo.txt', 'r')

print (file.read())
#print (file.readline())

file.close()

#-----------------------APPEND------------------------------------
file = open('demo1.txt','a')
text = "I will be added to demo.txt instead of deleting previous data."
file.write(text)

file.close()

#-----------------------------------------------------------------
'''
w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  open an existing file in read+write mode
a+  create file if it doesn't exist and open it in append mode
'''