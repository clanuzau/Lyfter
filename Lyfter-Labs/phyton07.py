"""
Ejercicio # 5 - Python Basic - Clasificador Nivel Gamer
Student: Cesar Lanuza Urbina
"""
def main():
# Request information
    player_name       = ''
    time_playing      = 0
    play_competitive  = ' '

    # I added these validations to ensure that user will enter valid data for the classification, otherwise it will keep asking until it gets valid data.
    while player_name == '':  
        player_name = input('Nombre del jugador : ').strip()
        if player_name == '':
            print(" ")
            print("Debe ingresar un nombre para el jugador")        

    while time_playing <= 0:
        time_input = input('Horas jugando      : ').strip()

        if time_input == '':
            print(" ")
            print("Debe ingresar horas jugando")
        elif not time_input.isdigit():
            print(" ")
            print("Debe ingresar un numero valido")
        else:
            time_playing = int(time_input)

    while play_competitive != 'si' and play_competitive != 'no':
        play_competitive = input('Juegas competitivo (si/no)? : ').strip().lower()
        if play_competitive != 'si' and play_competitive != 'no':
            print(" ")
            print("Debe ingresar Si o No")
    # Process to classify player level
    if time_playing <= 10 and play_competitive == "No":
        print(" ")
        print(f"{player_name} es un jugador Novato ")
    elif time_playing > 10 and time_playing <= 50:
        print(" ")
        print(f"{player_name} es un jugador de Nivel Casual")   
    elif time_playing > 50 and time_playing <= 200:
        print(" ")
        print(f"{player_name} es un jugador nivel Gamer")  
    elif time_playing >= 200 and play_competitive == "Si":
        print(" ")
        print(f"{player_name} es un jugador Nivel Pro")   
    elif time_playing >= 200 and play_competitive == "No":
        print(" ")
        print(f"{player_name} es un jugador Nivel Gamer") 

    
if __name__ == "__main__":
    main()
