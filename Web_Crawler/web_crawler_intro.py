from urllib.request import urlopen

html = urlopen("http://www.wikipedia.org") #whatever urlopen returns is stored in html

print (html.read())