class InvalidPrice(Exception):
    pass

class Product:
    def __init__(self,name,price):
        if price<=0:
            raise InvalidPrice("Price of product is equal or below to zero")
        self.name = name
        self.price = price
    
    def __str__(self):
        print(f"{self.name} {self.price}")


class Cart:
    def __init__(self):
        self.item = []
        
    def addProduct(self,product):
        self.item.append(product)
    def __add__(self,otherCart):
        newCart = Cart()
        newCart.item = self.item + otherCart.item
        return newCart
    
    def total(self):
        return sum(i.price for i in self.item)
   
try:
    c1 = Cart()
    c1.addProduct(Product("Apple",1))
    c2 = Cart()
    c2.addProduct(Product("Banana",2))
    c3 = c1+c2
    print(f"Total amount {c3.total()}")
except InvalidPrice as iv:
    print(f"Error: {iv}")