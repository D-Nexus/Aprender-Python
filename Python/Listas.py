"""Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos.
Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer elemento."""

demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numbers_list = list((1, 2, 3, 4))
print(numbers_list)

r = list(range(1, 100))  #Permite crear una lista en un rango de 1 a 100 con el metodo "range"
print(r)

print(dir(colors)) #Informacion de lo que podemos hacer con list

print("green" in colors) #Green esta en colors? True o False

#Modificacion de listas
print(colors) #Lista original
colors[1] ="yellow"  #Alterar los elementos de una lista modificandola
print(colors) #Lista modificada

#Metodos append
colors.append("Violet") #Agrega elementos a la lista
print(colors)
#Ejemplo 2 de append
colors.append(("black", "gray", "azure")) #Se puede agregar mas de uno a la vez usando una tupla
print(colors)                             #la tupla lo transforma en un solo elemento pero no los separa en la list

#Metodo extend
#Para agregar mas de un elemento a una list no sirve append ya que solo acepta un argumento en este caso usamos extend
colors.extend(("black", "gray", "azure")) #Agrega la tupla a la list pero los separa en elementos individuales cada uno
print(colors)

#Metodo insert
colors.insert(1, "white") #Agrega el elemento a la posicion indicada
print(colors)
#Ejemplo 2
colors2 = ["red", "green", "black"]
colors2.insert(len(colors2), "white") #Agrega un elemento nuevo a la lista en una posicion 4 donde no habia nada antes
print(colors2)

#Metodo pop
colors2.pop()  #Quita el ultimo elemento agregado a list
print(colors2)
#Ejemplo 2
colors2.pop() #Al repetir esta linea se quitaran dos elementos de list
colors2.pop() #Tambien se le puede dar un indice para quitar ejemplo: 1 ---> colors2.pop(1)
print(colors2)

#Metodo remove
colors3 = ["green", "red", "black"]
colors3.remove("red") #Remueve un elementos especificado
print(colors3)

#Metodo clear
colors4 = ["green", "red", "white", "black"]
print(colors4)
colors4.clear() #Limpia por completo la lista dejandola vacia []
print(colors4)

#Metodo sort
colors5 = ["green", "red", "white", "black", "blue", "azure", "red"]
colors5.sort() #Ordena los elementos de la lista alfabeticamente
print(colors5)
colors5.sort(reverse = True) #Ordena los elementos de la lista de la Z-A 
print(colors5)
print(colors5.index("blue")) #Conseguir el indice(posicion en la lista) de blue
print(colors5.count("red")) #Contar cuantos red existen en la lista