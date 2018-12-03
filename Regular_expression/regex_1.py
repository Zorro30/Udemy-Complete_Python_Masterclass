import re

myString = 'Send an email from 10-12-2018  or 11/12/2018 this@email.com to test@user.com 34 times'

#both below statement yield same output, i.e. date
result = re.findall(r'\d{2}[-/]\d{2}[-/]\d{2,4}',myString)
result = re.findall(r'[0-9]{2}[-/][0-9]{2}[-/][0-9]{2,4}',myString)
print(result)

#to get the email address
result = re.findall(r'\S+@\S+',myString)
print(result)