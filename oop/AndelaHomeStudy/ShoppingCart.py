# HST2 Andela Proctor OOP Lab

class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        item_name = str(item_name)
        if type(quantity) == int or type(price) == int:
            cost = quantity * price
            self.total += cost
            self.items[item_name] = quantity
        else:
            quantity = int(quantity)
            price = int(price)
            cost = quantity * price
            self.total += cost
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        item_name = str(item_name)
        if type(quantity) == int or type(price) == int:
            if item_name in self.items:
                if not quantity < self.items[item_name]:
                    del self.items[item_name]
                else:
                    self.items[item_name] -= quantity
                cost = quantity * price
                self.total -= cost
            else:
                pass
        else:
            pass

    def checkout(self, cash_paid):
        cash_paid = int(cash_paid)
        if not cash_paid > self.total:
            return "Cash paid not enough"
        elif cash_paid > self.total:
            bal = cash_paid - self.total
            return bal
        else:
            return self.total - cash_paid

class Shop(ShoppingCart):
    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100

    def remove_item(self, item_name = '', quantity = '', price = ''):
        if item_name == '' or quantity == ''  or price == '':
            self.quantity -= 1

cart = ShoppingCart()

cart.add_item(123, '200', '100')
print cart.total
print cart.items
cart.remove_item('Mango', 20, 100)
print cart.items
print cart.checkout(10000)

shop = Shop()
print shop.quantity
shop.remove_item()
print shop.quantity
