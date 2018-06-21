import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggsbread"):
    print ("Match found")
else: 
    print ("Sorry")