"""
Ejercicio Extra - Python Basic - Descuento
Student: Cesar Lanuza Urbina
"""
def main():
# Operations

    product_price  = 0
    product_price  = int(input('Ingrese Precio del Producto: '))     

    if product_price < 100: 
        final_price = product_price - (product_price * 0.02)
        print(" ")
        print(f"El Precio final del producto es : {final_price:.2f}")
    elif product_price >= 100: 
        final_price = product_price - (product_price * 0.10)
        print(" ")
        print(f"El Precio final del producto es : {final_price:.2f}") 
        
if __name__ == "__main__":
    main()