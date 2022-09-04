"""Una variable es un sitio donde guardamos una determinada información.
En función del tipo de información que guardemos (texto, números, booleanas, etc.),
la variable será de uno u otro tipo."""



name = "Fazt" #La variable guarda una string
name = 100 #La variable guarda un numero
name = [] #La variable guarda una lista
name = () #La variable guarda un tuples
name = {} #La variable guarda un diccionario

print(name) #Imprime lo que contenga la variable
print(10 + 101) #Imprime el resultado de la suma

#Ejemplo 2
x = 100
book = "I Robot"
#Podemos declararlo todo en una sola linea
x, book = 100, "I Robot"
print(x, book)