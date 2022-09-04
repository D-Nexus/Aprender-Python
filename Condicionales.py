"""En esta lección se trata la estructura de control if ... elif ... else ...: 
Estas construcciones permiten condicionar la ejecución de uno o varios bloques de 
sentencias al cumplimiento de una o varias condiciones."""

x = 20
y = 10
# if x < 30:
#     print("x es menor que 30")
# else:
#     print("x es mayor a 30")

#Ejemplo "not"
if (not(x == y)): #No lo es lo mismo que y
    print("x no es igual a y")

#Ejemplo de for para leer elementos de una lista

foods = ["apple", "bread", "cheese", "milk", "bananas"] #Si se edita la lista el for imprimira siempre la nueva
for food in foods:  #Quiero cada uno de los elementos que la lista foods (la variable del for se llama food)
    if food == "cheese":
        print("Tengo que comprar cheese")
        break #Finaliza bucle al cumplirse la condicion del if
    print(food)

print(" ")  #Salto de linea

foods = ["apple", "bread", "cheese", "milk", "bananas"] 
for food in foods:  
    if food == "cheese":
        continue #sirve para saltarse esa parte del codigo en este caso no imprime cheese
    print(food)

print(" ") #Salto de linea

for letras in "hello": #Imprimire cada uno de los caracteres de la palabra hello
    print(letras)

print(" ") #Salto de linea

for number in range(1, 8): #Imprimira los numeros en un rango del 1 al 8
    print(number)

print(" ") #Salto de linea

count = 1
while count <= 10: #Se repite mientras se cumpla su condición
    print(count)
    count = count + 1 #Si no aumentaramos el count el ciclo while se repetiria infinitamente