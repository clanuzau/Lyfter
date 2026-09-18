"""
Ejercicio Phyton Basico - Total sales by UPC
Student: Cesar Lanuza Urbina
"""


def main():

    # Define a list of sales (provided) with each sale containing a date, customer email, and a list of items sold
    sales = [
        {
            'date': '27/02/23',
            'customer_email': 'joe@gmail.com',
            'items': [
                {
                    'name': 'Lava Lamp',
                    'upc': 'ITEM-453',
                    'unit_price': 65.76,
                },
                {
                    'name': 'Iron',
                    'upc': 'ITEM-324',
                    'unit_price': 32.45,
                },
                {
                    'name': 'Basketball',
                    'upc': 'ITEM-432',
                    'unit_price': 12.54,
                },
            ],
        },
        {
            'date': '27/02/23',
            'customer_email': 'david@gmail.com',
            'items': [
                {
                    'name': 'Lava Lamp',
                    'upc': 'ITEM-453',
                    'unit_price': 65.76,
                },
                {
                    'name': 'Key Holder',
                    'upc': 'ITEM-23',
                    'unit_price': 5.42,
                },
            ],
        },
        {
            'date': '26/02/23',
            'customer_email': 'amanda@gmail.com',
            'items': [
                {
                    'name': 'Key Holder',
                    'upc': 'ITEM-23',
                    'unit_price': 3.42,
                },
                {
                    'name': 'Basketball',
                    'upc': 'ITEM-432',
                    'unit_price': 17.54,
                },
            ],
        },
    ]

    result = {}

    for sale in sales: # read the sales list
        for item in sale['items']: # read the items list
            upc = item['upc'] # get the upc of the item
            unit_price = item['unit_price'] # get the unit price of the item

            if upc not in result:
                result[upc] = 0

            result[upc] += unit_price # sum the unit price of the item to the total sales by UPC

    print()
    for upc, total_sales in result.items():     # get upc and total sales by UPC
        print(f"{upc}: {total_sales}")          # print the total sales by UPC
    print()
    print()
    print(f"Result = {result}")                 # print the result dictionary
    print()


if __name__ == "__main__":
    main() 
