#A continuación se presentan los datos de las votaciones

participacion = [70452,96270,177892,97332,253459,722752,2663667,366018,386670,183112,549968,348607,144312,305683,40701,62855]
regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","RM","O'higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén del General Carlos Ibáñez del Campo","Magallanes y la Antártica Chilena"]      

#obtenga la suma de votos (USAR SUM)
#obtenga la cantidad de regiones (USAR LEN)
#obtenga el promedio de votos (SUM/LEN)
#cantidad de regiones con más de 400 mil votantes
#liste las regiones que tuvieron más de 500 mil (nombre y cifra)
#imprimir región con mayor votación

mayor = -1
pos = 0
while pos < len(participacion):
    if participacion[pos] > mayor:
        mayor = participacion[pos]
    pos+=1
#print(mayor)       


           #0   #1    #2   #3
years = [2018,2017,2016,2015]
temps = [
            [23,25,22,20,21,15,13,10,7,15,18,22],#0
            [25,22,26,21,19,17,15,9,16,18,22,23],#1
            [22,23,19,17,15,11,10,12,17,19,20,21],#2
            [21,23,17,19,17,16,15,12,19,20,21,24]#3
        ]


#temperaturas de 2017
#print(temps[1])
#temperaturas de marzo 2015
#print(temps[3][2])
#temperaturas de enero a marzo de 2015
#print(temps[3][0:3]) 
#temperaturas de enero, febrero y marzo de 2016
#print(temps[2][0:3])

###area funciones
###programa principal
alumnos=[
            ['Alberto Gonzalez',40,30,70], #0
            ['Francisca Almonacid',100,40],#1
            ['Pedro Reyes',30,50],         #2
            ['Juan Campos',30,60,30,70],   #3
            ['Andrea Zamora',30]]          #4

#desarrollar una función para calcular promedio
#Con while
def promedio(lista_alumnos):
    prom_alumnos = []
    pos = 0
    while pos < len(lista_alumnos):
        nombre_est = lista_alumnos[pos][0]
        notas_est = lista_alumnos[pos][1:]
        promedio = int(sum(notas_est))/len(notas_est)
        prom_alumnos.append([nombre_est,round(promedio)])
        pos += 1
    return prom_alumnos

ninos = promedio(alumnos)
print(ninos)
#Con for
def promedio2(lista_alumnos):
    prom_alumnos = []
    for datos_alum in lista_alumnos:
       nombre_est = datos_alum[0]
       notas_est = datos_alum[1:]
       promedio = int(sum(notas_est))/len(notas_est)
       prom_alumnos.append([nombre_est,round(promedio)])
       #prom_alumnos.append([datos_alum[0],round(int(sum(datos_alum[1:]))/len(datos_alum[1:]))]) #Resumido en 1 linea
    return prom_alumnos

ninos2 = promedio2(alumnos)
print(ninos2)
#desarrollar una función para obtener el mejor promedio
#luego, en el programa principal, si el promedio de un
#estudiante es menor a 55,
#pedir ingresar una nueva nota y agregarla al final
#de las notas que tiene el estudiante






##
##
##
##
##for i in range(0,5,1)#(inicio, fin, paso) [0,1,2,3,4]
##for i in range(0,5)#no puse el paso, se asume que el paso de uno en uno [0,1,2,3,4]
##for i in range(5)#no puse inicio no paso, se asume que inicio es 0 y paso es 1 [0,1,2,3,4]
##
##for i in range(2)#[0,1]


#area de funciones
# def disparo(tablero, barco,fila,columna):

#     return tablero


#programa principal
# tablero= [["-","-","-","-","-","-","-","-","-"],
#            ["-","O","-","-","-","-","-","-","-"],
#            ["-","-","-","-","-"," ","-","-","-"],
#            ["-","-","-","-","-"," ","-","-","-"],
#            ["-","-","-","-","-","-","-","-","-"],
#            ["-","-","-","-","-","-","-","-","-"],
#            ["-","-","-","-","X","X","X","X","-"],
#            ["-","-","-","-","-","-","-","-","-"],
#            ["-","-","-","-","-","-","-","-","-"]]

#barcos = ...
# disparo_fila = 
# disparo_columna =

# print(disparo(tablero,barcos,disparo_fila,disparo_columna))

# tablero[0][1] = "hola"
# print(tablero[0][1])

#¿CUANTOS ELEMENTOS TIENE LA LISTA TABLERO? = 9 (SON LAS SUB LISTAS)
#¿CUANTOS ELEMENTOS TIENE CADA SUBLISTA ALMACENADA EN LAS POSICIONES DE LA LISTA TABLERO?9 Y SON STRINGS

##for listas in tablero:
##    for elemento in listas:
##        print(elemento)
##
##i = 0
##while i < len(tablero):
##    j = 0
##    while j < len(tablero[i]):
##        print(tablero[i][j])
##        j = j+1
##    i = i+1

    



        
    









