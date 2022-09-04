nombre_curso = list() #Lista vacia
nombre = ""
while nombre != "-1":
    nombre = input("Ingrese nombre: ")
    nombre_curso.append(nombre)
print(nombre_curso)
del nombre_curso[-1] #Borro el ultimo elemento de la lista que es el "-1"
print(nombre_curso)

#identificar nombre que terminan con n
#agregar a una nueva lista
nombre_con_n = list()
cont_nom_con_n = 0 #Total de nombres que terminan con n
for nom in nombre_curso:
    if nom[-1] == "n":
        nombre_con_n.append(nom)
        cont_nom_con_n += 1
print(nombre_con_n) #imprimir la lista con los nombre que terminan con "n"
print("Se encontraron",cont_nom_con_n,"nombres que terminan con n")

#liste la primera letra de los nombre que terminan con "n"
for nom in nombre_con_n:
    print(nom[0])

