import re

pattern = r"eggs"

if re.match(pattern,"moreeggs_extremeeggs"):
    print('Match Found!')
else:
    print ('No match found!')
#================================================
if re.search(pattern, "moreeggs_extremeeggs"):
    print('Match Found!')
else:
    print ('No match found!')
#================================================
if re.findall(pattern, "moreeggs_extremeeggs"):
    print('Match Found!')
else:
    print ('No match found!')
#================================================
print (re.findall(pattern, "moreeggs_extremeeggs"))