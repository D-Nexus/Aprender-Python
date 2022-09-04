#Variables
votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
coaliciones = "c1:p1-p2-p31-p3;c2:p4-p5;c3:p6-p310-p7"
#función 1
def votos_partido(votos,partido):
    cant_votos = 0
    i = 0
    letras = ""
    votos = votos+"$" #Sumamos un $ al string para contar el ultimo voto
    while i < len(votos): #Recorremos el largo del string
        if votos[i] != "$":
            letras += votos[i] #Voto antes del $
        else:
            #print(letras)
            if letras == partido: #Compara voto con el partido
                cant_votos += 1 #Suma 1 voto para ese partido
            letras = "" #Vaciamos el string con el voto 
        i +=1
    return cant_votos #Retornamos la cantidad de votos
#función 2
def coalicion(coaliciones):
    i = 0
    coaliciones = coaliciones + ";"
    coalicion = ""
    while i < len(coaliciones):
        coalicion += coaliciones
        if coaliciones[i] == ":":
            print("Coalición:",coalicion)
            coalicion = "" 
        elif coaliciones[i] == ";":
            print(coalicion)
            coalicion = ""
        i += 1
    return coalicion


#Salidas
print("La cantidad de votos es:",votos_partido(votos,"p3"))
print("La cantidad de votos es:",votos_partido(votos,"p6"))
print("La cantidad de votos es:",votos_partido(votos,"p7"))

print(coalicion(coaliciones))
       