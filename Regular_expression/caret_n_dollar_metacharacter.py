import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print ("Match 1")
else:
    print ("Sorry it doesn't match.")