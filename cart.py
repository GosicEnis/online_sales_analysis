# cart.py

from product import Product


class Cart:
    def __init__(self):
        self.cart_items = []

    # Adding products to the cart
    def add_to_cart(self, product):
        self.cart_items.append(product)

    # Calculating the total value of the basket, the amount to be paid
    def total_cart_value(self):
        return sum(p.price * p.quantity for p in self.cart_items)

    # Display the contents of the basket
    def show_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("\nCart contents:")
            for product in self.cart_items:
                print(f"Product name: {product.name}, Quantity: {product.quantity}, Price: ${product.price:.2f}")
