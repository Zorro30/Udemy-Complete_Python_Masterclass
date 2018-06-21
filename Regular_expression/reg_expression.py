import re

pattern = r"eggs"

if re.match(pattern,"moreeggs_extremeeggs"): # match looks for the exact start hence it will return No match found here.
    print('Match Found!')
else:
    print ('No match found!')