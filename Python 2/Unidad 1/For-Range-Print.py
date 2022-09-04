
"Ejemplos de como utilizar el for-range y el print"

"Ejemplos print"

"Ejemplo 1"
print(1,2,3,4,5, sep="-")
"Resultado: 1-2-3-4-5"
print("Salto de linea")

"Ejemplo 2"
print(1,2,3,4,5, sep=", ")
"Resultado: 1, 2, 3, 4, 5"
print("Salto de linea")

"Ejemplo 3"
print(1,2,3,4,5, sep="-", end=" ")
"El end omite el salto de linea del print"
"""print(1,2,3,4,5, sep="-", end=" ")
   1-2-3-4-5"""
print("Salto de linea")

"Ejemplo 4"
print([1,2,3,4,5])
"Imprimira [1,2,3,4,5]"
print("Salto de linea")

"Ejemplos range"

"Notas"
"Recibe solamente como parametro valeres enteros(int)"
"parametro (stop) obligatorio"
"por defecto el parametro (start) es 0"
"por defecto el parametro (step) es 1"

"Ejemplo 1"

for x in range(10):
    print(x)
"El range contara de 0 a 9 ya que el valor de star por defecto es 0"
print("Salto de linea")

"Ejemplo 2"

for x in range(1,10):
    print(x)
"Aqui definimos el valor start en 1 por lo que contara de 1 a 9"
print("Salto de linea")

"Ejemplo 3"

for x in range(1,10,2):
    print(x)
"Aqui estamos definiendo el valor de step que es como contara en este caso de 2 en 2"
print("Salto de linea")

"Ejemplo 4"

for x in range(10,0,-1):
    print(x)
"En este ejemplo contaremos de forma decreciente"
print("Salto de linea")

"Ejemplo 5"

for x in "Hola Mundo!":
    print(x)
"Imprimimos en la terminal Hola Mundo letra por letra"