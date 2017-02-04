# Python script to write items to a file

f = open('sample.txt', 'w')
f.write('hello')
f.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
