#Condicionales
#Compatibilidad de Pilotos de Pyger por diferencia de edad
nombre1 = input()
edad1 = int(input())
nombre2 = input()
edad2 = int(input())

if edad1 >= edad2:
    diferencia = edad1 - edad2
else:
    diferencia = edad2 - edad1

if diferencia <= 3:
    print("Excelente compatibilidad.")
elif diferencia > 3 and diferencia <= 5:
    print("Buena compatibilidad.")
elif diferencia > 5 and diferencia <= 10:
    print("Podría funcionar...")
else:
    print("Incompatibles, de ninguna manera podría funcionar.")