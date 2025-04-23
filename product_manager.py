# product_manager.py

from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    # Adding products
    def add_product(self, product):
        self.products.append(product)

    # View all products
    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    # Display the total value of all products
    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)
