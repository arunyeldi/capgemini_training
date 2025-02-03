class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def ckeck_availability(self, quantity):
        if quantity <= self.stock:
            return True
        else:
            return False

name_of_the_product = input("Enter the product name: ")
price_of_the_product = int(input("Enter the price of the product: "))
stock_available = int(input("Enter the sock availability: "))
product = Product(name_of_the_product, price_of_the_product, stock_available)
quantity = int(input("Enter the product quantity: "))
if product.ckeck_availability(quantity):
    print("Product available for the requested quantity")
else:
    print("Product is not available for the requested quantity")