#Codigo para calcular tu edad cuando se realizen los juegos olimpicos
#Entrada Variables
edad = int(input("Ingrese su edad: "))
j_olimpicos = int(input("Ingresar el año de los juegos olimpicos: "))
año_actual = int(input("Ingrese el año actual: "))
#Calculo matematico
diferencia = (j_olimpicos - año_actual)
edad = (edad + diferencia)
#Imprimir edad
print("Su edad sera:",edad,"en el año",j_olimpicos)