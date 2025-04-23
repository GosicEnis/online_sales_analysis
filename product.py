# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # A method for displaying product information
    def display_info(self):
        return f"Product name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    # Method to update product quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
