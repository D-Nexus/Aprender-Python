
def suma_n(n):
    "Suma los números pares entre 0 y 100"
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 2
    return result
print(suma_n(100))

"Suma todos los numeros par entre 0 y 100 usando una variable a la cual se le suman esos numeros"

print("Ejercicio de guia")

"Ejercicio 1"

s = 0
for n in range(10):
    s += n
print(s)

print("Siguiente ejercicio")

"Ejercicio 2"

n= 10
while n <= 10:
    print("Prueba")