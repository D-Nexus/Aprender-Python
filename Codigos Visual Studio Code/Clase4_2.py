#Ejercicio 2
#Entradas
año = int(input("Ingrese su año de nacimiento: "))
numero = int(input("Ingrese un numero entero: "))
#Proceso
operacion = (numero * año) / 21
resto = (numero * año) % 21
#Salida
print("año de nacimiento por el nro",año)
print("dividido por",numero)
print("resultado de operacion",operacion)
print("el resto de la operacion",resto)