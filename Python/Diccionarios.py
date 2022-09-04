"""Un Diccionario es una estructura de datos y un tipo de dato en Python con características 
especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. 
Estos diccionarios nos permiten además identificar cada elemento por una clave (Key)."""

#Ejemplo disccionario
productos = {
    "name": "book",
    "cantidad": 3,
    "precio": 4.99
}

#Ejemplo 2
persona = {
    "first_name": "ryan",
    "last_name": "ray"
}

print(type(productos))
print(dir(productos))

print(" ") #Salto de linea

print(persona.keys()) #Obtiene las key
print(persona.items()) #Obtiene los items
print(persona.clear()) #Limpiar el diccionario

#lista con diccionario interno
products = [ #Lista
    {"name": "book", "price": 3000}, #Diccionarios
    {"name": "laptop", "price": 10000}
]
print(products)

