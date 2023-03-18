def select_sort(lista):
    n = len(lista)
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista


salida = select_sort([3, 1, 4, 8, 7, 9, 5])
print(salida)
