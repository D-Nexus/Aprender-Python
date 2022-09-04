#Como recorrer un diccionario con for
capitales = {"Argentina": "Buenos aires","Peru":"Lima"}
capitales["Bolivia"] = "Sucre" #Lo busca si no lo encuentra lo agrega como llave y le asigna el valor "Sucre"
for elemento in capitales: #elemento solo guarda las llaves
    print(elemento) #Argentina,Peru
    print(capitales[elemento]) #capitales["Argentina"] su valor es "Buenos aires", lo mismo con Peru y Bolivia
    
print("  ") #Salto de linea

#Como recorrer un diccionario con listas como valores con for
capitales = {"Argentina": ["Buenos aires","Rosario"]}
for elemento in capitales: #elemento solo guarda las llaves
    print(elemento) #Argentina,Peru
    print(capitales[elemento][0]) 
    print(capitales[elemento][1])
    
#capitales["Argentina"][0] imprimira "Buenos aires" por que la llave "Argentina" contiene una lista una lista con 2 elementos los cuales son "Buenos aires" en la posición 0 y "Rosario" en la posición 1

print("  ") #Salto de linea

notas = {"PROGRA": [55,75,80],"MATE":[80,90,75]}
las_notas = notas["PROGRA"] #Ejemplo de una lista llamada "las_notas" que contiene un diccionario
#Notas de programación
promedio_progra = sum(notas["PROGRA"])/len(notas["PROGRA"])
print(promedio_progra)
#Notas de matematica
promedio_mate = sum(notas["MATE"])/len(notas["MATE"])
print(promedio_mate)

print("  ") #Salto de linea

encuesta = ["Talcahuano","Talcahuano","Arauco","Lebu","Arauco"] #Personas respondiendo donde viven

datos = {} #{"Talcahuano":2,"Arauco":1....} quiero contar cuantas personas viven en cada comuna y guardarlo 

for comuna in encuesta: #Recorro la lista "encuesta"
    if comuna not in datos: #Si? comuna no esta en el diccionario "datos", lo agrego con un valor 0
        datos[comuna] = 0
    datos[comuna] += 1 #En caso contrario(que si este en datos) le sumo 1 al valor de la comuna previamente agregada

print(datos) #Imprime el diccionario "datos" con los valores actualizados dependiendo de cuantas conto en encuesta
print(datos["Talcahuano"]) #Imprimo el valor de "Talcahuano" en el diccionario
