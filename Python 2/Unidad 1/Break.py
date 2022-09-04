
"Ejemplo de la sensentica (break)"

def buscar_numero_en(numero, lista):
    """Busca el número @numero en la lista @lista.
       Si lo encuentra devuelve la posición en la que
       se encontró su primera aparición.
       Si no lo encuentra devuelve -1"""

    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    return indice

print(buscar_numero_en(1, [2, 3, 1, 4, 5]))
print(buscar_numero_en(1, [2, 6, 3, 4, 5]))

"Ejemplo de la sentencia (continue)"

for num in range(2,10):
    if num % 2 == 0:
        print("Encontré un número par: ", num)
        continue
    print("Encontré un número impar: ", num)

"Ejemplo sentencia (else)"

def buscar_numero_en2(numero, lista):
    """Busca el número @numero en la lista @lista.
       Si lo encuentra devuelve la posición en la que
       se encontró su primera aparición.
       Si no lo encuentra devuelve -1"""

    
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    else:
        indice = -1   
    return indice

print(buscar_numero_en2(1, [2, 3, 1, 4, 5]))
print(buscar_numero_en2(1, [2, 6, 3, 4, 5]))

"Ejemplo de la sentencia (pass)"

for i in range(1,10):
    if True:
        pass
    elif False:
        pass
    print(i)

"Usamos pass para crear esqueletos de programación que posteriormente seran rellenados"
"En este esqueleto podemos luego rellenar el if y elif con las setencias correspondientes"