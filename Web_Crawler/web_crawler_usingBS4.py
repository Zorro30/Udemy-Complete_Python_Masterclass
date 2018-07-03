from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.wikipedia.org")
bsobject = BeautifulSoup(html.read(),'html.parser') #object of the BS created & html.parser is the type of parser we are using.
print (bsobject.title)