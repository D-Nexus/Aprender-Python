#Clacular tu IMC (indice de masa corporal)

p = float(input("Ingrese su peso en kg: "))
m = float(input("Ingrese su altura: "))
imc = p / (m)**2
print("Tu indice de masa corporal es:", imc)

"""  Por debajo de 18.5 ----> Bajo peso
     18.5 - 24.9 ----> Normal
     25.0 - 29.9 ----> Sobrepeso
     30.0 o más ----> Obeso
"""