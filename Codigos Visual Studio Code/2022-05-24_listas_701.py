#Solicitemos una cantidad de nros a ingresar al usuario
#agregar cada nro a una lista
#imprimir la lista ordenada de mayor a menor
#basado en los nros igresados,
#cree una función que retorne una lista con 2 elementos:
#cantidad de nros pares y cantidad de nros impares

##def pares_impares(lista_nros):#[56,45,33]
##    cant_pares = 0
##    cant_impares = 0
##    lista_pares_impares = []
##    for num in lista_nros:
##        if num%2==0:
##            cant_pares = cant_pares + 1
##        else:
##            cant_impares = cant_impares + 1
##    lista_pares_impares.append(cant_pares)
##    lista_pares_impares.append(cant_impares)
##    return lista_pares_impares#alt1
##    
##        
##    
###programa principal
##
##cant = int(input("ingrese cant. nros: "))
##numeros = list()
###numeros = []
##contador = 1
##while contador <= cant:
##    nro = int(input("ingrese nro: "))
##    numeros.append(nro)
##    contador = contador + 1
##print(numeros)
##numeros.sort()
##numeros.reverse()
##print(numeros)
##print(pares_impares(numeros))


#hagamos un programa para hacer la lista del curso
#el ingreso termina cuando se ingrese un -1
#debemos imprimir en pantalla:
#la lista de nombres
#la lista con nombres que terminan con n
#la cantidad de nombres que terminen con n
#luego de realizadas estas acciones,
#imprima en pantalla:
#la letra con la que inician
#los nombres que terminan con n

#ingresar los nombres a la lista
nombres_curso = list()
nombre = ""
while nombre != "-1":
    nombre = input("ingrese nombre: ")
    nombres_curso.append(nombre)
print(nombres_curso)
del nombres_curso[-1]
print(nombres_curso)

#identificar nombres que terminan con n
#agregar a una nueva lista
nombres_con_n = list()
cont_nom_con_n = 0
for nom in nombres_curso:
    if nom[-1] == "n":
        nombres_con_n.append(nom)
        cont_nom_con_n = cont_nom_con_n + 1
print(nombres_con_n)
print("cantidad:",cont_nom_con_n)

#liste la primera letra de los nom que terminan
#con n
for nom in nombres_con_n:
    print(nom[0])



    
    


#A continuación se presentan los datos de las votaciones

#participacion = [70452,96270,177892,97332,253459,722752,2663667,366018,386670,183112,549968,348607,144312,305683,40701,62855]
#regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","RM","O'higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén del General Carlos Ibáñez del Campo","Magallanes y la Antártica Chilena"]      

#obtenga la suma de votos (USAR SUM)
#obtenga la cantidad de regiones (USAR LEN)
#obtenga el promedio de votos (SUM/LEN)
#cantidad de regiones con más de 400 mil votantes (PUEDEN USAR CONTADOR, O PONER EN OTRA LISTA Y OBTENER LEN)
#liste las regiones que tuvieron más de 500 mil (nombre y cifra)



