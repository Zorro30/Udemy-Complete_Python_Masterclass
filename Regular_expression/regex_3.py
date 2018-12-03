import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
#to find the phone numbers
pattern = re.findall(r'\d{3}[./*/-]\d{3}[./*/-]\d{4}', text_to_search)
print(pattern)
#to find the names
pattern = re.findall(r'Mrs?\. [a-zA-z]+' ,text_to_search)
print(pattern)
