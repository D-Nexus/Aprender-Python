# Metodo 1 sin recursividad
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


salida = es_primo(5)

if salida:
    print('Es primo')
else:
    print('No es primo')


# Metodo 2 Recursividad
def esPrimo(n, i=2):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True

    return esPrimo(n, i+1)


salida2 = esPrimo(1)

if salida2:
    print('Es primo')
else:
    print('No es primo')
