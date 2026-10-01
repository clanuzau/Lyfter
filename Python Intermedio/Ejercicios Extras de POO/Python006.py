"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio -  Product and Inventory classes to manage products and calculate inventory value.
"""

# Define a Product class to store product information.
class Product:
    """Store a product's name, unit price, and quantity."""

    def __init__(self, name, price, quantity):
        """Initialize the product information."""
        self.name = name
        self.price = price
        self.quantity = quantity


# Define an Inventory class to manage a collection of products and calculate their total value.
class Inventory:
    """Store products in a list and calculate their combined value."""

    def __init__(self):
        """Create an empty list for this inventory's products."""
        self.products = []

    def add_product(self, product):
        """Add a product to the inventory."""
        self.products.append(product)

    # Define a method to display the products in the inventory.
    def show_products(self):
        """Display the name, unit price, and quantity of each product."""
        if not self.products:
            print("El inventario no tiene productos.")
            return

        # Iterate over the stored products to display their information.
        print()
        for product in self.products:
            print(
                f"Nombre: {product.name}    | Precio: {product.price:g}    | "
                f"Cantidad: {product.quantity}"
            )

    # Define a method to calculate the total value of the inventory.
    def calculate_total_value_of_inventory(self):
        """Return the sum of each product's price multiplied by its quantity."""
        return sum(product.price * product.quantity for product in self.products)


if __name__ == "__main__":
    # Create the example products and store them in the inventory.
    product1 = Product("  Mouse",  5000 , 3)
    product2 = Product("Teclado",  8000 , 2)
    product3 = Product("Monitor",  9825 , 5)
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # Display all products and the total value of the inventory.
    inventory.show_products() 
    print()
    print(f"Valor total del inventario: {inventory.calculate_total_value_of_inventory():g}") 
    print()
