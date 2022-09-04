#Strings
#imprimir ultimo caracter

palabra = input("Ingrese una palabra: ")
print(palabra[-1]) #Imprime el ultimo caracter del string.
print(palabra[len(palabra)-1]) #Otra forma de imprimir el ultimo caracter del string.
print(palabra[5:10]) #Imprimir una subcadena desde la posición 5 hasta la 10.
print(palabra[5:]) #Imprimir desde la posición 5 hasta el final.
print(palabra[:4]) #Imprimir desde la posición 4 hasta el inicio.

#identificador de generación
frase = input("Ingrese su frase: ")
frase = frase.lower() #Convertir a minusculas.

#función "in" sirve para buscar si la palabra esta contenida dentro de frase.
if "uwu" in frase or "pana" in frase: 
    print("Generación Z")
elif "bacan" in frase or "brigido" in frase:
    print("Millenial")
elif "grosso" in frase:
    print("Generación X")
else:
    print("No lo podemos clasificar")


#Contar cuantas consonantes y vocales tiene una palabra ingresada por teclado
consonantes = "bcdfghjklmnñpqrstvwxyz"
vocales = "aeiou"
palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
contar_consonantes = 0
contar_vocales = 0
contar_varios = 0
i = 0
while i <= len(palabra)-1:
    print(palabra[i])
    letra = palabra[i]
    if letra in consonantes:
        contar_consonantes += 1
    elif letra in vocales:
        contar_vocales += 1
    else:
        contar_varios += 1
        print("No es una letra")
    i+=1
print("La cantidad de consonantes es:",contar_consonantes)
print("La cantidad de vocales es:",contar_vocales)
print("La cantidad de varios NO letras es:",contar_varios)