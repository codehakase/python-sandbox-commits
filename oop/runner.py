from Encapsulation import Encapsulation

x = Encapsulation(11,12,13)
print x.public # can be accessed outside the class
x._protected = 40
print x._protected # is also accesible outside the class

print x.__private # will return a Traceback error, because it is a private object
