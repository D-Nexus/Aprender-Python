
"Ciclo while"

"Ejemplo 1"

def suma_n(n):
    "Suma los números de 1 a n"
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result
print(suma_n(5))
"Al result se le sumara el valor de x en cada repeticion, primero sera 5,4,3,2,1 y como resultado final result=15"
"""Result+5
   Result+4
   Result+3
   Result+2
   Result+1"""
"Ya que en cada repetición le restamos 1 a x por lo tanto el valor que se sumara a result sera menor cada vez"
print("Siguiente ejemplo")

"Ejemplo 2"

def ciclo_infinito():
    "Imprime el número 1 infinitas veces"
    i = 1
    while i <= 10:
        print(i, end=" ")
print(ciclo_infinito())
"Cuidado al ejecutar esto que es infinito :v ya que siempre sera 1 por que no hay ninguna sentencia que lo modifique"