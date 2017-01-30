from urllib import *

page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

contents = page.read()

page.close()

mess = contents.split("-->" )[1].split("<!--\n")[1]

items = {}

for item in mess:
    if item in items:
        items[item] = items[item] + 1
    else:
        items[item] = 1

for item in items:
    if items[item] == 1:
        print item
        
