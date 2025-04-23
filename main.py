# main.py

from product import Product
from product_manager import ProductManager


# Create a ProductManager instance and add a few arbitrary products;
manager = ProductManager()
manager.add_product(Product("Laptop", 1000, 4))
manager.add_product(Product("Mouse", 25.50, 10))
manager.add_product(Product("Keyboard", 50.45, 8))
manager.add_product(Product("Monitor", 150, 5))

# Display of products and total inventory value
# manager.display_all_products()
# print(f"\nTotal inventory value: {manager.total_value()}")
