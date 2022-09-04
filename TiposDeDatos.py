palabra = "hello world"

#Strings // Texto
print(palabra.upper())  #Lo convierte todo a mayusculas
print(palabra.lower())  #Lo convierte todo a minusculas
print(palabra.swapcase()) #Convierte las minusculas en mayusculas y viceversa
print(palabra.capitalize()) #Pone la primera letra de la primera palabra en mayuscula
print(palabra.replace('hello', 'bye')) #Reemplaza una palabra por otra
print(palabra.count(" ")) #Cuenta el caractere especificado entre comillas (Vacio vale 1 ya que son los espacios)
print(palabra.replace("hello", "bye").upper()) #Reemplaza y convierte a mayusculas "Metodos encadenados"
print(palabra.startswith("hola")) #Es para saber si la cadena de caracteres empieza con la palabra "hola"
print(palabra.endswith("world")) #Mi string termina con la palabra world? True o False
print(palabra.split()) #Divide en palabras basado en los espacios(defalut) de la cadena de caracteres(string)
print(palabra.split(",")) #Divide en base a una coma en la cadena de caracteres(si no hay coma no pasara nada)
print(palabra.split("o")) #Divide en base a las "o" en la cadena de caracteres(string)
print(palabra.find("o")) #Encuentra la letra "o" y entraga la posicion donde se ubica
print(len(palabra)) #Imprime la longitud con el metodo "len"
print(palabra.index("e")) #busca la posicion de la letra en el string(Siempre se empieza de 0)
print(palabra.isnumeric()) #Para saber si el string es numerico
print(palabra.isalpha()) #Para saber si el string es alfanumerico
print(palabra[1]) #Imprimira lo que se encuentre en la posicion 1
#El print no es necesario solo lo usamos para imprimir en pantalla los resultados

#Integer // Entero   
print(10)

#Float // Flotante
print(10.5)

#Boolean // verdadero o falso
True
False

#List // Listas  "Se definen con Corchetes"
[10,20,30,55] #Si se puede modificar
["Hello", "Bye", "Adios"]
[10, "Hello", True, 10.5]
[] #Lista vacia

#Tuples "Se definen con parentesis"
(10,20,30,40,50) #No se pueden modificar
() #Tuples vacio

#Diccionarios
{"nombre":"Ryan", #los elementos se separan por una coma
"apellido":"Ray", #los elementos secundarios van despues de un doble punto
"apodo":"Fazt"}   #"nombre" = clave(como se le conoce) y "Ryan" = valor(Como se le conoce)
#Ejemplo 2
{
    "latitud": 12121212,
    "longitud": 23123233
}

