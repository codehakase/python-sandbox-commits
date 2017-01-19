class Account(object):
    counter = 0 # will track how many instances of this class.
    def __init__(self, holder, number, balance, credit_line = 1500):
        Account.counter += 1
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line

    def deposit(self, amount):
        self.__Balance = amount

    def withdraw(self, amount):
        if(self.__Balance - amount < -self.__CreditLine):
            # insufficient coverage
            return False
        else:
            self.__Balance -= amount
            return True

    def balance(self):
        return self.__Balance

    def transfer(self, target, amount):
        if(self.__Balance - amount < -self.__CreditLine):
            # insufficient coverage
            return False
        else:
            self.__Balance = amount
            target.__Balance += amount
            return True
    def __del__(self):
        Account.counter -= 1
