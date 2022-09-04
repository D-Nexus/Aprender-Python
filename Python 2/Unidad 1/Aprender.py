

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


