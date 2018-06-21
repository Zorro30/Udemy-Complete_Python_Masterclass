import re

string = "My name is Khan, and I am not a terrorist"
pattern = r"Khan"

new_string = re.sub(pattern, "Salman", string)
print (new_string)
#================================================
string2 = "10-12-2017"
pattern = r"2017"

newstring = re.sub(pattern, "2018", string2)
print (newstring)