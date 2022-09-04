
"definir un for dentro de un def"

"Ejemplo 1"

def contador(n):
    c = 0
    for _ in range(n):
        c+=1
    return c
print(contador(10))
"Ejecutara el for 10 veces a lo que a C se le sumara 1 cada vez"
print("Siguiente ejemplo")

"Ejemplo 2"

def sumatoria(numeros):
    acum = 0
    for n in numeros:
        acum += n
    return acum
print(sumatoria([1,2,3,4,5]))
"Contara todos los numeros en orden y como resultado dara 15"
print("Siguiente ejemplo")

"Ejemplo 3"

def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar"
    for indice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"{numero} * {indice} = {numero * indice}")
print(tabla_multiplicar(2))
"Creara un tabla de multiplicacion en base al numero dado en tabla_multiplicar"

