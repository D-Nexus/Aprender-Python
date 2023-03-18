def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for pos in range(n-i-1):
            if lista[pos] > lista[pos+1]:
                lista[pos], lista[pos+1] = lista[pos+1], lista[pos]
    return lista


salida = bubble_sort([7, 2, 9, 6, 4, 5, 8])
print(salida)
