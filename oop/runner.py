from Encapsulation import Encapsulation

x = Encapsulation(11,12,13)
x.public # can be accessed outside the class
x._protected = 40
x._protected # is also accesible outside the class



from Account import Account
print Account.counter
a1 = Account("Johnny Fire", 4558445, 1000000)
print Account.counter
