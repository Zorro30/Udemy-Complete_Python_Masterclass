import re

pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbaconbacon"):
    print ("Match found!")
else: 
    print("Does not match!")