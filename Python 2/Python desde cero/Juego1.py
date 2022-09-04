#Juego de piedra-papel-tijeras
#Librerias
from random import randint

opcion = ["piedra","papel","tijeras"]

score_player = 0
score_computer = 0
estado = True

while estado:
    print("### Juego piedra-papel-tijeras ###")
    player = input("Tu opcion: ").lower()
    computer = opcion[randint(0,2)]
    
    if player == computer:
        print("Tu rival:",computer)
        print("Resultado: Empate\n")
    elif player == "piedra" and computer == "papel":
        print("Tu rival:",computer)
        print("Ganador: Computador\n")
        score_computer += 1
    elif player == "piedra" and computer == "tijeras":
        print("Tu rival:",computer)
        print("Ganador: Jugador\n")
        score_player += 1
    elif player == "papel" and computer == "tijeras":
        print("Tu rival:",computer)
        print("Ganador: Computador\n")
        score_computer += 1
    elif player == "papel" and computer == "piedra":
        print("Tu rival:",computer)
        print("Ganador: Jugador\n")
        score_player += 1
    elif player == "tijeras" and computer == "piedra":
        print("Tu rival:",computer)
        print("Ganador: Computador\n")
        score_computer += 1
    elif player == "tijeras" and computer == "papel":
        print("Tu rival:",computer)
        print("Ganador: Jugador\n")
        score_player += 1
    elif player == "fin":
        print("\n")
        print("## Fin del juego ##")
        print("You score:",score_player)
        print("You score:",score_computer)
        estado = False
    else:
        print("Entrada invalida\n")


