"""Establecer en Python es una estructura de datos equivalente a conjuntos en matemáticas. 
Puede consistir en varios elementos; el orden de los elementos en un conjunto no está definido. 
Puede agregar y eliminar elementos de un conjunto, puede iterar los elementos del conjunto, 
puede realizar operaciones estándar en conjuntos (unión, intersección, diferencia). 
Además de eso, puedes verificar si un elemento pertenece a un conjunto"""

#Ejemplo
colors = {"red", "green", "blue"} #Se declaran con corcheas
print(type(colors))
print("red" in colors) #Esta red en colors? True o False

#Metodo add
colors.add("violet") #Agrega violet al set
print(colors) #Los elementos no tiene un orden permanente pueden variar al imprimir

#Metodo remove
colors.remove("red") #Remueve red del set
print(colors)

#Metodo clear
colors.clear() #Vacia el set
print(colors)

#Eliminar un set
del colors
print(colors)