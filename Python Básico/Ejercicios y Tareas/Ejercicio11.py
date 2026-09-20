"""
Ejercicio Phyton Basico - Hotel and Rooms Dictionary
Student: Cesar Lanuza Urbina
"""

def main():

    hotel = {
        "nombre": "Hotel Intercontinental",
        "numero_de_estrellas": 5,
        "habitaciones": [
            {
                "numero": 101,
                "piso": 1,
                "precio_por_noche": 75.00
            },
            {
                "numero": 201,
                "piso": 2,
                "precio_por_noche": 95.00
            },
            {
                "numero": 301,
                "piso": 3,
                "precio_por_noche": 120.00
            }
         ]
    }

    print()
    print(hotel["nombre"], "tiene", hotel["numero_de_estrellas"], "estrellas y las siguientes habitaciones:")
    print()
    for habitacion in hotel["habitaciones"]:
        print(f"  Habitación {habitacion['numero']} - Piso {habitacion['piso']} - ${habitacion['precio_por_noche']}/noche")
    print()

if __name__ == "__main__":
    main()
