#A continuación se presentan los datos de las votaciones

#participacion = [70452,96270,177892,97332,253459,722752,2663667,366018,386670,183112,549968,348607,144312,305683,40701,62855]
#regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","RM","O'higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén del General Carlos Ibáñez del Campo","Magallanes y la Antártica Chilena"]      

#obtenga la suma de votos (USAR SUM)
#obtenga la cantidad de regiones (USAR LEN)
#obtenga el promedio de votos (SUM/LEN)
#cantidad de regiones con más de 400 mil votantes (PUEDEN USAR CONTADOR, O PONER EN OTRA LISTA Y OBTENER LEN)
#liste las regiones que tuvieron más de 500 mil (nombre y cifra)

participacion = [70452,96270,177892,97332,253459,722752,2663667,366018,386670,183112,549968,348607,144312,305683,40701,62855]
regiones = ["Arica y Parinacota","Tarapacá","Antofagasta","Atacama","Coquimbo","Valparaíso","RM","O'higgins","Maule","Ñuble","Biobío","Araucanía","Los Ríos","Los Lagos","Aysén del General Carlos Ibáñez del Campo","Magallanes y la Antártica Chilena"]

print("la suma de votos es",sum(participacion)) #imprime la suma total de todos los numeros de la lista
print("la cant. de reg.",len(regiones)) 
print("el prom es",int(sum(participacion)/len(regiones)))
cont = 0
for votos in participacion:
    if votos > 400000:
        cont += 1
print("cant reg. con mas de 400mil votos",cont)
i = 0
while i < len(participacion):
    if participacion[i] > 500000:
        print("La región",regiones[i],"tiene mas de 500mil con",participacion[i],"votos")
    i += 1
        

