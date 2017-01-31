# HST2 Andela Proctor OOP Lab
class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if not isinstance(item_name, basestring):
            return False
        elif not isinstance(quantity, int):
            quantity = 0
        elif not isinstance(price, int):
            price = 0
        cost = quantity * price
        self.total += cost
        self.items[item_name] = quantity
        return True

    def remove_item(self, item_name, quantity, price):
        if not isinstance(item_name, basestring):
            return False
        elif not isinstance(quantity, int):
            quantity = 0
        elif not isinstance(price, int):
            price = 0

        if item_name in self.items:
            if  not quantity <= self.items[item_name]:
                 self.items.pop(item_name, None)
            else:
                self.items[item_name] -= quantity
                cost = quantity * price
                self.total -= cost

    def checkout(self, cash_paid):
        if not isinstance(cash_paid, int):
            return False

        if cash_paid < self.total:
            return "Cash paid not enough"
        elif  cash_paid >= self.total:
            bal = cash_paid - self.total
            return bal
        else:
            return self.total - cash_paid

class Shop(ShoppingCart):
    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100

    def remove_item(self, item_name = None, quantity = None, price = None):
        if not item_name or not quantity or not price:
            self.quantity -= 1

cart = ShoppingCart()

cart.add_item('Mango', '20', 100)
print cart.total
print cart.items
