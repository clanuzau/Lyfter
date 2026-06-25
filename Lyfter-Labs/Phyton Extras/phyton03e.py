"""
Ejercicio Extra - Python Basic - Tiempo en segundos
Student: Cesar Lanuza Urbina
"""

def main():
    # Variable inizialization
    counter = 0
    addition = '('
    lenght = 0
    total_sum = 0

    mynumber = float(input("Enter number: "))

    while counter < mynumber:
        result = counter + 1
        counter +=1
        total_sum = total_sum + counter
        addition = addition + str(result) + '+'

    addition = addition + ')'

    lenght = len(addition.strip())
    lenght = lenght - 2

    addition = (str(addition[0:lenght])+ ')')

    print(" ")
    print(f"{mynumber:.0f} -> {total_sum} = {addition}")
    print(" ")

if __name__ == "__main__":
    main()
