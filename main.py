# main.py

from product import Product
from product_manager import ProductManager
from cart import Cart
import random


# Create a ProductManager instance and add a few arbitrary products;
manager = ProductManager()
manager.add_product(Product("Laptop", 1000, 3))
manager.add_product(Product("Mouse", 25.50, 10))
manager.add_product(Product("Keyboard", 50.45, 8))
manager.add_product(Product("Monitor", 150, 4))

# Display of products and total inventory value
# manager.display_all_products()
# print(f"\nTotal inventory value: ${manager.total_value():.2f}")

# Add three randomly selected products from the list of available
# products of the ProductManager instance to the cart.
cart = Cart()
cart_items = random.sample(manager.products, 3)
for item in cart_items:
    cart.add_to_cart(item)

# Print the total value for charging the contents of the basket
cart.show_cart()
print(f"\nTotal cart value: ${cart.total_cart_value():.2f}")
