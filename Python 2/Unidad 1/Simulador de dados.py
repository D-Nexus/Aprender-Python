

"Importar libreria"
import random

"Programación"

iniciar_lanzamiento = True

while iniciar_lanzamiento == True:

    "variables"
    resultado1 = random.randint(1,6)
    resultado2 = random.randint(1,6)
    sumaDados = resultado1 + resultado2

    input("\nPresione enter para lanzar los dados: ")

    print("Primer dado:",resultado1)
    print("Segundo dado:",resultado2)
    print("La suma de los dados es:", sumaDados)
    print("\n¿Deseas intentar lanzar los dados denuevo?")

    repetir_lanzamiento  = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

    if repetir_lanzamiento != "si":
        print("\nFin del programa")
        iniciar_lanzamiento = False






