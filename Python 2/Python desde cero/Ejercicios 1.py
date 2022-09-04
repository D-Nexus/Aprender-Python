import math
import cmath
import decimal

print("Ejercicio 1")

nombre = input("Porfavor escriba su nombre: ")
numero = int(input("escriba un numero: "))

n = numero

for x in range(n):
    print(nombre) #Imprimira el nombre la cantidad de veces que le pidamos

print("   ") # Salto de linea
print("Ejercicio 2")

"Ejercicio 2"

nombre = input("Introduzca su nombre: ")


print(nombre.upper() + " tiene " + str(len(nombre)) + " Letras ") #Muestra en consola la cantidad de letras que posee
" .upper() lo utilizamos para escribir la variable nombre en mayusculas y .lower para escribirlo en minusculas"

print("   ") # Salto de linea
print("Ejercicio 3")

"Ejercicio 3"

operacion = (3+2/2*5)**2

print(operacion) #usamos las ** para poder elevar un numero

print("   ") # Salto de linea
print("Ejercicio 4")

"Ejercicio 4"

horas = int(input("Cantidad de horas de trabajo: "))
costexhora = int(input("Valor por hora de trabajo: "))
total = horas*costexhora
print("El valor correpondiente es de:", total) #Utilizamos la "coma" ya que un INT no puede sumarse con un string
