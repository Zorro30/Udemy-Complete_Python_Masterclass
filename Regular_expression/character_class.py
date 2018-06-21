import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AZ1"):
    print ("Match found!")
else:
    print ("It didn't match")