#-------------'.' meta character--------------------------

import re

pattern = r"gr.y"

if re.match(pattern, "gray"):
    print ('Match Found')
else:
    print ("Only '.' character can be different")