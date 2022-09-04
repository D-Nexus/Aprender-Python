"""En Python, una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo.
Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas."""

#Ejemplos
x = (1, 2, 3) #Debe poseer multiples datos para considerarse una tupla.
r = (1,) # Si es de un solo elemento agregar una "coma"

print(dir(x))

print(x[2]) #Buscamos el elemento en la posición "2"

#Eliminar tupla
# del x  #Usamos del para borrar una tupla
print(x) #Emite error debido a que se elimino la tupla antes de imprimirla

locations = {
    (35.12121, 39.000):"Tokyo",  #Tuplas en diccionarios
    (35.12121, 42.000):"New york"
}
