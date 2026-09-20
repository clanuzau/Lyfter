"""
Ejercicio Phyton Basico - Total sales by category
Student: Cesar Lanuza Urbina
"""


def main():

    total_by_category = {}

    products = [
        {"name": "Monitor", "category": "Electrónica", "price": 200},
        {"name": "Teclado", "category": "Electrónica", "price": 50},
        {"name": "Silla", "category": "Muebles", "price": 120},
        {"name": "Mesa", "category": "Muebles", "price": 180},
        {"name": "Mouse", "category": "Electrónica", "price": 25},
        {"name": "Lámpara", "category": "Muebles", "price": 80},
        {"name": "Cámara", "category": "Electrónica", "price": 300},
        {"name": "Estantería", "category": "Muebles", "price": 150},
        {"name": "Auriculares", "category": "Electrónica", "price": 75},
        {"name": "Anillos", "category": "Joyería", "price": 475},   
        {"name": "Collares", "category": "Joyería", "price": 350},

    ]

    # Get the total sales by category using a dictionary
    for product in products:
        category = product["category"]
        price = product["price"]

        if category not in total_by_category:
            total_by_category[category] = 0

        total_by_category[category] += price

    print()
    print("Total sales by category:")
    print()

    # Print each category and its accumulated total from the dictionary
    for category in total_by_category.keys():
        print(f"{category}: {total_by_category[category]}")

    print()
    print("Result dictionary:")
    print()
    print(total_by_category)
    print()


if __name__ == "__main__":
    main()

