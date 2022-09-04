"Como sumar dos cadenas de caracteres del tipo string"

"Codigo a ejecutar"

mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"

print(mensaje)
"La respuesta sera la suma de ambos string, es decir 'Hola Hernesto' "

print(" ") #Para separar solamente

"La búsqueda, consiste en localizar dentro de una cadena, una subcadena más pequeña a un caracter"
"Para lo cual es necesario utilizar el método 'fIND' "

"Ejemplo"

mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)


print(" ")

"La extracion, se trata de sacar afuera de una cadena, una porci´pn de la misma según su posición dentro de ella"
"Para ello es necesario indicar la pisición a extraer ejemplo --> [1:8]"

"Ejemplo"

mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
